import pprint
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk, ImageFile
import bilibilirequests as bi
from tkinter import PhotoImage
import tkinter.font as tkFont

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Page_1:
    def __init__(self, window):
        self.window = window
        self.window.title("bilibilispider")
        self.window.geometry("1920x960")
        #self.window.config(bg='#000000')

        self.background = Image.open('test/background.png')
        self.bg = ImageTk.PhotoImage(self.background.resize((1800,1200)))
        self.lable1=Label(self.window,image=self.bg)
        self.lable1.place(x=0,y=0, relwidth=1, relheight=1)
        
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)

        self.lable=Label(self.window,text="请输入uid",background='white',font=fontStyle)
        self.lable.pack(padx=10, pady=80)
        self.entry = Entry(self.window,width=40)
        self.entry.pack(padx=20, pady=20)
        self.button = Button(self.window, text="确定", command=self.change,width=15,compound="c")
        self.button.pack()

    def change(self):
        # pass
        [allvideo, count] = bi.getdata(int(self.entry.get()))
        # pprint.pprint(allvideo)
        bi.imgdownload(allvideo, count)
        self.lable.destroy()
        self.button.destroy()
        self.entry.destroy()
        self.lable1.destroy()
        Page_2(root, allvideo, count)


class Page_2:
    def __init__(self, window, allvideo, count):
        self.window = window
        self.window.title("bilibilispider")
        self.window.geometry("1920x960")
        #self.window.config(bg="#0F375A")
        self.fr1 = self.printdata(allvideo, count)
        self.fr2 = Frame(self.window)


        self.fr1.place(width=1400, height=750, relx=0.5, rely=0.5, anchor="c")
        self.fr2.place(width=1400, height=50, relx=0.5, rely=0.95, anchor="c")

        self.button = Button(self.fr2, text="返回", command=self.back)
        self.button.place(relx=0.5, rely=0.5, anchor="c")
        self.button.pack()

        

    def back(self):
        # pass
        self.fr2.destroy()
        self.fr1.destroy()
        Page_1(root)

    def printdata(self, allvideo, count):
        fr1 = Frame(self.window)
        # fr1.place(width=1400,height=800,relx=0.5,rely=0.5,anchor="c")
        Style().configure("Treeview", rowheight=120)
        tree = Treeview(fr1, columns=(
            "num", "title", "bvid", "length", "play", "comment"))

        tree.heading("#0", text="封面")
        tree.heading("num", text="序号")
        tree.heading("title", text="标题")
        tree.heading("bvid", text="BV号")
        tree.heading("length", text="时长")
        tree.heading("play", text="播放量")
        tree.heading("comment", text="评论数")

        tree.column("#0", width=70, anchor="center")
        tree.column("num", width=4, anchor="center")
        tree.column("title", width=250, anchor="center")
        tree.column("bvid", width=15, anchor="center")
        tree.column("length", width=8, anchor="center")
        tree.column("play", width=15, anchor="center")
        tree.column("comment", width=15, anchor="center")

        for i in range(0, count):
            img = Image.open("E:/Spider/img/"+str(i)+".jpg")
            image = ImageTk.PhotoImage(img.resize((171, 108)))
            globals()['image'+str(i)] = image
            tree.insert("", index=END, text="", image=globals()['image'+str(i)], values=[allvideo[i]['num'], allvideo[i]['title'], allvideo[i]['bvid'], allvideo[i]['length'], allvideo[i]['play'], allvideo[i]['comment']])
        tree.pack(fill=BOTH, expand=True)

        return fr1


root = Tk()
p1 = Page_1(root)
root.mainloop()
