"""Local content-planning utilities for Content Factory workflows.

This module deliberately has no network dependency. It stores planning data in
``storage/content_studio`` and can be used by the WebUI, CLI, or a local
scheduler. Publishing adapters must authenticate with the official platform
OAuth flows separately.
"""

from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.utils import utils


STUDIO_DIR = Path(utils.storage_dir()) / "content_studio"
BRANDS_FILE = STUDIO_DIR / "brands.json"
SERIES_FILE = STUDIO_DIR / "series.json"
SCHEDULE_FILE = STUDIO_DIR / "schedule.json"
ANALYTICS_FILE = STUDIO_DIR / "analytics.json"


def _split_sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?。！？])\s+|\n+", text) if part.strip()]


def _read(path: Path, default: Any) -> Any:
    STUDIO_DIR.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def _write(path: Path, value: Any) -> None:
    STUDIO_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def save_brand(name: str, **settings: Any) -> dict[str, Any]:
    """Save a reusable brand preset for local video generation."""
    brands = _read(BRANDS_FILE, {})
    brand_id = str(settings.pop("id", "")) or str(uuid.uuid4())
    brands[brand_id] = {
        "id": brand_id,
        "name": name.strip() or "Default Brand",
        "settings": settings,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _write(BRANDS_FILE, brands)
    return brands[brand_id]


def list_brands() -> list[dict[str, Any]]:
    return list(_read(BRANDS_FILE, {}).values())


def generate_hooks(topic: str, count: int = 5) -> list[str]:
    """Create deterministic hook candidates without consuming an API call."""
    topic = topic.strip().rstrip(".")
    templates = [
        f"Kebanyakan orang belum tahu fakta ini tentang {topic}.",
        f"Dalam 30 detik, pahami hal terpenting tentang {topic}.",
        f"Jika Anda tertarik dengan {topic}, jangan lewatkan ini.",
        f"Kesalahan paling umum saat membahas {topic} adalah ini.",
        f"Apa yang terjadi jika kita melihat {topic} dari sudut pandang berbeda?",
        f"Tiga hal tentang {topic} yang jarang dibahas.",
    ]
    return templates[: max(1, min(count, len(templates)))]


def create_video_plan(
    topic: str,
    script: str = "",
    language: str = "id",
    style: str = "documentary",
    duration_minutes: int = 5,
    brand_id: str = "",
) -> dict[str, Any]:
    """Create a render-ready, provider-agnostic storyboard.

    The plan is intentionally independent from any particular LLM or media
    provider. This lets the WebUI preview/edit the plan before the expensive
    render job starts.
    """
    topic = topic.strip()
    script = script.strip()
    if not topic and not script:
        raise ValueError("topic atau script wajib diisi")
    source = _split_sentences(script) if script else [
        f"Pernah bertanya-tanya mengapa {topic} begitu penting? Mari kita lihat jawabannya.",
        f"Untuk memahaminya, kita perlu melihat konteks dan fakta utama di balik {topic}.",
        f"Yang paling menarik, dampak {topic} bisa kita lihat dalam contoh-contoh sederhana di sekitar kita.",
        f"Pada akhirnya, memahami {topic} membantu kita mengambil keputusan yang lebih baik ke depannya.",
    ]
    target_seconds = max(30, min(int(duration_minutes) * 60, 3600))
    scene_seconds = max(5, target_seconds // len(source))
    scenes = []
    for index, narration in enumerate(source, 1):
        scenes.append({
            "id": f"scene-{index}",
            "order": index,
            "narration": narration,
            "visual_prompt": f"{style} cinematic B-roll illustrating: {narration}",
            "search_terms": [topic, *[w for w in re.findall(r"[\w-]+", narration.lower()) if len(w) > 4][:4]],
            "duration": scene_seconds,
            "transition": "fade" if index > 1 else "none",
            "status": "planned",
        })
    return {
        "id": str(uuid.uuid4()),
        "topic": topic,
        "language": language or "auto",
        "style": style or "documentary",
        "duration_seconds": scene_seconds * len(scenes),
        "brand_id": brand_id,
        "scenes": scenes,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def revise_video_plan(plan: dict[str, Any], instruction: str) -> dict[str, Any]:
    """Apply safe, deterministic edits requested in natural language.

    LLM-backed rewriting can be layered on top later; these common edits work
    offline and make the chat workflow useful even without an API key.
    """
    instruction = instruction.strip()
    if not instruction:
        raise ValueError("instruction wajib diisi")
    updated = json.loads(json.dumps(plan))
    lowered = instruction.lower()
    if any(word in lowered for word in ("lebih cepat", "faster", "percepat")):
        for scene in updated.get("scenes", []):
            scene["duration"] = max(3, int(scene.get("duration", 5) * 0.8))
        updated["duration_seconds"] = sum(s["duration"] for s in updated.get("scenes", []))
    if any(word in lowered for word in ("lebih lambat", "slower", "perlambat")):
        for scene in updated.get("scenes", []):
            scene["duration"] = int(scene.get("duration", 5) * 1.2)
        updated["duration_seconds"] = sum(s["duration"] for s in updated.get("scenes", []))
    if "ganti" in lowered or "replace" in lowered:
        for scene in updated.get("scenes", []):
            scene["status"] = "needs_visual_review"
    updated["last_revision"] = instruction
    updated["updated_at"] = datetime.now(timezone.utc).isoformat()
    return updated


def create_series(topic: str, episodes: int = 10, brand_id: str = "") -> dict[str, Any]:
    """Create a local episode queue; actual scripts are generated by the LLM pipeline."""
    episodes = max(1, min(int(episodes), 365))
    hooks = generate_hooks(topic, 6)
    series = _read(SERIES_FILE, {})
    series_id = str(uuid.uuid4())
    payload = {
        "id": series_id,
        "topic": topic.strip(),
        "brand_id": brand_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "episodes": [
            {"number": index, "status": "planned", "hook": hooks[(index - 1) % len(hooks)]}
            for index in range(1, episodes + 1)
        ],
    }
    series[series_id] = payload
    _write(SERIES_FILE, series)
    return payload


def schedule_post(video_path: str, publish_at: str, platforms: list[str], **metadata: Any) -> dict[str, Any]:
    """Queue a local publication record for YouTube/TikTok adapters."""
    allowed = {"youtube", "tiktok"}
    selected = [p.lower() for p in platforms if p.lower() in allowed]
    if not selected:
        raise ValueError("platforms harus berisi youtube atau tiktok")
    item = {
        "id": str(uuid.uuid4()),
        "video_path": str(video_path),
        "publish_at": publish_at,
        "platforms": selected,
        "status": "scheduled",
        "metadata": metadata,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    schedule = _read(SCHEDULE_FILE, [])
    schedule.append(item)
    _write(SCHEDULE_FILE, schedule)
    return item


def list_schedule() -> list[dict[str, Any]]:
    return _read(SCHEDULE_FILE, [])


def assess_content(text: str) -> dict[str, Any]:
    """Perform a conservative local safety/copyright preflight.

    This is a warning system, not a legal copyright determination.
    """
    lowered = text.lower()
    terms = {
        "medical_claim": ["menyembuhkan", "pasti sembuh", "obat kanker"],
        "financial_claim": ["pasti untung", "jaminan profit", "cepat kaya"],
        "unsafe": ["bom", "racun", "bunuh diri"],
    }
    warnings = [
        {"category": category, "match": word}
        for category, words in terms.items()
        for word in words
        if word in lowered
    ]
    copyright_markers = re.findall(r"(?:©|all rights reserved|copyright|hak cipta)", lowered)
    return {
        "safe_to_review": not warnings,
        "warnings": warnings,
        "copyright_markers": copyright_markers,
        "notice": "Pemeriksaan ini bukan penentuan hukum dan tetap perlu review manual.",
    }


def record_analytics(platform: str, metrics: dict[str, Any]) -> dict[str, Any]:
    """Store manually imported or API-fetched metrics for local recommendations."""
    records = _read(ANALYTICS_FILE, [])
    record = {"platform": platform.lower(), "metrics": metrics, "recorded_at": datetime.now(timezone.utc).isoformat()}
    records.append(record)
    _write(ANALYTICS_FILE, records)
    return record


def recommend_next_content() -> dict[str, Any]:
    records = _read(ANALYTICS_FILE, [])
    if not records:
        return {"message": "Belum ada data analitik. Publikasikan beberapa video terlebih dahulu."}
    best = max(records, key=lambda item: float(item.get("metrics", {}).get("views", 0) or 0))
    return {
        "message": "Gunakan pola video dengan performa tertinggi sebagai eksperimen berikutnya.",
        "best_platform": best.get("platform"),
        "best_metrics": best.get("metrics", {}),
    }
