from tkinter import
from PIL import Imagetk,Image
import sqlite3

# root = Tk()
# root.title('Aplikasi Admin')
# root.iconbitmap()
# root.geometry("400x400")

conn = sqlite3.connect('framefit.db')
c = conn.cursor()

