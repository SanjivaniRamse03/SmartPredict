from tkinter import *
import funcs
import globals
from win32api import GetMonitorInfo,MonitorFromPoint
monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")  

globals.window = Tk()
globals.window.geometry("%sx%s" % (globals.window.winfo_screenwidth(),work_area[3]))
globals.window.config(background="#05141a")
globals.window.overrideredirect(TRUE)

globals.titlelabel = Label(globals.window,text=" P R E D I C T I O N S Y S T E M ",font=("Arial",14),background="#022229",foreground="#ffffff",padx=14,pady=10,width=137,height=1,anchor=NW)
globals.titlelabel.place(x=0,y=1)

globals.closeLabel = Label(globals.titlelabel,text="X",bg="#47575e",font=("Arial",16),padx=9,pady=6)
globals.closeLabel.place(x=1494,y=1)
globals.closeLabel.bind("<Button-1>",funcs.close)
globals.closeLabel.bind("<Enter>",funcs.enter)
globals.closeLabel.bind("<Leave>",funcs.leave)

globals.predictLabel = Label(globals.window,font=("Arial",11),padx=5,pady=6,width=170,height=1,anchor=NW,bg="#062b33")
globals.predictLabel.place(x=0,y=48)

globals.fileLabel = Label(globals.predictLabel,text="Choose File",font=("Arial",9),padx=9,pady=4,bg="#1a373d",fg="#ffffff")
globals.fileLabel.place(x=1442,y=1)
globals.fileLabel.bind("<Button-1>",funcs.openfile)
globals.fileLabel.bind("<Enter>",funcs.enter1)
globals.fileLabel.bind("<Leave>",funcs.leave1)

globals.window.mainloop()