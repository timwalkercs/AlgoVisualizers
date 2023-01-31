import time

def partition(data, head, tail, draw, speed):
    border = head
    pivot = data[tail]
    draw(data, getColors(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, getColors(len(data), head, tail, border, j, True))
            time.sleep(speed)
            data[border], data[j] = data[j], data[border]
            border += 1

        draw(data, getColors(len(data), head, tail, border, j))
        time.sleep(speed)
    
    #swapping pivot and border
    draw(data, getColors(len(data), head, tail, border, tail, True))
    time.sleep(speed)
    data[border], data[tail] = data[tail], data[border]
    return border

def quickSort(data, head, tail, draw, speed):
    if head<tail:
        partitionIndex = partition(data, head, tail, draw, speed)

        #Left recursive call
        quickSort(data, head, partitionIndex-1, draw, speed)

        #Right recursive call
        quickSort(data, partitionIndex+1, tail, draw, speed)
    else:
        return

def getColors(size, head, tail, border, crnt, swapping=False):
    colorArr = []
    for i in range(size):
        if i>= head and i<=tail:
            colorArr.append('gray')
        else:
            colorArr.append('white')
        
        if i==tail:
            #blue
            colorArr[i] = '#4f87db'
        elif i==border:
            #red
            colorArr[i] = '#eb4959'
        elif i==crnt:
            #purple
            colorArr[i] = '#d16cf0'

        if swapping:
            if i==border or i==crnt:
                colorArr[i] = '#82e856'
    return colorArr
