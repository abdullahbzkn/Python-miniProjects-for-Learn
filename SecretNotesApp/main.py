import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt():
    key = my_entry3.get()
    note = my_entry2.get(1.0, tk.END)
    note_title = my_entry1.get()

    if len(my_entry1.get()) == 0 or len(my_entry2.get(1.0,tk.END)) == 0 or len(my_entry3.get()) == 0:
        messagebox.showinfo('Error!', 'Please enter all')
    else:

        message_encrypted = encode(key, note)

        try:
            with open("secret notes/secret_notes.txt", "a") as data_file:
                data_file.write(f'\n{note_title}\n{message_encrypted}')
        except FileNotFoundError:
            with open("secret notes/secret_notes.txt", "w") as data_file:
                data_file.write(f'\n{note_title}\n{message_encrypted}')
        finally:
            my_entry1.delete(0, tk.END)
            my_entry3.delete(0, tk.END)
            my_entry2.delete("1.0", tk.END)


def decrypt():
    message_encrypted = my_entry2.get("1.0", tk.END)
    key = my_entry3.get()

    if len(message_encrypted) == 0 or len(key) == 0:
        messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        try:
            decrypted_message = decode(key, message_encrypted)
            my_entry2.delete("1.0", tk.END)
            my_entry2.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please make sure of encrypted info.")


window = tk.Tk()
window.title('Secret Notes')
window.config(padx=80, pady=20)

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
