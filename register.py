from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1550x800+0+0")
        #+===============variables=========
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ= StringVar()
        self.var_securityA = StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        #==============bg Image==================
        img = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\wallpape.jpg")
        img = img.resize((1550, 800), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=800)

        #================left image=================
        img1 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\very.jpg")
        img1 = img1.resize((470, 550), Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=50, y=100, width=470, height=550)

        # ============frme==========
        frame = Frame(self.root, bg='white')
        frame.place(x=520, y=100, width=800, height=550)
        #lablal
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold",'underline'), bg='white',
                          fg="dark green", bd=4)
        register_lbl.place(x=20, y=20)

        # =====================labels and entrys=================
        # -----------row1
        fname = Label(frame, text="First Name:", font=("times new roman", 15, "bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15, "bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame, text="Last Name:", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # -----------row2
        contact = Label(frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        self.txt_contact= ttk.Entry(frame, textvariable=self.var_contact,font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email:", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # -----------row3
        security_Q = Label(frame, text="Select Ssecurity Quetions:", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,font=("arial", 13, "bold"), width=27,
                                    state="readonly")
        self.combo_security_Q["value"] = ("Select","Your Birth Place","Your BestFriend Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A = Label(frame, text="Security Answer:", textvariable=self.var_securityA,font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)

        self.security = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.security.place(x=370, y=270, width=250)

        # -----------row4
        pswd = Label(frame, text="Password:", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass,font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password:", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #=============checkbutton====================

        checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #==============button============================
        img3 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\regester.jpg")
        img3 = img3.resize((200, 50), Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(frame, image=self.photoimg3,command=self.register_data, borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10, y=420, width=200)

        img4 = Image.open("C:\\Users\\Admin\\roshaniproject\\hotel_management_system\\now3.jpg")
        img4 = img4.resize((200, 45), Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b2 = Button(frame, image=self.photoimg4, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=330, y=420, width=200)

        #==================Fuction Delartion==============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_securityQ=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plaese agree our terms one condition")
        else:
            conn = mysql.connector.connect(
                username="root",
                password="",
                host="localhost",
                database="hotel"
            )
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")







if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()