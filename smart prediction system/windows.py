import globals
import funcs
from tkinter import ttk
from tkinter import *
from NaiveBayes.naive_bayes import *



def showData(list_values_name,cols):   
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("Treeview",rowheight=35)
    globals.tree  = ttk.Treeview(globals.datawindow,columns=cols,show='headings',height=17)

    globals.scrollbarV = ttk.Scrollbar(globals.datawindow,orient="vertical",command=globals.tree.yview)
    globals.scrollbarV.pack(side="right",fill='y')
    globals.scrollbarH = ttk.Scrollbar(globals.datawindow,orient="horizontal",command=globals.tree.xview)
    globals.scrollbarH.pack(side="bottom",fill='x')
    globals.tree.configure(yscrollcommand=globals.scrollbarV.set)
    globals.tree.configure(xscrollcommand=globals.scrollbarH.set)
    
    for colname in cols:
        globals.tree.heading(colname,text=colname)
        if(len(cols)>3):
            globals.tree.column(column=colname,width=400,anchor=CENTER)
        elif(len(cols) == 2):
            globals.tree.column(column=colname,width=398,anchor=CENTER)
        else:
            globals.tree.column(column=colname,width=520,anchor=CENTER)
    globals.tree.pack()


    for value_tuple in list_values_name[0:]:      
        globals.tree.insert('','end',values=tuple(value_tuple)) 

def samewidget(name):
    globals.model_label = Label(globals.modelwindow,text=name,font=("Arial",17),bg="#1c4352",width=59,height=2,padx=0)
    globals.model_label.place(x=0,y=0) 

    globals.resetButton = Button(globals.modelwindow,text="R E S E T",bg="#1c4352",font=("Arial",13),padx=5,pady=8,width=30,command=funcs.reset)
    globals.resetButton.place(x=80,y=580)

    globals.nextButton = Button(globals.modelwindow,text="P R E D I C T",bg="#1c4352",font=("Arial",13),padx=5,pady=8,width=30,command=funcs.proceed,state=DISABLED)
    globals.nextButton.place(x=400,y=580)

def getting_input_reg():

    globals.attribute_list = (globals.data.columns.values)[:-1]
    globals.maximum = globals.data.max().tolist()[:-1]
    globals.minimum = globals.data.min().tolist()[:-1]

    samewidget(globals.modelName)

    globals.input_label = Label(globals.modelwindow,bg="#1a4757",width=62,height=14,font=("Arial",15),padx=4,pady=15,borderwidth=2,relief="groove")
    globals.input_label.place(x=35,y=140)

    globals.algoLabel1 = Label(globals.input_label,text="MULTIPLE LINEAR REGRESSOR",font=("Arial",13,"bold"),width=66,height=1,bg="#0a2630",padx=13,pady=10) 
    globals.algoLabel1.place(x=0,y=0)

    globals.attribute_label = Label(globals.input_label,bg="#0a2629",fg="#e31414",text=globals.attribute_list[0],width=20,height=2,font=("Arial",15),borderwidth=1,relief='solid')
    globals.attribute_label.place(x=40,y=90)
    
    globals.range = Label(globals.input_label,text="range of input : ["+str(globals.minimum[globals.count])+"-"+str(globals.maximum[globals.count])+"]",bg="#0a2629",fg="#e31414",width=25,height=2,font=("Arial",15),borderwidth=1,relief='solid')
    globals.range.place(x=350,y=90)
    
    globals.inputEntry = Entry(globals.input_label,width=12,font=("Arial",24),bg="#256b85",fg="#000000",borderwidth=1,relief="solid")
    globals.inputEntry.place(x=40,y=170)
    
    globals.next = Button(globals.input_label,text="Next",bg="#0a2629",fg="#ffffff",width=15,height=2,font=("Arial",11),borderwidth=1,relief="solid",command=funcs.nextinput)
    globals.next.place(x=350,y=170)
    
    globals.invalid_range = Label(globals.input_label,width=54,height=1,font=("consolas",5),bg="#1a4757",fg="red")
    globals.invalid_range.place(x=39,y=210)

    globals.submit = Button(globals.input_label,text="Submit",bg="#0a2629",fg="#ffffff",width=15,height=2,font=("Arial",11),borderwidth=1,relief='solid',command=funcs.submitresult,state="disabled")
    globals.submit.place(x=230,y=250)
   

    

def Merge():
    for i in range(len(globals.attribute_list)):
        list1 = [globals.attribute_list[i],globals.selected_list[i]]
        globals.selected_list_show.append(tuple(list1))

def getting_input_class():

    globals.x = IntVar()

    globals.datasetNumpy = globals.data.to_numpy()

    globals.attribute_list = (globals.data.columns.values)[:-1]
    globals.values_list = attribute_val(globals.datasetNumpy,globals.data.shape[0],globals.data.shape[1])

    samewidget(globals.modelName)

    globals.input_label1 = Label(globals.modelwindow, font=('Arial 15'),padx=10, pady=20, bg='#1a4757', fg='#282e27', width=60, height=12,borderwidth=2,relief='ridge')
    globals.input_label1.place(x=40,y=150)

    globals.algoLabel2 = Label(globals.input_label1,text="NAIVE BAYES CLASSIFIER",font=("Arial",13,"bold"),width=66,height=1,bg='#0a2630',padx=8,pady=10) 
    globals.algoLabel2.place(x=0,y=0)

    globals.att_label = Label(globals.input_label1, text="For " + globals.attribute_list[0], font=('Consolas',15),fg='#e31414', bg='#0a2629',width=15,height=1,borderwidth=1,relief="groove",pady=5)
    globals.att_label.place(x=80,y=80)

    globals.choic_count = len(globals.values_list[globals.count])

    globals.choice_label = Label(globals.input_label1, width=70,height=2, bg='#0a2629', relief='groove',pady=4)
    globals.choice_label.place(x=80,y=140)

    globals.btn1 = Button(globals.input_label1, text="next", font=('Consolas',12), bg='#0a2629', fg='#ffffff', width=11, padx=3,borderwidth=1,relief="solid",command=funcs.submit1,state=DISABLED)
    globals.btn1.place(x=390,y=250)

    globals.btn2 = Button(globals.input_label1, bg='#0a2629',font=('Consolas',12), fg='#ffffff', text="submit",padx=10, width=9,borderwidth=1,relief="solid",command=funcs.submitresult,state=DISABLED)
    globals.btn2.place(x=520,y=250)

    for i in range( globals.choic_count):
        globals.choice = Radiobutton(globals.choice_label, text=globals.values_list[globals.count][i],font=('plain',13), bg='#1a4757', fg='#0bd923',padx=5, variable=globals.x, value=i, command=funcs.select,pady=2)
        globals.choice.place(x=102*i+2, y=3)
    globals.choice_label.place(x=80,y=150)