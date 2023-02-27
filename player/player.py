from pygame import mixer
from tkinter import *
import os
import fnmatch


window = Tk() 
window.title('Music player')
window.geometry("500x500")
window.config(bg="white")

play_img = PhotoImage(file="play.png")
pause_img = PhotoImage(file="pause.png")
stop_img = PhotoImage(file="stop.png")
prec_img = PhotoImage(file="precedent.png")
suiv_img = PhotoImage(file="suivant.png")

ecran = Listbox(window, fg="white", bg="black",width=80,height=17, font=10)
ecran.place(x=-1, y=0)

musique = "C:\\Users\papou\OneDrive\Bureau\musiqua"
paterne = "*.wav"
mixer.init()


def choix():
    label.config(text=ecran.get("anchor"))
    mixer.music.load(musique+"\\"+ ecran.get("anchor"))
    mixer.music.play()

def stopp():
    mixer.music.stop()
    ecran.selection_clear('active')

def suiv():
    next_song =ecran.curselection()
    next_song = next_song[0]+1
    next_song_name = ecran.get(next_song)
    
    label.config(text=next_song_name)
    mixer.music.load(musique+"\\"+ next_song_name)
    mixer.music.play()
    ecran.select_clear(0,'end')
    ecran.activate(next_song)
    ecran.select_set(next_song)

def pre():
    pre_song =ecran.curselection()
    pre_song = pre_song[0]-1
    pre_song_name = ecran.get(pre_song)
    
    label.config(text=pre_song_name)
    mixer.music.load(musique+"\\"+ pre_song_name)
    mixer.music.play()
    ecran.select_clear(0,'end')
    ecran.activate(pre_song)
    ecran.select_set(pre_song)

def pausee():
    if pause["text"]== "pause":
        mixer.music.pause()
        pause["text"] = "pay"

    else:
        mixer.music.unpause()
        pause["text"] = "pause"

label = Label(window, bg="white", text="", fg="black", font=15)
label.place(x=220, y=330)
play = Button(window, text="play", bg="white",image=play_img, width=60, height=60, borderwidth=0, command=choix)
play.place(x=210, y=365)
stop = Button(window, text="stop", bg="white",image=stop_img, width=60, height=60, borderwidth=0, command=stopp)
stop.place(x=280, y=365)
suivant = Button(window, text="suiv", bg="white",image=suiv_img, width=60, height=60, borderwidth=0, command=suiv)
suivant.place(x=350, y=365)
precedant = Button(window, text="prec",bg="white", image=prec_img, width=60, height=60, borderwidth=0, command=pre)
precedant.place(x=80, y=365)
pause = Button(window, text="pause", bg="white",image=pause_img, width=65, height=65, borderwidth=0, command=pausee)
pause.place(x=140, y=365)



for root, dirs,files in os.walk(musique):
    for format in fnmatch.filter(files,paterne):
        ecran.insert('end',format)

window.mainloop() 