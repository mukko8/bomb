import tkinter as tk
import random

root=tk.Tk()
cvs=tk.Canvas(width=900,height=600)
cvs.pack()
#bg=tk.PhotoImage(file='bg.png')
bg='white'
cvs.create_image(450,300,)#image=bg)
msg=tk.Label(
        text='○○ゲーム',
        bg='yellow',
        fg='black'
        )
msg.place(x=200,y=30)
root.mainloop()
