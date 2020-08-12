from tkinter import *
import webbrowser
root=Tk()
root.geometry("400x350")
root.title("Python Tutorial")
Label(root,text="Learn python from these",font="Consolas 15 bold",height=4).pack()

def tutorial():
    url="https://www.tutorialspoint.com/python/"
    webbrowser.open(url,new=1)
def w3sch():
    url="https://www.w3schools.com/python/default.asp"
    webbrowser.open(link.get(),new=1)
def prgmz():
    url="https://www.programiz.com/python-programming"
    webbrowser.open(url,new=1)
link=StringVar
link=Entry(root)
Button(root,text= "tutorial point" ,activebackground='yellow',bg='white',command=tutorial).pack(pady=10)
Button(root,text="w3schools",activebackground='yellow',bg='white',command=w3sch).pack(pady=10)
Button(root,text="Programiz",activebackground='yellow',bg='white',command=prgmz).pack(pady=10)
root.mainloop()