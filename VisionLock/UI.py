#import modules
 
from tkinter import *
import os
from tkinter import messagebox

# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.geometry("1200x600")
    register_screen.title("MAIN PAGE")
    register_screen.config(bg="#91b4ed")
    register_screen.resizable(0,0)
 
    global username
    global password

    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

 
    Label(register_screen, text="Please enter details below", bg="#4e8ef5", width="103", height="3", font=("Calibri", 18)).place(x=0,y=0)
##    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ", bg="#4e8ef5", font=("Calibri", 18))
    username_lable.place(x=400,y=180)
    username_entry = Entry(register_screen, textvariable=username, bg="#4e8ef5", font=("Calibri", 18))
    username_entry.place(x=700,y=180)
    password_lable = Label(register_screen, text="Password * ", bg="#4e8ef5", font=("Calibri", 18))
    password_lable.place(x=400,y=280)
    password_entry = Entry(register_screen, textvariable=password, show='*', bg="#4e8ef5", font=("Calibri", 18))
    password_entry.place(x=700,y=280)

##    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user, font=("Calibri", 18)).place(x=400,y=480)
 
 
# Designing window for login 
 
def login():

    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.geometry("1200x600")
    login_screen.title("MAIN PAGE")
    login_screen.config(bg="#91b4ed")
    login_screen.resizable(0,0)
    loglbl=Label(login_screen, text="Please enter details below to login", bg="#4e8ef5", width="103", height="3", font=("Calibri", 18))
    loglbl.place(x=0,y=0)
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",font=("Calibri", 18)).place(x=400,y=150)
    username_login_entry = Entry(login_screen, textvariable=username_verify,font=("Calibri", 18))
    username_login_entry.place(x=700,y=150)
##    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",font=("Calibri", 18)).place(x=400,y=230)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*',font=("Calibri", 18))
    password_login_entry.place(x=700,y=230)
##    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify,font=("Calibri", 18)).place(x=400,y=430)
    
    
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()

    if len(username_info) ==0:
        messagebox.showerror("Error", "Uaer Name Given Empty!")
    elif len(password_info) ==0:
        messagebox.showerror("Error", "Password Given Empty!")
    else:
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
     
        username_entry.delete(0, END)
        password_entry.delete(0, END)
     
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        Button(register_screen,text="Register Face ID", height="2", width="30",bg="#4e8ef5", command=face_reg).place(x=700,y=480)
    
def face_reg():
    os.system("python face_reg.py")
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    os.system("python face_recognition.py")
    with open("check.txt", 'r') as file:
            saved_name = file.read().strip()
    if saved_name == username1:
        messagebox.showinfo("Success", f"Detected face {username1}!")
        print("The name matches!")
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                messagebox.showinfo("Success", "Login Sucess")
                os.system("python GAZE.py")
     
            else:
                password_not_recognised()
                
     
        else:
            user_not_found()
    else:
        print("The name does not match.")
        messagebox.showerror("Error", "Person not matched!")
    
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1200x600")
    main_screen.title("MAIN PAGE")
    main_screen.config(bg="#91b4ed")
    main_screen.resizable(0,0)
    lbl1=Label(text="Dual-Factor Authentication Using \n Eye Blinks and Facial Recognition", bg="#4e8ef5", width="103", height="3", font=("Calibri", 18))
    lbl1.place(x=0,y=0)
##    Label(text="").pack()
    btn1=Button(text="Login", height="2", width="30", bg="#4e8ef5",command = login)
    btn1.place(x=500,y=250)
##    Label(text="").pack()
    btn2=Button(text="Register", height="2", width="30",bg="#4e8ef5", command=register)
    btn2.place(x=500,y=350)
 
    main_screen.mainloop()
 
 
main_account_screen()
