from tkinter import *
from tkinter import ttk
from random import sample
import random
from collections import Counter
firstRun = 0
previous = 0
master = Tk()
master.title("Random Digits")
master.configure(background="#544c4c")
master.wm_iconbitmap("favicon.ico")
addPhoto=PhotoImage(file="icon.png")
ngPhoto=PhotoImage(file="genbtn.gif")
topFrame = Frame(master)
topFrame.configure(background="#5195c6")
topFrame.pack(side="top",fill="x")
titleLabel = Label(topFrame,height=100,width=650,image=addPhoto, compound="left",bg="#5195c6",relief=FLAT,text=" Random Numbers Generator & Selector Tool",fg="#ffffff",font=("Helvetica",16))
titleLabel.pack(side="left",padx=3,pady=4)
genBtn = Button(topFrame,height=60,width=100,image=ngPhoto, bg="#5195c6",relief=FLAT,fg="#ffffff")
genBtn.pack(side="right",padx=6)
optionsFrame = Frame(master)
optionsFrame.configure(background="#fdc242")
optionsFrame.pack(side="top",fill="x")
glLabel = Label(optionsFrame,bg="#fdc242",relief=FLAT,text="Number of Games: ",fg="#000000",font=("Helvetica",12))
glLabel.pack(side="left",padx=3,pady=5)
ng = ('10','20','30','40','50','60','70','80','90','100')
sr = ('1','2','3','4','5','6','7','8','9','10')
fr = ('20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100')
lp = ('none','atleast 3 times','atleast 4 times','atleast 5 times','atleast 6 times','atleast 7 times','atleast 8 times','atleast 9 times','atleast 10 times')
setnum = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
glist = ttk.Combobox(optionsFrame, values=ng, state='readonly')
glist.current(0)
glist.pack(side="left",pady=5, padx=3)
slLabel = Label(optionsFrame,bg="#fdc242",relief=FLAT,text="Start value: ",fg="#000000",font=("Helvetica",12))
slLabel.pack(side="left",padx=3,pady=5)
slist = ttk.Combobox(optionsFrame, values=sr, state='readonly')
slist.current(0)
slist.pack(side="left",pady=5, padx=3)
flLabel = Label(optionsFrame,bg="#fdc242",relief=FLAT,text="End value: ",fg="#000000",font=("Helvetica",12))
flLabel.pack(side="left",padx=3,pady=5)
flist = ttk.Combobox(optionsFrame, values=fr, state='readonly')
flist.current(0)
flist.pack(side="left",pady=5, padx=3)
lpLabel = Label(optionsFrame,bg="#fdc242",relief=FLAT,text="Least parameter: ",fg="#000000",font=("Helvetica",12))
lpLabel.pack(side="left",padx=3,pady=5)
lpList = ttk.Combobox(optionsFrame, values=lp, state='readonly')
lpList.current(0)
lpList.pack(side="left",pady=5, padx=3)
snLabel = Label(optionsFrame,bg="#fdc242",relief=FLAT,text="Total Numbers: ",fg="#000000",font=("Helvetica",12))
snLabel.pack(side="left",padx=3,pady=5)
snList = ttk.Combobox(optionsFrame, values=setnum, state='readonly')
snList.current(0)
snList.pack(side="left",pady=5, padx=3)
numHolder = []
finalLabel = Label(topFrame,bg="#5195c6",relief=FLAT,text=" Final Result: ",fg="#ffffff",font=("Helvetica",12))
finalLabel.pack(side="left",padx=3,pady=5)
ent1 = Text(topFrame,relief = "flat", height=3,width=46, borderwidth=0)
ent1.pack(side="left",padx=3,pady=4)
ent1.configure(state="disabled")
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(master, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(master, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")
frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

def leastcalc():
    leastPara = lpList.get()
    num = 0
    if leastPara == lp[0]:
        num = 0
    elif leastPara == lp[1]:
        num = 3
    elif leastPara == lp[2]:
        num = 4
    elif leastPara == lp[3]:
        num = 5
    elif leastPara == lp[4]:
        num = 6
    elif leastPara == lp[5]:
        num = 7
    elif leastPara == lp[6]:
        num = 8
    elif leastPara == lp[7]:
        num = 9
    elif leastPara == lp[8]:
        num = 10
    return num

def comparator(l1,counts,nums):
    p = counts
    original=[]
    for items,times in p.items():
        original.append(items)
        original = original[:nums+2]
    finals=[i for i in l1 if not i in original]
    return finals



def genNemesis():
    
    numHolder = []
    key = []
    num1 = leastcalc()
    ent1.configure(state="normal")
    ent1.delete(1.0,END)
    ent1.configure(state="disabled")
    numOfGames = int(glist.get())
    tot = int(snList.get())
    global previous
    for gn in range(numOfGames):
         numLabel=Label(frame, text="Game "+str(gn+1), width=8, borderwidth="1", 
                    relief="solid")
         numLabel.grid(row=gn, column=1,pady=4)
    if (previous != 0 and previous !=5):
        
        for kn in range(numOfGames):
            for k in range(previous+1):
                nameLabel=Label(frame, text="   ",bg="#ffffff")
                nameLabel.grid(row=kn, column= k+10,padx=14,pady=4)
                
    for gn in range(numOfGames):
         rnum = sample(range((int(slist.get())),(int(flist.get()))+1),tot)
         for i in range(tot):
            numHolder.append(rnum[i])
            nameLabel=Label(frame, text=rnum[i],bg="#ffffff")
            nameLabel.grid(row=gn, column=i+10,padx=14,pady=4)
    previous = i
    global firstRun   
    if gn<99:
     
        while(gn<99):
            numLabel=Label(frame, text="        ", width=8, 
                    relief="flat",bg="#ffffff")
            numLabel.grid(row=gn+1, column=1,pady=4)
            for i in range(firstRun):
                nameLabel=Label(frame, text="   ",bg="#ffffff")
                nameLabel.grid(row=gn+1, column=i+10,padx=14,pady=4)
            gn =gn+1
    
    firstRun = tot
            
    c = Counter(numHolder)
    k = c.most_common()
    for i in range(tot-1):
        ent1.configure(state="normal")
        ent1.insert(i+2.0, str(k[i][0])+', ')
        ent1.configure(state="disabled")
    for leastN,least in c.items():
        if least >= num1:
            key.append(leastN)
    if num1 == 0:
        fin = str(k[tot-1][0])
        ent1.configure(state="normal")
        ent1.insert(tot*2.0,random.choice(fin))
        ent1.configure(state="disabled")
        
    else:
        fin = comparator(key,c,tot)
        ent1.configure(state="normal")
        try:
            ent1.insert(tot*2.0,random.choice(fin)) #random.choice(key)
        except:
            ent1.insert(tot*2.0,"--")
        ent1.configure(state="disabled")
    
        
    
genBtn.configure(command=genNemesis)
master.mainloop()
