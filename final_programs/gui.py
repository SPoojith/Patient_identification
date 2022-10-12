from train import trainimages 
from test import testimages as t
from searchtest import SearchP
import os
from importlib.resources import path
import shutil
from posixpath import join
import tkinter as tk
import cv2
import face_recognition as fr
import os
from tkinter import *
import time
from PIL import Image,ImageTk
import tkinter as tk
import tkinter.ttk as ttk

class NewprojectApp:
    window = tk.Tk()
    def __init__(self, master=None):
        NewprojectApp.window.geometry("1200x700+200+50")
        NewprojectApp.window.title("home")
        NewprojectApp.window.configure(bg = "#266f78")
        canvas = Canvas(
            NewprojectApp.window,
            bg = "#266f78",
            height = 900,
            width = 1300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img =ImageTk.PhotoImage(file = r"E:\final_year_project\gui_images\bg2.png")
        background = canvas.create_image( 600,400,
            image=background_img)


        # register_lbl=Label(NewprojectApp.window,text="PATIENT IDENTIFICATION USING FACIAL RECOGNITION",font=("times new roman ",20,"bold"),fg="black")
        # register_lbl.place(x=250,y=84)

        img0 = PhotoImage(file = r"E:\final_year_project\gui_images\img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = NewprojectApp.totest,
            relief = "flat")

        b0.place(
            x = 782, y = 335,
            width = 218,
            height = 210)

        img1 = PhotoImage(file =  r"E:\final_year_project\gui_images\img13.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = NewprojectApp.totrain,
            relief = "flat")

        b1.place(
            x = 200, y = 335,
            width = 218,
            height = 210)
        
        img2 = PhotoImage(file =  r"E:\final_year_project\gui_images\img110.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = NewprojectApp.searchtest,
            relief = "flat")

        b2.place(
            x = 500, y = 335,
            width = 218,
            height = 210)
       # NewprojectApp.window.resizable(False, False)
        NewprojectApp.window.mainloop()

       # NewprojectApp.window.resizable(False, False)
        NewprojectApp.window.mainloop()

    def run(self):
        self.window.mainloop()

    def searchtest():
        NewprojectApp.window.destroy()
        NewprojectApp.window.quit()
        SearchP.flow1()
        NewprojectApp.window = tk.Tk()
        NewprojectApp.startwindow(NewprojectApp.window)

    def totrain():
    
        
        NewprojectApp.window.destroy()
        NewprojectApp.window.quit()
        trainimages.flow()
        NewprojectApp.window = tk.Tk()
        NewprojectApp.startwindow(NewprojectApp.window)
        
    
    def totest():
        # NewprojectApp.root.destroy()
        # NewprojectApp.root.quit()
        # s=t()
        # s.shofaces(t.path_all_images)
        # NewprojectApp.root = tk.Tk()
        # NewprojectApp.startwindow(NewprojectApp.root)
        NewprojectApp.window.destroy()
        NewprojectApp.window.quit()
        s=t()
        s.shofaces(t.path_all_images)
        NewprojectApp.window = tk.Tk()
        NewprojectApp.startwindow(NewprojectApp.window)


    def startwindow(root):
        # NewprojectApp.root.geometry("1200x800")
        # app = NewprojectApp(NewprojectApp.root)
        # app.run()

        NewprojectApp.window.geometry("1200x800")
        app = NewprojectApp(NewprojectApp.window)
        app.run()

if __name__ == "__main__":
    # NewprojectApp.startwindow(NewprojectApp.root)
    NewprojectApp()