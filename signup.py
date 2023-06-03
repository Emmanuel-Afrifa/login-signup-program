import tkinter as tk
from tkinter import messagebox
import login

class Signup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Sign up')
        self.root.configure(bg='white')
        self.root.geometry('950x500')
        self.root.resizable(False, False)

        img = tk.PhotoImage(file='login1.png')
        tk.Label(self.root,image=img,bg='white').place(x=50,y=100)

        self.frame = tk.Frame(self.root, width=400, height=400, bg='white')
        self.frame.place(x=500,y=50)

        self.heading = tk.Label(self.frame, text='Sign Up', bg='white', fg='#57a1f8', font=('Arial',25,'bold'))
        self.heading.place(x=75, y=10)

        self.username = tk.Entry(self.frame, width= 30, fg='gray', border=0, font=('Arial', 11))
        self.username.place(x=75, y=70)
        self.username.insert(0, 'Username')
        self.username.bind('<FocusIn>', self.user_on_enter)
        self.username.bind('<FocusOut>', self.user_on_leave)

        tk.Frame(self.frame, width=250, height=2, bg='gray').place(x=75,y=95)

        self.password = tk.Entry(self.frame, width=30, border=0, fg='gray', font=('Arial',11))
        self.password.place(x=75,y=125)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.pass_on_enter)
        self.password.bind('<FocusOut>', self.pass_on_leave)

        tk.Frame(self.frame, width=250, height=2, bg='gray').place(x=75,y=150)

        self.pass_confirm = tk.Entry(self.frame, width=30, border=0, fg='gray', font=('Arial',11))
        self.pass_confirm.place(x=75,y=180)
        self.pass_confirm.insert(0, 'Confirm Password')
        self.pass_confirm.bind('<FocusIn>', self.confirm_on_enter)
        self.pass_confirm.bind('<FocusOut>', self.confirm_on_leave)

        tk.Frame(self.frame, width=250, height=2, bg='gray').place(x=75,y=205)

        self.signupbutt = tk.Button(self.frame, text='Sign Up', cursor='hand2', width=25, bg='#57a1f8', border=0, fg='white', font=('Arial', 13, 'bold'))
        self.signupbutt.place(x=75,y=240)

        self.loginlabel = tk.Label(self.frame, text='I have an account?', font=('Arial', 11), bg='white', fg='gray')
        self.loginlabel.place(x=80, y=290)

        self.buttonsignin = tk.Button(self.frame, width=5, border=0, bg='white', fg='#57a1f8', cursor='hand2', text='Sign in', font=('Arial', 11), command=self.existinguser)
        self.buttonsignin.place(x=215, y=287)


        self.root.mainloop()


    def user_on_enter(self,event):
        self.username.delete(0, tk.END)

    def pass_on_enter(self,event):
        self.password.delete(0, tk.END)

    def confirm_on_enter(self,event):
        self.pass_confirm.delete(0, tk.END)

    def user_on_leave(self,event):
        initial = self.username.get()
        if initial == '':
            self.username.insert(0, 'Username')

    def pass_on_leave(self,event):
        initial = self.password.get()
        if initial == '':
            self.password.insert(0, 'Password')

    def confirm_on_leave(self,event):
        initial = self.pass_confirm.get()
        if initial == '':
            self.pass_confirm.insert(0, 'Confirm Password')

    def existinguser(self):
       #self.root.destroy()
        login.Login()
        
Signup()