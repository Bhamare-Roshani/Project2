from tkinter import *
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
import os
from deatails import DeatailsRoom

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1550x800+0+0")
        #===================ist img====================
        img1=Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\hotel3.jpg")
        img1=img1.resize((1550,140),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #===================logo=======================
        img2 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\grand.jpg")
        img2 = img2.resize((230, 140), Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        #================Title=======================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg='black',fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        #===============in frame====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #============menu=======================
        lbl_title = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg='black',fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230)
        # ===============button frame====================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=150)
        #btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman", 14, "bold"), bg='black',fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking,width=22, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22,command=self.details_room, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0,pady=1)

        #report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        #report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22,command=self.logout ,font=("times new roman", 14, "bold"), bg='black',fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0,pady=1)

        #=========================RIGHT IMG============================
        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\hotel.jpg")
        img3 = img3.resize((1310, 592), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=592)

        #=======================down images===========================
        img4 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\taj.jpg")
        img4 = img4.resize((230, 240), Image.ADAPTIVE)
        #img4 = img4.resize((230, 210), Image.ADAPTIVE)
        self.photoimg4= ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=186, width=230, height=240)
        #lblimg1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\khana.jpg")
        img5 = img5.resize((230, 190), Image.ADAPTIVE)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 0.7)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        converter.setProperty('voice', voice_id)
        converter.say("GREAT Welcome to show the Customer Details")
        converter.runAndWait()

    def roombooking(self, converter=None):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 0.7)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        converter.setProperty('voice', voice_id)
        converter.say("GREAT Welcome to show the roombooking details")
        converter.runAndWait()

    def details_room(self, converter=None):
        self.new_window=Toplevel(self.root)
        self.app=DeatailsRoom(self.new_window)
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 0.7)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        converter.setProperty('voice', voice_id)
        converter.say("GREAT Welcome to show the room details")
        converter.runAndWait()

    def logout(self):
        import pyttsx3
        converter = pyttsx3.init()
        converter.setProperty('rate', 150)
        converter.setProperty('volume', 0.7)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        converter.setProperty('voice', voice_id)
        converter.say("Logout your project good byeee")
        converter.runAndWait()
        self.root.destroy()







if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()