from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found on your device.")
button = Button(root , text = "Scan For Virus", command = msg)
button.place(x = 250 , y = 250)
root.mainloop()