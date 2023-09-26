import sqlite3

# Buat koneksi ke database
conn = sqlite3.connect('framefit.db')

# Buat objek kursor
cursor = conn.cursor()

# Fungsi untuk membuat tabel
def tabel_baru_wajah():
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS wajah (
            id_wajah INTEGER NOT NULL PRIMARY KEY, 
            bentuk_wajah TEXT NOT NULL, 
            gambar BLOB NOT NULL) 
    ''') 

def tabel_baru_kacamata():
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS kacamata (
            id_kacamata INTEGER PRIMARY KEY, 
            kacamata INTEGER NOT NULL, 
            gambar BLOB NOT NULL) 
    ''') 

def tabel_baru_optik():
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS optik (
            id_optik INTEGER PRIMARY KEY, 
            toko_optik INTEGER NOT NULL, 
            link_url TEXT NOT NULL) 
    
    ''') 

def tabel_baru_admin():
    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS admin (
            id_admin INTEGER PRIMARY KEY, 
            password TEXT NOT NULL) 
    
    ''') 


# Fungsi perintah SQL untuk menginput tabel-tabel dalam database
def masukin_data_kacamata(id_kacamata, kacamata, gambar):
    cursor.execute('''
        INSERT INTO IF NOT EXISTS kacamata (id_kacamata, kacamata, gambar) 
        VALUES (?,?,?)

    ''', (id_kacamata, kacamata, gambar)
    )
def masukin_data_wajah(id_wajah, bentuk_wajah, gambar):
    cursor.execute('''
        INSERT INTO IF NOT EXISTS wajah (id_wajah, bentuk_wajah, gambar) 
        VALUES (?,?,?)

    ''', (id_wajah, bentuk_wajah, gambar)
    )
def masukin_data_optik(id_optik, toko_optik, link_url):
    cursor.execute('''
        INSERT INTO IF NOT EXISTS optik (id_optik, toko_optik, link_url) 
        VALUES (?,?,?)

    ''', (id_optik, toko_optik, link_url)
    )
def masukin_data_admin(id_admin, password):
    cursor.execute('''
        INSERT INTO IF NOT EXISTS admin (id_admin, password) 
        VALUES (?,?)

    ''', (id_admin, password)
    )

# Fungsi ambil data
cursor.execute('''
    SELECT * FROM kacamata

''', 
data = cursor.fetchall()
for row in data:
    print(row)
)

cursor.execute('''
    SELECT * FROM wajah ( 
         
    )

''')

# Commit perubahan dan tutup koneksi
conn.commit()
conn.close()
