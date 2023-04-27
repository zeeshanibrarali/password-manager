from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ('courier', 15, 'normal')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_1 = [choice(letters) for _ in range(randint(8, 10))]
    list_2 = [choice(numbers) for _ in range(randint(2, 4))]
    list_3 = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = list_1 + list_2 + list_3
    shuffle(password_list)
    pass_word = "".join(password_list)
    if len(input_3.get()) != 0:
        input_3.delete(0, END)
    input_3.insert(0, pass_word)
    pyperclip.copy(pass_word)


# ---------------------------- SEARCH ------------------------------- #


def searching():
    user_website = input_1.get()
    try:
        with open('data.json', mode='r') as data_file:
            # reading data
            data = json.load(data_file)
            website_1 = data[user_website]
            messagebox.showinfo(title=user_website, message=f'Email : {website_1["Email"]}\nPassword : '
                                                            f'{website_1["Password"]}')
    except FileNotFoundError:
        messagebox.showinfo(title=user_website, message="The relevant data is not present")
    except KeyError:
        messagebox.showinfo(title=user_website, message=f"The {user_website} data is not present")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_website = input_1.get()
    user_email = input_2.get()
    user_password = input_3.get()
    new_data = {
        user_website: {
            "Email": user_email,
            "Password": user_password
        }
    }
    if len(user_website) == 0 or len(user_password) == 0 or len(user_email) == 0:
        messagebox.showinfo(title='oops', message='You can\'t left any field empty')
    else:
        try:
            with open('data.json', mode='r') as data_file:
                # reading data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating data
            data.update(new_data)

            with open('data.json', mode='w') as data_file:
                # write data
                json.dump(data, data_file, indent=4)
        finally:
            input_1.delete(0, END)
            input_3.delete(0, END)
            input_1.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=2, row=1)

website = Label(text='Website       :', font=FONT)
website.grid(column=1, row=2)
Email = Label(text='Email/Username:', font=FONT)
Email.grid(column=1, row=3)
password = Label(text='Password      :', font=FONT)
password.grid(column=1, row=4)

input_1 = Entry(width=35)
input_1.grid(column=2, row=2)
input_1.focus()
input_2 = Entry(width=60)
input_2.grid(column=2, row=3, columnspan=2)
input_2.insert(0, 'zeeshanibrar10987@gmail.com')
input_3 = Entry(width=35)
input_3.grid(column=2, row=4)

generate_pass = Button(text='Generate Password', font=('courier', 10, 'normal'), highlightthickness=0,
                       command=generate_password)
generate_pass.grid(column=3, row=4)
add = Button(text='Add', font=('courier', 10, 'normal'), width=45, highlightthickness=0, command=save)
add.grid(column=2, row=5, columnspan=2)
search = Button(text="Search", font=('courier', 10, 'normal'), highlightthickness=0, width=17, command=searching)
search.grid(column=3, row=2)

window.mainloop()
