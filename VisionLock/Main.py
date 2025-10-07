from tkinter import *
from PIL import Image,ImageTk
import cv2
import os

win=Tk()
win.title("FAC RECOGNITION SYSTEM")
win.geometry("1500x750")
win.resizable(0,0)

img=Image.open("bag.jpg")
img=img.resize((1500,750))

bgg=ImageTk.PhotoImage(img)

lbl=Label(win,image=bgg)
lbl.place(x=0,y=0)

label=Label(win,text="FACE RECOGNITION MODULE",bg="black",fg="white",font=("times",24,"bold"))
label.place(x=200,y=50)



def recognize():
    os.system("python face_recognition.py")

    


label=Button(win,text="FAC RECOGNITION ",bg="black",fg="white",font=("times",24,"bold"),command=recognize)
label.place(x=150,y=350)
