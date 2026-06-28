from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(
    __name__,
    template_folder='frontend',
    static_folder='frontend'
)

# ── Halaman utama ──────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

# ── Static assets (CSS, JS, gambar) ───────────────────────
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

# ── Contoh API endpoint (opsional, bisa dikembangkan) ─────
@app.route('/api/info')
def api_info():
    return jsonify({
        "kelompok": "Kelompok Kita",
        "anggota": [
            {"nama": "Anggota 1", "role": "Data Analyst"},
            {"nama": "Anggota 2", "role": "Visualisasi Data"},
            {"nama": "Anggota 3", "role": "Backend Developer"},
        ],
        "status": "aktif"
    })

# ── Jalankan server ────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    print("=" * 45)
    print("  Dashboard Kelompok - Server Berjalan")
    print(f"  Port: {port}")
    print("=" * 45)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )