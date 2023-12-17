import tkinter
import pyshorteners

window=tkinter.Tk()
window.title("URL Shortner")
window.geometry('360x360')
window.configure(bg='orange')
frame=tkinter.Frame(bg="green")

def ShortenURL():
    shortener=pyshorteners.Shortener()
    short_url=shortener.tinyurl.short(longurl_entry.get())
    short_url_entry.insert(0,short_url)

title_label=tkinter.Label(frame,text="Welcome To URL Shortening Services",fg='#FF3399',bg='#333333',font=("Arial",30))
longurl_label=tkinter.Label(frame,text="Enter Long URL",font=("Arial",15))
longurl_entry=tkinter.Entry(frame,font=("Arial",15))
short_url_label=tkinter.Label(frame,text="Generating Short URL",font=("Arial",15))
short_url_entry=tkinter.Entry(frame,font=("Arial",15))
shortening_button=tkinter.Button(frame,text="Shorten URL",command=ShortenURL,font=("Arial",15))

#title_label.grid(row=0,column=0,columnspan=2,sticky="news",pady=40,padx=25)
# longurl_label.grid(row=1,column=0,padx=12,pady=10)
# longurl_entry.grid(row=2,column=0,pady=13,padx=10)

title_label.pack()
longurl_label.pack()
longurl_entry.pack()
short_url_label.pack()
short_url_entry.pack()
shortening_button.pack()
frame.pack()
window.mainloop()
