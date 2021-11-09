import pymysql
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Modify:
    def __init__(self, root):
        self.root = root
        self.root.title("Modify Vaccine Stock")
        self.root.config(bg="light grey")

        # Designate Height and Width of our window
        self.app_width = 390
        self.app_height = 350

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.resizable(False, False)

        # Frame
        frame_main = Frame(self.root, bg='light yellow')
        frame_main.place(x=0, y=0, height=350, width=390)

        # receive input for vaccine label
        Label(frame_main, text="Enter the number of vaccines", font=("Cambria", 14, "bold"), fg='#002147',
              bg='light yellow').place(x=55, y=15)

        # receive input field
        self.txt_inp = Entry(frame_main, font=('Consolas', 12), bg='white')
        self.txt_inp.insert(0, 0)
        self.txt_inp.place(x=45, y=55, width=280, height=35)

        self.store = self.txt_inp.get()
        self.store = int(self.store)
        # print(self.store)

        # receive input for hospital selection label
        Label(frame_main, text="Select the hospital", font=("Cambria", 14, "bold"), fg='#002147',
              bg='light yellow').place(x=100, y=100)

        self.hosp_box = ttk.Combobox(frame_main, font=('Sans-serif', 8), state='readonly', justify=CENTER)
        self.hosp_box['values'] = (
                                    'Alphine Life Solutions', 'Atlantis Hospital', 'Fortis Hospital', 'Four Care Hospital', 'Hinduja Healthcare', 'Holy Spirit Hospital', 'JJ Hospital', 'KEM Hospital', 'Kokilaben Hospital', 'Lifeline Hospital', 'Lilavati Hospital', 'Phoenix Hospital', 'Saraswati Hospital', 'Seven Hills Hospital', 'Shatabdi Hospital', 'Silverline Hospital', 'Suchak Hospital', 'Zenith Hospital'
                                    )
        self.hosp_box.place(x=45, y=140, width=280, height=25)

        # add vac
        Button(frame_main, command=self.add_vac, text='Add', font=("Georgia", 14, 'bold'), fg='white',
               bg='red').place(x=30, y=195, width=135, height=45)

        # subtract/delete/remove vac
        Button(frame_main, command=self.rem_vac, text='Remove', font=("Georgia", 14, 'bold'), fg='white',
               bg='red').place(x=210, y=195, width=135, height=45)

        # close
        Button(frame_main, command=self.clo, text='Close', font=("Georgia", 17, 'bold'), fg='white',
               bg='red').place(x=115, y=255, width=140, height=45)

    def add_vac(self):
        try:
            if int(self.txt_inp.get()) <= 0:
                messagebox.showerror("Error", "Enter a valid input!", parent=self.root)
            else:
                con = pymysql.connect(user='root', password='', host='localhost', database='registration')
                cur = con.cursor()
                int(self.txt_inp.get())
                cur.execute("UPDATE vaccine SET vaccines = vaccines + %s where hospital = %s ",
                            (self.txt_inp.get(), self.hosp_box.selection_get()))
                con.commit()
                con.close()
                cur.close()
                messagebox.showinfo("Success!",
                                    "" + self.txt_inp.get() + " vaccines were successfully added to the stock of " + str(self.hosp_box.selection_get()) + "!",
                                    parent=self.root)
        except TclError as err:
            messagebox.showerror("Error!", f"Select a hospital!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    def rem_vac(self):
        try:
            if int(self.txt_inp.get()) <= 0:
                messagebox.showerror("Error", "Enter a valid input!", parent=self.root)
            else:
                con = pymysql.connect(user='root', password='', host='localhost', database='registration')
                cur = con.cursor()
                cur.execute("Select `vaccines` from `vaccine` where `hospital` = %s", (str(self.hosp_box.selection_get())))
                row = cur.fetchone()
                if int(self.txt_inp.get()) > row[0]:
                    messagebox.showerror("Invalid Operation!", "Number of vaccines is already less than the ones being removed!")
                else:
                    cur.execute("UPDATE vaccine SET vaccines = vaccines - %s where hospital = %s ",
                                (self.txt_inp.get(), self.hosp_box.selection_get()))
                    con.commit()
                    con.close()
                    cur.close()
                    messagebox.showinfo("Success!",
                                        "" + self.txt_inp.get() + " vaccines were successfully removed from the stock of " + self.hosp_box.selection_get() + " !",
                                        parent=self.root)
        except TclError as err:
            messagebox.showerror("Error!", f"Select a hospital!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to:{str(e)}", parent=self.root)

    def clo(self):
        self.root.destroy()


def main():
    root = Tk()
    Modify(root)
    root.mainloop()


if __name__ == "__main__":
    main()