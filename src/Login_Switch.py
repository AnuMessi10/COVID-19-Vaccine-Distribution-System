import tkinter
from tkinter import *
from tkinter import messagebox

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")

        # Designate Height and Width of our window
        self.app_width = 500
        self.app_height = 300

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2)

        self.root.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        self.root.resizable(False, False)

        self.root.config(bg="grey")

        Frame_window = Frame(self.root, bg='light blue')
        Frame_window.place(x=25, y=25, height=250, width=450)

        Admin_Label = Label(Frame_window, text='Admin Login:', font=14 ,bg='light blue')
        Admin_Label.place(x=25, y=10)

        Admin_Button = Button(Frame_window, text='Admin Login', font=14, command=self.Admin_window, bg='blue', fg='white')
        Admin_Button.place(x=25, y=40)

        User_Label = Label(Frame_window, text='User Login:', font=14, bg='light blue')
        User_Label.place(x=25, y=100)

        User_Button = Button(Frame_window, text='User Login', command=self.User_window, font = 14, bg='blue', fg='white')
        User_Button.place(x=25, y=130)

        Button(Frame_window, text="Do not have an account? Click here to register!!"
                                   , command=self.Registration_window, fg='blue', bg='light blue',
                                   bd=0, font=('times new roman', 14)).place(x=25, y=175)

    def Registration_window(self):
        self.root.destroy()
        import Registration as Rg
        Rg.main()

    def Admin_window(self):
        self.root.destroy()
        import AdminLogin as adml
        adml.main()

    def User_window(self):
        self.root.destroy()
        import LoginGui as Lg
        Lg.main()


def main():
    root = tkinter.Tk()
    Window(root)
    root.mainloop()


if __name__ == "__main__":
    main()