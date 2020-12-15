# import modules

import random
import time
from tkinter import *


# Designing window for registration
from db_conn import *

db_conn()  # needs to be first


def register():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Register")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()
    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width="300", height="2", font=("Ubuntu", 33)).pack()
    Label(main_screen, text="").pack()
    username_label = Label(main_screen, text="Username ")
    username_label.pack()
    username_entry = Entry(main_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(main_screen, text="Password ")
    password_label.pack()
    password_entry = Entry(main_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Register", width=10, height=2, command=register_user).pack()


# Designing window for login

def login():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Login")
    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width="300", height="2",
          font=("Ubuntu", 33)).pack()
    Label(main_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(main_screen, text="Username ").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(main_screen, text="").pack()
    Label(main_screen, text="Password ").pack()
    password_login_entry = Entry(main_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    for widget in main_screen.winfo_children():
        widget.destroy()

    username_info = username.get()
    password_info = password.get()

    create_user(username_info, password_info)

    Label(main_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(main_screen, text="Back", width=10, height=1, command=login).pack()


# Implementing event on login button

def login_verify():
    for widget in main_screen.winfo_children():
        widget.destroy()

    global user_id
    username1 = username_verify.get()
    password1 = password_verify.get()

    print(check_username(username1))
    print(check_password(password1))
    if check_username(username1):
        if check_password(password1):
            user_id = check_password(password1)[1]
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()


# Designing popup for login success

def login_success():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Success")

    Label(main_screen, text="Login Success").pack()
    Button(main_screen, text="OK", command=lambda:[delete_login_success, menu()]).pack()


# Designing popup for login invalid password

def password_not_recognised():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Success")

    Label(main_screen, text="Invalid Password ").pack()
    Button(main_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Success")

    Label(main_screen, text="User Not Found").pack()
    Button(main_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    main_screen.destroy()


def delete_password_not_recognised():
    main_screen.destroy()


def delete_user_not_found_screen():
    main_screen.destroy()


# Designing Main(first) window

def menu():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Menu")

    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width='300', height='2', font=('Ubuntu', 33)).pack()

    Label(main_screen, text="").pack()
    Button(main_screen, text="Dictionaries", height="2", width="30", command=dictionaries_screen).pack()
    Button(main_screen, text="Distillations", height="2", width="30", command=distillations_screen).pack()
    Button(main_screen, text="Word Count", height="2", width="30", command=word_count_screen).pack()
    Button(main_screen, text="Help", height="2", width="30", command=help_screen).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Start", height="2", width="30", command=main_app).pack()
    Button(main_screen, text="Quit", height="2", width="30", command=quit_program).pack()


def quit_program():
    main_screen.destroy()


def on_enter(event):
    content = entry.get()

    if len(content) > 0:
        word = content.split(' ', 1)[0]
        explanation = content.split(' ', 1)[1]
        word = str(word.title())
        explanation = str(explanation.title())

        print(type(user_id))
        insert_word(word, explanation, user_id[0])

    main_app()


def on_enter_dist(event):

    content = entry_dis.get()
    if len(content) > 0:
        word = content.split(' ', 1)[0]
        explanation = content.split(' ', 1)[1]
        word = str(word.title())
        explanation = str(explanation.title())
        insert_distil(word, explanation, user_id[0])

    distillations_screen()


def main_app():
    for widget in main_screen.winfo_children():
        widget.destroy()
    global entry

    main_screen.title("List")
    main_screen.bind('<Return>', on_enter)

    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width='300', height='2',
          font=('Ubuntu', 33)).pack()

    entry = Entry(main_screen, width='100')
    entry.pack(side=BOTTOM, anchor=N, fill=X, expand=YES)
    main_screen.bind('<Return>', on_enter)
    try:
        Label(main_screen, text=dict_sample_line(dict_name), width='400', height='4', font=('Ubuntu', 16)).pack(side=BOTTOM, anchor=E, expand=YES)
    except NameError:
        Label(main_screen, text=dict_sample_line('PL.csv'), width='400', height='4', font=('Ubuntu', 16)).pack(
            side=BOTTOM, anchor=E, expand=YES)
    Label(main_screen, text="Word", width='30', height='2', font=('Ubuntu', 14)).pack(side=LEFT, anchor=N)
    Label(main_screen, text="Word Count {}".format(word_count(user_id)),  width='30', height='2', font=('Ubuntu', 14)).pack(side=RIGHT, anchor=N)

    Label(main_screen, text="Explanation",  width='30', height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Button(main_screen, text="Back", width=20, height=1, command=menu).pack(side=BOTTOM)
    entry.bind('<Return>', on_enter)


def change_dict(name):
    global dict_name
    dict_name = name
    print(dict_name)


def dictionaries_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Dictionaries")

    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width='300', height='2',
          font=('Ubuntu', 33)).pack()

    Label(main_screen, text="").pack()
    Button(main_screen, text="German", height="2", width="30", command=lambda:[change_dict('DE.csv'), menu()]).pack()
    Button(main_screen, text="Spanish", height="2", width="30", command=lambda:[change_dict('ES.csv'), menu()]).pack()
    Button(main_screen, text="French", height="2", width="30", command=lambda:[change_dict('FR.csv'), menu()]).pack()
    Button(main_screen, text="Polish", height="2", width="30", command=lambda:[change_dict('PL.csv'), menu()]).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Back", height="2", width="30", command=menu).pack()


def distillations_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()

    global entry_dis

    main_screen.title("Distillations")

    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width='300', height='2',
          font=('Ubuntu', 33)).pack()

    Label(main_screen, text="").pack()
    entry_dis = Entry(main_screen, width='100')
    entry_dis.pack(side=BOTTOM, anchor=N, fill=X, expand=YES)
    main_screen.bind('<Return>', on_enter_dist)
    Label(main_screen, text=oldest_word(user_id), width='500', height='2', font=('Ubuntu', 14)).pack(side=BOTTOM,
                                                                                                           anchor=N,
                                                                                                           expand=YES)
    Label(main_screen, text="Word", width='30', height='2', font=('Ubuntu', 14)).pack(side=LEFT, anchor=N)
    Label(main_screen, text="Word Count", width='30', height='2', font=('Ubuntu', 14)).pack(side=RIGHT, anchor=N)
    Label(main_screen, text="Explanation", width='30', height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Button(main_screen, text="Back", width=20, height=1, command=menu).pack(side=BOTTOM)
    Label(main_screen, text="").pack()


def word_count_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Word Count")

    Label(main_screen, text="Gold List", fg='#DAA520', bg='#333333', width="300", height="2", font=("Ubuntu", 33)).pack()
    Label(main_screen, text="").pack()

    Label(main_screen, text="").pack()

    Label(main_screen, text="Word Count", width='10', height='2', font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text=word_count(user_id), width='10', height='2', font=('Ubuntu', 18)).pack(side=TOP)
    Button(main_screen, text="Back", width=10, height=1, command=menu).pack(side=BOTTOM)


def help_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()

    main_screen.title("Help")

    Label(main_screen, text="").pack()

    Label(main_screen, text="").pack()

    Label(main_screen, text="If you struggle with learning a foreign language", height='2', font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="or if you're tired of flashcards and memorising glossaries", height='2', font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="then you may find this program useful.", height='2', font=('Ubuntu', 14)).pack(
        side=TOP)
    Label(main_screen, text="You start by typing words from the dictionary.", height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="Then you wait for at least two weeks.", height='2', font=('Ubuntu', 14)).pack(
        side=TOP)
    Label(main_screen, text="When you revisit the words again ", height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="you should be able to remember around 30% of them.", height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="You then repeat the process until you remember more and more words.", height='2',
          font=('Ubuntu', 14)).pack(side=TOP)
    Label(main_screen, text="", height='2', font=('Ubuntu', 14)).pack()
    Button(main_screen, text="Back", width=10, height=1, command=menu).pack(side=BOTTOM)


def dict_sample_line(name):
    print(name)
    if name is None:
        file_name = 'dicts/PL.csv'
    else:
        file_name = 'dicts/{}'.format(name)

    count = len(open(file_name).readlines())
    n = random.randrange(1, count)
    try:
        line = open(file_name, 'r').readlines()[n]
        line = line.replace(';', '-')
        line = line.replace(',', '')
        line = line.replace('  ', ' ')
        line = line.replace('   ', ' ')
        line = line.replace('    ', ' ')
        line = line.replace('     ', ' ')
        line = line.replace('      ', ' ')
        line = line.replace('       ', ' ')

        output = line.title()
        return output
    except ValueError as e:
        print(e)


def main_account_screen():

    global main_screen
    main_screen = Tk()
    main_screen.geometry("1280x860")
    main_screen.title("Account Login")
    Label(text="Gold List", fg='#DAA520', bg='#333333', width="300", height="2", font=("Ubuntu", 33)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()


