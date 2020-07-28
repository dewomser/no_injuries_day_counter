#from tkinter import *
#1.Zeile ist nur zum Testen deaktiviert.
from tkinter import Tk


# def clipboard_get():
#    r = Tk()
#    r.withdraw()
#    return r.clipboard_get()


import datetime
import threading


#main window
root = Tk()
root.withdraw()
return root.clipboard_get()
root.configure(background="green")
#root.geometry("1024x600")
root.geometry("1280x720")
root.title("Unfallfrei Counter")
#Global roots
counter = 0
startwert = 0

#zeit zähler
def print_every_n_seconds(n=60):
    while True:
        global counter
        time.sleep(n)
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 42:
            counter +=1
            label1.config(text = counter)
            f = open('dump.txt','w') 
            f.write('{}'.format(counter))
            f.close()

thread = threading.Thread(target=print_every_n_seconds, daemon=True)
thread.start()

#Button commands
def nClick():
    global counter
    counter += 1
    label1.config(text = counter)
    # dump : put the data of the object in a file
    f = open('dump.txt','w')
    f.write('{}'.format(counter))
    f.close()


def nClick100():
    global counter
    counter +=100
    label1.config(text = counter)
    f = open('dump.txt','w') 
    f.write('{}'.format(counter))
    f.close()

def nClick1():
    global counter
    counter -= 1
    label1.config(text = counter)
    f = open('dump.txt','w') 
    f.write('{}'.format(counter))
    f.close()

def nClick2():
    global counter
    counter = 0
    label1.config(text = counter)
    f = open('dump.txt','w') 
    f.write('{}'.format(counter))
    f.close()

#buttons

if startwert == 0: 
    fa = open('dump.txt', 'r')
    startwert = fa.readline()
    fa.close()
    counter = int(startwert)



label1 = Label(root, text=startwert, bg="green", fg="white")
mButton2 = Button(text="+ 1", bg="black", fg="white", command = nClick)
mButton3 = Button(text="- 1", bg="black", fg="white", command = nClick1)
mButton4 = Button(text="Reset", bg="black", fg="white", command = nClick2)
mButton5 = Button(text="+100", bg="black", fg="white", command = nClick100)  
#Button Config files
mButton2.config(font=("arial"))
mButton3.config(font=("arial"))
mButton4.config(font=("arial"))
mButton5.config(font=("arial"))
label1.config(font=("arial", 350, "bold"))

label1.pack()
mButton4.place(x=10, y=10, height=20,width=110)
mButton3.place(x=10, y=30, height=20,width=30)
mButton2.place(x=40, y=30, height=20,width=30)
mButton5.place(x=70, y=30, height=20,width=50)

root.mainloop()

