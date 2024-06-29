import tkinter as tk

window = tk.Tk()
window.minsize(600, 400)
window.title('BMI Calculator')


def window_get_w():
    window.update()
    window_w = window.winfo_width()
    return window_w


def window_get_h():
    window.update()
    window_h = window.winfo_height()
    return window_h


def label_get_w(l):
    l.update()
    label_w = l.winfo_width()
    return label_w


def label_get_h(l):
    l.update()
    label_h = l.winfo_height()
    return label_h


def entry_get_w(e):
    e.update()
    entry_w = e.winfo_width()
    return entry_w


def entry_get_h(e):
    e.update()
    entry_h = e.winfo_height()
    return entry_h


def button_get_w(b):
    b.update()
    button_w = b.winfo_width()
    return button_w


def button_get_h(b):
    b.update()
    button_h = b.winfo_height()
    return button_h


def calculate_bmi():
    global score
    global desc

    kg = my_entry.get()
    cm = my_entry2.get()

    if kg.isdigit() and cm.isdigit():
        kg = int(kg)
        cm = int(cm)
        score = kg / ((cm / 100) ** 2)
        if score < 18.5:
            desc = "Your BMI is {:.2f}. You are under weight".format(score)
        elif 18.5 <= score < 24.9:
            desc = "Your BMI is {:.2f}. You are normal weight".format(score)
        elif 24.9 <= score < 29.9:
            desc = "Your BMI is {:.2f}. You are over weight".format(score)
        elif 29.9 <= score < 34.9:
            desc = "Your BMI is {:.2f}. You are obesity. (class I)".format(score)
        elif 34.9 <= score < 39.9:
            desc = "Your BMI is {:.2f}. You are obesity. (class II)".format(score)
        else:
            desc = "Your BMI is {:.2f}. You are extreme obesity".format(score)

        my_label3.config(text=desc)
        my_label3.place(x=0, y=0)
        my_label3.place(x=window_get_w() / 2 - label_get_w(my_label3) / 2,
                        y=margin * label_get_h(my_label)
                          + pad * (label_get_h(my_label) + label_get_h(my_label2) + entry_get_h(my_entry) + entry_get_h(
                            my_entry2) + button_get_h(my_button)))
    else:
        my_label3.config(text="Please enter valid numbers.")
        my_label3.place(x=window_get_w() / 2 - label_get_w(my_label3) / 2,
                        y=margin * label_get_h(my_label)
                          + pad * (label_get_h(my_label) + label_get_h(my_label2) + entry_get_h(my_entry) + entry_get_h(
                            my_entry2) + button_get_h(my_button)))


margin = 3
pad = 2
score = 0
desc = "blabla"

my_label = tk.Label(window, text="Enter your weight (kg)")
my_label.place(x=0, y=0)
my_label.place(x=window_get_w() / 2 - label_get_w(my_label) / 2, y=margin * label_get_h(my_label))

my_entry = tk.Entry(window)
my_entry.place(x=0, y=0)
my_entry.place(x=window_get_w() / 2 - entry_get_w(my_entry) / 2,
               y=margin * label_get_h(my_label) + pad * label_get_h(my_label))

my_label2 = tk.Label(window, text="Enter your height (cm)")
my_label2.place(x=0, y=0)
my_label2.place(x=window_get_w() / 2 - label_get_w(my_label2) / 2,
                y=margin * label_get_h(my_label) + pad * (label_get_h(my_label) + entry_get_h(my_entry)))

my_entry2 = tk.Entry(window)
my_entry2.place(x=0, y=0)
my_entry2.place(x=window_get_w() / 2 - entry_get_w(my_entry2) / 2,
                y=margin * label_get_h(my_label) + pad * (
                            label_get_h(my_label) + label_get_h(my_label2) + entry_get_h(my_entry)))

my_label3 = tk.Label(window, text="Your BMI is {}. {}".format(score, desc))
my_label3.place(x=0, y=0)
my_label3.place_forget()

my_button = tk.Button(window, text="Calculate", command=lambda: calculate_bmi())
my_button.place(x=0, y=0)
my_button.place(x=window_get_w()/2-button_get_w(my_button)/2,
                y=margin * label_get_h(my_label)
                  + pad * (label_get_h(my_label) + label_get_h(my_label2) + entry_get_h(my_entry) + entry_get_h(
                    my_entry2)))


window.mainloop()
