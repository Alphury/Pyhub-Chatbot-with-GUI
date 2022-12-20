from tkinter import *
from tkinter import ttk
from main2 import *

class gui:
    def __init__(self,master):
        self.master = master
        self.master.title("ChatBot")
        self.master.geometry("500x600")
        self.master.configure(bg='purple')

        mframe=Frame(self.master,bd=4,bg='purple',width=600)
        mframe.pack()

        maintitle=Label(mframe,bd=3,relief=RAISED,text="ChatBot",font=('ROG Fonts',30))
        maintitle.pack(side=TOP)

        self.chatWindow=Entry(master,bd=1,foreground='black',bg='white',width=50,font=('arial',20))
        self.chatWindow.place(x=25,y=470,width=450)

        self.messageWindow= Text(master,bd=1,foreground='black',bg='white',width=50, height=10,font=('arial',20))
        self.messageWindow.place(x=25,y=100,width=450,height=350)

        self.send=Button(text="Send",command=self.send,bg='white',fg='black')
        self.send.place(x=150,y=550,height=40,width=70)

        self.clear=Button(text="Clear",command=self.clean,bg='red',fg='black')
        self.clear.place(x=300,y=550,height=40,width=70)

    def clean(self):
        self.chatWindow.delete(END)
        self.messageWindow.delete("1.0",END)
    
    def send(self):
        x=self.chatWindow.get()
        y=get_response(x)
        self.messageWindow.insert(END,y+"\n")





if __name__=='__main__':
    master=Tk()
    obj=gui(master)
    master.mainloop()