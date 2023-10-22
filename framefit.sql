CREATE DATABASE IF NOT EXISTS framefit;

-- Tabel user
CREATE TABLE IF NOT EXISTS user (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    username_user VARCHAR(15),
    password_user TEXT NOT NULL
);

-- Tabel gambar wajah
CREATE TABLE IF NOT EXISTS gambar_wajah (
    id_gambar INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_wajah VARCHAR(15),
    bentuk_wajah BLOB NOT NULL 
);

-- Tabel kacamata 
CREATE TABLE IF NOT EXISTS kacamata (
    id_kacamata INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kacamata VARCHAR(20), 
    gambar_kacamata BLOB NOT NULL
);

-- Tabel optik
CREATE TABLE IF NOT EXISTS optik (
    id_optik INTEGER PRIMARY KEY AUTOINCREMENT,
    toko_optik VARCHAR(50),
    link VARCHAR(50)
);
