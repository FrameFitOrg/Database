# import sqlite3

# # Membuka koneksi ke database (atau membuatnya jika belum ada)
# conn = sqlite3.connect('framefit.db')

# # Membuka cursor untuk mengeksekusi perintah SQL
# cursor = conn.cursor()

# # Membaca gambar sebagai byte array
# with open('kemal.jpg', 'rb') as file:
#     image_data = file.read()

# # Menyimpan gambar ke dalam database sebagai tipe data BLOB
# cursor.execute("INSERT INTO kacamata VALUES (?,NULL,?)", (sqlite3.Binary(image_data),))

# # Menyimpan perubahan ke dalam database
# conn.commit()

# # Menutup koneksi ke database
# conn.close()
 

import sqlite3
import os

# Menggunakan os.path.join untuk menggabungkan direktori dengan nama file
directory_path = 'C:/Users/lenovo/WPy64-310111/scripts/Database'
database_path = 'database.db'

# Membuka koneksi ke database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Loop melalui berkas gambar di direktori
for filename in os.listdir(directory_path):
    if filename.endswith('kemal.jpg'):
        with open(os.path.join(directory_path, filename), 'rb') as file:
            image_data = file.read()
            frame_name = filename  # Frame name is assumed to be the filename
            
            # Masukkan data ke dalam tabel
            cursor.execute('INSERT INTO frame (id_frame, frame, gambar) VALUES (?, ?, ?)',
                           (frame_name, sqlite3.Binary(image_data)))
            conn.commit()

# Tutup koneksi ke database setelah selesai
conn.close()
