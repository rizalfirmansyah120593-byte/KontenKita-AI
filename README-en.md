# ✨ KontenKita AI

<div align="center">

### Local AI Video Content Factory for short videos, UGC, and affiliate content.

<a href="#get-started">🚀 Get Started</a> · <a href="#video-showcase">🎬 Video Showcase</a> · <a href="README-id.md">🇮🇩 Bahasa Indonesia</a> · <a href="README-ja.md">🇯🇵 日本語</a>

![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-5865F2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-22C55E?style=for-the-badge)

Topic → Script → Voice-over → Subtitles → Visuals → Publish-ready video

</div>

---

## Video showcase

Click a thumbnail to watch a generated example.

| Portrait 9:16 | Landscape 16:9 | English Short |
|:---:|:---:|:---:|
| [![Portrait](https://github.com/harry0703/mpt-assets/releases/download/assets/03-zh-portrait-city-morning.jpg)](https://harry0703.github.io/mpt-assets/?video=03-zh-portrait-city-morning.mp4) | [![Landscape](https://github.com/harry0703/mpt-assets/releases/download/assets/02-zh-landscape-deep-ocean.jpg)](https://harry0703.github.io/mpt-assets/?video=02-zh-landscape-deep-ocean.mp4) | [![English](https://github.com/harry0703/mpt-assets/releases/download/assets/09-en-portrait-future-robotics.jpg)](https://harry0703.github.io/mpt-assets/?video=09-en-portrait-future-robotics.mp4) |

[▶️ Browse the complete video collection](https://harry0703.github.io/mpt-assets/)

## Features

- AI scripts, hooks, captions, hashtags, voice-over, subtitles, music, and editing.
- Content Factory for batch variations and multi-episode series.
- Brand templates and faceless-channel presets.
- Shopee UGC affiliate briefs from public product metadata when available.
- Smart subtitles, safety preflight, local scheduling, analytics, and recommendations.
- Portrait 9:16, landscape 16:9, and square 1:1 formats.
- Local WebUI, API, and CLI.

## Get started

### Windows

    cd "D:\website\MoneyPrinterTurbo-main\MoneyPrinterTurbo-main"
    uv sync --frozen
    .\webui.bat

Open http://127.0.0.1:8501.

### macOS / Linux

    uv sync --frozen
    sh webui.sh

## API configuration

    Copy-Item .env.example .env

Then edit .env:

    MPT_LLM_PROVIDER=openai
    OPENAI_API_KEY=your_api_key
    OPENAI_BASE_URL=https://api.openai.com/v1
    OPENAI_MODEL_NAME=gpt-5-mini

Keep .env private. Edge TTS can be used without a paid TTS key.

## First workflow

1. Open the WebUI and configure the LLM provider.
2. Enter a topic such as: 5 small habits that improve productivity.
3. Choose language, aspect ratio, footage source, voice, and subtitles.
4. Click Generate Video.
5. Open KontenKita Studio for Content Factory, UGC Affiliate, brand presets, scheduling, safety review, and analytics.

For Shopee UGC, open KontenKita Studio → Shopee UGC Affiliate, enter a product URL, choose a style, and generate the brief. Manual product data is supported when public metadata is unavailable.

## Content Studio

| Module | Purpose |
|---|---|
| Content Factory | Hooks and multi-episode series |
| Shopee UGC Affiliate | Product brief, script, CTA, caption, and hashtags |
| Brand & Faceless | Reusable visual identity and channel presets |
| Publishing Schedule | Local YouTube and TikTok queue |
| Safety & Analytics | Preflight warnings, metrics, and recommendations |

Local data is stored in storage/content_studio/.

## API and CLI

    uv run python main.py
    uv run python cli.py --video-subject "How AI helps everyday life"

API docs: http://127.0.0.1:8080/docs

## Responsible use

Use properly licensed footage and music. Do not create fake testimonials or unsupported product claims. YouTube and TikTok publishing must use official OAuth/API flows. The local copyright checker is a preflight warning system, not legal advice.

## Project map

    app/services/content_studio.py   Content Factory, brand, scheduler, analytics
    app/services/shopee_ugc.py        Product metadata and UGC brief
    webui/Main.py                     Main WebUI
    .env                              Local secrets; never share
    storage/content_studio/           Local studio data
    storage/tasks/                    Generated task files

<div align="center">

Create more content. Stay local. Move faster. 🚀

<a href="README-id.md">🇮🇩 Indonesian</a> · <a href="README-ja.md">🇯🇵 Japanese</a> · <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues">🐞 Issues</a>

</div>

## License

MIT. See [LICENSE](LICENSE).

