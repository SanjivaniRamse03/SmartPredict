from tkinter import *
from tkinter import Toplevel, filedialog
from tkinter import ttk
import pandas as pd
import os
import sys
import windows
import globals
import time
from NaiveBayes.naive_bayes import *
from regression.multiple_regression_model import *

    

def close(event):
    sys.exit()

def enter(event):
    globals.closeLabel.config(bg="#cc0a0a")
def leave(event):
    globals.closeLabel.config(bg="#47575e")

def enter1(event):
    globals.fileLabel.config(bg="#244e57")
def leave1(event):
    globals.fileLabel.config(bg="#1a373d")

def tn_enter(event):
    globals.trainButton.config(bg="#183b47")
    globals.trainButton.config(fg="#000000")
def tn_leave(event):
    globals.trainButton.config(bg="#122e33")
    globals.trainButton.config(fg="#ffffff")

def ts_enter(event):
    globals.testButton.config(bg="#183b47")
    globals.testButton.config(fg="#000000")
def ts_leave(event):
    globals.testButton.config(bg="#122e33")
    globals.testButton.config(fg="#ffffff")

def db_enter(event):
    globals.dataButton.config(bg="#1a4757")
    globals.dataButton.config(fg="#ffffff")
def db_leave(event):
    globals.dataButton.config(bg="#1c4352")
    globals.dataButton.config(fg="#000000")


def openfile(event):
    globals.choic_count = 0
    globals.count = 0
    globals.selected_list = []
    globals.selected_list_show = []
    
    if(globals.tree != None):
        globals.datawindow.attributes('-topmost',False)
    
    if(globals.input_label1 != None or globals.input_label != None):
        globals.modelwindow.attributes('-topmost',False)
        
    globals.filepath = filedialog.askopenfilename(initialdir='C:/Users/sanjivani ramse/Desktop/projects',filetypes=(("csv files","*.csv"),("all files","*.*")),title="open files very well")
    if(globals.filepath == ""):
        if(globals.tree != None):
            globals.datawindow.attributes('-topmost',True)
        if(globals.input_label1 != None or globals.input_label != None):
            globals.modelwindow.attributes('-topmost',True)
        return
    
    globals.datawindow = Toplevel(globals.window)
    globals.datawindow.config(background="#051d26")
    globals.datawindow.geometry("1534x730+0+83")
    globals.datawindow.overrideredirect(True)

    globals.trainButton = Label(globals.datawindow,text="Train",bg="#122e33",font=("Arial",13),padx=5,pady=8,width=30)
    globals.trainButton.place(x=-630,y=-650)    
    globals.trainButton.bind("<Button-1>",train)
    globals.trainButton.bind("<Enter>",tn_enter)
    globals.trainButton.bind("<Leave>",tn_leave)

    globals.testButton = Label(globals.datawindow,text="Test",bg="#122e33",font=("Arial",13),padx=5,pady=8,width=30)
    globals.testButton.place(x=-100,y=-100)
    globals.testButton.bind("<Button-1>",test)
    globals.testButton.bind("<Enter>",ts_enter)
    globals.testButton.bind("<Leave>",ts_leave)

    
    globals.inputtitleLabel = Label(globals.datawindow,fg="black",font=("Arial",10),bg="#051d26",foreground="#ffffff")
    globals.inputtitleLabel.place(x=-100,y=-100)

    globals.dataButton = Label(globals.datawindow,width=15,height=2,font=("Arial",11),borderwidth=1,relief='solid',bg="#1c4352",fg="#000000")
    globals.dataButton.place(x=-100,y=-100)
    globals.dataButton.bind("<Button-1>",originaldata)
    globals.dataButton.bind("<Enter>",db_enter)
    globals.dataButton.bind("<Leave>",db_leave)

    globals.taskLabel = Label(globals.datawindow,bg="#031e24",font=("Arial",13),padx=5,pady=8,width=120,height=3,fg="white",anchor="n")
    globals.taskLabel.place(x=-100,y=-100)

    globals.percent = StringVar()
    st = ttk.Style()
    st.theme_use("clam")
    st.configure("Horizontal.TProgressbar",troughcolor='white',background="green")
    globals.percentLabel = Label(globals.taskLabel,textvariable=globals.percent,bg="#031e24",fg="#ffffff",width=15,font=("Arial",11))
    globals.percentLabel.place(x=-300,y=-100)

    globals.bar = ttk.Progressbar(globals.taskLabel,orient=HORIZONTAL,length=995,style='green.Horizontal.TProgressbar')
    globals.bar.place(x=-100,y=-100)
      
    globals.trainButton.place(x=1200,y=650)

    globals.data = pd.read_csv(globals.filepath)
    windows.showData(globals.data.values,tuple(globals.data.columns.values))


def test(event):
    globals.trainButton.destroy()
    globals.testButton.destroy()
    globals.datawindow.geometry("764x730+0+82")
    globals.modelwindow = Toplevel(globals.window)
    globals.modelwindow.config(background="#051d26")
    globals.modelwindow.geometry("766x730+767+82")
    globals.modelwindow.overrideredirect(True)

    globals.summaryLabel = Label(globals.modelwindow,font=("Arial",15,"bold"),width=60,height=14,bg="#1a4757",borderwidth=2,relief="groove")
    globals.summaryLabel.place(x=-700,y=-700)

    globals.sumpredLabel = Label(globals.summaryLabel,text="PREDICTION",bg="#0a2630",fg="#e31414",font=("Arial",13,"bold"),width=70,height=1,padx=9,pady=15)
    globals.sumpredLabel.place(x=-700,y=-700)

    globals.outputLabel = Label(globals.summaryLabel,text="Model used             :",font=("Arial",14,"bold"),bg="#1a4757")
    globals.outputLabel.place(x=-100,y=-100)

    globals.prediction = Label(globals.summaryLabel,bg="#1a4757",width=30,height=1,font=("Arial",14,"bold"),pady=5,fg="#ffffff")
    globals.prediction.place(x=-100,y=-100) 

    globals.outputLabel1 = Label(globals.summaryLabel,text="Algorithm used       :",font=("Arial",14,"bold"),bg="#1a4757")
    globals.outputLabel1.place(x=-100,y=-100)

    globals.prediction1 = Label(globals.summaryLabel,bg="#1a4757",width=30,height=1,font=("Arial",14,"bold"),pady=5,borderwidth=1,fg="#ffffff")
    globals.prediction1.place(x=-100,y=-100) 

    globals.outputLabel2 = Label(globals.summaryLabel,text="Prediction is           :",font=("Arial",14,"bold"),bg="#1a4757")
    globals.outputLabel2.place(x=-100,y=-100)

    globals.prediction2 = Label(globals.summaryLabel,bg="#1a4757",width=30,height=1,font=("Arial",14,"bold"),pady=5,fg="#ffffff")
    globals.prediction2.place(x=-100,y=-100)

    globals.doneLabel = Label(globals.modelwindow,text=" Prediction is Done....!!!!!!!",font=("Arial",19,"italic"),bg="#051d26",fg='#0bd923')
    globals.doneLabel.place(x=-100,y=-600)

    globals.taskLabel.destroy()
    if(globals.modelFlag == 1):
        windows.getting_input_class()
    elif(globals.modelFlag == 2):
        windows.getting_input_reg()

def train(event): 
    for column in  (globals.data.columns.values)[:-1]:
        if(globals.data[column].dtype == "O"):
            globals.modelName = " C l a s s i f i c a t i o n  M o d e l "
            globals.modelFlag = 1
        if(globals.data[column].dtype == 'int64'):
            globals.modelName =" R e g r e s s i o n  M o d e l "
            globals.modelFlag = 2

    globals.trainButton.config(state="disabled")
    globals.taskLabel.place(x=40,y=630)
    if(globals.modelFlag == 1):
        globals.taskLabel.config(text=" The dataset is trained with Naive Bayes classifier")
    elif(globals.modelFlag == 2):
        globals.taskLabel.config(text=" The dataset is trained with Multiple Linear Regression")
    globals.bar.place(x=10,y=38)
    globals.percentLabel.place(x=985,y=34)
    task = 100
    download = 0
    speed = 2
    while(download<task):
        time.sleep((globals.data.shape[0]*globals.data.shape[1])/100000)
        globals.bar['value']+=(speed/task)*100
        download+=speed
        globals.percent.set((str(int((download/task)*100)))+'%')
        globals.window.update_idletasks()
    globals.testButton.place(x=1200,y=650) 
      
    

def nextinput():
    val = globals.inputEntry.get()

    try:
        value = int(val)

        if value > globals.maximum[globals.count] or value < globals.minimum[globals.count]:
            globals.inputEntry.delete(0,END)
            globals.invalid_range.config(text="********   please  enter  value  in  given  range   ********")
            return

        globals.selected_list.append(value)
        globals.invalid_range.config(text="")
             
    except:

        globals.invalid_range.config(text="********   please   enter  numerical  value  in  given  range   ********")
        flag = True
        globals.inputEntry.delete(0,END)
        return
        
    if((len(globals.attribute_list))-1==globals.count):
        globals.submit.config(state="normal")
        globals.next.config(state="disabled")

    else:
        globals.count+= 1
        globals.attribute_label.config(text=globals.attribute_list[globals.count])
        globals.range.config(text="range of input : ["+str(globals.minimum[globals.count])+"-"+str(globals.maximum[globals.count])+"]")

    globals.inputEntry.delete(0,END)

def submitresult():

    globals.tree.destroy()
    globals.scrollbarV.destroy()
    globals.scrollbarH.destroy()   

    windows.Merge()
    windows.showData(globals.selected_list_show,globals.col)
    globals.inputtitleLabel.place(x=320,y=635)
    globals.inputtitleLabel.config(text="Selected Input Data")
    globals.dataButton.place(x=595,y=660)
    globals.dataButton.config(text="original data")
    globals.nextButton.config(state="normal")
    if(globals.modelFlag == 1):
        globals.btn2.config(state="disabled")
    elif(globals.modelFlag == 2):
        globals.submit.config(state="disabled")

def originaldata(event):
    if(globals.dataFlag):
        globals.tree.destroy()
        globals.scrollbarH.destroy()
        globals.scrollbarV.destroy()
        windows.showData(globals.data.values,tuple(globals.data.columns.values))
        globals.inputtitleLabel.config(text="Processed Data")
        globals.dataButton.config(text="input data")
        globals.dataFlag = False
    else:
        globals.tree.destroy()
        globals.scrollbarH.destroy()
        globals.scrollbarV.destroy()
        windows.showData(globals.selected_list_show,globals.col)
        globals.inputtitleLabel.config(text="Selected Input Data")
        globals.dataButton.config(text="original data")
        globals.dataFlag = True

def reset():
    globals.selected_list = []
    globals.selected_list_show = []
    globals.count = 0
    if(globals.modelFlag == 1):
        globals.choic_count = len(globals.values_list[globals.count])
        for widgets in globals.choice_label.winfo_children():
            widgets.destroy()
        for i in range( globals.choic_count):
            globals.choice = Radiobutton(globals.choice_label,text=globals.values_list[globals.count][i],font=('plain',13), bg='#1a4757', fg='#0bd923', variable=globals.x,padx=5, value=i, command=select)
            globals.choice.place(x=122*i+2, y=3) 
        globals.choice_label.place(x=80,y=150)   
        globals.att_label.config(text="For " + globals.attribute_list[globals.count])  
        globals.btn2.config(state="disabled")
        globals.btn1.config(state="disabled")           
    elif(globals.modelFlag == 2):
        globals.attribute_label.config(text=globals.attribute_list[globals.count])
        globals.range.config(text="range of input : ["+str(globals.minimum[globals.count])+"-"+str(globals.maximum[globals.count])+"]")
        globals.inputEntry.delete(0,END)
        globals.submit.config(state='disabled')
        globals.next.config(state="normal")
    
    globals.nextButton.config(state="disabled")
    

def proceed():
    globals.resetButton.destroy()
    globals.nextButton.destroy()
    globals.summaryLabel.place(x=20,y=150)
    globals.sumpredLabel.place(x=0,y=0)
    globals.outputLabel.place(x=40,y=80)
    globals.prediction.place(x=280,y=80)
    globals.outputLabel1.place(x=40,y=150)
    globals.prediction1.place(x=280,y=150)
    globals.outputLabel2.place(x=40,y=220)
    globals.prediction2.place(x=280,y=220)
    globals.model_label.config(text="  S U M M A R Y  ")
    if(globals.modelFlag == 1):
        globals.input_label1.destroy()
        globals.prediction.config(text="Classification Model")
        globals.prediction1.config(text="Naive Bayes Algorithm")
        output_class = prediction_class(globals.datasetNumpy,globals.data.shape[0],globals.data.shape[1],globals.selected_list)
        globals.prediction2.config(text=output_class)
    elif(globals.modelFlag == 2):
        globals.input_label.destroy()
        globals.prediction.config(text="Regression Model")
        globals.prediction1.config(text="MultipleLinear Regression Algorithm")
        X = globals.data.iloc[:,:-1].to_numpy()
        y = globals.data.iloc[:,-1].to_numpy()
        input_list = []
        input_list.append(globals.selected_list)
        output_reg = prediction_reg(X,y,input_list)
        globals.prediction2.config(text=output_reg)
    
    globals.dataButton.destroy()
    globals.tree.destroy()
    globals.scrollbarH.destroy()
    globals.scrollbarV.destroy()
    windows.showData(globals.selected_list_show,globals.col)
    globals.inputtitleLabel.config(text="Selected Input Data")

    globals.doneLabel.place(x=180,y=570)


    

def select():
    
    if(globals.count == len(globals.attribute_list)):
        return
    
    globals.btn1.config(state="normal")
    for i in range(globals.choic_count):
        if( globals.x.get() == i):
            globals.selected_val = globals.values_list[globals.count][i]
    
    
def submit1():
    
    globals.selected_list.append(globals.selected_val)
    globals.count += 1

    if globals.count == len(globals.attribute_list):
        globals.btn1.config(state="disabled")
        globals.btn2.config(state="normal")
        globals.resetButton.config(state="normal")
        for i in range( globals.choic_count):
            globals.choice.config(state="disabled") 
         
    elif(globals.count > len(globals.attribute_list)):
        pass
    else:
        for widgets in globals.choice_label.winfo_children():
            widgets.destroy()
               
        globals.choic_count = len(globals.values_list[globals.count])

        for i in range( globals.choic_count):
            globals.choice = Radiobutton(globals.choice_label,text=globals.values_list[globals.count][i],font=('plain',13), bg='#1a4757', fg='#0bd923', variable=globals.x,padx=5, value=i, command=select)
            globals.choice.place(x=122*i+2, y=3) 
        globals.choice_label.place(x=80,y=150)              

        globals.att_label.config(text="For " + globals.attribute_list[globals.count]) 
    
    globals.btn1.config(state="disabled")