# ✨ KontenKita AI

<div align="center">

### AI Video Content Factory untuk membuat video pendek, konten UGC, dan konten affiliate secara lokal.

<a href="#-mulai-dalam-5-menit">🚀 Mulai Sekarang</a> · <a href="#-demo-hasil-video">🎬 Lihat Demo</a> · <a href="README-id.md">📖 Panduan Indonesia</a> · <a href="README-en.md">🌍 English</a>

![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-5865F2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-22C55E?style=for-the-badge)
![Status](https://img.shields.io/badge/status-local%20ready-F97316?style=for-the-badge)

**Topik → Script → Voice-over → Subtitle → Visual → Video siap publikasi**

</div>

---

## 🎥 Demo hasil video

Berikut beberapa contoh video yang dibuat menggunakan project ini. Klik thumbnail untuk memutar atau mengunduh video.

<div align="center">

| 📱 Portrait 9:16 | 🖥️ Landscape 16:9 | ⚡ Short Demo |
|:---:|:---:|:---:|
| [![Portrait demo](https://github.com/harry0703/mpt-assets/releases/download/assets/03-zh-portrait-city-morning.jpg)](https://harry0703.github.io/mpt-assets/?video=03-zh-portrait-city-morning.mp4) | [![Landscape demo](https://github.com/harry0703/mpt-assets/releases/download/assets/02-zh-landscape-deep-ocean.jpg)](https://harry0703.github.io/mpt-assets/?video=02-zh-landscape-deep-ocean.mp4) | [![English demo](https://github.com/harry0703/mpt-assets/releases/download/assets/09-en-portrait-future-robotics.jpg)](https://harry0703.github.io/mpt-assets/?video=09-en-portrait-future-robotics.mp4) |
| Video vertikal untuk TikTok, Reels, dan Shorts | Video horizontal untuk YouTube | Video pendek berbahasa Inggris |

</div>

<p align="center"><a href="https://harry0703.github.io/mpt-assets/?video=05-zh-portrait-clean-energy.mp4">▶️ Lihat koleksi video lengkap</a></p>

## 🌟 Apa yang bisa dilakukan?

KontenKita AI membantu mengubah ide sederhana menjadi konten siap produksi:

```text
Ide produk / topik
        ↓
AI membuat hook, script, caption, dan hashtag
        ↓
Voice-over + subtitle pintar + materi visual
        ↓
Video UGC / faceless siap dipublikasikan
```

### Content Factory

- Membuat banyak variasi video dari satu topik.
- Membuat seri konten hingga ratusan episode.
- Menghasilkan hook, CTA, caption, dan hashtag.
- Preset faceless channel untuk edukasi, motivasi, fakta, teknologi, dan review produk.

### UGC dan affiliate

- Membuat brief UGC dari data produk.
- Mendukung gaya review, unboxing, tutorial, masalah-solusi, dan soft selling.
- Membaca metadata publik dari URL produk Shopee jika tersedia.
- Menyertakan disclosure affiliate pada script.

### Produksi video

- Script dari topik atau script manual.
- Voice-over otomatis.
- Subtitle dengan pengaturan font, warna, posisi, dan latar.
- Materi lokal, Pexels, Pixabay, Coverr, serta sumber AI yang didukung.
- Rasio 9:16, 16:9, dan 1:1.

### Otomasi lokal

- Template brand dan warna brand.
- Antrean jadwal publikasi lokal.
- Pemeriksaan keamanan konten dasar.
- Penyimpanan analitik dan rekomendasi konten.
- Target publikasi YouTube Shorts dan TikTok melalui OAuth resmi.

## 🚀 Mulai dalam 5 menit

### Windows

```powershell
cd "D:\website\MoneyPrinterTurbo-main\MoneyPrinterTurbo-main"
uv sync --frozen
.\webui.bat
```

Buka browser:

```text
http://127.0.0.1:8501
```

Jika project belum memiliki environment, gunakan:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\webui.bat
```

### macOS / Linux

```bash
uv sync --frozen
sh webui.sh
```

## 🔐 Konfigurasi API key

Salin template environment:

```powershell
Copy-Item .env.example .env
```

Kemudian isi `.env`:

```env
MPT_LLM_PROVIDER=openai
OPENAI_API_KEY=isi_api_key_anda
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL_NAME=gpt-5-mini
```

API key juga dapat diisi melalui menu **Setelan** di WebUI. Jangan mengunggah `.env` ke GitHub dan jangan membagikan screenshot yang menampilkan API key.

## 🎬 Contoh penggunaan

### Membuat video biasa

Masukkan topik berikut pada kolom **Topik Video**:

```text
5 kebiasaan kecil yang membuat hidup lebih produktif
```

Pilih bahasa Indonesia, rasio `9:16`, Edge TTS, subtitle aktif, lalu klik **Hasilkan Video**.

### Membuat konten affiliate Shopee

Buka:

```text
KontenKita Studio → Shopee UGC Affiliate
```

Masukkan URL produk, pilih gaya UGC, lalu klik **Ambil data & buat brief UGC**. Jika metadata Shopee tidak dapat dibaca, masukkan data produk secara manual.

### Membuat seri konten

Buka:

```text
KontenKita Studio → Content Factory → Buat seri otomatis
```

Masukkan topik dan jumlah episode. Data seri akan disimpan di:

```text
storage/content_studio/
```

## 🧩 Content Studio

Panel **🎬 KontenKita Studio** menyediakan:

| Modul | Fungsi |
|---|---|
| Content Factory | Membuat hook dan seri konten |
| Shopee UGC Affiliate | Membuat brief UGC dari URL produk |
| Brand & Faceless | Menyimpan gaya brand dan preset channel |
| Jadwal Publikasi | Menyimpan antrean YouTube dan TikTok |
| Keamanan & Analitik | Review konten, metrik, dan rekomendasi |

Semua data studio disimpan lokal di `storage/content_studio/`.

## 🛠️ API dan CLI

Jalankan API:

```powershell
uv run python main.py
```

Dokumentasi API:

```text
http://127.0.0.1:8080/docs
```

Jalankan melalui CLI:

```powershell
uv run python cli.py --video-subject "Cara AI membantu kehidupan sehari-hari"
```

## 📦 Persyaratan

- Python 3.11 atau lebih baru.
- RAM minimal 4 GB; 8 GB atau lebih disarankan.
- FFmpeg.
- GPU tidak wajib jika menggunakan layanan AI cloud.
- API key LLM untuk membuat script dengan AI.
- API key materi online jika menggunakan Pexels, Pixabay, atau provider lainnya.

## ⚠️ Catatan penggunaan

- Pastikan materi visual, musik, voice-over, dan klaim produk memiliki izin penggunaan yang sesuai.
- Fitur pemeriksaan hak cipta adalah pemeriksaan awal, bukan penentuan hukum.
- Jangan membuat testimoni palsu atau klaim produk yang tidak dapat dibuktikan.
- Upload otomatis YouTube dan TikTok harus menggunakan OAuth serta API resmi platform.
- Hindari scraping agresif dan jangan memasukkan username/password marketplace ke aplikasi.

## 🗂️ Struktur penting

```text
app/services/content_studio.py   # Content Factory, brand, scheduler, analitik
app/services/shopee_ugc.py        # Data produk dan brief UGC affiliate
webui/Main.py                     # WebUI utama
config.toml                       # Konfigurasi aplikasi
.env                              # API key lokal, jangan dibagikan
storage/content_studio/           # Data studio lokal
storage/tasks/                    # Hasil dan task video
```

<div align="center">

### Buat lebih banyak konten. Lebih cepat. Tetap di komputer Anda. 🚀

<a href="README-id.md">📖 Panduan lengkap</a> · <a href="README-en.md">🌍 English</a> · <a href="https://github.com/harry0703/MoneyPrinterTurbo/issues">🐞 Laporkan masalah</a>

<br><br>

Made with ❤️ for creators by KontenKita AI

</div>

## 📄 Lisensi

Project ini dirilis di bawah lisensi MIT. Lihat [LICENSE](LICENSE).

