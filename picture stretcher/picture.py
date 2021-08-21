import tkinter as tk
import easygui
from tkinter import filedialog
from tkinter import *
from PIL import *
def upload():
    path=filedialog.askopenfilename(initialdir='C:/',title='选择图片')
    #C:/image/
    easygui.msgbox(path)
    img=Image.open(path)
    new=img.resize((int(xentry.get()),int(yentry.get())))
    new.save(fileentry.get()+nameentry.get()+'.'+imgentry.get(),imgentry.get())
    image=ImageTk.PhotoImage(file='img/new.'+imgentry.get())
window=tk.Tk()
window.geometry('500x300')
window.resizable(False,False)
xtext=tk.Label(text='请输入拉伸后的宽度（单位:像素）')
xtext.place(x=0,y=0)
xentry=tk.Entry()
xentry.place(x=0,y=25)
ytext=tk.Label(text='请输入拉伸后的高度（单位:像素）')
ytext.place(x=0,y=50)
yentry=tk.Entry()
yentry.place(x=0,y=75)
filetext=tk.Label(text='请输入图片保存路径')
filetext.place(x=0,y=100)
fileentry=tk.Entry()
fileentry.place(x=0,y=125)
nametext=tk.Label(text='请输入图片保存名称')
nametext.place(x=0,y=150)
nameentry=tk.Entry()
nameentry.place(x=0,y=175)
imgtext=tk.Label(text='请输入图片格式')
imgtext.place(x=0,y=200)
imgentry=tk.Entry()
imgentry.place(x=0,y=225)
ULB=tk.Button(window,text='选择要拉伸的照片',command=upload)
ULB.place(x=0,y=250)
window.mainloop()