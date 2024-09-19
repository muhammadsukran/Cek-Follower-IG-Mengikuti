# Instagram Followers vs Following Comparison

Proyek ini bertujuan untuk membandingkan daftar akun yang di-follow (following) dengan akun yang mengikuti kembali (followers) pada Instagram. Program ini akan menampilkan daftar akun yang Anda follow, tetapi tidak follow back.

## Persyaratan

- **Python 3.x** harus sudah terinstal di komputer Anda.
- Data **followers** dan **following** dari akun Instagram Anda dalam format JSON.

## Langkah-langkah

### 1. Mengunduh Data dari Instagram (Meta)

Sebelum menjalankan program ini, Anda harus mengunduh data followers dan following dari akun Instagram Anda:

1. Masuk ke akun Instagram Anda melalui browser atau aplikasi Instagram.
2. Pergi ke **Pengaturan** (Settings).
3. Di bagian **Privasi dan Keamanan**, cari opsi **Unduh Data Anda** (Download Your Data).
4. Masukkan alamat email Anda dan klik **Selanjutnya** (Next).
5. Instagram akan mengirimkan tautan untuk mengunduh data ke email Anda. Klik tautan tersebut untuk mengunduh file ZIP yang berisi data akun Instagram Anda.
6. Ekstrak file ZIP tersebut di komputer Anda.

### 2. Struktur File yang Diperlukan

Setelah Anda mengekstrak file ZIP, Anda akan menemukan beberapa file JSON. File yang diperlukan untuk program ini adalah:

- `following.json`: Berisi daftar akun yang Anda follow.
- `followers.json`: Berisi daftar akun yang mengikuti Anda.

Pastikan kedua file ini berada di direktori yang sama dengan script Python yang akan Anda jalankan.

### 3. Menyiapkan Lingkungan Python

Pastikan Python sudah terinstal di komputer Anda. Jika belum, Anda bisa mengunduhnya dari [python.org](https://www.python.org/downloads/).


