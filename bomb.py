import tkinter as tk
import random

def bt_click(e):
    pass

class Timer:
    def __init__(self,master):
        self.master=master
        self.master.title("💣")
        self.remaining_time=10.0

        self.label=tk.Label(master,font=("Helvetica",50),anchor='e',bg='#3f3f3f',fg='green')
        self.label.place(x=405,y=280)

        button_frame=tk.Frame(master)
        button_frame.pack()

        #self.canvas=tk.Canvas(master,width=400,height=300)
        #self.canvas.pack()

        self.start_button=tk.Button(master,text="Start",font=("Helvetica",10),command=self.start_timer,width=15,height=2)
        self.start_button.place(x=390,y=500)

    def start_timer(self):
        if self.remaining_time>0:
            self.update_timer()
        elif self.remaining_time==0:
            img=tk.PhotoImage(file='bombed.png')
            self.canvas.create_image(500,400,image=img)

    def update_timer(self):
        if self.remaining_time>0:
            self.label.config(text=f'{self.remaining_time:.1f}')
            self.remaining_time -= 0.1
            self.master.after(100,self.update_timer)

        else:
            self.start_button.config(state=tk.DISABLED)

root=tk.Tk()
root.geometry("900x600")
cvs=tk.Canvas(width=900,height=600)
cvs.pack()
cvs.create_rectangle(0,0,900,600,fill="lightgray")
bg=tk.PhotoImage(file='bomb.png')
cvs.create_image(450,350,image=bg)
msg=tk.Label(
        font=("Helvetica",20),
        text='💣爆弾処理💣',
        bg='yellow',
        fg='black'
        )
msg.place(x=370,y=25)
msg2 = tk.Label(
    font=("Helvetica", 15),
    text='６本のコードのうちはずれの１本を切ると爆発してしまいます。\n１０秒以内に爆弾を解除してください！',
    bg='lightgray',
    fg='black'
)
msg2.place(x=180, y=60)

images=[
        tk.PhotoImage(file='hasami.png'),
        tk.PhotoImage(file='safe.png'),
        tk.PhotoImage(file='bombed.png')
        ]
lucky=random.randint(0,5)
buttons=[None]*6
for i in range(6):
    x=30+(i%2)*750
    y=100+(i//2)*150
    b_name='safe' if lucky == i else str(i)
    buttons[i]=tk.Button(image=images[0],name=b_name)
    buttons[i].place(x=x,y=y)
    buttons[i].bind('<ButtonPress>',bt_click)

app=Timer(root)
root.mainloop()
