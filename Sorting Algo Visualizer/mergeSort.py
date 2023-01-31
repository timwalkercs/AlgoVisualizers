import time

def mergeSort(data, draw, speed):
    mergeSortAlgo(data, 0, len(data)-1, draw, speed)


def mergeSortAlgo(data, left, right, draw, speed):
    if left < right:
        middle = (left+right) // 2
        mergeSortAlgo(data, left, middle, draw, speed)
        mergeSortAlgo(data, middle+1, right, draw, speed)
        merge(data, left, middle, right, draw, speed)


def merge(data, left, middle, right, draw, speed):
    draw(data, getColorArray(len(data), left, middle, right))
    time.sleep(speed)
    lPartition = data[left:middle+1]
    rPartition = data[middle+1:right+1]

    lIndex = rIndex = 0

    for i in range (left, right+1):
        if lIndex < len(lPartition) and rIndex < len(rPartition):
            if lPartition[lIndex] <= rPartition[rIndex]:
                data[i] = lPartition[lIndex]
                lIndex += 1
            else:
                data[i] = rPartition[rIndex]
                rIndex += 1
        
        elif lIndex < len(lPartition):
            data[i] = lPartition[lIndex]
            lIndex += 1

        else:
            data[i] = rPartition[rIndex]
            rIndex += 1
    
    draw(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(speed)

def getColorArray(size, left, middle, right):
    colorArray = []

    for i in range(size):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")

    return colorArray