import tkinter as tk
from tkinter import messagebox


class Login:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title('Login')
        self.root.geometry('950x500')
        self.root.configure(bg='white')
        self.root.resizable(False,False)

        #global img
        img = tk.PhotoImage(file='login.png')
        tk.Label(self.root, image=img, bg='white').place(x=50,y=50)

        frame = tk.Frame(self.root, width=400, height=400, bg='white')
        frame.place(x = 500,y=50)

        heading = tk.Label(frame,text='Sign in', bg='white', fg='#57a1f8', font=('Arial',25,'bold'))
        heading.place(x=75,y=10)


        # User name Entry
        self.username = tk.Entry(frame, width= 30, fg='gray', border=0, font=('Arial', 11))
        self.username.place(x=75, y=70)
        self.username.insert(0, 'Username')
        self.username.bind('<FocusIn>', self.user_on_enter)
        self.username.bind('<FocusOut>', self.user_on_leave)


        # Line seperating the username entry field from the password entry field
        tk.Frame(frame,width=250,height=2,bg='gray').place(x=75,y=95)

        
        # Password entry field
        self.password = tk.Entry(frame, width=30, border=0, fg='gray', font=('Arial',11))
        self.password.place(x=75,y=120)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.password_on_enter)
        self.password.bind('<FocusOut>', self.password_on_leave)
        self.password.bind('<KeyPress>', self.signin_ent)

        tk.Frame(frame,width=250,height=2,bg='gray').place(x=75,y=145)


        buttonsignin = tk.Button(frame, width=25, bg='#57a1f8', fg='white',border=0, cursor='hand2', text='Sign in', font=('Arial', 13, 'bold'), command=self.signin)
        buttonsignin.place(x=75,y=180)
        

        newaccountlabel = tk.Label(frame, text='Don\'t have an account?', font=('Arial', 13), bg='white', fg='gray')
        newaccountlabel.place(x=85, y=230)

        buttonsignup = tk.Button(frame, width=25, border=0, bg='#57a1f8', fg='white', cursor='hand2', text='Sign up', font=('Arial', 13, 'bold'))
        buttonsignup.place(x=75, y=270)

        self.root.mainloop()

    def user_on_enter(self,event):
        self.username.delete(0, tk.END)

    def user_on_leave(self,event):
        user = self.username.get()
        if user == '':
            self.username.insert(0, 'Username')

    def password_on_enter(self, event):
        self.password.delete(0,tk.END)

    def password_on_leave(self, event):
        userpass = self.password.get()
        if userpass == '':
            self.password.insert(0, 'Username')
    
    def signin(self):
        user = self.username.get()
        userpass = self.password.get()

        if user != 'Emma' and userpass != 'cat456':
            messagebox.showerror('Invalid', 'Invalid username and password')
        elif userpass != 'cat456':
            messagebox.showerror('Invalid', 'Invalid password')
        elif user != 'Emma':
            messagebox.showerror('Invalid', 'Invalid username')
        elif user == 'Emma' and userpass == 'cat456':
            newWindow = tk.Toplevel(self.root)
            newWindow.title('Home')
            newWindow.geometry('950x500')
            newWindow.config(bg='white')
            newWindow.resizable(False,False)

            tk.Label(newWindow, text='WELCOME HOME', fg='#57a1f8', bg='white' ,font=('Arial',30,'bold')).pack(expand=True)

            newWindow.mainloop()

    def signin_ent(self, event):
        # print(event)
        if event.keysym == 'Return' and event.keycode == 13:
            self.signin()


if __name__ == '__main__':
    Login()
