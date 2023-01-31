import imp
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from quickSort import quickSort
from mergeSort import mergeSort


#Initial UI setup
root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
root.config(bg='#f5f5f5')

#Setup frame for the top portion of the window
frame = Frame(root, width=600, height=200, bg='#dedede')
frame.grid(row=0, column=0, padx=10, pady=5)

#Canvas area for displaying the data
canvas = Canvas(root, width=600, height=380, bg='white') #height = 600-200-(5*4)
canvas.grid(row=1, column=0, padx=10, pady=5)


#Variables
algoChoice = StringVar()
data = []

def draw(data, colorArray):
    Clear()
    canvas_height = 380
    canvas_width = 600
    gap = 10 #space between bars
    offset = 30 #avoid starting at the borders
    xWidth = ((canvas_width-offset)/(len(data)+1)) #width of bars will scale to fit the bounds
    normalizeData = [i/max(data) for i in data] #divide each index by maxVal to scale bar height
    for i, height in enumerate(normalizeData):
        #calculate top left coordinates of each rectangle
        x0 = i*xWidth + offset + gap
        y0 = canvas_height - height * 340 #makes it so the max of the data will be 340px and all other values scale upon that
        #bottom right
        x1 = (i+1)*xWidth + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

def Generate():
    global data

    canvas.delete('all')
    min = int(minVal.get())
    max = int(maxVal.get())
    size = int(sizeEntry.get())

    data = []
    for i in range(size):
        data.append(random.randrange(min,max+1))

    draw(data, ['#4f87db' for x in range(len(data))])

def Clear():
    canvas.delete('all')

def Start():
    global data
    if not data: return
    selection = algoChoice.get()
    tick = runSpeed.get()
    print('Selected Sorting Method: ' + selection)

    if selection == 'Merge Sort':
        mergeSort(data, draw, tick)
        draw(data, ['#4bdb95' for x in range(len(data))])
    elif selection == 'Quicksort':
        quickSort(data, 0, len(data)-1, draw, tick)
        draw(data, ['#4bdb95' for x in range(len(data))])
    elif selection == 'Bubble Sort':
        bubbleSort(data, draw, tick)
        draw(data, ['#4bdb95' for x in range(len(data))])
        


#--------Interface Area - variable seelection portion of window----------

#--------Row[0] - Sorting choice and Generate button-------------

#Selection box for algo choice
algoMenu = ttk.Combobox(frame, state="readonly", textvariable=algoChoice, values=['Merge Sort', 'Quicksort', 'Bubble Sort'])
algoMenu.grid(row=0, column=0, padx=5, pady=5, sticky=W)
algoMenu.current(0)

runSpeed = Scale(frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Select Speed [s]")
runSpeed.grid(row=0, column=1, padx=5, pady=5)

#GENERATE BUTTON
Button(frame, text='Generate', command=Generate, bg='#ff7070').grid(row=0, column=2, padx=5, pady=5)

#START BUTTON
Button(frame, text='Start Algorithm', command=Start, bg='#ff7070').grid(row=0, column=3, padx=5, pady=5)

#-------------Row[1] - Size, Min, Max entry--------------
sizeEntry = Scale(frame, from_=5.0, to=25.0, length=200, digits=2, resolution=1, orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)

minVal = Scale(frame, from_=1.0, to=10, length=200, digits=2, resolution=1, orient=HORIZONTAL, label="Min. Value")
minVal.grid(row=1, column=1, padx=5, pady=5, sticky=W)

maxVal = Scale(frame, from_=15.0, to=100.0, length=200, digits=3, resolution=1, orient=HORIZONTAL, label="Max. Value")
maxVal.grid(row=1, column=2, padx=5, pady=5, sticky=W)

#CLEAR BUTTON
Button(frame, text='Clear', command=Clear, bg='#ffe9a1').grid(row=1, column=3, padx=5, pady=5)









root.mainloop()