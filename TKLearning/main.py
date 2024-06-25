import tkinter

window = tkinter.Tk()
window.title("Python TKinter Tutorial")
window.minsize(width=700, height=500)


def window_get_h():
    window.update()
    window_height = window.winfo_height()
    return window_height


def window_get_w():
    window.update()
    window_width = window.winfo_width()
    return window_width


def label_get_w(l):
    l.update()
    label_width = l.winfo_width()
    return label_width


def label_get_h(l):
    l.update()
    label_height = l.winfo_height()
    return label_height


def input_get_w(i):
    i.update()
    input_width = i.winfo_width()
    return input_width


def input_get_h(i):
    i.update()
    input_height = i.winfo_height()
    return input_height


def button_get_w(b):
    b.update()
    button_width = b.winfo_width()
    return button_width


def button_get_h(b):
    b.update()
    button_height = b.winfo_height()
    return button_height


def click_button():
    user_input = my_entry.get()
    print(user_input)


# label
my_label = tkinter.Label(window, text="Hello World",font=("Arial", 20,"italic"))
# my_label.config(bg="white", fg="black")
# my_label.pack(side="left")

my_label.place(x=0,y=0)
my_label.place(x=window_get_w()/2-label_get_w(my_label)/2,y=0)


# entry
my_entry = tkinter.Entry(window, width=50)
# my_entry.pack()
my_entry.place(x=0,y=0)
my_entry.place(x=window_get_w()/2-input_get_w(my_entry)/2,y=label_get_h(my_label)+10)



# button
my_button = tkinter.Button(window, text="Click Me", command=click_button)
# my_button.pack()
my_button.place(x=0,y=0)
my_button.place(x=window_get_w()/2-button_get_w(my_button)/2,y=label_get_h(my_label)+input_get_h(my_entry) +20)


window.mainloop()