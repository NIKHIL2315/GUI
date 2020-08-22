''' Firstly name the music file as  'file.mp3' and 
it should be in same directory of the code. 
click on the buttons to control. '''


from pygame import mixer
from tkinter import *
root=Tk()
root.title('Music Player')
root.geometry('600x350')
mixer.init()
mixer.music.load('file.mp3')
def play():
    mixer.music.play()
def resume():
    mixer.music.unpause()
def pause():
    mixer.music.pause()
Label(root,text=' Welcome to \nMUSIC PLAYER',font="Consolas 15 bold").pack()
Button(root,text='Play',command=play).place(x=200,y=100)
Button(root,text='Pause',command=pause).place(x=250,y=100)
Button(root,text='Resume',command=resume).place(x=300,y=100)
Button(root,text='Exit',command=quit).place(x=360,y=100)
root.mainloop()