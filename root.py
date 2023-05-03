from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import bilibilirequests

root = Tk()
root.title("bilibilispider")
root.geometry("1920x780")


Style().configure("Treeview",rowheight=100)  # 格式化扩充row高度

#str(i+1)+' '+str(bilibilirequests.allvideo[i]['title'])+' '+str(bilibilirequests.allvideo[i]['title'])+' '+str(bilibilirequests.allvideo[i]['bvid'])+' '+str(bilibilirequests.allvideo[i]['length'])+' '+str(bilibilirequests.allvideo[i]['play'])+' '+str(bilibilirequests.allvideo[i]['comment'])

tree = Treeview(root,columns=("num","title","bvid","length","play","comment"))

tree.heading("#0",text="封面")
tree.heading("num",text="序号")
tree.heading("title",text="标题")              
tree.heading("bvid",text="BV号")
tree.heading("length",text="时长")
tree.heading("play",text="播放量")
tree.heading("comment",text="评论数")

   # 格式化栏标题
tree.column("#0",width=200,anchor="center") 
tree.column("num",width=4,anchor="center")              
tree.column("title",width=180,anchor="center") 
tree.column("bvid",width=15,anchor="center") 
tree.column("length",width=8,anchor="center") 
tree.column("play",width=15,anchor="center") 
tree.column("comment",width=15,anchor="center") 



img=Image.open("E:/Spider/img/2.jpg")
image = ImageTk.PhotoImage(img.resize((int(img.width/10),int(img.height/10))))

for i in range(0,bilibilirequests.response_1.json()['data']['list']['tlist']['4']['count']):
    tree.insert("",index=END,text="",image=image,values=[bilibilirequests.allvideo[i]['num'],bilibilirequests.allvideo[i]['title'],bilibilirequests.allvideo[i]['bvid'],bilibilirequests.allvideo[i]['length'],bilibilirequests.allvideo[i]['play'],bilibilirequests.allvideo[i]['comment']])


tree.pack(fill=BOTH,expand=True)

root.mainloop()