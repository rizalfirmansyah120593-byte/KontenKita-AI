# ✨ KontenKita AI

<div align="center">

### ショート動画・UGC・アフィリエイト動画をローカルで作成する AI コンテンツ工場。

<a href="#5分で始める">🚀 はじめる</a> · <a href="#動画デモ">🎬 動画デモ</a> · <a href="README-id.md">🇮🇩 Bahasa Indonesia</a> · <a href="README-en.md">🌍 English</a>

![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-5865F2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-22C55E?style=for-the-badge)

テーマ → 台本 → 音声 → 字幕 → 素材 → 投稿用動画

</div>

---

## 動画デモ

サムネイルをクリックすると生成例を確認できます。

| 縦型 9:16 | 横型 16:9 | 英語ショート |
|:---:|:---:|:---:|
| [![Portrait](https://github.com/harry0703/mpt-assets/releases/download/assets/03-zh-portrait-city-morning.jpg)](https://harry0703.github.io/mpt-assets/?video=03-zh-portrait-city-morning.mp4) | [![Landscape](https://github.com/harry0703/mpt-assets/releases/download/assets/02-zh-landscape-deep-ocean.jpg)](https://harry0703.github.io/mpt-assets/?video=02-zh-landscape-deep-ocean.mp4) | [![English](https://github.com/harry0703/mpt-assets/releases/download/assets/09-en-portrait-future-robotics.jpg)](https://harry0703.github.io/mpt-assets/?video=09-en-portrait-future-robotics.mp4) |

[▶️ 動画コレクションを見る](https://harry0703.github.io/mpt-assets/)

## 主な機能

- AI による台本、フック、キャプション、ハッシュタグ、音声、字幕、BGM、動画編集。
- Content Factory による一括生成とシリーズ動画。
- ブランドテンプレートと顔出し不要のチャンネルプリセット。
- Shopee 商品の公開メタデータから UGC アフィリエイト案を作成。
- 字幕スタイル、安全確認、ローカル予約、分析、推薦。
- 縦型 9:16、横型 16:9、正方形 1:1 に対応。
- ローカル WebUI、API、CLI。

## 5分で始める

### Windows

    cd "D:\website\MoneyPrinterTurbo-main\MoneyPrinterTurbo-main"
    uv sync --frozen
    .\webui.bat

ブラウザで http://127.0.0.1:8501 を開きます。

### macOS / Linux

    uv sync --frozen
    sh webui.sh

## API の設定

    Copy-Item .env.example .env

.env を編集します:

    MPT_LLM_PROVIDER=openai
    OPENAI_API_KEY=your_api_key
    OPENAI_BASE_URL=https://api.openai.com/v1
    OPENAI_MODEL_NAME=gpt-5-mini

.env は共有しないでください。Edge TTS は API key なしでも利用できます。

## 基本ワークフロー

1. WebUI を開き、LLM provider を設定します。
2. テーマを入力し、言語、画面比率、素材、音声、字幕を選択します。
3. 動画を生成をクリックします。
4. KontenKita Studio で Content Factory、UGC、ブランド、予約、確認、分析を利用します。
5. Shopee UGC は KontenKita Studio → Shopee UGC Affiliate から作成できます。

## Content Studio

| モジュール | 目的 |
|---|---|
| Content Factory | フックとシリーズ動画 |
| Shopee UGC Affiliate | 商品概要、台本、CTA、キャプション、ハッシュタグ |
| Brand & Faceless | ブランド設定と顔出し不要プリセット |
| Publishing Schedule | YouTube と TikTok のローカル予約キュー |
| Safety & Analytics | 注意事項、指標、推薦 |

ローカルデータは storage/content_studio/ に保存されます。

## API と CLI

    uv run python main.py
    uv run python cli.py --video-subject "AIが日常生活を支援する方法"

API ドキュメント: http://127.0.0.1:8080/docs

## 注意事項

素材と音楽の利用許諾を確認してください。架空の体験談や根拠のない商品効果を作らないでください。YouTube と TikTok の投稿は公式 OAuth/API を利用してください。

<div align="center">

もっと作る。ローカルで守る。速く届ける。🚀

<a href="README-id.md">🇮🇩 Indonesian</a> · <a href="README-en.md">🌍 English</a> · <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues">🐞 Issues</a>

</div>

## ライセンス

MIT。詳細は [LICENSE](LICENSE) を参照してください。

