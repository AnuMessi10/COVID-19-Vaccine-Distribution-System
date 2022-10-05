from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
from tkcalendar import *
import pymysql


class Apt:
    def __init__(self, root):
        self.root = root
        self.root.title('Admin Portal - Appointment')

        # Designate Height and Width of our window
        self.app_width = 900
        self.app_height = 768

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.iconbitmap('administrator.ico')

        self.bg = ImageTk.PhotoImage(file="admin_apt.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=1, y=1, relwidth=1,
                                                              relheight=1)

        self.my_style = ttk.Style()
        self.my_style.theme_use("clam")
        self.my_style.configure("Treeview", foreground="white", background="white", rowheight=23,
                                fieldbackground="white")
        self.my_style.map('Treeview', background=[('selected', 'blue')])

        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=20)

        # Treeview ScrollBar
        self.tree_scrollbar = Scrollbar(self.tree_frame)
        self.tree_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scrollbar.set, selectmode="browse")
        self.my_tree.pack()

        self.tree_scrollbar.config(command=self.my_tree.yview)

        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")

        # Define our columns
        self.my_tree['columns'] = ("UserName", "Hospital", "Date of dosage", "Dose", "Vaccine")

        # Format our columns
        self.my_tree.column("#0", width=45, minwidth=30, anchor=CENTER)
        self.my_tree.column("UserName", width=120, minwidth=75, anchor=CENTER)
        self.my_tree.column("Hospital", width=250, minwidth=100, anchor=CENTER)
        self.my_tree.column("Date of dosage", width=140, minwidth=75, anchor=CENTER)
        self.my_tree.column("Dose", width=100, minwidth=75, anchor=CENTER)
        self.my_tree.column("Vaccine", width=100, minwidth=75, anchor=CENTER)

        # Create Headings
        self.my_tree.heading("#0", text="Sr. No.")
        self.my_tree.heading("UserName", text="UserName", anchor=CENTER)
        self.my_tree.heading("Hospital", text="Hospital", anchor=CENTER)
        self.my_tree.heading("Date of dosage", text="Date of dosage", anchor=CENTER)
        self.my_tree.heading("Dose", text="Dose", anchor=CENTER)
        self.my_tree.heading("Vaccine", text="Vaccine", anchor=CENTER)

        self.my_tree.pack(pady=30)

        # Frame for buttons
        edit_frame = Frame(root)
        edit_frame.pack(pady=40)

        # Creating Labels for columns
        self.user_lbl = Label(edit_frame, text="UserName")
        self.user_lbl.grid(row=0, column=0)

        self.hosp_lbl = Label(edit_frame, text="Hospital")
        self.hosp_lbl.grid(row=0, column=1)

        self.date_lbl = Label(edit_frame, text="Date")
        self.date_lbl.grid(row=0, column=2)

        self.dose_lbl = Label(edit_frame, text="Dose")
        self.dose_lbl.grid(row=0, column=3)

        self.vaccine_lbl = Label(edit_frame, text="Vaccine")
        self.vaccine_lbl.grid(row=0, column=4)

        # Entry Boxes
        self.user_box = Entry(edit_frame)
        self.user_box.grid(row=1, column=0)

        self.hosp_box = ttk.Combobox(edit_frame, font=('Sans-serif', 8), state='readonly', justify=CENTER)
        self.hosp_box['values'] = (
        'Alphine Life Solutions', 'Atlantis Hospital', 'Fortis Hospital', 'Four Care Hospital', 'Hinduja Healthcare', 'Holy Spirit Hospital', 'JJ Hospital', 'KEM Hospital', 'Kokilaben Hospital', 'Lifeline Hospital', 'Lilavati Hospital', 'Phoenix Hospital', 'Saraswati Hospital', 'Seven Hills Hospital', 'Shatabdi Hospital', 'Silverline Hospital', 'Suchak Hospital', 'Zenith Hospital')
        self.hosp_box.grid(row=1, column=1)

        self.date_box = DateEntry(edit_frame, date_pattern='dd/mm/yyyy')
        self.date_box.delete(0, END)
        self.date_box.grid(row=1, column=2)

        self.dosage_box = ttk.Combobox(edit_frame, font=('Sans-serif', 8), state='readonly', justify=CENTER)
        self.dosage_box['values'] = ('Dose 1', 'Dose 2')
        self.dosage_box.grid(row=1, column=3)

        self.vaccine_box = ttk.Combobox(edit_frame, font=('Sans-serif', 8), state='readonly', justify=CENTER)
        self.vaccine_box['values'] = ('Covaxin', 'Covishield', 'Sputnik-V')
        self.vaccine_box.grid(row=1, column=4)

        # Bind the treeview to our entry boxes
        self.my_tree.bind('<ButtonRelease-1>', self.select_record)

        # Display Button
        self.display = Button(root, text="Display data", command=self.view)
        self.display.pack(padx=0, pady=10)

        # Add Records Button
        self.add_records = Button(root, text="Add Records", command=self.add_record)
        self.add_records.pack(padx=15, pady=10)

        # Delete Selection Button
        self.del_selection = Button(root, text="Delete Selection", command=self.delete_data)
        self.del_selection.pack(padx=30, pady=10)

        # Update Records Button
        self.update_records = Button(root, text="Update Selected Record", command=self.update_data)
        self.update_records.pack(padx=45, pady=10)

    # Get treeview selection into entry boxes
    def select_record(self, e):
        try:
            # Clear the content first
            self.user_box.delete(0, END)
            self.hosp_box.set('')
            self.date_box.delete(0, END)
            self.dosage_box.set('')
            self.vaccine_box.set('')

            # Grab the data from selection
            selected = self.my_tree.focus()

            # Grab the record values
            values = self.my_tree.item(selected, 'values')

            self.user_box.insert(0, values[0])
            self.hosp_box.set(values[1])
            self.date_box.set_date(values[2])
            self.dosage_box.set(values[3])
            self.vaccine_box.set(values[4])

            global old_user
            old_user = self.user_box.get()
        except IndexError:
            pass
        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    # View Data Function
    def view(self):
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)

        con1 = pymysql.connect(user='root', password='', host='localhost', database='registration')

        cur1 = con1.cursor()

        cur1.execute("SELECT username, hospital, DATE_FORMAT(date_vac, '%d/%m/%Y'), dose, vaccine FROM appointment")

        rows = cur1.fetchall()

        global counter
        counter = 1
        for row in rows:
            if counter % 2 == 0:
                self.my_tree.insert('', index='end', iid=counter, text=counter,
                                    values=(row[0], row[1], row[2], row[3], row[4]), tags=('evenrow',))
            else:
                self.my_tree.insert('', index='end', iid=counter, text=counter,
                                    values=(row[0], row[1], row[2], row[3], row[4]), tags=('oddrow',))

            counter += 1

        con1.close()

    # Add Data Function
    def add_record(self):
        if self.user_box.get() == '' or self.hosp_box.get() == '' or self.date_box.get() == '' or self.dosage_box.get() == '' or self.vaccine_box.get() == '':
            messagebox.showerror("Error", "Fill in all the fields before adding a new record!", parent=self.root)
        else:
            try:
                con1 = pymysql.connect(user='root', password='', host='localhost', database='registration')

                cur1 = con1.cursor()

                cur1.execute(
                    'INSERT into appointment(username, hospital, date_vac, dose, vaccine) values (%s, %s, STR_TO_DATE(%s, %s), %s, %s)',
                    (self.user_box.get(), self.hosp_box.get(), self.date_box.get(), '%d/%m/%Y', self.dosage_box.get(),
                     self.vaccine_box.get()
                     )
                )

                con1.commit()

                con1.close()

                self.my_tree.insert('', index='end', iid=counter, text=counter,
                                    values=(
                                        self.user_box.get(), self.hosp_box.get(), self.date_box.get(),
                                        self.dosage_box.get(),
                                        self.vaccine_box.get()))

                # Clear the content of entry boxes
                self.user_box.delete(0, END)
                self.hosp_box.set('')
                self.date_box.delete(0, END)
                self.dosage_box.set('')
                self.vaccine_box.set('')

                self.view()
            except Exception as e:
                if e.__class__.__name__ != "IntegrityError":
                    messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)
                else:
                    messagebox.showerror("Duplicate Entry Found!", "A record with the same username already exists!")

    # Update Data Function
    def update_data(self):
        if self.user_box.get() == '' or self.hosp_box.get() == '' or self.date_box.get() == '' or self.dosage_box.get() == '' or self.vaccine_box.get() == '':
            messagebox.showerror("Error", "Fill in all the fields before updating any record!", parent=self.root)
        else:
            try:
                con1 = pymysql.connect(user='root', password='', host='localhost', database='registration')

                cur1 = con1.cursor()

                cur1.execute(
                    "UPDATE appointment SET username = %s, date_vac = STR_TO_DATE(%s, %s),  vaccine = %s, dose = %s, hospital = %s, WHERE "
                    "username = %s",
                    (
                        self.user_box.get(), self.date_box.get(),'%d/%m/%Y', self.vaccine_box.get(),
                        self.dosage_box.get(), self.hosp_box.get(), old_user
                    ))

                con1.commit()

                con1.close()

                self.view()

                # Clear the content of entry boxes
                self.user_box.delete(0, END)
                self.hosp_box.set('')
                self.date_box.delete(0, END)
                self.dosage_box.set('')
                self.vaccine_box.set('')

            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

    # Delete Record Function
    def delete_data(self):
        if self.user_box.get() == '':
            messagebox.showerror("Error", "Fill in the username before deleting any record", parent=self.root)
        else:
            try:
                con1 = pymysql.connect(user='root', password='', host='localhost', database='registration')

                cur1 = con1.cursor()

                cur1.execute(
                    "DELETE FROM appointment where username = %s",
                    (
                        self.user_box.get()
                    ))

                con1.commit()

                con1.close()

                messagebox.showinfo("Success", "Record of " + self.user_box.get() + " deleted successfully!",
                                    parent=self.root)

                self.view()

                # Clear the content of entry boxes
                self.user_box.delete(0, END)
                self.hosp_box.set('')
                self.date_box.delete(0, END)
                self.dosage_box.set('')
                self.vaccine_box.set('')

            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

def main():
    root = Toplevel()
    Apt(root)
    root.mainloop()


if __name__ == "__main__":
    main()
