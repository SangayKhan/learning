from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
	hello = "Hello " + e.get()
	#Creating a label widget
	myLabel = Label(root, text=hello)#.grid(row=0, column=0)
	myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.pack()

#Shoving it onto the screan
#myLabel1.pack()
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=1)

root.mainloop()