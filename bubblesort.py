import time
def bubble_sort(data,drawData,timetick):
    for i in range(len(data)):
        temp=0
        for j in range(len(data)-i-1):
            if data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]
                drawData(data,["OliveDrab1" if x==j or x==j+1 else "red2" for x in range(len(data))])# green for the current bars
                time.sleep(timetick)
    drawData(data,["OliveDrab1" for x in range(len(data))])          

