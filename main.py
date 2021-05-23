from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip

# Colors:
BACKGROUND = "#e1e5ea"
TYPING = "#faf3f3"
CLICK = "#a7bbc7"

LABEL_FONT = ("Arial", 10)
PADX = PADY = 3

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(3, 4))]
    password_list += [choice(numbers) for _ in range(randint(3, 4))]
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()

    if website == '' or user_name == '' or password == '':
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user_name} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {user_name} | {password}\n")
            website_entry.delete(0, END)
            user_name_entry.delete(0, END)
            user_name_entry.insert(0, "gmail@gmail.com")
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
widows = Tk()
widows.title("Password Manager")
widows.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:", font=LABEL_FONT, bg=BACKGROUND)
website_label.grid(column=0, row=1, sticky="E")
website_label.config(padx=PADX, pady=PADY)

# Email/User_name Label
mail_user_name_label = Label(text="Email/Username:", font=LABEL_FONT, bg=BACKGROUND)
mail_user_name_label.grid(column=0, row=2, sticky="E")
mail_user_name_label.config(padx=PADX, pady=PADY)

# Password Label
password_label = Label(text="Password:", font=LABEL_FONT, bg=BACKGROUND)
password_label.grid(column=0, row=3, sticky="E")
password_label.config(padx=PADX, pady=PADY)

# Website Entry
website_entry = Entry(width=49, bg=TYPING)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/User_name Entry
user_name_entry = Entry(width=49, bg=TYPING)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "gmail@gmail.com")

# Password Entry
password_entry = Entry(width=30, bg=TYPING)
password_entry.grid(column=1, row=3)

# Generate_password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
generate_password_button.config(padx=PADX, pady=PADY)

# Add button
add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(padx=0, pady=0)

widows.mainloop()
