from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksortforpro import quicksort
from insertionsort import insertion


root = Tk()
root.title("sorting")
root.maxsize(900,600)
root.config(bg ="DodgerBlue3")

# Variables
selected_alg = StringVar()
data=[]


def drawData(data,colorArray):
    canvas.delete("all")
    c_height=380
    c_width=600
    x_width = c_width/(len(data)+1)
    offset = 30
    spacing = 10
    normaliseData = [i/max(data) for i in data]
    for i ,height in enumerate(normaliseData):
        # top left
        x0 = i*x_width + offset+ spacing
        y0 = c_height - height*340

        # bottom right
        x1 = (i+1)*x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0,y0,x1,y1, fill =colorArray[i])
        canvas.create_text(x0+2,y0, anchor =SW , text = str(data[i]))
    root.update_idletasks()



def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    

    data=[]
    for _ in range(size):
        data.append(random.randrange(minVal,maxVal+1))

    drawData(data, ["red2" for x in range(len(data))]) # red

    
    print("algorithm selected:"+selected_alg.get())



def StartAlgo():
    global data
    if not data: return

    if(algMenu.get()=="Quicksort"):
        quicksort(data,0,len(data)-1,drawData,speedScale.get())
        drawData(data,["OliveDrab1"for x in range(len(data))])
    elif(algMenu.get()=="Bubble Sort"):
        bubble_sort(data,drawData,speedScale.get())
    elif(algMenu.get()=="Insertion Sort"):
        insertion(data,drawData,speedScale.get())
        
    
    print ("algo")

    
# frame /base layout
UI_frame = Frame(root,width=600, height = 200, bg="black")
UI_frame.grid(row=0,column=0,padx = 10, pady =5)

canvas = Canvas(root,width=600,height=380,bg="white")
canvas.grid(row=1, column =0, padx=10,pady =5)
# UI
#Row[0]
Label(UI_frame,text="Algorithm:",bg="yellow").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable= selected_alg, values=["Bubble Sort","Quicksort","Insertion Sort"])
algMenu.grid(row =0,column =1,padx=5,pady=5)
algMenu.current(0)


#Speed Scale

speedScale = Scale(UI_frame,from_= 0.2 ,to =2.0,length=200,digits=2,resolution=0.2,orient = HORIZONTAL, label="Speed [s]" )
speedScale.grid(row =0, column=2,padx=5,pady=5)

Button(UI_frame, text ="Start", command =StartAlgo,bg= "red").grid(row = 0, column=3, padx=5, pady=5)

#Row[1]

Label(UI_frame,text="Size",bg="grey").grid(row=1,column=0,padx=5,pady=5,sticky=W)
sizeEntry =  Scale(UI_frame,from_= 3 ,to =25,length=200,resolution=1,orient = HORIZONTAL, label="Size [s]" )
sizeEntry.grid(row=1,column=0,padx=5,pady=5)



Label(UI_frame,text="Min_Val",bg="grey").grid(row=1,column=2,padx=5,pady=5,sticky=W)
minEntry =  Scale(UI_frame,from_= 0 ,to =10,length=200,resolution=1,orient = HORIZONTAL, label="Min_Val" )
minEntry.grid(row=1,column=1,padx=5,pady=5)


Label(UI_frame,text="Max_Val",bg="grey").grid(row=1,column=3,padx=5,pady=5,sticky=W)
maxEntry =  Scale(UI_frame,from_= 10 ,to=100,length=200,resolution=0.2,orient = HORIZONTAL, label="Max_Val" )
maxEntry.grid(row=1,column=2,padx=5,pady=5)


Button(UI_frame, text ="Generate", command =Generate,bg= "blue").grid(row = 1, column=4, padx=5, pady=5)



root.mainloop()
