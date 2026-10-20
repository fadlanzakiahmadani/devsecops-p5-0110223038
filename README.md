# SecureTask API

SecureTask adalah aplikasi pengelola tugas sederhana berbasis Python. Aplikasi ini memungkinkan pengguna menambahkan tugas dan melihat daftar tugas yang tersimpan dalam file JSON.

## Teknologi yang Digunakan

- Python 3.12
- pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk menjalankan pipeline CI/CD

## Struktur Aplikasi

- `app.py`: menjalankan aplikasi dan mengelola tugas.
- `models.py`: mendefinisikan model data tugas.
- `storage.py`: membaca dan menyimpan data tugas dalam format JSON.
- `validators.py`: memvalidasi judul tugas.
- `security.py`: menangani validasi input terkait keamanan.
- `tests/`: berisi unit test aplikasi.

## Cara Menjalankan Aplikasi

Pastikan Python 3.12 telah terpasang.

Instal dependency pengembangan:

```bash
python -m pip install -r requirements-dev.txt
```

Menambahkan tugas:

```bash
python app.py add "Menyelesaikan tugas DevSecOps"
```

Melihat daftar tugas:

```bash
python app.py list
```

Menjalankan unit test:

```bash
python -m pytest -v
```

## DevSecOps Pipeline

Pipeline didefinisikan dalam `.github/workflows/devsecops.yml` dan berjalan ketika terjadi push ke branch `main` atau pull request yang menargetkan branch `main`.

Pipeline memiliki dua job:

1. **build**: memasang dependency dan menjalankan unit test menggunakan pytest.
2. **sast-scan**: menjalankan Bandit untuk memeriksa potensi masalah keamanan pada kode Python. Job ini hanya berjalan setelah job build berhasil.

Quality Gate menggunakan hasil pemindaian Bandit. Temuan dengan tingkat severity dan confidence tinggi sesuai filter konfigurasi menyebabkan job SAST gagal.

Pipeline ini mendemonstrasikan pemeriksaan kualitas dan keamanan otomatis sebelum perubahan kode diterima. Pipeline belum melakukan deployment ke production.