import tkinter as tk
import random
from tkinter import messagebox


class Timer:
    def __init__(self,master):
        self.master=master
        self.master.title("残り時間")
        self.remaining_time=10.00

        self.label=tk.Label(master,font=("Helvetica",24))
        self.label.pack(pady=20)

        button_frame=tk.Frame(master)
        button_frame.pack()

        self.start_button=tk.Button(master,text="Start",command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        if self.remaining_time>0:
            self.update_timer()
        else:
            messagebox.showinfo("Time up!")

    def update_timer(self):
        if self.remaining_time>0:
            self.label.config(text=f'残り{self.remaining_time:.2f}秒')
            self.remaining_time -= 0.01
            self.master.after(10,self.update_timer)

        else:
            self.start_button.config(state=tk.DISABLED)

root=tk.Tk()
root.geometry("900x600")
cvs=tk.Canvas(width=900,height=600)
cvs.pack()
#bg=tk.PhotoImage(file='bg.png')
bg='white'
cvs.create_image(450,300)#,image=bg)
msg=tk.Label(
        text='○○ゲーム',
        bg='yellow',
        fg='black'
        )
msg.place(x=200,y=30)

app=Timer(root)
root.mainloop()
