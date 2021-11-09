import pymysql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class User:
    def __init__(self, root):
        self.root = root
        self.root.title("User Portal")

        # Designate Height and Width of our window
        self.app_width = 1280
        self.app_height = 720

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.root.resizable(False, False)

        con = pymysql.connect(user='root', password='', host='localhost', database='registration')
        cur = con.cursor()
        cur.execute("Select entry from username")
        self.row = cur.fetchone()
        print(self.row)
        cur.execute("Delete from username")
        con.commit()
        cur.close()

        # User Frame
        self.frame_user = Frame(self.root, bg='#acb6ff')
        self.frame_user.place(x=190, y=40, height=640, width=900)

        # Username importing
        Label(self.frame_user, text="Welcome:", font=("Cambria", 14, "bold"), fg='#002147',
              bg='#acb6ff').place(x=50, y=10)

        Label(self.frame_user, text=self.row, font=("Cambria", 12), fg='#002147',
              bg='#acb6ff').place(x=140, y=12)

        # Give title into frame
        Label(self.frame_user, text="User Portal", font=("Cambria", 30, "bold"), fg='#002147',
              bg='#acb6ff').place(x=400, y=30)

        # View Vaccine Button
        Button(self.frame_user, text='View Available Vaccine Stock', command=self.view_vacc,
               font=("Georgia", 15, 'bold'), fg='#2604eb',
               bg='white').place(x=40, y=110)

        self.hospital_choosen = ttk.Combobox(self.frame_user, width=50, font=('Sans-serif', 13), state='readonly',
                                             justify=CENTER)

        # Adding combobox drop down list
        self.hospital_choosen['values'] = ('Alphine Life Solutions', 'Atlantis Hospital', 'Fortis Hospital', 'Four Care Hospital', 'Hinduja Healthcare', 'Holy Spirit Hospital', 'JJ Hospital', 'KEM Hospital', 'Kokilaben Hospital', 'Lifeline Hospital', 'Lilavati Hospital', 'Phoenix Hospital', 'Saraswati Hospital', 'Seven Hills Hospital', 'Shatabdi Hospital', 'Silverline Hospital', 'Suchak Hospital', 'Zenith Hospital'
                                           )
        self.hospital_choosen.place(x=400, y=120)
        self.hospital_choosen.current(0)

        Button(self.frame_user, command=self.book_apt, text='Book Appointment',
               font=("Georgia", 15, 'bold'), fg='#2604eb', bg='white').place(x=40, y=180)

        # View Covid Stats
        Button(self.frame_user, text='View COVID Stats', font=("Georgia", 15, 'bold'),
               command=self.view_covidstats, fg='#2604eb', bg='white').place(x=40, y=250)

    def book_apt(self):
        import Appointment as ap
        ap.main(self.row)

    def view_covidstats(self):
        try:
            con = pymysql.connect(user='root', password='', host='localhost', database='registration')
            cur = con.cursor()
            cur.execute("Select * from covidstats")
            row = cur.fetchone()
            Label(text="Total doses given:" + str(row[0]),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=225, y=350)
            Label(text="Number of people who received first dose:" + str(row[1]),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=225, y=400)
            Label(text="Number of people who received second dose:" + str(row[2]),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=225, y=450)
            Label(text="Number of males vaccinated:" + str(row[3]),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=225, y=500)
            Label(text="Number of females vaccinated:" + str(row[4]),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=225, y=550)
            con.commit()
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    def view_vacc(self):
        try:
            con = pymysql.connect(user='root', password='', host='localhost', database='registration')
            cur = con.cursor()
            cur.execute("Select vaccines from vaccine where hospital = %s", str(self.hospital_choosen.selection_get()))
            row = cur.fetchone()
            # View Vaccine Label
            Label(self.frame_user, text=str(row[0]) + " vaccines are available in " + str(self.hospital_choosen.selection_get()),
                  font=("Cambria", 16, "bold"), fg='#002147', bg='#acb6ff').place(x=400, y=165)
            con.commit()
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

def main():
    root = Tk()
    User(root)
    root.mainloop()


if __name__ == "__main__":
    main()