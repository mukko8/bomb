import tkinter as tk
import random
from tkinter import messagebox

root=tk.Tk()
root.geometry("900x600")
cvs=tk.Canvas(width=900,height=600)
cvs.pack()
cvs.create_rectangle(0,0,900,600,fill="lightgray")
bg=tk.PhotoImage(file='bomb.png')
cvs.create_image(450,300,image=bg)
msg=tk.Label(
        text='爆弾処理',
        bg='yellow',
        fg='black'
        )
msg.place(x=450,y=30)

class Timer:
    def __init__(self,master):
        self.master=master
        self.master.title("爆弾処理")
        self.remaining_time=10

        self.label=tk.Label(master,font=("Helvetica",24))
        self.label.pack(pady=20)

        button_frame=tk.Frame(master)
        button_frame.pack()

        self.canvas=tk.Canvas(master,width=400,height=300)
        self.canvas.pack()

        self.start_button=tk.Button(master,text="Start",command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        if self.remaining_time>0:
            self.update_timer()
        else:
            self.show_image(file='failure.png')

    def update_timer(self):
        if self.remaining_time>0:
            self.label.config(text=f'残り{self.remaining_time}秒')
            self.remaining_time -= 1
            self.master.after(1000,self.update_timer)

        else:
            self.start_button.config(state=tk.DISABLED)


app=Timer(root)
root.mainloop()
