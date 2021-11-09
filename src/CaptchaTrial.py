#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install Captcha <-- Install this first
from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os

image_captcha=''

def generate_captcha():
    data_set = list(string.ascii_letters+string.digits) #a-z,A-Z,0-9
    s=''
    for i in range(4):
        a=random.choice(data_set)
        s=s+a
        data_set.remove(a)
        
    global image_captcha
    image_captcha=s
        
    return s
    
def generate_digit_captcha():
    s1='';s=''
    for i in range(4):
        a = str(random.randint(0,9))
        s=s+a
        s1=s1+a+" "
        
    
        
    return s1


def generate_image_captcha():
    os.startfile('c1.png')
    
def generate_first_image():
    img = ImageCaptcha()
    
    s = generate_captcha()
    #print(s)
    value = img.generate(s)
    img.write(s,"c1.png")


def regenerate_image_captcha():
    img = ImageCaptcha()
    
    s = generate_captcha()
    #print(s)
    value = img.generate(s)
    img.write(s,"c1.png")
    os.startfile('c1.png')
    #print("Image Captcha Generated.\n\n")
    


def get_image():
    return image_captcha
        
def check_image_captcha():
    if ans1.get() == get_image():
        tkinter.messagebox.showinfo("SUCCESS!","Captcha Code Matched.")
        ans1.set("")
            
    else:
        tkinter.messagebox.showinfo("WRONG!","Captcha Code does not Matched.")
        ans1.set("")
        
        
root = Tk()
root.title("CAPTCHA Generation")

root.geometry("842x498")

root.configure(background = 'white')
Tops = Frame(root,bg = 'white',pady = 1, width =550, height = 50, relief = "ridge")
Tops.grid(row=0,column=0)

ans = StringVar()
ans1 = StringVar()
generate_first_image()


MainFrame = Frame(root,bg = 'White',pady = 2, width =1350, height = 100, relief = RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame = Frame(MainFrame ,bd=10, width =200, height=200, pady=2,padx=10,bg='white'  ,relief=RIDGE)
LeftFrame.pack(side=RIGHT)


Label_2 =Label(LeftFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="white",fg = "black")
Label_2.grid(row=1, column=0,sticky=W)

Label_9 =Button(LeftFrame, font=('arial', 10,'bold'), text="Show Image",padx=1,pady=1,height=1,width=10,bg="white",fg = "black",command=generate_image_captcha)
Label_9.grid(row=2, column=0)

Label_7 =Label(LeftFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="white",fg = "black")
Label_7.grid(row=2, column=0,sticky=W)

Entry_1=Entry(LeftFrame,font=('arial',20,'bold'),bd=2,fg="black",textvariable= ans1, width=14,
justify=LEFT).grid(row=5,column=0)

Label_7 =Label(LeftFrame, font=('arial', 20,'bold'), text="",padx=2,pady=2, bg="white",fg = "black")
Label_7.grid(row=6, column=0,sticky=W)

Label_7 =Label(LeftFrame, font=('arial', 20,'bold'), text="  ",padx=2,pady=2, bg="white",fg = "black")
Label_7.grid(row=6, column=1,sticky=W)

Label_8 =Button(LeftFrame, font=('Arial', 10,'bold'), text="Check",padx=2,pady=2, bg="white",fg = "black",command=check_image_captcha)
Label_8.grid(row=6, column=0)

Label_4 =Button(LeftFrame, font=('arial', 10,'bold'), text="Regenerate",padx=2,pady=2, bg="white",fg = "black",command=regenerate_image_captcha)
Label_4.grid(row=9, column=0)

Label_7 =Label(LeftFrame, font=('arial', 20,'bold'), text="      ",padx=2,pady=2, bg="white",fg = "black")
Label_7.grid(row=11, column=1,sticky=W)

root.mainloop()


# In[ ]:





# In[ ]:





# In[1]:


pip install Captcha


# In[ ]:




