from tkinter import *
from datetime import date
window = Tk()
window.title("This cant be beaton")
window.geometry("600x700")
lbl = Label(text = "hey there !",fg="white",bg= "blue",height = 1,width = 300)
name_lbl = Label(text = "Enter your full name please! :",bg = "red")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome here is the todays date :"
    greet = "Hello "+ name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height = 3)
btn = Button(text = "Begin" , command = display , height = 1,bg= "black",fg= "green")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()