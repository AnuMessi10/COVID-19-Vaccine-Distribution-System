import re
import tkinter
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk

import pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")

        # Designate Height and Width of our window
        self.app_width = 1000
        self.app_height = 850

        # Center pop up
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.resizable(False, False)
        self.root.config(bg='#19d3e8')

        self.x = '#04fff7'

        # Registration Frame
        Frame_registration = tkinter.Frame(self.root, bg=self.x)
        Frame_registration.place(x=150, y=40, height=700, width=700)

        # Give title into frame
        title = tkinter.Label(Frame_registration, text="Register Here", font=("Helvetica", 32, "bold"), fg='#002147',
                              bg=self.x).place(
            x=220, y=50)

        # Name
        fname = tkinter.Label(Frame_registration, text='First Name', font=("Sans-Serif", 15, 'bold'), fg='blue',
                              bg=self.x).place(x=110, y=150)
        self.txt_fname = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_fname.place(x=110, y=180, width=200, height=30)

        # lname
        lname = tkinter.Label(Frame_registration, text='Last Name', font=("Sans-Serif", 15, 'bold'), fg='blue',
                              bg=self.x).place(x=400, y=150)
        self.txt_lname = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_lname.place(x=400, y=180, width=200, height=30)

        # contact no
        contact_no = tkinter.Label(Frame_registration, text='Contact No', font=("Sans-Serif", 15, 'bold'), fg='blue',
                                   bg=self.x).place(x=110, y=220)
        self.txt_contact_no = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_contact_no.place(x=110, y=250, width=200, height=30)

        # Aadhar no
        aadhar_no = tkinter.Label(Frame_registration, text='Aadhar Number', font=("Sans-Serif", 15, 'bold'), fg='blue',
                                  bg=self.x).place(x=400, y=220)
        self.txt_aadhar_no = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white',
                                           text='Enter 12 digits only')
        self.txt_aadhar_no.place(x=400, y=250, width=200, height=30)

        # gender
        gender = tkinter.Label(Frame_registration, text='Gender', font=("Sans-Serif", 15, 'bold'), fg='blue', bg=self.x).place(
            x=110, y=290)
        self.cmb_txt = ttk.Combobox(width=50, font=('Sans-Serif', 13), background='white', state='readonly',
                                    justify=tkinter.CENTER)
        self.cmb_txt['values'] = ('Select','Male', 'Female', 'Transgender')
        self.cmb_txt.place(x=260, y=360, width=200, height=30)
        self.cmb_txt.current(0)

        # email id
        email_id = tkinter.Label(Frame_registration, text='Email id', font=("Sans-Serif", 15, 'bold'), fg='blue',
                                 bg=self.x).place(x=400, y=290)
        self.txt_email = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_email.place(x=400, y=320, width=200, height=30)

        # Address
        address = tkinter.Label(Frame_registration, text='Address', font=("Sans-Serif", 15, 'bold'), fg='blue',
                                bg=self.x).place(x=110, y=360)
        self.txt_address = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_address.place(x=110, y=400, width=200, height=30)

        # Age
        age = tkinter.Label(Frame_registration, text='Age', font=("Sans-Serif", 15, 'bold'), fg='blue',
                            bg=self.x).place(x=400, y=360)
        self.txt_age = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_age.place(x=400, y=400, width=200, height=30)

        # username
        username = tkinter.Label(Frame_registration, text='Username', font=("Sans-Serif", 15, 'bold'), fg='blue',
                                 bg=self.x).place(x=110, y=450)
        self.txt_username = tkinter.Entry(Frame_registration, font=('times new roman', 15), bg='white')
        self.txt_username.place(x=110, y=490, width=200, height=30)

        # Password
        password = tkinter.Label(Frame_registration, text='Password',font=("Sans-Serif", 15, 'bold'), fg='blue',
                                 bg=self.x).place(x=400, y=450)
        self.txt_password = tkinter.Entry(Frame_registration, show='*', font=('times new roman', 15), bg='white')
        self.txt_password.place(x=400, y=490, width=200, height=30)

        # Submit Button
        submit_button = tkinter.Button(Frame_registration, command=self.Registration_details, text="Submit", fg='white',
                                       bg='blue',
                                       font=('Lucida fax ', 20)).place(x=250, y=580, width='200', height='40')

        # already having account
        old_account = tkinter.Button(Frame_registration, command=self.login_switch, text="Already have an account? Click here!",
                                     fg='#5b038a', bg=self.x,
                                     bd=0, font=('times new roman', 15)).place(x=100, y=520)

    def login_switch(self):
        self.root.destroy()
        import Login_Switch as LS
        LS.main()

    def Registration_details(self):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if self.cmb_txt.get() == "Select" or self.txt_username.get() == "" or self.txt_password.get() == "" or self.txt_address.get() == "" or self.txt_email.get() == "" or self.txt_aadhar_no.get() == "" or self.txt_contact_no.get() == "" or self.txt_age.get() == "" or self.txt_fname.get() == "" or self.txt_lname.get() == "":
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.root)

        elif len(self.txt_contact_no.get()) != 10:
            messagebox.showerror("Error", "Mobile number must consist of exactly 10 digits!", parent=self.root)
        elif len(self.txt_aadhar_no.get()) != 12:
            messagebox.showerror("Error", "Aadhar number must consist of exactly 12 digits", parent=self.root)

        elif eval(self.txt_age.get()) <= 0:
            messagebox.showerror("Error", "Enter a valid age! ", parent=self.root)

        elif not (re.search(regex, self.txt_email.get())):
            messagebox.showerror("Error", "Enter a valid email address! ", parent=self.root)


        else:
            try:
                con = pymysql.connect(user='root', password='', host='localhost', database='registration')
                cur = con.cursor()
                cur.execute(
                    'insert into details(fname,lname,contact_no,age,email,password,aadhar_no,Login,Gender) values(%s,'
                    '%s,%s,%s,%s,%s,%s,%s,%s)',
                    (self.txt_fname.get(),
                     self.txt_lname.get(),
                     self.txt_contact_no.get(),
                     self.txt_age.get(),
                     self.txt_email.get(),
                     self.txt_password.get(),
                     self.txt_aadhar_no.get(),
                     self.txt_username.get(),
                     self.cmb_txt.get()
                     )
                    )
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                self.root.destroy()
                import LoginGui
            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

def main():
    root = tkinter.Tk()
    obj = Register(root)
    root.mainloop()

if __name__ == "__main__":
    main()