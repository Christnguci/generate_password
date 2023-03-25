import tkinter as tk
from tkinter import Canvas,Image,messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pasword_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def Save():
    website=website_entry.get()
    email=email_username_entry.get()
    password=pasword_entry.get()
    if website=="" or email =="" or password=="":
        messagebox.showwarning("Alert","Lack of information ! ")
    else:
        is_ok=messagebox.askyesno("Save",f"Do you want to save Website: {website}  \n Email:  {email} \n Password: {password} \n  ||  Yes or No || ")
        if is_ok :
            with  open("data.txt",'a') as data_file :
                data_file.write(f"{website} | {email} | {password}  \n")
                website_entry.delete(0, tk.END)
                pasword_entry.delete(0,tk.END)

 

# ---------------------------- UI SETUP ------------------------------- #

Window=tk.Tk()
Window.title("Pasword Manager")
Window.config(padx=50,pady=50)

logo=tk.PhotoImage(file="logo.png")
setCanvas=Canvas(Window,width=200,height=200)
setCanvas.create_image(100,100,image=logo)
setCanvas.grid(row=0,column=1)

#Lable

website_lable=tk.Label(text="Website: ")
website_lable.grid(row=1,column=0)
email_username_lable=tk.Label(text="Email/Username: ")
email_username_lable.grid(row=2,column=0)
password_lable=tk.Label(text="Password: ")
password_lable.grid(row=3,column=0)



#Entries
website_entry=tk.Entry(width=55)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_username_entry=tk.Entry(width=55)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0, "cuongdeptrai@gmail.com")
pasword_entry=tk.Entry(width=36)
pasword_entry.grid(row=3,column=1)
generate_button=tk.Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)
add_button=tk.Button(text="Add",width=46,command=Save)
add_button.grid(row=4,column=1,columnspan=2)








Window.mainloop()