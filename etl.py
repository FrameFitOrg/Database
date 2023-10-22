import sqlite3
import mysql.connector

# Fungsi untuk mengekstrak data dari SQLite
def extract_data_from_sqlite():
    conn = sqlite3.connect('database.db')  # Menghubungkan ke database SQLite
    cursor = conn.cursor()

    # Menjalankan query SQL untuk mengambil data dari tabel SQLite
    tabel_wajah_query = 'SELECT * FROM wajah'
    tabel_frame_query = 'SELECT * FROM frame'
    tabel_optik_query = 'SELECT * FROM optik'
    cursor.execute(tabel_wajah_query)
    data_wajah = cursor.fetchall()
    cursor.execute(tabel_frame_query)
    data_frame = cursor.fetchall()
    cursor.execute(tabel_optik_query)
    data_optik = cursor.fetchall()

    # Menutup koneksi SQLite
    conn.close()

    return data_wajah, data_frame, data_optik

# Fungsi untuk menggabungkan data dari tabel wajah, kacamata, dan optik ke dalam tabel transformasi
def transform_data(extracted_data):
    data_wajah, data_frame, data_optik = extracted_data

    # Menggabungkan data dari tabel wajah, kacamata, dan optik
    transformed_data = []
    for wajah in data_wajah:
        for frame in data_frame:
            for optik in data_optik:
                transformed_data.append({
                    'id_wajah': wajah[0],
                    'bentuk_wajah': wajah[1],
                    'gambar_wajah': wajah[2],
                    'id_frame': frame[0],
                    'bentuk_frame': frame[1],
                    'gambar_frame': frame[2],
                    'id_optik': optik[0],
                    'optik': optik[1],
                    'link_optik': optik[2]
                })

    return transformed_data

# Fungsi untuk memuat data ke MariaDB
def load_data_to_mysql(transformed_data):
    conn = mysql.connector.connect(
        host='localhost',  # Ganti dengan host MariaDB Anda
        user='root',    # Ganti dengan username MariaDB Anda
        password='',  # Ganti dengan password MariaDB Anda
        database='framefit'  # Ganti dengan nama database MariaDB target
    )
    cursor = conn.cursor()

    # Menjalankan query SQL untuk memasukkan data ke dalam tabel MariaDB untuk wajah
    insert_query_wajah = 'INSERT INTO wajah (id_wajah, bentuk_wajah, gambar) VALUES (%s, %s, %s)'
    cursor.executemany(insert_query_wajah, [(item['id_wajah'], item['bentuk_wajah'], item['gambar_wajah']) for item in transformed_data])

    # Menjalankan query SQL untuk memasukkan data ke dalam tabel MariaDB untuk frame
    insert_query_frame = 'INSERT INTO frame (id_frame, frame, gambar) VALUES (%s, %s, %s)'
    cursor.executemany(insert_query_frame, [(item['id_frame'], item['bentuk_frame'], item['gambar_frame']) for item in transformed_data])

    # Menjalankan query SQL untuk memasukkan data ke dalam tabel MariaDB untuk optik
    insert_query_optik = 'INSERT INTO optik (id_optik, optik, link_optik) VALUES (%s, %s, %s)'
    cursor.executemany(insert_query_optik, [(item['id_optik'], item['optik'], item['link_optik']) for item in transformed_data])

    # Melakukan commit dan menutup koneksi MariaDB
    conn.commit()
    conn.close()

# Menjalankan ETL 
def main():
    # Mengekstrak data dari SQLite
    extracted_data = extract_data_from_sqlite()
    transformed_data = transform_data(extracted_data)
    load_data_to_mysql(transformed_data)
    print('Berhasil')

if __name__ == "__main__":
    main()
