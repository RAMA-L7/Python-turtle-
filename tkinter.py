from tkinter import*

root=Tk()
e=(root)
def myClick():
        hello= "Hello" + e.get()
        myLabel=Label (root, text=hello)
        myLabel.pack()
        
        
        
myButton=Button(root,text="enter your name",command=myClick)
myButton.pack()
root.mainloop()
import autotyping