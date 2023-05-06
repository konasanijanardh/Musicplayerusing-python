#required Libraries
from tkinter import *
from random import randint

root = Tk()
root.title('CodeClause | Task-1 - Random PAssword')
root.geometry('500x300')
root.config(background = "#002B5B")  

#F9D949
my_password = chr(randint(33,126))

#generating the password
def click():

    #Convert str to int
    pass_length = int(my_entry.get())

    #Variable to store password
    my_password = ''

    for i in range(pass_length):
        my_password += chr(randint(33,126))

    #Output to screen
    password.insert(0, my_password)
    

my_label = LabelFrame(root, text="How many characters?",bg="#ABC4AA",fg="#000", bd=1, font=("Helvetica",18))
my_label.pack(pady=20)

#Entry Box For Take Length Of Characters
my_entry = Entry(my_label, font=("Helvetica",24))
my_entry.pack(pady=20, padx=20)

#Entry box For Our Returned Password
password = Entry(root, font=("Helvetica",25),bg="#002B5B",fg='#F9D949', justify=CENTER , width=30,bd=0)
password.pack(pady=10)

#Creating buttons
my_btn = Button(root, command=click , text="Generate",bg="#03001C",fg='#F9D949',font=("Helvetica",18))
my_btn.pack(pady=20)

root.mainloop()


