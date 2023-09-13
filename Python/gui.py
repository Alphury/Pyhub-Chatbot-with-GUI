from tkinter import *
from tkinter import ttk
from main2 import *

#Creating the GUI
class gui:
    def __init__(self,master):
        self.master = master
        self.master.title("ChatBot")
        self.master.geometry("500x600")
        self.master.configure(bg='purple')

        mframe=Frame(self.master,bd=4,bg='purple',width=600)
        mframe.pack()

        maintitle=Label(mframe,bd=3,relief=RAISED,fg='white',bg='black',text="ChatBot",font=('algerian',30))
        maintitle.pack(side=TOP)

        self.l1=Label(text="BOT:",bg='purple',fg='white',font=('berlin sans fb',15))
        self.l1.place(x=25,y=70)

        self.chatWindow=Entry(master,bd=1,foreground='black',bg='white',width=50,font=('arial',20))
        self.chatWindow.place(x=25,y=500,width=450)

        self.l1=Label(text="You:",bg='purple',fg='white',font=('berlin sans fb',15))
        self.l1.place(x=25,y=470)

        self.messageWindow= Text(master,bd=1,foreground='black',bg='white',width=50, height=10,font=('berlin sans fb',20))
        self.messageWindow.place(x=25,y=100,width=450,height=350)

        self.send=Button(text="Send",command=self.send,bg='white',fg='black')
        self.send.place(x=300,y=550,height=40,width=70)

        self.clear=Button(text="Clear",command=self.clean,bg='red',fg='black')
        self.clear.place(x=150,y=550,height=40,width=70)

#Creating the clear button function.
    def clean(self):
        self.chatWindow.delete(END)
        self.messageWindow.delete("1.0",END)

#Creating the send fuction for talking to the Bot.    
    def send(self):
        x=self.chatWindow.get()
        y=get_response(x)
        self.messageWindow.insert(END,"Samah: "+y+"\n")

#fuction to run the mainloop
if __name__=='__main__':
    master=Tk()
    obj=gui(master)
    master.mainloop()