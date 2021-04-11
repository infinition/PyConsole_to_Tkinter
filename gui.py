import tkinter as tk
from tkinter import *
import threading
import time

class Gui(threading.Thread):
    def __init__(self, program):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.root.geometry("550x500")
        self.root.title("Template")
        self.program = program
        self.initComponents()
        self.console_rows = 0
        self.max_console_rows = 20
        self.stop = False

    def run(self):
        self.root.mainloop()

    def output_console(self, new_text):
        self.consoleText.config(state=NORMAL)
        self.consoleText.insert(END, "\n" + new_text)
        self.consoleText.see(END)
        self.consoleText.config(state=DISABLED)

    def initComponents(self):
        root = self.root

        # Input Frame
        inputFrame = Frame(root, width="200")
        inputFrame.pack(pady=15, padx=15)

        # Init Components
        field1Label = Label(inputFrame, text="Field 1:")
        field2Label = Label(inputFrame, text="Field 2:")
        self.Field1Entry = Entry(inputFrame)
        self.Field1Entry.insert(0, "Field 1")
        self.Field2Entry = Entry(inputFrame)
        self.Field2Entry.insert(0, "Field 2")
        field3Label = Label(inputFrame, text="Field 3:")
        self.Field3Entry = Entry(inputFrame)
        self.Field3Entry.insert(0, "Field 3")
        hostButton = Button(inputFrame, text="Program 1", command=self.program1)
        stopButton = Button(inputFrame, text="Stop", command=self.stopProgram)
        scanButton = Button(inputFrame, text="Program 2", command=self.program2)

        # Set Component Grid Positions
        field1Label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        field2Label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.Field1Entry.grid(row=0, column=1, padx=5, pady=5)
        self.Field2Entry.grid(row=0, column=3, padx=5, pady=5)
        field3Label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.Field3Entry.grid(row=1, column=3, padx=5, pady=5)
        hostButton.grid(row=1, column=1, padx=5, pady=5)
        scanButton.grid(row=0, column=4, padx=10, pady=5)
        stopButton.grid(row=1, column=4, padx=10, pady=5)

        # Console Frame
        self.consoleFrame = Frame(root)
        self.consoleFrame.pack(expand=1, pady=15, padx=15, fill= BOTH)
        self.consoleText = Text(self.consoleFrame, fg="green", bg="black",state=DISABLED)
        self.consoleText.pack(expand=1, fill= BOTH)

    def program2(self):
        self.stop = False
        field1 = self.Field1Entry.get()
        field2 = self.Field2Entry.get()
        field3 = self.Field3Entry.get()
        self.ip_scan_index = 0
        self.output_console("\n Test ¨Program : " + field1+ " - " + field2+" - " + field2)

    def program1(self):
        try:
            self.output_console("\nTest2" )
        except:
            self.output_console("\nTest2" )
    
    def stopProgram(self):
        self.stop = True

# recursive function with call to root.after() to keep gui from freezing
# self.root.after(1400, program)
