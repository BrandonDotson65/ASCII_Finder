from tkinter import *

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.title("ASCII Converter")
mainWindow.iconbitmap('../pythonProjects/ASCII_Finder/ascii.ico')

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
canvas1.create_window(200, 90, window=entryLabel)

def getASCII():

    varTemp.set(entryLabel.get())
    temp = StringVar()

    if bool(varTemp.get()):
        temp.set(ord(varTemp.get()[0]))
        varTemp.set("The ASCII value of "+ varTemp.get()[0] + " is:")
        label3 = Label(mainWindow, textvariable=varTemp, font=('helvetica', 11))
        canvas1.create_window(200, 120, window=label3)
        label4 = Label(mainWindow, textvariable=temp, font=('helvetica', 11))
        canvas1.create_window(200, 140, window=label4)

    else:
        varTemp.set("Please enter a value")
        label3 = Label(mainWindow, textvariable=varTemp, font=('helvetica', 11))
        canvas1.create_window(200, 120, window=label3)
        temp.set("   ") # clear text for label 4
        label4 = Label(mainWindow, textvariable=temp, font=('helvetica', 11))
        canvas1.create_window(200, 140, window=label4)

b1 = Button(text="Get ASCII Value", font=('helvetica', 11, 'bold'), command=getASCII, bg='brown', fg='white')
canvas1.create_window(200, 180, window=b1)

mainWindow.mainloop()
