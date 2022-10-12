from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
def home():
    p2=tk.Tk()
    p2.title("ASLRBVA")
    p2.geometry("1350x700+100+10")
    # next_btn=Image.open(r"E:\final_year_project\gui_images\nex1.png")
    # imgph=ImageTk.PhotoImage(next_btn)
    p2.configure(bg = "#266f78")
    textlabel1=tk.Label(p2,text="ASL Recognition based Voice Assistance",font=("times new roman ",20,"bold"),fg="black",bg="white").place(x=400,y=200)
    textlabel2=tk.Label(p2,text="American Sign Language converter \n is a system that can detect \n and convert sign language gestures in real time.",font=("times new roman ",20,"bold"),fg="black",bg="white").place(x=200,y=350)
    def phi():
        p2.quit()
        p2.destroy()
        p1=tk.Tk()
        p1.title("ASLRBVA")
        p1.geometry("1350x700+100+10")
        res=messagebox.askretrycancel("error","patient details already exist")
    reg_Button = tk.Button(p2,text="click here to detect",font=("times new roman ",10,"bold"),bg="white",bd=0,command=phi,height=2,width=20).place(x=900,y=375)
    p2.mainloop()