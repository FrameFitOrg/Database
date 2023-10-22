
import sqlite3
from tkinter import *
from tkinter import filedialog

# Fungsi untuk memilih gambar dari file dialog
def choose_image():
    file_path = filedialog.askopenfilename()
    entry_image_path.delete(0, END)
    entry_image_path.insert(0, file_path)

# Fungsi untuk menyimpan data ke dalam database
def save_data():
    id_frame = entry_id_frame.get()
    nama_frame = entry_nama_frame.get()
    image_path = entry_image_path.get()
    
    if id_frame and nama_frame and image_path:
        try:
            with open(image_path, 'rb') as file:
                image_data = file.read()
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO frame (id_frame, frame, gambar) VALUES (?, ?, ?)",
                           (id_frame, nama_frame, sqlite3.Binary(image_data)))
            connection.commit()
            connection.close()
            status_label.config(text="Data berhasil disimpan!")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")
    else:
        status_label.config(text="Semua kolom harus diisi!")

# Membuat jendela utama
root = Tk()
root.title("Input Data Frame")

# Label dan input untuk id_frame
label_id_frame = Label(root, text="ID Frame:")
label_id_frame.grid(row=0, column=0, padx=10, pady=10)
entry_id_frame = Entry(root, width=20)
entry_id_frame.grid(row=0, column=1, padx=10, pady=10)

# Label dan input untuk nama_frame
label_nama_frame = Label(root, text="Nama Frame:")
label_nama_frame.grid(row=1, column=0, padx=10, pady=10)
entry_nama_frame = Entry(root, width=20)
entry_nama_frame.grid(row=1, column=1, padx=10, pady=10)

# Tombol dan input untuk memilih gambar
btn_choose_image = Button(root, text="Pilih Gambar", command=choose_image)
btn_choose_image.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
entry_image_path = Entry(root, width=40)
entry_image_path.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Tombol untuk menyimpan data
btn_save = Button(root, text="Simpan", command=save_data)
btn_save.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Label untuk menampilkan status
status_label = Label(root, text="")
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Memulai loop utama tkinter
root.mainloop()
