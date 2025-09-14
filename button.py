from tkinter import * 
win = Tk() 
win.geometry("200x500")      
btn = Button(win,text="Click me !", bd=5, background="blue",
        activebackground="green", activeforeground="white", 
        command=win.destroy)    
btn.pack(side="top")  


win.mainloop() 
