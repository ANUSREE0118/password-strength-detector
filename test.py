import customtkinter
from tkinter import *
from tkinter import messagebox
import re
app=customtkinter.CTk()
app.title("Password strength checker")
app.geometry('400x300+480+200')
app.config(bg='#000')
app.resizable(False,False)
#app.iconbitmap('lock.ico')

title_font=('Arial',20,'bold')
subtitle_font=('Arial',17,'bold')
button_font=('Arial',18,'bold')
def is_strong_password(password):
    if len(password)<8:
       # print("password is too short")
        return False
    if not re.search(r'[A-Z]',password):
     #   print("must contail at least one capital letter")
        return False
    
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[!@#$%^&*()-{}|,.,.?/]',password):
        return False
    return True 
def display_password_result():
    password=password_text_box.get()
    if password:
        result_text_box.configure(state='normal')
        result_text_box.delete(0,END)
        if is_strong_password(password):
             result_text_box.insert(0,'strong password')
             result_text_box.configure(fg_color="#069602")
        else:
            
            result_text_box.insert(0,"not recommended")
            result_text_box.configure(fg_color="#F53905")
        result_text_box.configure(state='disabled')  
    else:       
        messagebox.showerror(title='Error',message='Enter a password to check')
            
title_label=customtkinter.CTkLabel(app,text='Password Strength Checker',font=title_font,text_color='#FFF',bg_color='#000')
title_label.place(x=70,y=20)
password_text_box=customtkinter.CTkEntry(app,font=subtitle_font,text_color='#FFF',fg_color='#000',bg_color='#000',border_color='#F53905',width=300,height=50)
password_text_box.place(x=50,y=60)
check_button=customtkinter.CTkButton(app,command=display_password_result,text='Check Password',font=button_font,text_color='#FFF',fg_color='#F53905',bg_color='#000',hover_color='#BD3602',cursor='hand2',corner_radius=20,width=150,height=40)
check_button.place(x=105,y=130)
password_strength_label=customtkinter.CTkLabel(app,text="Your password strength:",font=title_font,text_color='#FFF',bg_color='#000')
password_strength_label.place(x=80,y=180)
result_text_box=customtkinter.CTkEntry(app,state='disabled',font=subtitle_font,text_color='#FFF',fg_color='#000',bg_color='#000',justify='center',width=200,height=30)
result_text_box.place(x=100,y=240)

app.mainloop()