from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():

    site = site_input.get()
    email = name_input.get()
    password = password_input.get()
    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }

    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        site_input.delete(0, END)
        password_input.delete(0, END)
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:        
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:        
                json.dump(data, f, indent=4)


# ---------------------------- SITE SEARCH ------------------------------- #


def search_site():
    site = site_input.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Data file does not exist.")
    else:
        if site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Entry for {site} does not exist.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1, column=0)

site_input = Entry(width=17)
site_input.focus()
site_input.grid(row=1, column=1,)

search_button = Button(text="Search", command=search_site)
search_button.grid(row=1, column=2)

name_label = Label(text="Email/Username:")
name_label.grid(row=2, column=0)

name_input = Entry(width=35)
name_input.insert(END, "adoubtfullogic@gmail.com")
name_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
