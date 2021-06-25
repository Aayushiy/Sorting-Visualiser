import time
def partition(data,head,tail,drawData,timetick):
    border = head
    pivot = data[tail]

    drawData(data,getColorArray(len(data),head,tail,border,border))
    time.sleep(timetick)
    for i in range(head,tail):
        if data[i]<pivot:
            drawData(data,getColorArray(len(data),head,tail,border,i,isSwaping=True))
            time.sleep(timetick)
            
            data[border],data[i]=data[i],data[border]
            border+=1
        drawData(data,getColorArray(len(data),head,tail,border,i))
        time.sleep(timetick)

    # swap border with pivot i.e creating partition
    drawData(data,getColorArray(len(data),head,tail,border,tail,isSwaping=True))
    time.sleep(timetick)
    data[border],data[tail]=data[tail],data[border]
    
    return border
            
                    
    
    




def quicksort(data,head,tail,drawData,timetick):
    
    if head < tail:
        partition_idx=partition(data,head,tail,drawData,timetick)
        #left
        quicksort(data,head,partition_idx-1,drawData,timetick)

        #right
        quicksort(data,partition_idx+1,tail,drawData,timetick)
        

def getColorArray(dataLen,head,tail,border,currIdx,isSwaping=False):
    colorArray=[]
    for i in range(dataLen):
        # base color
        if i>=head and i<=tail:
            colorArray.append("grey")
        else:
            colorArray.append("yellow")

        # color 

        if i ==tail:
            colorArray[i]="blue"
        elif i == border:
            colorArray[i]="red2"
        elif i==currIdx:
            colorArray[i]="brown"

        if isSwaping:
            if i == border or i==currIdx:
                colorArray[i]="OliveDrab1"


    return colorArray
