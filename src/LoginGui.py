from tkinter import *
from tkinter import messagebox
import pymysql
import random
import string
from tkinter import Tk, Label, Entry, Button
from PIL import ImageTk, Image
from captcha.image import ImageCaptcha


class login:

    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        # Designate Height and Width of our window
        self.app_width = 995
        self.app_height = 702

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.resizable(False, False)  # user cannot expand image

        # Image Frame
        self.bg = ImageTk.PhotoImage(file="Login.jpg")  # add image in background
        self.bg_image = Label(self.root, image=self.bg).place(x=1, y=1, relwidth=1,
                                                              relheight=1)  # insert image into frame

        # Login Frame
        Frame_login = Frame(self.root, bg='light blue')
        Frame_login.place(x=400, y=150, height=400, width=500)

        # Give title into frame
        title = Label(Frame_login, text="User Login", font=("Cambia", 30, "bold"),
                      fg='#002147', bg='light blue').place(x=140, y=30)

        # creating label username
        user_name = Label(Frame_login, text='Username', font=("Georgia", 15, 'bold'),
                          fg='#0067A5', bg='light blue').place(x=70, y=90)
        self.txt_user = Entry(Frame_login, font=('times new roman', 15))
        self.txt_user.place(x=70, y=120, width=350, height=30)

        # creating label password
        password = Label(Frame_login, text='Password', font=("Georgia", 15, 'bold'),
                         fg='#0067A5', bg='light blue').place(x=70, y=150)
        self.txt_pass = Entry(Frame_login, font=('times new roman', 15), show="•")
        self.txt_pass.place(x=70, y=180, width=350, height=30)

        # creating label captcha
        Label(Frame_login, text='Enter Captcha', font=("Georgia", 15, 'bold'),
              fg='black', bg='light blue').place(x=250, y=220)

        # Refresh button
        path = 'refresh.jpg'
        reload_img = ImageTk.PhotoImage(Image.open(path).resize((30, 30), Image.ANTIALIAS))
        reload_button = Button(Frame_login, text='Reload', image=reload_img,
                               fg='red', bg='light blue', borderwidth=0, command=self.generate_image_captcha)
        reload_button.place(x=60, y=290)

        # Entry
        self.entry = Entry(Frame_login, width=15, borderwidth=5, font=("Georgia", 15), justify="center")
        self.entry.grid(row=2, column=0)
        self.entry.place(x=250, y=250)

        # submit button
        submit = Button(Frame_login, command=self.login_function, text='Login', font=("Georgia", 15, 'bold'),
                        fg='#0067A5', bg='light blue').place(x=130, y=330, width=180, height=40)
        self.generate_image_captcha()
        mainloop()

    def generate_image_captcha(self):
        self.image_label = Label(self.root)
        self.random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        self.image_captcha = ImageCaptcha(width=180, height=60)
        self.image_generated = self.image_captcha.generate(self.random_string)
        self.image_display = ImageTk.PhotoImage(Image.open(self.image_generated))
        self.image_label.grid_forget()
        self.image_label = Label(self.root, image=self.image_display)
        self.image_label.grid(padx=450, pady=380, row=1, column=0, columnspan=2)

    def login_function(self):
        print(self.random_string)
        print(self.entry.get())

        # check if all fields are filled or not
        if self.txt_user.get() == '' or self.txt_pass.get() == '' or self.entry.get() == '':
            messagebox.showerror("Error", "All fields are mandatory to fill", parent=self.root)

        # check if captcha matched or not
        if self.entry.get() != self.random_string:
            messagebox.showerror("Error", "Invalid Captcha", parent=self.root)
        else:
            try:
                # database connection
                con = pymysql.connect(user='root', password='', host='localhost', database='registration')
                cur = con.cursor()
                cur.execute("Select * from details where Login=%s and password = %s",
                            (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchone()
                print(row)

                if row is None:
                    messagebox.showerror("Error", 'Invalid Username or password', parent=self.root)
                    con.close()
                else:
                    messagebox.showinfo("Welcome", 'Login Successful!', parent=self.root)
                    part1 = 'insert into username(entry) values (%s)'
                    part2 = (self.txt_user.get(),)
                    cur.execute(part1, part2)
                    con.commit()
                    con.close()
                    self.root.destroy()
                    import UserGUI as UG
                    UG.main()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to:{str(e)}", parent=self.root)

def main():
    root = Tk()
    obj = login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
