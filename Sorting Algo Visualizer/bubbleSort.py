import time

def bubbleSort(data, draw, speed):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

                draw(data, ['#4bdb95' if x == j or x == j+1 else '#4f87db' for x in range(len(data))])
                time.sleep(speed)
    draw(data, ['#4bdb95' for x in range(len(data))])