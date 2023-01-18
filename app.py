import tkinter as tk
import os
import pyttsx3

root = tk.Tk()
records=["are you crazy?","what are you thinking?","I'm sure","are you sure?","I'm OK","my throat hurts, and i don't want to talk","I'm tired",'OK','nope','yes']
dis=[]
root.title('speak!')
nowvoice=2

def renewRecord():
    for i in dis:
        i.destroy()
    y=350
    for i in range(len(records)):
        label = tk.Label(root,text=str(i+1)+'. '+records[i],bg="black",fg='white')
        dis.append(label)
        canvas.create_window(200, y, window=label)
        y+=20

def readtxt(txt):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[nowvoice].id)
    engine.setProperty('rate', 120)
    if(e2.get()!=''):
        engine.setProperty('rate', int(e2.get()))
    engine.say(txt)
    engine.runAndWait()

def readprev():
    num=e3.get()
    if(num==''):
        num="1"
    index=int(num)
    txt=records[index-1]
    readtxt(txt)

def read():
    txt = e.get()
    if txt not in records:
        records.append(txt)
        if(len(records)==11):
            records.pop(0)
    readtxt(txt)
    renewRecord()
    

def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False


    

canvas = tk.Canvas(root,height=600,width=600,bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="black")
frame.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)

# normal input
lb=tk.Label(root, text="input a senetence",bg="black",fg='white')
lb.config(font=('helvetica', 17))
canvas.create_window(303,80,window=lb)

e = tk.Entry(root,width=30,font=('微軟正黑體',16))
canvas.create_window(303, 130, window=e)

btn1 = tk.Button(root, text='read', command=read)   
btn1['font']=('times new roman',15)
canvas.create_window(303,290,window=btn1)

# set speed
lb2=tk.Label(root, text="speed",bg="black",fg='white')
lb2.config(font=('helvetica', 17))
canvas.create_window(153,180,window=lb2)

vcmd = (root.register(validate), '%P')
e2 = tk.Entry(root,width=5,font=('微軟正黑體',16),validate='key', validatecommand=vcmd)
canvas.create_window(153, 230, window=e2)

# set voice
lb10=tk.Label(root, text="now voice : "+str(nowvoice),bg="black",fg='white')
lb10.config(font=('helvetica', 17))
canvas.create_window(403,180,window=lb10)

def changevoice():
    tmp = e10.get()
    temp = int(tmp)
    if(temp>2 or temp<0):
        return
    global nowvoice 
    nowvoice = temp
    tmp = "now voice : "+tmp
    lb10=tk.Label(root, text=tmp,bg="black",fg='white')
    lb10.config(font=('helvetica', 17))
    canvas.create_window(403,180,window=lb10)

lb11=tk.Label(root, text="1:Female Eg-Ch\n2:Female Eg\n3:Male Eg",bg="black",fg='white')
lb11.config(font=('helvetica', 10))
canvas.create_window(353,230,window=lb11)

e10 = tk.Entry(root,width=2,font=('微軟正黑體',16),validate='key', validatecommand=vcmd)
canvas.create_window(423, 230, window=e10)

btn3 = tk.Button(root, text='set', command=changevoice)   
btn3['font']=('helvetica',12)
canvas.create_window(468,231,window=btn3)

# use record
lb3=tk.Label(root, text="use record",bg="black",fg='white')
lb3.config(font=('helvetica', 15))
canvas.create_window(403,380,window=lb3)

e3 = tk.Entry(root,width=2,font=('微軟正黑體',16),validate='key', validatecommand=vcmd)
canvas.create_window(403, 430, window=e3)

btn2 = tk.Button(root, text='read', command=readprev)   
btn2['font']=('times new roman',15)
canvas.create_window(403,490,window=btn2)

renewRecord()
root.mainloop()