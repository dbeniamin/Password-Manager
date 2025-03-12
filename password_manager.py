from tkinter import *
from tkinter import messagebox
import random
import base64
# import pyperclip

FONT_NAME = "Calibri"
GREEN = "#008170"
BLUE = "#0766AD"
RED = "#B31312"
GRAY = "#E5CFF7"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # delete the pass every time you press the generate button
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # use list comprehension to loop the available options in the lists the random generated number by saved variables
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    # shuffle the characters in the final list
    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    # copy the pass to clipboard
    # pyperclip.copy(password)


# ---------------------------- ENCODE/DECODE FUNCTIONS ------------------------------- #
def encode_password(password):
    """Encode the password using base64"""
    # convert string to bytes, encode with base64, then convert back to string
    encoded_bytes = base64.b64encode(password.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def decode_password(encoded_password):
    """Decode the base64 encoded password"""
    # convert string to bytes, decode with base64, then convert back to string
    decoded_bytes = base64.b64decode(encoded_password.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    website_entry = input_website.get().lower()
    try:
        with open("data.txt", "r") as data_file:
            for line in data_file:
                stored_website, email, encoded_password = line.strip().split(" | ")
                if website_entry == stored_website.lower():
                    # decode the password before displaying it
                    decoded_password = decode_password(encoded_password)
                    input_password.delete(0, END)
                    input_password.insert(0, decoded_password)  # insert decoded password
                    break
            else:
                messagebox.showinfo(title=website_entry, message=f"No password found for {website_entry}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except Exception as e:
        messagebox.showinfo(title="Error", message=f"An error occurred: {e}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = input_website.get().lower()
    email_entry = input_username.get()
    pass_entry = input_password.get()

    # encode the password before saving
    encoded_password = encode_password(pass_entry)

    # check if all fields are filled
    if len(website_entry) == 0 or len(pass_entry) == 0 or len(email_entry) == 0:
        messagebox.showinfo(title="Error !!", message="Please fill out all the fields !")
        return

    try:
        with open("data.txt", "r") as data_file:
            lines = data_file.readlines()

        website_exists = False
        modified_lines = []

        # Check if website exists and update if needed
        for line in lines:
            parts = line.strip().split(" | ")
            if len(parts) == 3: 
                stored_website, stored_email, _ = parts
                if website_entry == stored_website.lower():
                    line = f"{website_entry} | {email_entry} | {encoded_password}\n"
                    website_exists = True
            modified_lines.append(line)

        # write back all lines (with any updates)
        with open("data.txt", "w") as data_file:
            data_file.writelines(modified_lines)

        if not website_exists:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_entry} | {email_entry} | {encoded_password}\n")

        # show success message and clear fields
        messagebox.showinfo(title="Success", message="Password saved successfully!")
        input_website.delete(0, END)
        input_username.delete(0, END)
        input_password.delete(0, END)

    except FileNotFoundError:
        # if file doesn't exist, create it and add the first entry
        with open("data.txt", "w") as data_file:
            data_file.write(f"{website_entry} | {email_entry} | {encoded_password}\n")
        messagebox.showinfo(title="Success", message="Password saved successfully!")
        input_website.delete(0, END)
        input_username.delete(0, END)
        input_password.delete(0, END)

    except Exception as e:
        messagebox.showinfo(title="Error", message=f"An error occurred: {e}")


# ---------------------------- UI SETUP ------------------------------- #

""" adding all the elements required for the UI - buttons, entry fields, labels """
""" input field and buttons need to have the padx / pady passed in the .grid() command """
""" .config(padx= x value , pady= y value) only works for labels """

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website :", font=(FONT_NAME, 15, "bold"))
label_website.grid(row=1, column=0)
label_website.config(padx=5, pady=5)

label_username = Label(text="Email/Username :", font=(FONT_NAME, 15, "bold"))
label_username.grid(row=2, column=0)
label_username.config(padx=5, pady=5)

label_password = Label(text="Password :", font=(FONT_NAME, 15, "bold"))
label_password.grid(row=3, column=0)
label_password.config(padx=5, pady=5)

input_website = Entry(width=40, font=(FONT_NAME, 15, "bold"))
input_website.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
# use .focus() to have the mouse in that specific input field.
input_website.focus()

input_username = Entry(width=40, font=(FONT_NAME, 15, "bold"))
input_username.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

input_password = Entry(width=21, font=(FONT_NAME, 15, "bold"))
input_password.grid(row=3, column=1, padx=5, pady=5)

button_generate = Button(text="Generate Password", font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=BLUE,
                         command=generate_pass)
button_generate.grid(row=3, column=2, padx=5, pady=5)

button_add = Button(text="Add", width=40, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=GREEN, command=save)
button_add.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

button_show_password = Button(text="Show Password", width=40, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=RED,
                              command=show_password)
button_show_password.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()

