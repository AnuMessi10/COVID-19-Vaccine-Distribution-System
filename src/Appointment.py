import pymysql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

class Appointment_details:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Appointment Details")

        # Designate Height and Width of our window
        self.app_width = 1280
        self.app_height = 720

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.color_bg = 'white'
        self.root.config(bg='light blue')
        self.root.resizable(False, False)
        self.username = username

        self.Frame_registration1 = Frame(self.root, bg='white')
        self.Frame_registration1.place(x=140, y=40, height=630, width=1000)

        self.uname_lbl = Label(self.Frame_registration1, text="Welcome:", font=("Cambria", 14, "bold"), fg='#002147',
                               bg='white').place(x=50, y=10)

        self.uname_imp = Label(self.Frame_registration1, text=self.username, font=("Cambria", 12), fg='#002147',
                               bg='white').place(x=140, y=12)

        # label text for title
        Label(self.Frame_registration1, text="Select your Hospital", background=self.color_bg, foreground="black",
              font=("Times New Roman", 18)).place(x=425, y=30)

        # Select Hospital
        def callbackFunc_hospital(event):
            self.hospital_chosen = event.widget.get()
            print(self.hospital_chosen)

        Label(self.Frame_registration1, text="Name :-", background='white', font=("Times New Roman", 15)).place(x=250,
                                                                                                                y=80)
        self.hospital_chosen = ttk.Combobox(self.Frame_registration1, width=50, font=('Sans-serif', 13),
                                            state='readonly', justify=CENTER)
        self.hospital_chosen['values'] = ('Select',
                                          'Alphine Life Solutions', 'Atlantis Hospital', 'Fortis Hospital', 'Four Care Hospital', 'Hinduja Healthcare', 'Holy Spirit Hospital', 'JJ Hospital', 'KEM Hospital', 'Kokilaben Hospital', 'Lifeline Hospital', 'Lilavati Hospital', 'Phoenix Hospital', 'Saraswati Hospital', 'Seven Hills Hospital', 'Shatabdi Hospital', 'Silverline Hospital', 'Suchak Hospital', 'Zenith Hospital'
                                          )
        self.hospital_chosen.place(x=375, y=80)
        self.hospital_chosen.current(0)
        self.hospital_chosen.bind("<<ComboboxSelected>>", callbackFunc_hospital)

        # vaccine name
        def callbackFunc_vaccine(event):
            self.vaccine_chosen = event.widget.get()
            print(self.vaccine_chosen)

        Label(self.Frame_registration1, text="Vaccine:-", background=self.color_bg,
              font=("Times New Roman", 15)).place(x=250, y=120)
        self.vaccine_chosen = ttk.Combobox(self.Frame_registration1, width=50, font=('Sans-serif', 13),
                                           state='readonly', justify=CENTER)
        self.vaccine_chosen['values'] = ('Select', 'Covaxin', 'Covishield', 'Sputnik-V')
        self.vaccine_chosen.place(x=375, y=120)
        self.vaccine_chosen.current(0)
        self.vaccine_chosen.bind("<<ComboboxSelected>>", callbackFunc_vaccine)

        def callbackFunc_dose(event):
            self.dose_chosen = event.widget.get()
            # print(self.dose_chosen)

        # select dose no
        dose = Label(self.Frame_registration1, text="Select Dose:-", background=self.color_bg,
                     font=("Times New Roman", 15)).place(x=250, y=160)
        self.dose_chosen = ttk.Combobox(self.Frame_registration1, width=50, font=('Sans-serif', 13), state='readonly',
                                        justify=CENTER)
        self.dose_chosen['values'] = ('Select', 'Dose 1', 'Dose 2',)
        self.dose_chosen.place(x=375, y=160)
        self.dose_chosen.current(0)
        self.dose_chosen.bind("<<ComboboxSelected>>", callbackFunc_dose)

        def print_sel():
            print(self.choose_date.get_date())
            date.config(text="Selected Date is: " + str(self.choose_date.get_date()))

        self.choose_date = Calendar(self.Frame_registration1, selectmode='day', background='blue', date_pattern='dd/mm/yyyy')
        self.choose_date.place(x=250, y=200, width=500, height=250)

        # def grad_date():
        #    date.config(text="Selected Date is: " + choose_date.get_date())

        # Add Button and Label
        self.x = Button(self.Frame_registration1, text="Get Slot", fg='#0047AB', bg='light blue', width='15',
                        font=('Lucida fax ', 15), command=print_sel).place(x=250, y=465, height=35)
        date = Label(self.Frame_registration1, text="Choose a date", background='white', font=('Sans-Serif', 15))
        date.place(x=430, y=465)

        # Submit Button
        submit_button = Button(self.Frame_registration1, command=self.appointment_details, text="Submit", fg='blue',
                               bg='light blue',
                               font=('Lucida fax ', 18)).place(x=390, y=540, width='200', height='40')

    def appointment_details(self):
        if self.hospital_chosen == 'Select' or self.dose_chosen == "Select" or self.vaccine_chosen == 'Select':
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.root)

        else:
            try:
                con = pymysql.connect(user='root', password='', host='localhost', database='registration')
                cur = con.cursor()
                cur.execute(
                    "insert into appointment(username, hospital, date_vac ,dose, vaccine) values(%s,%s,%s,%s,%s)",
                    (
                        self.username,
                        self.hospital_chosen,
                        self.choose_date.selection_get(),
                        self.dose_chosen,
                        self.vaccine_chosen
                    )
                )
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)


def main(username):
    root = Tk()
    Appointment_details(root, username)
    root.mainloop()

if __name__ == "__main__":
    main()