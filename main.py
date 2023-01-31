import imp
from tkinter import *
from tkinter import font
import subprocess


#Initial UI setup
root = Tk()
root.resizable(width=False, height=False)
root.title('Main Menu')
root.maxsize(500, 600)
root.minsize(500, 600)
root.config(bg='#f5f5f5')
root.columnconfigure(0, weight=1)



#Setup frame for the top portion of the window
frame = Frame(root, width=480, height=590, bg='white')
frame.grid(row=0, column=0, padx=10, pady=5)



def Pathfinder():
    print("Launching Pathfinder!")
    root.withdraw()
    subprocess.call(["python", "pathfinder.py"], cwd="Pathfinding Visualizer")
    print("Closing Pathfinder!")
    root.deiconify()

def Sorter():
    print("Launching Sorter!")
    root.withdraw()
    subprocess.call(["python", "sorter.py"], cwd="Sorting Algo Visualizer")
    print("Closing Sorter!")
    root.deiconify()

l = Label(frame, text='Welcome to the\nAlgorithm Visualizer!', bg='white', font=("Arial", 25)).grid(row=0, column=0, padx=100, pady=100, sticky="N")
#Button to generate data given parameters
b1 = Button(frame, text='Patfinding Visualizer', command=Pathfinder, bg='#ff7070', height=3).grid(row=1, column=0, padx=5, pady=25)
b2 = Button(frame, text='Sorting Algorithms', command=Sorter, bg='#ffe9a1', height=3).grid(row=2, column=0, padx=5, pady=70)



root.mainloop()