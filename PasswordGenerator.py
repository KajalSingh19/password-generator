
from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("300x275")
root.resizable(0,0)
root.config(bg="azure2")
root.title("Generate your Password")
Font = ('arial' ,13,'bold')
Label(root, text = 'PASSWORD GENERATOR' , font ='cambria 15 bold').pack(padx= 5, pady= 10)
Label(root, text ='keep is safely', font ='arial 7  ').pack(side = BOTTOM)

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 20).pack()
pass_str = StringVar()
def Generator():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_char = string.punctuation
    password = ''
    for x in range (0,4):
        password = random.choice(capital_letters) + random.choice(small_letters) + random.choice(numbers) + random.choice(special_char)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = " GENERATE PASSWORD " ,font =("Arial 10 bold") , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack() 


def copy():
   copied_password =pass_str.get()
   pyperclip.copy(copied_password.replace(" "," "))

CopyButton = Button(root, text = 'Copy Password',font =("Arial 10 bold") , command= copy).pack(padx= 5,pady= 10)



root.mainloop()