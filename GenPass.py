from tkinter import *
import string
import random
import pyperclip

def Generator():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_char = string.punctuation

    finalStr = small_letters + capital_letters + numbers + special_char
    pass_len =int (len_Box.get()) 

    if choice.get() == 1:
       Field_password.insert(0,random.sample( small_letters+ capital_letters , pass_len))
    # password = random.sample(finalStr,pass_len)
    # Field_password.insert(0,password)
    if choice.get() == 2:
       Field_password.insert(0,random.sample( small_letters+ capital_letters + numbers , pass_len))

    if choice.get() == 3:
       Field_password.insert(0,random.sample( finalStr , pass_len))

def copy():
   copied_password =Field_password.get()
   pyperclip.copy(copied_password.replace(" ",""))

obj = Tk()
obj.config(bg="azure2")
choice = IntVar()
Font = ('arial' ,13,'bold')
PasswordLabel =Label(obj , text= "PASSWORD GENERATOR", font = ('bell mt', 20, 'bold'), bg= "gray20", fg= "white" )
PasswordLabel.grid( padx=5, pady= 10)

weakRadioButton = Radiobutton(obj, text ="Weak", value=1, variable= choice,font=Font)
weakRadioButton.grid(pady= 5)

MediumRadioButton = Radiobutton(obj , text ="Medium", value=2, variable= choice,font=Font)
MediumRadioButton.grid(pady = 5)

StrongRadioButton = Radiobutton(obj , text ="Strong", value=3, variable= choice,font=Font)
StrongRadioButton.grid(pady = 5)

length_Label =Label(obj , text= "PASSWORD LENGTH", font = Font, bg= "gray20", fg= "white" )
length_Label.grid()

len_Box = Spinbox(obj , from_= 4 , to= 12 , width = 5, font = Font)
len_Box.grid()

generateButton = Button(obj, text = 'Generate Password',font =Font , command= Generator)
generateButton.grid(pady = 5)

Field_password = Entry(obj, width = 25, bd = 2 , font=Font)
Field_password.grid(pady= 5)
CopyButton = Button(obj, text = 'Copy Password',font =Font , command= copy)
CopyButton.grid(pady = 5)
Credits = Label(obj, text ='Made by Kajal', font =('bell mt',6))#.pack(side = BOTTOM)
Credits.grid()

obj.mainloop()
