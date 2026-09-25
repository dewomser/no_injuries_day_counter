import datetime
import threading
import time
import tkinter as tk


def save_counter(value):
    with open("dump.txt", "w", encoding="utf-8") as file:
        file.write(f"{value}")


def print_every_n_seconds(n=60):
    global counter
    while True:
        time.sleep(n)
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 42:
            counter += 1
            label1.config(text=counter)
            save_counter(counter)


def n_click():
    global counter
    counter += 1
    label1.config(text=counter)
    save_counter(counter)


def n_click_100():
    global counter
    counter += 100
    label1.config(text=counter)
    save_counter(counter)


def n_click_1():
    global counter
    counter -= 1
    label1.config(text=counter)
    save_counter(counter)


def n_click_reset():
    global counter
    counter = 0
    label1.config(text=counter)
    save_counter(counter)


# main window
root = tk.Tk()
root.configure(background="green")
root.geometry("1280x720")
root.title("Unfallfrei Counter")

counter = 0
startwert = 0

if startwert == 0:
    try:
        with open("dump.txt", "r", encoding="utf-8") as file:
            startwert = int(file.readline().strip() or 0)
    except FileNotFoundError:
        startwert = 0
    counter = startwert

label1 = tk.Label(root, text=startwert, bg="green", fg="white")
m_button_2 = tk.Button(text="+ 1", bg="black", fg="white", command=n_click)
m_button_3 = tk.Button(text="- 1", bg="black", fg="white", command=n_click_1)
m_button_4 = tk.Button(text="Reset", bg="black", fg="white", command=n_click_reset)
m_button_5 = tk.Button(text="+100", bg="black", fg="white", command=n_click_100)

m_button_2.config(font=("arial"))
m_button_3.config(font=("arial"))
m_button_4.config(font=("arial"))
m_button_5.config(font=("arial"))
label1.config(font=("arial", 350, "bold"))

label1.pack()
m_button_4.place(x=10, y=10, height=20, width=110)
m_button_3.place(x=10, y=30, height=20, width=30)
m_button_2.place(x=40, y=30, height=20, width=30)
m_button_5.place(x=70, y=30, height=20, width=50)

thread = threading.Thread(target=print_every_n_seconds, daemon=True)
thread.start()

root.mainloop()
