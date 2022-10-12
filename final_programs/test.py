import face_recognition
from tkPDFViewer import tkPDFViewer as pdf
from tkinter.scrolledtext import ScrolledText
import cv2
import os
import base64
import glob
import numpy as np
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import pandas as pd 
import smtplib
from PIL import Image,ImageTk
import fitz
path="E:/final_year_project/final_programs/temppdf"
class testimages:
    
    path_all_images="E:/final_year_project\Patients_face_image"
    def outgui(root,Patient_firstName,Patient_lastName,gender,dateOfBirth,Patient_PhoneNumber,Patient_email,Patient_bloodGroup,Patient_aadhar,MedicationList,Emergency_firstName,Emergency_lastName,RelationToPatient,Emergency_ContactNumber,Emergency_ContactEmail,Pdf_filename,Pdf_data,Medical_history):
        root.title("patient_details")
        root.geometry("1350x700+100+10")
        root.resizable(False,False)


        bg=ImageTk.PhotoImage(file=r"E:\final_year_project\gui_images/bg1.jpg")
        bg_lbl=tk.Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

        
        
        #======patient frame =================#
        frame1=tk.Frame(root,bg="BLACK")
        frame1.place(x=50,y=100,width=600,height=550)

        #======pic========

        img = Image.open(os.path.join(os.path.join(testimages.path_all_images,Patient_aadhar+"/"+Patient_aadhar+"_0.jpg")))
        img = img.resize((165, 165))        
        tkimage = ImageTk.PhotoImage(img)
        
        tk.Label(frame1,image = tkimage).place(x="360", y="70")


        register_lbl=tk.Label(frame1,text="PATIENT DETAILS",font=("times new roman ",20,"bold"),fg="orange",bg="black")
        register_lbl.place(x=180,y=20)


         #======emergency frame =================#
        frame2=tk.Frame(root,bg="black")
        frame2.place(x=660,y=100,width=600,height=550)
        register_lbl=tk.Label(frame2,text="EMERGENCY CONTACT DETAILS",font=("times new roman ",20,"bold"),fg="orange",bg="black")
        register_lbl.place(x=80,y=20)


          #======fname=================#
        label6 = tk.Label(frame1)
        label6.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="First Name :"
            )

        label6.place(anchor="nw", height="30", width="150", x="10", y="80")

        label16 = tk.Label(frame1)
        label16.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Patient_firstName
        )
        label16.place(anchor="nw", height="30", width="150", x="160", y="80")

          #======lname =================#
        label7 = tk.Label(frame1)
        label7.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Last Name :"
            )
        label7.place(anchor="nw", height="30", width="150", x="10", y="140")

        label17 = tk.Label(frame1)
        label17.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Patient_lastName
        )
        label17.place(anchor="nw", height="30", width="150", x="160", y="140")

          #======Bloodgp=================#
        label8 = tk.Label(frame1)
        label8.configure(
                background="BLACK",fg="white",font="{Times New Roman} 14 {}", text="Blood Group:"
            )
        label8.place(anchor="nw", height="30", width="150", x="2", y="200")

        label18 = tk.Label(frame1)
        label18.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Patient_bloodGroup
        )
        label18.place(anchor="nw", height="30", width="150", x="160", y="200")
         #======gender =================#
        label9 = tk.Label(frame1)
        label9.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Gender :"
            )
        label9.place(anchor="nw", height="30", width="150", x="20", y="260")

        label19 = tk.Label(frame1)
        label19.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=gender
        )
        label19.place(anchor="nw", height="30", width="150", x="160", y="260")
         #======dob=================#
        label10 = tk.Label(frame1)
        label10.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="DOB :"
            )
        label10.place( height="30", width="150", x="300", y="260")
        label100 = tk.Label(frame1)
        label100.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=dateOfBirth
        )
        label100.place(anchor="nw", height="30", width="150", x="420", y="260")
         #======phno=================#
        label11 = tk.Label(frame1)
        label11.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Phone No:"
            )
        label11.place(anchor="nw", height="30", width="150", x="10", y="380")

        label111 = tk.Label(frame1)
        label111.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Patient_PhoneNumber
        )
        label111.place(anchor="nw", height="30", width="150", x="160", y="380")
         
         
         #======email=================#
        label12 = tk.Label(frame1)
        label12.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="E-mail :"
            )
        label12.place( height="30", width="150", x="10", y="320")
        label112 = tk.Label(frame1)
        label112.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text= Patient_email
        )
        label112.place(anchor="nw", height="30", width="200", x="160", y="320")
        
         #======addhar no=================#
        label13 = tk.Label(frame1)
        label13.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Addhar No :"
            )
        label13.place(anchor="nw", height="30", width="150", x="4", y="440")
        label113 = tk.Label(frame1)
        label113.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Patient_aadhar
        )
        label113.place(anchor="nw", height="30", width="150", x="160", y="440")
        
        
         #======history=================#
        label14 = tk.Label(frame1)
        label14.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Medical History :"
            )
        label14.place( height="30", width="150", x="380", y="350")
        label114 = tk.Label(frame1)
        label114.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=MedicationList
        )
        label114.place(anchor="nw", height="100", width="150", x="385", y="380")
          #======patient relationship =================#
        label1 = tk.Label(frame2)
        label1.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Relationship To Patient :"
            )
        label1.place( height="30", width="200", x="30", y="100")

        label101 = tk.Label(frame2)
        label101.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=RelationToPatient
        )
        label101.place(anchor="nw", height="30", width="150", x="300", y="100")

         #======fname in emergency =================#
        label2 = tk.Label(frame2)
        label2.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="First Name :"
            )
        label2.place(anchor="nw", height="30", width="150", x="100", y="170")

        label102 = tk.Label(frame2)
        label102.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Emergency_firstName
        )
        label102.place(anchor="nw", height="30", width="150", x="300", y="170")
          #======Lname in emergency =================#
        label3 = tk.Label(frame2)
        label3.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Last Name :"
            )
        label3.place(anchor="nw", height="30", width="150", x="100", y="240")
        label103 = tk.Label(frame2)
        label103.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Emergency_lastName
        )
        label103.place(anchor="nw", height="30", width="150", x="300", y="240")

          #======phno in emergency =================#
        label4 = tk.Label(frame2)
        label4.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="Phone No :"
            )
        label4.place(anchor="nw", height="30", width="150", x="100", y="310")
        label104 = tk.Label(frame2)
        label104.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Emergency_ContactNumber
        )
        label104.place(anchor="nw", height="30", width="150", x="300", y="310")

        label5 = tk.Label(frame2)
        label5.configure(
                background="BLACK",fg="white", font="{Times New Roman} 14 {}", text="E-mail :"
            )
        label5.place(anchor="nw", height="30", width="150", x="115", y="380")
        
        label105 = tk.Label(frame2)
        label105.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text=Emergency_ContactEmail
        )
        label105.place(anchor="nw", height="30", width="200", x="280", y="380")
        class PDFViewer(ScrolledText):
            def show(self , pdf_file):
                self.delete('1.0', 'end') # clear current content
                pdf = fitz.open(pdf_file) # open the PDF file
                self.images = []   # for storing the page images
                for page in pdf:
                    pix = page.get_pixmap()
                    pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
                    photo = tk.PhotoImage(data=pix1.tobytes('ppm'))
                    # insert into the text box
                    self.image_create('end', image=photo)
                    self.insert('end', '\n')
                    # save the image to avoid garbage collected
                    self.images.append(photo)

        def show1():
            file_64_decode = base64.b64decode(Pdf_data) 
            file_result = open(os.path.join(path,Pdf_filename), 'wb') 
            file_result.write(file_64_decode)
            pdf2 = PDFViewer(root, width=70, height=30, spacing3=5, bg='blue')
            pdf2.place(x=100,y=30)
            pdf2.show(os.path.join(path,Pdf_filename))
            def close():
                pdf2.place_forget()
                os.remove(os.path.join(path,Pdf_filename))
            medical_btn2=tk.Button(frame2,text="close pdf", font="{Times New Roman} 14 {}",bg="white",command=close).place(x=20,y=450)    
                
        medical_btn=tk.Button(frame1,text="show pdf",command=show1)
        medical_btn.configure(font="{Times New Roman} 14 {}")

        if  Medical_history == 1 :
            medical_btn.place(x="385", y="500")

            
        else :
            if (Medical_history == 2) :
                label114.configure(text="no history")
        def qui():
            root.quit()
            root.destroy()
            # for f in os.listdir(path):
            #     os.remove(f)
        
        close_btn=Image.open(r"E:\final_year_project\gui_images\home2.png")
        close_btn=close_btn.resize((150,50))
        imgph=ImageTk.PhotoImage(close_btn)
        closeButton = tk.Button(frame2,image=imgph,bg="black",bd=0,command=qui)
        closeButton.image=imgph
        closeButton.place(x=125,y=444)
        def send_sms():
            import pywhatkit as kit
            import time
            from datetime import datetime
            currentDateAndTime = datetime.now()

            try:
                print("msg will be sent in 120 seconds")
                kit.sendwhatmsg("+91"+Emergency_ContactNumber,"You Received this mail because you were listed as an emergency contact person for "+Patient_firstName+" "+Patient_lastName+" who as been admited to **Vijayanagr hospital** Contact us immeditly  Hospital Contact Number: 080 000 000 0000 Hospital Address: Vijayanagar Banglore-60",currentDateAndTime.hour,currentDateAndTime.minute+2)
            except Exception as E:
                print("wait for 120 seconds")
                time.sleep(120)     
                print("msg will be sent in 120 seconds")           
                kit.sendwhatmsg("+91"+Emergency_ContactNumber,"You Received this mail because you were listed as an emergency contact person for "+Patient_firstName+" "+Patient_lastName+" who as been admited to **Vijayanagr hospital** Contact us immeditly  Hospital Contact Number: 080 000 000 0000 Hospital Address: Vijayanagar Banglore-60",currentDateAndTime.hour,currentDateAndTime.minute+2)
        def mailto():
            sspath="E:/final_year_project/test_screeshots"
            def takess():
                
                import numpy as np
                import cv2
                import pyautogui


                # take screenshot using pyautogui
                image = pyautogui.screenshot()

                # since the pyautogui takes as a 
                # PIL(pillow) and in RGB we need to 
                # convert it to numpy array and BGR 
                # so we can write it to the disk

                image = cv2.cvtColor(np.array(image),
                                     cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(sspath,Patient_firstName+" "+Patient_lastName+".jpg"), image)
                im = Image.open(os.path.join(sspath,Patient_firstName+" "+Patient_lastName+".jpg"))


                left = 90
                top = 9
                right = 1460
                bottom = 720

                im1 = im.crop((left, top, right, bottom))
                im1=cv2.cvtColor(np.array(im1),
                                     cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(sspath,Patient_firstName+" "+Patient_lastName+".jpg"), im1)
                # Shows the image in image viewer
                #im1.show()
            takess()
            root.quit()
            root.destroy()
            
            import smtplib, ssl
            import smtplib
            from email.mime.image import MIMEImage
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.message import EmailMessage
            import imghdr

            smtp_server = "smtp.gmail.com"
            port = 587  # For starttls
            sender_email = "dbit.patientidentification@gmail.com"
            receiver_email = Emergency_ContactEmail
            print(sender_email," mail ", receiver_email)
            imgsrc=os.path.join(sspath,Patient_firstName+" "+Patient_lastName+".jpg")
            html ="<html><body><p><h1>    You Received this mail because you were listed as an emergency contact person for <br>** "+Patient_firstName+" "+Patient_lastName+" ** <br> Who is admited to <br>**Vijayanagr hospital ** </h1><h2>    Contact us immeditly      <br>Hospital Contact Number:<br> 080 000 000 0000    <br>Hospital Address:<br> Vijayanagar Banglore-60</h2></p></body></html>"

            
            

            message = MIMEMultipart("alternative")
            message["Subject"] = "Emergency contact us Immediatly!!"
            message["From"] = sender_email
            message["To"] = receiver_email
            message['X-Priority'] = '1'
            password ='Capsicum_2012' 
            
            part2 = MIMEText(html, "html")
            message.attach(part2)
            img_path=os.path.join(sspath,Patient_firstName+" "+Patient_lastName+".jpg")
            file_name=os.path.basename(img_path)
            print(file_name)
            im = Image.open(img_path)
            
    
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
            fp = open(img_path, 'rb')
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment', filename=file_name)
            fp.close()
            message.attach(img)

            #adding the image
            
            
            context = ssl.create_default_context()

            # Try to log in to server and send email
            try:
                print(password)
                print(sender_email)
                server = smtplib.SMTP(smtp_server,port)
                server.ehlo() # Can be omitted
                server.starttls(context=context) # Secure the connection
                server.ehlo() # Can be omitted
                server.login(sender_email, password)
                # TODO: Send email here
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("mailsent")
            except Exception as e:
                print(e)
            finally:
                server.quit() 


        send_btn=Image.open(r"E:\final_year_project\gui_images\mail3.jpeg")
        imgph=ImageTk.PhotoImage(send_btn)
        sendButton = tk.Button(frame2,image=imgph,bg="black",bd=0,command=send_sms)    #mailto)
        sendButton.image=imgph
        sendButton.place(x=350,y=440,height=60)
        root.mainloop()
        
    def con(self,dbpname, dbphn, dbbg):
        # build ui
        self.frame1 = tk.Frame()
        self.label1 = tk.Label(self.frame1)
        self.label1.configure(
            background="#c0c0c0", font="{Times New Roman} 20 {}", text="Patient_Details"
        )
        self.label1.place(anchor="nw", height="40", width="800", x="0", y="0")
        self.label6 = tk.Label(self.frame1)
        self.label6.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text="Name :"
        )
        self.label6.place(anchor="nw", height="30", width="150", x="10", y="100")
        self.label7 = tk.Label(self.frame1)
        self.label7.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text="Phone_number :"
        )
        self.label7.place(anchor="nw", height="30", width="150", x="10", y="170")
        self.label8 = tk.Label(self.frame1)
        self.label8.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text="blood_group :"
        )
        self.label8.place(anchor="nw", height="30", width="150", x="10", y="240")

        img = Image.open(os.path.join(os.path.join(testimages.path_all_images,dbpname+"/"+dbpname+"_0.jpg")))
        # if(dbpname=="kulli"):
        #     img="E:/final_year_project\Patients_face_image\kulli\kulli_5.jpg"
        # img=Image.open("E:/final_year_project\Patients_face_image\kulli\kulli_5.jpg")        
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self,image = self.tkimage).place(x="450", y="70")
    
        self
        self.label9.place(anchor="nw", height="30", width="150", x="200", y="100")
        self.label12 = tk.Label(self.frame1)
        self.label12.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text= dbphn
        )
        self.label12.place(anchor="nw", height="30", width="150", x="200", y="170")
        self.label13 = tk.Label(self.frame1)
        self.label13.configure(
            background="#c0c0c0", font="{Times New Roman} 14 {}", text= dbbg
        )
        self.label13.place(anchor="nw", height="30", width="150", x="200", y="240")
        self.frame1.configure(background="#030303", height="400", width="800")
        self.frame1.place(anchor="nw", height="400", relwidth="0.0", width="800")

        # Main widget
        self.mainwindow = self.frame1
        self.mainwindow.mainloop()
    
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self,images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        
        im_path = glob.glob(os.path.join(images_path, "*.*"))
        print("{} encoding images found.".format(len(im_path)))

        # Store image encoding and names
        i=0
        for img_path in im_path:
            img2 = cv2.imread(img_path,cv2.IMREAD_COLOR)
            #print(img2.shape)
       #     cv2.imshow("img",img2)
            rgb_img = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            # Get the filename only from the initial file path.
            basename = os.path.basename(images_path)
            #print(basename)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding=[]
            try: 
                img_encoding = face_recognition.face_encodings(rgb_img)[0]
            except:
                pass
            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
            i=i+1
            print(str(i) + " Encoding images loaded")
            #print(str(i))

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
    
    def findp(piname):
        from createdatabase import get_database
        dbname = get_database()
        # Create a new collection
        collection_name = dbname["Patient_data"]
        
        # item_details = collection_name.find()
        # for item in item_details:
        #     # This does not give a very readable output
        #     print(item) #*****to print all items in db****

        #to find by id
        item = list(collection_name.find({ "Patient_aadhar" : piname }))
        valuelist = list(item[0].values())
        # dbpname=valuelist[0]
        # dbphn=valuelist[1]
        # dbbg=valuelist[2]
        
        Patient_firstName=valuelist[1]
        Patient_lastName=valuelist[2]
        gender=valuelist[3]
        dateOfBirth=valuelist[4]
        Patient_PhoneNumber=valuelist[5]
        Patient_email=valuelist[6]
        Patient_bloodGroup=valuelist[7]
        Patient_aadhar=valuelist[8]
        MedicationList=valuelist[9]
        Emergency_firstName=valuelist[10]
        Emergency_lastName=valuelist[11]
        RelationToPatient=valuelist[12]
        Emergency_ContactNumber=valuelist[13]
        Emergency_ContactEmail=valuelist[14]
        Pdf_content=list(valuelist[15].values())
        Pdf_filename=Pdf_content[0]
        Pdf_data=Pdf_content[1]
        Medical_history=valuelist[16]
        #print(item)
        print(Patient_firstName,Pdf_filename,Patient_lastName,gender,dateOfBirth,Patient_PhoneNumber,Patient_email,Patient_bloodGroup,Patient_aadhar,MedicationList,Emergency_firstName,Emergency_lastName,RelationToPatient,Emergency_ContactNumber,Emergency_ContactEmail)


        root = tk.Tk()
        root.title("Patient_details")
        root.geometry("800x400")
        app = testimages.outgui(root,Patient_firstName,Patient_lastName,gender,dateOfBirth,Patient_PhoneNumber,Patient_email,Patient_bloodGroup,Patient_aadhar,MedicationList,Emergency_firstName,Emergency_lastName,RelationToPatient,Emergency_ContactNumber,Emergency_ContactEmail,Pdf_filename,Pdf_data,Medical_history)
        
    def shofaces(self,path_all_images):
        for path in os.listdir(path_all_images):
            print(path)
            self.load_encoding_images(os.path.join(path_all_images,path))
    # Load Camera
        cap = cv2.VideoCapture(0)
        while True:
            (_, frame) = cap.read()
            # Detect Faces
            #cv2.imshow("we0",frame)
            face_locations, face_names = self.detect_known_faces(frame)
            if(len(face_names)>0):
                print(face_names[0])
                i=0
                if(face_names[0] == "Unknown"):
                    i=i+1
                    print(face_names[0])
                    print(i)
                    messagebox.showinfo("sorry!!","Patient Details not exist")
                    # win=tk.Tk()
                    # win.geometry("400x100")
                    # tk.Label(win,text="!!!Patient details not found!!!!",background="#c0c0c0", font="{Times New Roman} 20 {}").grid(row=0,column=1,pady=5)
                    # win.mainloop()
                    # cap.release()
                    # cv2.destroyAllWindows()
                    break
                    
                cap.release()
                cv2.destroyAllWindows()
                testimages.findp(face_names[0])
                break
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,200), 4)
            frame=cv2.resize(frame,(1200,800))
            cv2.imshow("Frame", frame,)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
if __name__=="__main__":
    s=testimages() 
    s.shofaces(testimages.path_all_images)