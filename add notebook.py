from tkinter import *
from datetime import datetime



tk=Tk()
tk.title("notebook")
tk.geometry("600x700")
tk.resizable(width=False,height=False)

def notebook_plus():
        global k    
        k=[]
        user_note=e_note.get()
        s=user_note + ":" + str(datetime.now().time())+'\n'
        (text.insert(END, s))
        k.append(s)
        print(k)
global k       
def del_text():

    text.delete("1.0", END)


def notebook_minds():
    global k
    if k:
        last_note = text.get("end-2l linestart", "end-1c")
        text.delete("end-2l linestart", "end-1c")
        k.pop()

    
    








note=Label(tk, text="note",width=10,bg="green")
note.place(x=50, y=100)
e_note=Entry(tk,width=50)
e_note.place(x=200,y=100)

b_note=Button(tk, text="+",command=notebook_plus)
b_note.place(x=150, y=200)

b_note=Button(tk, text="-",command=notebook_minds)
b_note.place(x=300, y=200)
book=Label(tk, text="notebook", width=20)
book.place(x=350,y=280)
text=Text(tk,width=30,height=30)
text.place(x=300,y=300)

b_clear=Button(tk, text="Clear", command=del_text)
b_clear.place(x=400, y=200)
tk.mainloop()