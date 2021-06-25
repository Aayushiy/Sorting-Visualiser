import time
def insertion(data,drawData,timetick):

    for i in range(1,len(data)):
        key = data[i]
        j = i-1
        
        while key < data[j] and j>=0:
            data[j+1]=data[j]
            drawData(data,["black" if x==i  else "red2" for x in range(len(data))])
            j= j-1
            time.sleep(timetick)
        data[j+1]= key

 
    drawData(data,["OliveDrab1" for x in range(len(data))]) 


            
    
