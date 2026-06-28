# Dashboard Kelompok

Dashboard kelompok berbasis Flask + HTML.

## Struktur Proyek

```
dashboard-kelompok/
├── app.py              ← Backend Flask (server)
├── requirements.txt    ← Dependensi Python
├── README.md
├── frontend/
│   └── index.html      ← Halaman dashboard (semua-dalam-satu)
└── img/                ← Foto anggota (opsional)
    ├── member1.jpg
    ├── member2.jpg
    └── member3.jpg
```

## Cara Menjalankan

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Jalankan server
```bash
python app.py
```

### 3. Buka browser
```
http://localhost:5000
```

---

## Cara Kustomisasi

### Ganti info anggota
Buka `frontend/index.html`, cari bagian `<!-- Member 1 -->` dst, lalu ubah:
- **Nama** di `<div class="mc-name">`
- **Role** di `<div class="mc-role">`
- **Bio** di `<p class="mc-bio">`
- **Skills** di tag `<span class="sk">`

### Ganti foto anggota
Letakkan file foto di folder `img/` dengan nama:
- `member1.jpg`, `member2.jpg`, `member3.jpg`

### Ganti data grafik
Di bagian `<script>` paling bawah `index.html`, cari array `data:` pada masing-masing chart dan ganti angkanya.

---

## Deploy Online (Gratis)

### Tanpa Flask (Pure HTML)
Buka langsung `frontend/index.html` di browser, atau upload ke:
- **Netlify**: drag & drop folder `frontend/`
- **GitHub Pages**: push ke repo, aktifkan Pages

### Dengan Flask (Server Python)
- **Railway**: [railway.app](https://railway.app)
- **Render**: [render.com](https://render.com)
- **PythonAnywhere**: [pythonanywhere.com](https://pythonanywhere.com)
