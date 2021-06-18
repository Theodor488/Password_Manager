from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_password = []
    random_length = random.randint(8, 12)
    for _ in range(random_length):
        random_password.append(random.choice(chars))

    random_password = ''.join(random_password)
    password_input.delete(0, END)
    password_input.insert(0, random_password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showwarning("Oops", "Don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"Website: {website} - Email: {email} - Password: {password}\n")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
            f.close()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Website
website_label = Label(text="Website: ", font=("Arial", 12))
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")

#Email
email_label = Label(text="Email/Username: ", font=("Arial", 12))
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

#Password
password_label = Label(text="Password: ", font=("Arial", 12))
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

#Generate Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

#Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()



