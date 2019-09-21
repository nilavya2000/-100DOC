from tkinter import*
from tkinter import messagebox
def binary():
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    num1=bin(fn1)
    num2=bin(fn2)
    sum = bin(int(num1,2) + int(num2,2))
    result.insert(0, sum)


###################
root=Tk()
root.title("MINI CONVERTER")
root.geometry("600x600")
Fno=StringVar()
Sno=StringVar()
#######################
binary = Button(root, text="sum",command=binary,width=15)

cancel = Button(root,text="cancel",command=root.destroy,width=15)
#######################
Lb11 = Label(root,text="calculation")
fst_no = Label(root,text="enter a Number")
snd_no=Label(root, text="enter the Number").grid(column=1, row=3)
result=Label(root, text="result")
n1 = Entry(root,width=25,textvariable=Fno)
n2 = Entry(root, width=25, textvariable=Sno).grid(row=3, column=2)
result= Entry(root, width=25)
###########################
Lb11.grid(column=1,row=1,columnspan=2)
fst_no.grid(column=1,row=2)
n1.grid(column=2,row=2)
binary.grid(column=1,row=6)

cancel.grid(column=2,row=7)
result.grid(column=2, row=6)
root.mainloop()
