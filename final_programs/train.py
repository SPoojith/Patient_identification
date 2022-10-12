from importlib.resources import path
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
#from gui import NewprojectApp
import shutil
import base64
#from final_year_project import telegram
from posixpath import join
import tkinter as tk
import cv2
import face_recognition as fr
import os
from tkinter import *
import cv2
import glob

import time
from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry   
import datetime as dt
import tkinter as tk
from black import main
cap = cv2.VideoCapture(0)
path="E:/final_year_project\Patients_face_image"
pname=""
class trainimages:
    Patient_firstName=""
    Patient_lastName=""
    gender=""
    dateOfBirth=""
    Patient_PhoneNumber=""
    Patient_email=""
    Patient_bloodGroup=""
    Patient_aadhar=""
    MedicationList=""
    Emergency_firstName=""
    Emergency_lastName=""
    RelationToPatient=""
    Emergency_ContactNumber=""
    Emergency_ContactEmail=""
    Pdf_path=""
    Pdf_data=""
    Pdf_filename=""
    Medical_history=""
    
    
    path="E:/final_year_project\Patients_face_image"
    
    def newperson():
        def inputtodb(Patient_firstName,Patient_lastName,gender,dateOfBirth,Patient_PhoneNumber,Patient_email,Patient_bloodGroup,Patient_aadhar,MedicationList,Emergency_firstName,Emergency_lastName,RelationToPatient,Emergency_ContactNumber,Emergency_ContactEmail,Pdf_data,Pdf_filename,Medical_history):
            dbname = trainimages.get_database()
            collection_name = dbname["Patient_data"]
            item_1 = {
            "Patient_firstName" : Patient_firstName,
            "Patient_lastName":Patient_lastName,
            "gender":gender,
            "dateOfBirth":dateOfBirth,
            "Patient_PhoneNumber":Patient_PhoneNumber,
            "Patient_email":Patient_email,
            "Patient_bloodGroup":Patient_bloodGroup,
            "Patient_aadhar":Patient_aadhar,
            "MedicationList":MedicationList,
            "Emergency_firstName":Emergency_firstName,
            "Emergency_lastName":Emergency_lastName,
            "RelationToPatient":RelationToPatient,
            "Emergency_ContactNumber":Emergency_ContactNumber,
            "Emergency_ContactEmail":Emergency_ContactEmail,
            "Reports Pdf":{
                "file name":Pdf_filename,
                "file data":Pdf_data
            },
            "Medical history":Medical_history
            }
            collection_name.insert_many([item_1])
            print(Patient_firstName,Pdf_filename,Patient_lastName,gender,dateOfBirth,Patient_PhoneNumber,Patient_email,Patient_bloodGroup,Patient_aadhar,MedicationList,Emergency_firstName,Emergency_lastName,RelationToPatient,Emergency_ContactNumber,Emergency_ContactEmail)
            print("entry successful")
        

        def newgui():
            p1=tk.Tk()
            p1.title("Register")
            p1.geometry("1350x700+100+10")

            bg=ImageTk.PhotoImage(file=r"E:\final_year_project\gui_images\bg1.jpg")
            bg_lbl=tk.Label(p1,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

            frame1=Frame(p1,bg="white")
            frame1.place(x=300,y=40,width=700,height=700)
            register_lbl=tk.Label(frame1,text="NEW PATIENT REGISTER",font=("times new roman ",20,"bold"),fg="green",bg="white").place(x=180,y=20)

            fn=tk.StringVar()
            ln=tk.StringVar()
            ph=tk.StringVar()
            e=tk.StringVar()
            dobb=tk.StringVar()
            an=tk.StringVar()
            ml=tk.StringVar()
            
            bld=StringVar()
            

            fname=tk.Label( frame1 ,text="First Name",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            fname.place(x=50,y=100)
    
            f_name_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=fn)
            f_name_entry.place(x=50,y=130,width=250)

            lname=tk.Label( frame1 ,text="Last Name",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            lname.place(x=380,y=100)

            l_name_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=ln)
            l_name_entry.place(x=380,y=130,width=250)

            gender=tk.Label(frame1,text="Gender",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            gender.place(x=50,y=180)

            gen=tk.StringVar()
            gen.set("Select Gender")
            gend=tk.OptionMenu(frame1,gen," ","Male","Female")
            gend.place(x=50,y=210,width=250,height=30)
            gend.config(bg="white", fg="black",bd=1)
            gend["menu"].config(bg="white")

            dob=tk.StringVar()
            dob.set("Enter your DOB")
            dob1=tk.Label( frame1 ,text="DOB",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            dob1.place(x=380,y=180)

            dob_entry=DateEntry(frame1,text=dob,background='white', foreground='darkgreen',bd=2,textvariable=dobb)
            dob_entry.place(x=380,y=210,width=250,height=30)

            phoneno=tk.Label( frame1 ,text="Phone Number",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            phoneno.place(x=50,y=270)

            ph_no_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=ph)
            ph_no_entry.place(x=50,y=300,width=250)

            email=tk.Label( frame1 ,text="Email",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            email.place(x=380,y=270)

            e_mail_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=e)
            e_mail_entry.place(x=380,y=300,width=250)

            blood=tk.Label( frame1 ,text="Blood Group",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            blood.place(x=50,y=350)

            
            blood_entry=tk.OptionMenu(frame1,bld,"O+","O-","A+","A-","B+","B-","AB+","AB-")
            blood_entry.place(x=50,y=380,width=250,height=30)
            blood_entry.config(bg="white", fg="black",bd=1,font=("times new roman",10))
            blood_entry["menu"].config(bg="lightblue",font=("times new roman",10))

            aadhar=tk.Label( frame1 ,text="Aadhar number",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
            aadhar.place(x=380,y=350)

            aadhar1=tk.Label( frame1 ,text="*",font=("times new roman ",15,"italic"),fg="RED",bg="white")
            aadhar1.place(x=525,y=350)

            aadhar_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=an)
            aadhar_entry.place(x=380,y=380,width=250)

            m=IntVar()  
            med=tk.Label(frame1,text="Are you currently taking any medication?",font=("times new roman ",10,"bold italic"),fg="darkgreen",bg="white")
            med.place(x=50,y=430)

            list1=tk.Label(frame1,text="Please list them....(eg: dolo,relent)",font=("times new roman ",10," bold italic"),fg="DARKGREEN",bg="white")
            list_entry=ttk.Entry(frame1,font=("times new roman ",15),textvariable=ml)
            list_entry.configure(textvariable=ml)

            list2=tk.Label(frame1,text="Please upload the pdf \n of all reports and scans:",font=("times new roman ",10," bold italic"),fg="DARKGREEN",bg="white")
            #list_entry=tk.text(frame1, width=30, height=6,font=("times new roman ",11," bold"),bg="white",bd=1,textvariable=ml)
            def selectfile1():
                trainimages.Pdf_path=fd.askopenfilename(filetypes=[('pdf file', '.pdf')])
                trainimages.Pdf_filename=os.path.basename(trainimages.Pdf_path)
                with open(trainimages.Pdf_path, "rb") as Pdf_file:
                    encoded_string=base64.b64encode(Pdf_file.read())
                    # print(encoded_string)
                    trainimages.Pdf_data=encoded_string.decode('utf-8')
                    print(trainimages.Pdf_data)
                file_label=Label(frame1,text="choosen pdf :",font=("times new roman ",10," bold italic"),fg="DARKGREEN",bg="white").place(x=380,y=625)
                file_label=Label(frame1,text=os.path.basename(trainimages.Pdf_path),font=("times new roman ",10,"italic"),fg="DARKGREEN",bg="white").place(x=500,y=625)
            choosefile_btn=tk.Button(frame1,text="choose_file",command=selectfile1)
            
            def selyes():
              trainimages.Medical_history=1
              list1.place(x=380,y=430)
              list_entry.place(x=380,y=450,width=300, height=100)
              list2.place(x=380,y=580)
              choosefile_btn.place(x=550,y=590)
              

            med1=Radiobutton(frame1, text="Yes",variable=m,value=1,bg="white",command=selyes)
            med1.place(x=50,y=450)

            def selno():
              trainimages.Medical_history=2
              list1.place_forget()
              list_entry.place_forget()
              list2.place_forget()
              choosefile_btn.place_forget()
              file_label.place_forget()

            med2=Radiobutton(frame1, text="No",variable=m,value=2,bg="white",command=selno)
            med2.place(x=50,y=470)

            
            def nextpage():
                # p1.quit()
                # p1.destroy()
                # cv2.destroyAllWindows()
                trainimages.Patient_firstName=fn.get()
                trainimages.Patient_lastName=ln.get()
                trainimages.gender=gen.get()
                trainimages.dateOfBirth=dobb.get()
                trainimages.Patient_PhoneNumber=ph.get()
                trainimages.Patient_email=e.get()
                trainimages.Patient_bloodGroup=bld.get()
                trainimages.Patient_aadhar=an.get()
                trainimages.MedicationList=ml.get()
                print("111111111111111111111111111111111111111111111111",trainimages.Patient_firstName)
                print(len(trainimages.Patient_firstName),len(trainimages.Patient_lastName),len(trainimages.gender),len(trainimages.dateOfBirth),len(trainimages.Patient_PhoneNumber),len(trainimages.Patient_email),len(trainimages.Patient_bloodGroup),len(trainimages.Patient_aadhar))
                
                if(len(trainimages.Patient_firstName)>0 and len(trainimages.Patient_lastName)>0 and len(trainimages.gender)>0 and len(trainimages.dateOfBirth)>0 and len(trainimages.Patient_PhoneNumber)>0 and len(trainimages.Patient_email)>0 and len(trainimages.Patient_bloodGroup)>0 and len(trainimages.Patient_aadhar)>0):
                    p1.quit()
                    p1.destroy()
                    cv2.destroyAllWindows()
                    def ecgui():
                        p2=tk.Tk()
                        p2.title("Register")
                        p2.geometry("1350x700+100+10")

                        bg=ImageTk.PhotoImage(file=r"E:\final_year_project\gui_images\bg1.jpg")
                        bg_lbl=Label(p2,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

                        frame1=Frame(p2,bg="white")
                        frame1.place(x=300,y=80,width=700,height=500)
                        register_lbl=Label(frame1,text="EMERGENCY CONTACT DETAILS",font=("times new roman ",20,"bold"),fg="green",bg="white").place(x=130,y=60)


                        #-------lables and entry-----#
                        efn=tk.StringVar()
                        eln=tk.StringVar()
                        eph=tk.StringVar()
                        ee=tk.StringVar()


                        fname=Label( frame1 ,text="First Name",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
                        fname.place(x=50,y=100)


                        f_name_entry=ttk.Entry(frame1,textvariable=efn,font=("times new roman ",15,"bold"))
                        f_name_entry.place(x=50,y=130,width=250)

                        lname=Label( frame1 ,text="Last Name",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
                        lname.place(x=380,y=100)


                        l_name_entry=ttk.Entry(frame1,textvariable=eln,font=("times new roman ",15,"bold"))
                        l_name_entry.place(x=380,y=130,width=250)

                        relation=Label(frame1,text="Relationship With Patient",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
                        relation.place(x=50,y=180)

                        rel=StringVar()
                        rel.set("Select Relationship")
                        rels=OptionMenu(frame1,rel,"Father","Mother","Brother/Sister","wife/life-partner","Husband","Guardian")
                        rels.place(x=50,y=210,width=250,height=35)
                        rels.config(bg="white", fg="black",bd=1,font=("times new roman",10,"bold"))
                        rels["menu"].config(bg="lightblue",font=("times new roman",10,"bold"))

                        phoneno=Label( frame1 ,text="Phone Number",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
                        phoneno.place(x=380,y=180)

                        ph_no_entry=ttk.Entry(frame1,textvariable=eph,font=("times new roman ",15,"bold"))
                        ph_no_entry.place(x=380,y=210,width=250)

                        email=Label( frame1 ,text="Email",font=("times new roman ",15,"italic"),fg="DARKGREEN",bg="white")
                        email.place(x=210,y=270)

                        e_mail_entry=ttk.Entry(frame1,textvariable=ee,font=("times new roman ",15,"bold"))
                        e_mail_entry.place(x=210,y=300,width=250)
                    
                        def emergency():
                            # p2.quit()
                            # p2.destroy()
                            # cv2.destroyAllWindows()
                            trainimages.Emergency_firstName=efn.get()
                            trainimages.Emergency_lastName=eln.get()
                            trainimages.RelationToPatient=rel.get()
                            trainimages.Emergency_ContactNumber=eph.get()
                            trainimages.Emergency_ContactEmail=ee.get()
                            print("2222222222222222",len(trainimages.Emergency_firstName))#,len(trainimages.Patient_lastName),len(trainimages.gender),len(trainimages.dateOfBirth),len(trainimages.Patient_PhoneNumber),len(trainimages.Patient_email),len(trainimages.Patient_bloodGroup),len(trainimages.Patient_aadhar))
                            if len(trainimages.Emergency_firstName)>0 and len(trainimages.Emergency_lastName)>0 and len(trainimages.RelationToPatient)>0 and len(trainimages.Emergency_ContactNumber)>0 and len(trainimages.Emergency_ContactEmail)>0:
                                p2.quit()
                                p2.destroy()
                                cv2.destroyAllWindows()
                                pass
                            else:
                                if len(trainimages.Emergency_firstName)<=0:
                                    win=tk.Tk()
                                    win.geometry("400x100")
                                    tk.Label(win,text="Emergency_firstName required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                                    win.mainloop()

                                if len(trainimages.Emergency_lastName)<=0:
                                    win=tk.Tk()
                                    win.geometry("400x100")
                                    tk.Label(win,text="Emergency_lastName required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                                    win.mainloop()

                                if len(trainimages.RelationToPatient)<=0:
                                    win=tk.Tk()
                                    win.geometry("400x100")
                                    tk.Label(win,text="RelationToPatient required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                                    win.mainloop()

                                if len(trainimages.Emergency_ContactNumber)<=0:
                                    win=tk.Tk()
                                    win.geometry("400x100")
                                    tk.Label(win,text="Emergency_ContactNumber required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                                    win.mainloop()

                                if len(trainimages.Emergency_ContactEmail)<=0:
                                    win=tk.Tk()
                                    win.geometry("400x100")
                                    tk.Label(win,text="Emergency_ContactEmail required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                                    win.mainloop()
                                #ecgui()
                            print("patient name: ",fn.get()," ",ln.get())
                            print("patient phone number: ",ph.get())
                            print("patient email: ",e.get())
                            print("patient aadhar number: ",an.get())
                            print("patient gender: ",gen.get())
                            print("patient dob: ",dobb.get())
                            print("emergency contact name: ",efn.get()+" "+eln.get())
                            print("emergency contact phone number: ",eph.get())
                            print("emergency contact email: ",ee.get())
                            print("emergency contact person realtion to patients: ",rel.get())
                            print("clicked")
                        reg_btn=Image.open(r"E:\final_year_project\gui_images\next1.png")
                        imgph=ImageTk.PhotoImage(reg_btn)
                        reg_Button = tk.Button(frame1,image=imgph,bg="white",bd=0,command=emergency)
                        reg_Button.image=imgph
                        reg_Button.place(x=190,y=400)
                        p2.mainloop()
                    ecgui()
                else:
                    if len(trainimages.Patient_firstName)<=0:
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text=" Patient_firstName required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.Patient_lastName)<=0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="Patient_lastName required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.gender)<=0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="gender required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.dateOfBirth)<=0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text=" dateOfBirth required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.Patient_PhoneNumber) <= 0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="Patient_PhoneNumber required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.Patient_email)<=0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="Patient_email required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if len(trainimages.Patient_email)<=0 :
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="Patient_email required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                    if(len(trainimages.Patient_aadhar)<=0):
                        win=tk.Tk()
                        win.geometry("400x100")
                        tk.Label(win,text="Patient_aadhar required", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                        win.mainloop()
                
            
            next_btn=Image.open(r"E:\final_year_project\gui_images\nex1.png")
            imgph=ImageTk.PhotoImage(next_btn)
            loginButton = tk.Button(frame1,image=imgph,bg="white",bd=0,command=nextpage)
            loginButton.image=imgph
            loginButton.place(x=100,y=560)
            p1.mainloop()

        newgui()
        trainimages.cf(trainimages.Patient_aadhar)
        inputtodb(trainimages.Patient_firstName,trainimages.Patient_lastName,trainimages.gender,trainimages.dateOfBirth,trainimages.Patient_PhoneNumber,trainimages.Patient_email,trainimages.Patient_bloodGroup,trainimages.Patient_aadhar,trainimages.MedicationList,trainimages.Emergency_firstName,trainimages.Emergency_lastName,trainimages.RelationToPatient,trainimages.Emergency_ContactNumber,trainimages.Emergency_ContactEmail,trainimages.Pdf_data,trainimages.Pdf_filename,trainimages.Medical_history)
        return trainimages.Patient_aadhar
    
    def personphoto(pname,pathf):
        path = pathf
        print("insidepp",path)
        for f in os.listdir(path):
            if(f.endswith(".jpg")):
                os.remove(os.path.join(path,f))
        file_count=0
        face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  
        i=0
        while True:
            try:
                (_,img)=cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4,minSize=(30,50))
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0,), 0)
                    roi_color = img[y-50:y + h+50, x-50:x+ w+50]
                   # print(roi_color.shape)
                    if(len(faces)>=1 and int(str(w)+str(h))>8000):
                        #print("[INFO] Object found. Saving locally.")
                        try:
                            cv2.imwrite(os.path.join(path, str(pname) +'_'+ str(i)+'.jpg'), roi_color)
                            i=i+1
                        except:
                            pass
                    else:pass
                cv2.imshow("img",img)
            except:
                cap = cv2.VideoCapture(0)
                (_,img)=cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4,minSize=(30,50))
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0,), 0)
                    roi_color = img[y-50:y + h+50, x-50:x+ w+50]
                   # print(roi_color.shape)
                    if(len(faces)>=1 and int(str(w)+str(h))>8000):
                        #print("[INFO] Object found. Saving locally.")
                        try:
                            cv2.imwrite(os.path.join(path, str(pname) +'_'+ str(i)+'.jpg'), roi_color)
                            i=i+1
                        except:
                            pass
                    else:pass
                cv2.imshow("img",img)

           

            k=cv2.waitKey(30) & 0xff 
            if (k==27):
                cap.release()
                cv2.destroyAllWindows()
                break
            file_count=0
            for f in os.listdir(path):
                if(f.endswith(".jpg")):
                    file_count+=1
            if(file_count>=5):
                cap.release()
                cv2.destroyAllWindows()
                break
        cap.release()
        cv2.destroyAllWindows()
        def checkimg(pathf):
                    from PIL import Image
                    import glob
                    import os
                    import cv2
                    import face_recognition
                    import cv2
                    import os
                    import glob
                    import numpy as np
                    import tkinter as tk
                    import tkinter.ttk as ttk
                    import pandas as pd 
                    from PIL import Image,ImageTk
                    image_list = []
                    path=pathf
                    popup=tk.Tk()
                    popup.geometry("650x450+200+50")
                    popup.config(bg="#000")
                    r=0
                    c=0
                    count=0 
                    i=0 
                    a=[]
                    for f in os.listdir(path):
                        print(f)
                        img=Image.open(os.path.join(path,f))
                        newsize = (200,200)
                        img=img.resize(newsize)
                        image_list.append(ImageTk.PhotoImage(img))
                        tk.Label(popup,image = image_list[i]).grid(row = r, column = c,pady=5,padx=5,)
                        c=c+1
                        i=i+1
                        if c>2:
                            r=r+1
                            c=0
                    def yes():
                        popup.quit()
                        popup.destroy()

                    def no():
                        popup.quit()
                        popup.destroy()
                        trainimages.personphoto(pname,pathf)
    
                    check=tk.Label(popup,text="Are Training Images Clear?",background="#c0c0c0", font="{Times New Roman} 14 {}").place(x=430,y=270)
                    yes=tk.Button(popup,bg="#c0c0c0",bd=1,text="Yes",command=yes).place(x=470,y=320,width=50,height=20 )
                    no=tk.Button(popup,bg="#c0c0c0",bd=1,text="No",command=no).place(x=530,y=320,width=50,height=20)
                    popup.mainloop()
        checkimg(pathf)
    
    def filerename(pname,paths): 
            pathn= paths
            i=0
            file_count=0
            for f in os.listdir(paths):
                if(f.endswith(".jpg")):
                    file_count+=1
            if(file_count<5):
                print("run again")
                os.remove(paths)
                SystemExit(0)
            for f in os.listdir(pathn):
                fn=os.path.join(pathn,f)
                pn=os.path.join(pathn,pname+"_"+str(i)+".jpg")
                i=i+1
                os.rename(fn,pn)
    
    def get_database():
        from pymongo import MongoClient
        import pymongo

        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = "mongodb://localhost:27017/"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        from pymongo import MongoClient
        client = MongoClient(CONNECTION_STRING)

        # Create the database for our example (we will use the same database throughout the tutorial
        return client['PI']
    
    def cf(pname):
        try:
            print("inside cf->>>>>>>>>>>",pname)
            print(os.path.join(path,pname))
            os.makedirs(os.path.join(path,pname))
            print(pname+" folder creadted")
        except:
            file_count=0
            pathn=os.path.join(path,pname)
            for f in os.listdir(pathn):
                if(f.endswith(".jpg")):
                    file_count+=1
            print(file_count)
            if(file_count<5):
                os.remove(pathn)
            else:
                res=messagebox.askretrycancel("error","patient details already exist")
                if(res == True):
                    trainimages.flow()
                else:
                    SystemExit(0)
                #print("name already exist")
            cap.release()
            exit(0)
    
    def flow():
        print("reached here ie flow")
        print("before pname")
        pname=trainimages.newperson()
        print("after pname inside flow--->",pname," <--")
        print(pname)
        print("after print pname")
        #trainimages.cf(pname)
        trainimages.personphoto(pname,os.path.join(path,pname))
        #NewprojectApp.startwindow()

if __name__=="__main__":
    print("reached here ie main")
    trainimages.flow()
    #trainimages.pname=trainimages.newperson()
    #print(trainimages.pname)
    #trainimages.cf(trainimages.pname)
    #trainimages.personphoto(trainimages.pname,os.path.join(path,trainimages.pname))
    #filerename(pname,os.path.join(path,pname))