from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='template')
db_path = "database.db"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enter')
def get_wajah():
    return render_template('wajah.html')

@app.route('/addrec', methods=['POST'])
def addrec():
    try:
        # Mengambil data dari formulir
        id_wajah = request.form['id']
        bentuk_wajah = request.form['wajah']
        gambar = request.files['gambar'].read()

        # Menyimpan data ke dalam database SQLite
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO wajah (id_wajah, bentuk_wajah, gambar) VALUES (?, ?, ?)",
                           (id_wajah, bentuk_wajah, sqlite3.Binary(gambar)))
            conn.commit()

        print("Berhasil")
        return redirect('/')  # Mengarahkan pengguna kembali ke halaman utama setelah menyimpan data.

    except Exception as e:
        print(str(e))
        print("Terjadi Kesalahan Dalam Menginput")
        return redirect('/')
    
@app.route('/list')
def list():
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM wajah")
            rows = cursor.fetchall()

        return render_template("hasil.html", rows=rows)

    except Exception as e:
        print(str(e))
        return "Terjadi kesalahan saat mengambil data dari database."

if __name__ == '__main__':
    app.run(debug=True)
