# 🌐 Website Biodata Kelompok — Kuintet Angkatan Mahasiswa 2024 (Django)

Website ini dikembangkan untuk memenuhi tugas mata kuliah **Pengantar Keamanan Perangkat Lunak (PKPL)**.
Fokus utama proyek ini adalah implementasi mekanisme **Autentikasi dan Otorisasi** yang aman.

---

## Anggota Kelompok

| Nama | NPM | Peran |
|------|-----|-------|
| Karla Ameera Raswanda | 2406414542 | Authorization (Access Control) |
| Raida Khoyyara | 2406495445 | Frontend & Public Page |
| Josh Christmas Rommlynn | 2406395291 | Authentication (OAuth Google) | 
| Muhammad Fadhlurrohman Pasya | 2406411830 | Integration + Deployment + QA |
| Christopher Evan Tanuwidjaja | 2406358056 | Feature Edit (UI + Logic) |

---

## 1. Cara Menjalankan Proyek

### Link Deployment
```bash
https://tugas-2-pkpl.fly.dev/
```

---

## 2. Mekanisme Autentikasi & Otorisasi

### Autentikasi
Mekanisme autentikasi Google OAuth 2.0 memungkinkan aplikasi pihak ketiga mengakses data pengguna (email/profil) secara aman tanpa harus mengetahui kata sandi. Prosesnya melibatkan pengguna, aplikasi (klien), dan server Google, dimulai dari permintaan izin (consent), pertukaran kode otorisasi dengan akses token, hingga validasi token untuk mendapatkan data pengguna. 
Alur Kerja Utama Google OAuth 2.0:
- **Konfigurasi Kredensial**: Developer (kami) membuat proyek di Google Cloud Console, mengatur OAuth consent screen, dan mendapatkan Client ID serta Client Secret.
- **Permintaan Otorisasi**: Aplikasi mengarahkan pengguna ke halaman login Google. URL permintaan menyertakan Client ID, scope (data yang diminta, misal: email/profil pengguna), dan redirect URI.
- **Persetujuan Pengguna**: Pengguna login ke akun Google dan memberikan izin kepada aplikasi untuk mengakses data (tampilan consent screen).
- **Pertukaran Kode (Authorization Code)**: Setelah disetujui, Google mengalihkan kembali ke redirect URI aplikasi dengan membawa authorization code.
- **Penukaran Token**: Aplikasi mengirimkan authorization code, Client ID, dan Client Secret ke server Google untuk ditukar dengan Access Token (dan Refresh Token jika perlu).
- **Akses Data & Login**: Aplikasi menggunakan Access Token untuk mengambil data profil pengguna dari API Google, kemudian membuat sesi atau mendaftarkan pengguna di sistem internal.

### Otorisasi
Setelah pengguna berhasil login, sistem melakukan pengecekan otorisasi menggunakan fungsi `is_authorized`. Mekanisme ini terdiri dari dua kondisi utama:
- **Email pengguna harus terdaftar** dalam daftar anggota kelompok (GROUP_MEMBER_EMAILS di settings).
- **Pengguna harus login melalui Google**, yang divalidasi melalui keberadaan `SocialAccount` dengan provider `"google"` dari `django-allauth`.

Jika kedua kondisi terpenuhi, maka pengguna dianggap sebagai **authorized member** dan memiliki akses untuk mengedit biodata miliknya. Sebaliknya, pengguna yang tidak memenuhi syarat hanya memiliki akses **read-only**.

Pada sisi implementasi:

Endpoint edit (`edit_biodata`) dilindungi dengan decorator `@login_required`.
Terdapat validasi tambahan menggunakan `is_authorized`; jika gagal, pengguna akan diarahkan kembali ke halaman utama dengan pesan error.
Pengguna hanya dapat mengedit biodata miliknya sendiri karena adanya relasi one-to-one antara `user` dan model `Biodata`.


---


### Struktur Folder Penting
```
biodata_kelompok/
├── static/css/style.css          # Pusat styling dan variabel warna
├── templates/
│   ├── base.html                 # Layout utama dengan CSS dinamis
│   └── partials/                 # Komponen reusable (kartu anggota, dll.)
```

---

## 4. Komponen Teknologi

| Layer | Teknologi |
|-------|-----------|
| Backend | Django 5.x |
| Auth | django-allauth (Google OAuth 2.0) |
| Database | SQLite (Development) |
| Styling | CSS3 dengan CSS Variables dan HTML5 |
| Settings | django-config-models (tema global) |

---


