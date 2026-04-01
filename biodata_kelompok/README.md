# 🌐 Website Biodata Kelompok — Kuintet AM 2024 (Django)

Website ini dikembangkan untuk memenuhi tugas mata kuliah **Pengantar Keamanan Perangkat Lunak (PKPL)**.
Fokus utama proyek ini adalah implementasi mekanisme **Autentikasi dan Otorisasi** yang aman.

---

## 👥 Anggota Kelompok

| Nama | NPM | Peran |
|------|-----|-------|
| Karla Ameera Raswanda | 2406414542 | Authorization (Access Control) |
| Raida Khoyyara | 2406495445 | Frontend & Public Page |
| Josh Christmas Rommlynn | 2406395291 | Authentication (OAuth Google) | 
| Muhammad Fadhlurrohman Pasya | 2406411830 | Integration + Deployment + QA |
| Christopher Evan Tanuwidjaja | 2406358056 | Feature Edit (UI + Logic) |

---

## 🚀 1. Cara Menjalankan Proyek

### Prasyarat
- 
- 

### Langkah Instalasi

**1. Clone & Setup Virtual Environment**
```bash
git clone https://github.com/PKPL-Kuintet-Angkatan-Mahasiswa-2024/Tugas-2-PKPL
cd Tugas-2-PKPL
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**2. Instal Dependensi**
```bash
pip install -r requirements.txt
```

**3. Konfigurasi Environment**

Buat file `.env` dan isi dengan kredensial Google OAuth kamu:
```env
GOOGLE_OAUTH_CLIENT_ID=your_client_id
GOOGLE_OAUTH_SECRET=your_client_secret
GROUP_MEMBER_EMAILS=raida.khoyyara@ui.ac.id,karla.ameera@ui.ac.id,...
```

**4. Migrasi Database & Jalankan Server**
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔐 2. Mekanisme Autentikasi & Otorisasi

### Autentikasi
[isi di sini]

### Otorisasi
[isi di sini]

---

## 🎨 3. Fitur Utama (Scope Member A)

### Halaman Publik *(No Login)*
Daftar biodata 5 anggota kelompok dapat diakses oleh siapa saja tanpa perlu login. Data ditampilkan secara dinamis dari `ANGGOTA_LIST` di `views.py`.

### Tema Dinamis *(CSS Variables)*
[isi di sini]

### Struktur Folder Penting
```
biodata_kelompok/
├── static/css/style.css          # Pusat styling dan variabel warna
├── templates/
│   ├── base.html                 # Layout utama dengan CSS dinamis
│   └── partials/                 # Komponen reusable (kartu anggota, dll.)
```

---

## 🛠️ 4. Komponen Teknologi

| Layer | Teknologi |
|-------|-----------|
| Backend | Django 5.x |
| Auth | django-allauth (Google OAuth 2.0) |
| Database | SQLite (Development) |
| Styling | CSS3 dengan CSS Variables & Grid Layout |
| Settings | django-config-models (tema global) |

---

## 📸 5. Screenshot Aplikasi
[isi di sini]