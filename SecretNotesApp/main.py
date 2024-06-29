import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pybase64

window = tk.Tk()
window.title('Secret Notes')
window.config(padx=80, pady=20)


def save_and_encrypt():
    key = my_entry3.get()

    if len(my_entry1.get()) == 0 or len(my_entry2.get(1.0,tk.END)) == 0 or len(my_entry3.get()) == 0:
        messagebox.showinfo('Error!', 'Please enter all')
    else:
        my_entry3.delete(0, tk.END)
        my_entry3.focus()
        if key == "tkinter":
            file_path = open(file="secret notes/secret_notes.txt", mode='a')
            note_title = my_entry1.get()
            my_entry1.delete(0, tk.END)
            file_path.write(note_title)
            file_path.write("\n")
            note = my_entry2.get(1.0, tk.END)
            my_entry2.delete(1.0, tk.END)
            note = note.encode("ascii")
            note = pybase64.b64encode(note)
            note = note.decode("ascii")
            file_path.write(note)
            file_path.write("\n")
            file_path.close()


def decrypt():
    key = my_entry3.get()
    my_entry3.delete(0, tk.END)

    if key == "tkinter":
        note = my_entry2.get(1.0, tk.END)
        note = note.encode("ascii")
        note = pybase64.b64decode(note)
        note = note.decode("ascii")
        my_entry2.delete(1.0, tk.END)
        my_entry2.insert(1.0, note)


image = Image.open("secret notes/logo.png")
resized_img = image.resize((200,200))
img = ImageTk.PhotoImage(resized_img)

image_label = tk.Label(window, image=img)
image_label.pack()

my_label1 = tk.Label(window, text="Enter your title")
my_label1.pack(padx=5, pady=5)

my_entry1 = tk.Entry(window,width=33)
my_entry1.pack(padx=5, pady=5)
my_entry1.focus()

my_label2 = tk.Label(window, text="Enter your secret note")
my_label2.pack(padx=5, pady=5)

my_entry2 = tk.Text(window,width=25, height=15)
my_entry2.pack(padx=5, pady=5)

my_label3 = tk.Label(window, text="Enter master key")
my_label3.pack(padx=5, pady=5)

my_entry3 = tk.Entry(window, width=33)
my_entry3.pack(padx=5, pady=5)

my_button1 = tk.Button(window, text="Save & Encrypt", command=lambda: save_and_encrypt())
my_button1.pack(padx=5, pady=5)

my_button2 = tk.Button(window, text="Decrypt", command=lambda: decrypt())
my_button2.pack(padx=5, pady=5)


window.mainloop()
