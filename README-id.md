# KontenKita AI

KontenKita AI adalah aplikasi open-source untuk membuat video pendek dengan bantuan AI. Cukup masukkan topik atau naskah, lalu aplikasi dapat membantu membuat naskah, voice-over, subtitle, memilih materi visual, musik latar, dan merender video akhir.

## Fitur utama

- WebUI, API, dan CLI.
- Pembuatan naskah dari topik atau penggunaan naskah sendiri.
- Voice-over melalui Edge TTS (gratis, tidak memerlukan API key) atau layanan TTS lain.
- Subtitle otomatis dan pengaturan gaya subtitle.
- Materi visual dari file lokal atau layanan seperti Pexels, Pixabay, dan Coverr.
- Format video vertikal `9:16`, horizontal `16:9`, dan persegi `1:1`.
- Dukungan berbagai penyedia LLM, termasuk OpenAI, Gemini, DeepSeek, Moonshot, Qwen, Anthropic, dan lainnya.

## Persyaratan

- Windows 10 atau lebih baru, macOS, atau Linux.
- Python 3.11 atau lebih baru untuk instalasi manual.
- RAM minimal 4 GB; 8 GB atau lebih disarankan.
- GPU tidak wajib, tetapi dapat mempercepat pemrosesan lokal.
- Untuk Windows, simpan project di path tanpa spasi atau karakter non-ASCII jika memungkinkan.

## Cara cepat di Windows

Jika menggunakan paket Windows satu klik, unduh versi terbaru dari [GitHub Releases](https://github.com/harry0703/MoneyPrinterTurbo/releases/latest), ekstrak, lalu jalankan `start.bat`.

Untuk source code yang sudah diunduh, buka PowerShell di folder project dan jalankan:

```powershell
cd "D:\website\MoneyPrinterTurbo-main\MoneyPrinterTurbo-main"
.\webui.bat
```

Kemudian buka browser dan akses:

```text
http://127.0.0.1:8501
```

## Instalasi manual

Pastikan Python 3.11+ dan [uv](https://docs.astral.sh/uv/) sudah terpasang. Dari folder utama project:

```powershell
uv sync --frozen
.\webui.bat
```

Jika tidak menggunakan `uv`, gunakan virtual environment Python:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\webui.bat
```

Folder utama project adalah folder yang berisi `webui.bat`, `main.py`, `cli.py`, dan `config.toml`.

## Konfigurasi API key

Setelah WebUI terbuka, buka pengaturan dasar dan isi API key layanan yang ingin digunakan. API key yang diperlukan bergantung pada workflow:

- LLM: untuk membuat atau mengubah naskah, misalnya OpenAI, Gemini, DeepSeek, atau Moonshot.
- Pexels/Pixabay/Coverr: untuk mengambil video atau gambar stok online.
- Penyedia TTS berbayar: hanya diperlukan jika tidak memakai Edge TTS.
- Penyedia video AI: hanya diperlukan jika ingin membuat materi video dengan AI.

Konfigurasi juga dapat disimpan di [config.toml](config.toml). Jangan membagikan file ini jika berisi API key.

Untuk percobaan awal, pilih Edge TTS, masukkan topik sederhana, pilih sumber materi lokal atau layanan yang sudah memiliki API key, lalu mulai proses pembuatan video.

## Alur penggunaan pertama

1. Jalankan WebUI dengan `.\webui.bat`.
2. Buka `http://127.0.0.1:8501`.
3. Isi API key pada pengaturan dasar.
4. Masukkan topik video atau tempelkan naskah sendiri.
5. Pilih bahasa, rasio video, durasi, suara, subtitle, musik, dan sumber materi.
6. Klik tombol untuk mulai membuat video.
7. Setelah selesai, unduh hasil video dari halaman tugas atau folder output project.

## Menjalankan API

Untuk menjalankan server API:

```powershell
uv run python main.py
```

Dokumentasi API tersedia di:

```text
http://127.0.0.1:8080/docs
```

Alternatifnya, gunakan `python main.py` setelah virtual environment diaktifkan.

## Menjalankan melalui CLI

Contoh membuat video dari topik:

```powershell
uv run python cli.py --video-subject "Bagaimana AI membantu kehidupan sehari-hari"
```

Untuk melihat semua opsi CLI:

```powershell
uv run python cli.py --help
```

## Docker

Jika Docker Desktop sudah terpasang:

```powershell
docker compose -f docker-compose.release.yml up
```

WebUI tersedia di `http://127.0.0.1:8501`, sedangkan dokumentasi API tersedia di `http://127.0.0.1:8080/docs`.

## Masalah umum

- Jika `webui.bat` tidak dapat dijalankan, pastikan perintah dijalankan dari folder utama project.
- Jika dependensi belum ditemukan, jalankan `uv sync --frozen` atau instal `requirements.txt`.
- Jika materi online gagal diambil, periksa API key dan koneksi internet.
- Jika proses video gagal, periksa log terminal, ruang disk, serta instalasi FFmpeg.
- Jika browser tidak terbuka otomatis, akses `http://127.0.0.1:8501` secara manual.

## Dokumentasi lain

- [README utama](README.md)
- [README bahasa Inggris](README-en.md)
- [Dokumentasi API](http://127.0.0.1:8080/docs) setelah server API berjalan
- [GitHub Issues](https://github.com/harry0703/MoneyPrinterTurbo/issues)

## Lisensi

Project ini dirilis di bawah lisensi MIT. Lihat [LICENSE](LICENSE).
