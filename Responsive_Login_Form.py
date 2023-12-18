import tkinter
from tkinter import messagebox
def login():
    username="adityabikramjena"
    password="17082002"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Success",message="Logged In Successfully")
    else:
        messagebox.showerror(title="Error",message="Invalid Login Credentials")

window=tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

frame=tkinter.Frame(bg='#333333')  #For Responsiveness

#widgets
login_label=tkinter.Label(frame,text="Login",fg='#FF3399',bg='#333333',font=("Arial",30))
username_label=tkinter.Label(frame,text="Username",bg='#333333',fg='#FFFFFF',font=("Arial",16))
username_entry=tkinter.Entry(frame,font=("Arial",16))
password_label=tkinter.Label(frame,text="Password",bg='#333333',fg='#FFFFFF',font=("Arial",16))
password_entry=tkinter.Entry(frame,show="*",font=("Arial",16))
login_button=tkinter.Button(frame,text="Submit",bg='#FF3399',fg='#FFFFFF',font=("Arial",16),command=login)

#placing widgets into grids
login_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column=0,padx=3)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0,padx=3)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)

frame.pack()
window.mainloop()
