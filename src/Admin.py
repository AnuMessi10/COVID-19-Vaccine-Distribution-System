from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import pymysql
import Modify
from PIL import ImageTk  # pip install pillow


class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Portal")

        # Designate Height and Width of our window
        self.app_width = 1280
        self.app_height = 720

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.resizable(False, False)

        # Image Frame
        self.bg = ImageTk.PhotoImage(file="sample.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=1, y=1, relwidth=1,
                                                              relheight=1)  # insert image into frame

        # Admin Frame
        frame_admin = Frame(self.root, bg='#acb6ff')
        frame_admin.place(x=190, y=40, height=640, width=900)

        # Give title into frame
        title_admin = Label(frame_admin, text="Admin Portal", font=("Cambria", 30, "bold"), fg='#002147',
                            bg='#acb6ff').place(
            x=335, y=30)

        # View Vaccine Button
        view_vaccine = Button(frame_admin, command=self.view_vacc, text='View Available Vaccine Stock',
                              font=("Georgia", 15, 'bold'), fg='#2604eb',
                              bg='white').place(x=40, y=110)

        self.hospital_choosen = ttk.Combobox(width=50, font=('Sans-serif', 13), state='readonly', justify=CENTER)

        # Adding combobox drop down list
        self.hospital_choosen['values'] = ('Alphine Life Solutions', 'Atlantis Hospital', 'Fortis Hospital', 'Four Care Hospital', 'Hinduja Healthcare', 'Holy Spirit Hospital', 'JJ Hospital', 'KEM Hospital', 'Kokilaben Hospital', 'Lifeline Hospital', 'Lilavati Hospital', 'Phoenix Hospital', 'Saraswati Hospital', 'Seven Hills Hospital', 'Shatabdi Hospital', 'Silverline Hospital', 'Suchak Hospital', 'Zenith Hospital')
        self.hospital_choosen.place(x=590, y=155)
        self.hospital_choosen.current(0)

        # Modify Vaccine Button
        modify_vaccine = Button(frame_admin, command=self.mod_vacc, text='Modify Current Vaccine Stock',
                                font=("Georgia", 15, 'bold'), fg='#2604eb',
                                bg='white').place(x=40, y=180)

        # Modify appointment button
        modify_appointment = Button(frame_admin, command=self.mod_app, text='Modify Current Appointments',
                                    font=("Georgia", 15, 'bold'), fg='#2604eb',
                                    bg='white').place(x=40, y=250)

    def view_vacc(self):
        try:
            con = pymysql.connect(user='root', password='', host='localhost', database='registration')
            cur = con.cursor()
            cur.execute("Select vaccines from vaccine where hospital = %s", str(self.hospital_choosen.selection_get()))
            row = cur.fetchone()
            vacc_lb = Label(
                                text=str(row[0]) + " vaccines are available in " + str(self.hospital_choosen.selection_get()),
                                font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff')
            vacc_lb.place(x=590, y=225)
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    def mod_vacc(self):
        import Modify as mod
        mod.main()

    def mod_app(self):
        import Appointment_Admin as apt
        apt.main()


def main():
    root = Tk()
    obj = Admin(root)
    root.mainloop()


if __name__ == "__main__":
    main()