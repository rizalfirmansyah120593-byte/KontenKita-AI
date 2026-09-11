"""Shopee product brief extraction and UGC affiliate planning.

The extractor only reads public metadata exposed by a product URL. It does
not log in, bypass protections, or automate Shopee interactions.
"""

from __future__ import annotations

import json
import re
from html import unescape
from typing import Any
from urllib.parse import urlparse

import requests

from app.services import llm


def _meta(html: str, key: str) -> str:
    pattern = rf'<meta[^>]+(?:property|name)=["\']{re.escape(key)}["\'][^>]+content=["\']([^"\']*)'
    match = re.search(pattern, html, re.IGNORECASE)
    if not match:
        pattern = rf'<meta[^>]+content=["\']([^"\']*)["\'][^>]+(?:property|name)=["\']{re.escape(key)}["\']'
        match = re.search(pattern, html, re.IGNORECASE)
    return unescape(match.group(1)).strip() if match else ""


def extract_product(url: str, timeout: int = 20) -> dict[str, Any]:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Masukkan URL produk Shopee yang valid.")
    if "shopee" not in parsed.netloc.lower():
        raise ValueError("URL harus berasal dari domain Shopee.")
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; KontenKitaAI/1.0)"},
        timeout=timeout,
    )
    response.raise_for_status()
    html = response.text
    product = {
        "url": url,
        "title": _meta(html, "og:title") or _meta(html, "twitter:title"),
        "description": _meta(html, "og:description") or _meta(html, "description"),
        "image": _meta(html, "og:image"),
        "price": "",
        "source": "public_metadata",
    }
    json_ld = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.I | re.S)
    for raw in json_ld:
        try:
            data = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        entries = data if isinstance(data, list) else [data]
        for entry in entries:
            if isinstance(entry, dict):
                product["title"] = product["title"] or str(entry.get("name", ""))
                product["description"] = product["description"] or str(entry.get("description", ""))
                image = entry.get("image", "")
                product["image"] = product["image"] or (image[0] if isinstance(image, list) else str(image))
                offer = entry.get("offers", {})
                if isinstance(offer, dict):
                    product["price"] = str(offer.get("price", ""))
    return product


def create_ugc_brief(product: dict[str, Any], style: str = "review jujur", duration: int = 30) -> str:
    prompt = f"""Buat brief video UGC affiliate berbahasa Indonesia berdasarkan data produk berikut.
Jangan mengarang klaim medis, angka, diskon, rating, atau pengalaman pribadi yang tidak ada di data.
Gaya: {style}. Durasi: {duration} detik.
Kembalikan bagian: HOOK, SCRIPT, VISUAL, CTA, CAPTION, HASHTAGS.
Sertakan disclosure bahwa konten mengandung tautan affiliate.

DATA PRODUK:
{json.dumps(product, ensure_ascii=False, indent=2)}"""
    return llm._generate_response(prompt)
