from tkinter import*
from tkinter import messagebox
def binary():
    result.delete(0,'end')
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    num1=bin(fn1)
    num2=bin(fn2)
    sum = bin(int(num1,2) * int(num2,2))
    result.insert(0, sum)
def octal():
    result1.delete(0,'end')
    fn1=(Fno.get())
    fn2=(Sno.get())
    num1=(fn1)
    num2=(fn2)
    mul=oct((num1,2)*(num2, 2))
    result1.insert(0,mul)
def decimal():
    result2.delete(0,'end')
    fn1=int(Fno.get())
    fn2=int(Sno.get())
    s=fn1*fn2
    result2.insert(0,s)    

    


###################
root=Tk()
root.title("BINARY MUltiplication")
root.geometry("600x600")
Fno=StringVar()
Sno=StringVar()
#######################
binary = Button(root, text="binary",command=binary,width=15)
octal = Button(root, text="octal",command=octal,width=15)
decimal = Button(root, text="decimal",command=decimal,width=15)
cancel = Button(root,text="cancel",command=root.destroy,width=15)
#######################
Lb11 = Label(root,text="calculation")
fst_no = Label(root,text="enter a Number")
snd_no=Label(root, text="enter the Number").grid(column=1, row=3)
result=Label(root, text="binary")
result1=Label(root, text="octal")
result2=Label(root, text="decimal")
n1 = Entry(root,width=25,textvariable=Fno)
n2 = Entry(root, width=25, textvariable=Sno).grid(row=3, column=2)
result= Entry(root, width=25)
result1= Entry(root, width=25)
result2= Entry(root, width=25)

###########################
Lb11.grid(column=1,row=1,columnspan=2)
fst_no.grid(column=1,row=2)
n1.grid(column=2,row=2)
binary.grid(column=1,row=6)
octal.grid(column=1,row=7)
decimal.grid(column=1,row=8)
cancel.grid(column=2,row=9)
result.grid(column=2, row=6)
result1.grid(column=2, row=7)
result2.grid(column=2, row=8)

root.mainloop()
