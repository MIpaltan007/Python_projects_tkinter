import tkinter

window=tkinter.Tk()
window.configure(bg='orange')
frame=tkinter.Frame(bg='pink')

text=tkinter.Text(frame,width=70,height=25,font=("Algerian",15),bg='lightblue',fg='black')
text.pack()

def getText():
    print(text.get("1.0","end"))

get_button=tkinter.Button(frame,text="Get Text",command=getText,font=("Arial",15))
get_button.pack()

def insertText():
    text.insert("1.0","Hello World!")

insert_button=tkinter.Button(frame,text="Insert Text",command=insertText,font=("Arial",15))
insert_button.pack()

def DeleteText():
    text.delete("1.0","end")

delete_button=tkinter.Button(frame,text="Delete Text",command=DeleteText,font=("Arial",15))
delete_button.pack()

frame.pack()
window.mainloop()
