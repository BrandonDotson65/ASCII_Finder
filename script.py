from tkinter import *

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.title("ASCII Converter")
mainWindow.iconbitmap('../pythonProjects/ASCII_Finder/ascii.ico')

#rid placeholder text variable
numVar = 0

canvas1 = Canvas(mainWindow, width=400, height=200, relief='raised')
canvas1.pack()

label1=Label(mainWindow, text="Calculate the ASCII value")
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 30, window=label1)

label2=Label(mainWindow, text="Enter character to be converted:")
label2.config(font=('helvetica', 11))
canvas1.create_window(200, 60, window=label2)

varTemp = StringVar()
entryLabel= Entry(mainWindow)
entryLabel.insert(0, 'Enter Character')
canvas1.create_window(200, 90, window=entryLabel)

def getASCII():

    varTemp.set(entryLabel.get())
    temp = StringVar()

    if bool(varTemp.get()):
        temp.set(ord(varTemp.get()[0]))
        varTemp.set("The ASCII value of "+ varTemp.get()[0] + " is:")
        label3 = Label(mainWindow, textvariable=varTemp, font=('helvetica', 11))
        canvas1.create_window(200, 120, window=label3)
        #label for answer
        label4 = Label(mainWindow, textvariable=temp, font=('helvetica', 11, 'bold'))
        canvas1.create_window(200, 140, window=label4)

    else:
        varTemp.set("Please enter a value")
        label3 = Label(mainWindow, textvariable=varTemp, font=('helvetica', 11))
        canvas1.create_window(200, 120, window=label3)
        temp.set("    ") # clear text for label 4
        label4 = Label(mainWindow, textvariable=temp, font=('helvetica', 11))
        canvas1.create_window(200, 140, window=label4)

def openInfoWindow():
    newWindow = Toplevel(mainWindow)
    newWindow.title("Info")
    newWindow.iconbitmap('../pythonProjects/ASCII_Finder/ascii.ico')
    newWindow.geometry("200x150")
    newWindow.resizable(0,0)
    Label(newWindow, text="Written in Python 3.9\nutilizing Tkinter by \nBrandon Dotson", font=('helvetica', 11, 'bold')).pack()
    Label(newWindow, text="\nThe program will find the\nASCII value (in decimal) of\nonly the first character\nin the string entered", font=('helvetica', 11)).pack()

def showAnswerOnEnter(event=None): #handler
    getASCII()

def onClick(*args):
    global numVar
    #check if placeholder text
    if (numVar == 0):
        entryLabel.delete(0, 'end')
        numVar += 1

entryLabel.bind('<Return>', showAnswerOnEnter) #pressing enter finds value
entryLabel.bind("<Button-1>", onClick) #gets rid of placeholder text

b1 = Button(text="Get ASCII Value", font=('helvetica', 11, 'bold'), command=getASCII, bg='brown', fg='white')
canvas1.create_window(200, 180, window=b1)

b2 = Button(text="Info", command=openInfoWindow, font=('helvetica', 11, 'bold'))
canvas1.create_window(350, 180, window=b2)

mainWindow.mainloop()
