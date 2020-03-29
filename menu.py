#!/usr/bin/python3
import os
import csv
import subprocess
from tkinter import *

STATES = [
	'AL', 'AK', 'AZ', 'AR', 'CA', 
	'CO', 'CT', 'DE', 'FL', 'GA', 
	'HI', 'ID', 'IL', 'IN', 'IA', 
	'KS', 'KY', 'LA', 'ME', 'MD', 
	'MA', 'MI', 'MN', 'MS', 'MO', 
	'MT', 'NE', 'NV', 'NH', 'NJ', 
	'NM', 'NY', 'NC', 'ND', 'OH', 
	'OK', 'OR', 'PA', 'RI', 'SC', 
	'SD', 'TN', 'TX', 'UT', 'VT', 
	'VA', 'WA', 'WV', 'WI', 'WY']
YEARS = [
	'06-07', 
	'07-08', 
	'08-09', 
	'09-10', 
	'10-11',
	'11-12',
	'12-13',
	'13-14',
	'14-15',
	'15-16',
	'16-17']
ATTRIBUTES = [
	"SAT AVG", 
	"ADMISSION RATE", 
	"AVG COST FOR 4 YEARS"
	]

CHOSEN_STATES= []

SAT_PRICE=0
SAT_PRICE=2400
master = Tk()
logo = PhotoImage(file="resources/FlexiRankLogo.png")
master.title("FlexiRankColleges Form")
master.geometry('1000x1000')

label_0 = Label(master, image = logo)
label_0.pack(side=TOP)
label_1 = Label(master, text= "Please fill out the following form to get your personal college ranking", width=0, font=("bold", 9))
label_1.pack(side=TOP)

##STATES
#DROP DOWN MENU
state= Frame(master)
label_2 = Label(state, text= "Select states:", width=20, font=("bold", 10))
label_2.pack(side=TOP)

variable = StringVar(master)
variable.set('AL')
Sdrop = OptionMenu(state, variable, *STATES)
Sdrop.pack(side=TOP)

state.pack(side=TOP)


#SEE CHOSEN OPTIONS
chosen=Frame(master)
def chosen_label(label):
  def chosen():
    label.config(text=CHOSEN_STATES)
    label.after(1000, chosen)
    label.pack(side=TOP)
  chosen()
 
label = Label(chosen, fg="green")
label.pack()
chosen_label(label)


#FUNCTIONS FOR BUTTONS
def agane(*args):
    if variable.get() not in CHOSEN_STATES:
        CHOSEN_STATES.append(variable.get())

def peek():
    CHOSEN_STATES.clear()
Button(chosen, text="CLEAR", command = peek).pack(side=RIGHT)
Button(chosen, text="ADD", command = agane).pack(side=RIGHT)
chosen.pack(side=TOP)

##YEARS
#DROP DOWN MENU
label_2_1 = Label(master, text= "Select year:", width=20, font=("bold", 10))
label_2_1.pack(side=TOP)

variabley = StringVar(master)
variabley.set('16-17')

ydrop = OptionMenu(master, variabley, *YEARS)
ydrop.pack(side=TOP)


##ATTRIBUTE TO SORT BY
#RADIO BUTTON
label_2_2= Label(master, text= "Select Attribute To Rank By:", width=30, font=("bold", 10))
label_2_2.pack(side=TOP)

v = IntVar()
v.set(0)
def SHOW():
	print(v.get())
for val, attribute in enumerate(ATTRIBUTES):
	Radiobutton(master, text= attribute, padx=20,variable=v, value=val).pack(side=TOP)

##SAT AVERAGE
minsat=Frame(master)
label_3= Label(minsat, text="Min SAT Average:", width=20, font=("bold", 10))
label_3.pack(side=LEFT)
MIN_SAT = Entry(minsat)
MIN_SAT.pack(side=LEFT)
minsat.pack(side=TOP)

maxsat=Frame(master)
label_3= Label(maxsat, text="Max SAT Average:", width=20, font=("bold", 10))
label_3.pack(side=LEFT)
MAX_SAT = Entry(maxsat)
MAX_SAT.pack(side=LEFT)
maxsat.pack(side=TOP)


##ADMISSION RATE
minadm=Frame(master)
label_4= Label(minadm, text="Min Admission Rate:", width=20, font=("bold", 10))
label_4.pack(side=LEFT)
MIN_ADM = Entry(minadm)
MIN_ADM.pack(side=LEFT)
minadm.pack(side=TOP)

maxadm=Frame(master)
label_5= Label(maxadm, text="Max Admission Rate:", width=20, font=("bold", 10))
label_5.pack(side=LEFT)
MAX_ADM = Entry(maxadm)
MAX_ADM.pack(side=LEFT)
maxadm.pack(side=TOP)

##COST OF ATTENDANCE
mincst=Frame(master)
label_6= Label(mincst, text="Min Tuition:", width=20, font=("bold", 10))
label_6.pack(side=LEFT)
MIN_CST = Entry(mincst)
MIN_CST.pack(side=LEFT)
mincst.pack(side=TOP)

maxcst=Frame(master)
label_7= Label(maxcst, text="Max Tuition:", width=20, font=("bold", 10))
label_7.pack(side=LEFT)
MAX_CST = Entry(maxcst)
MAX_CST.pack(side=LEFT)
maxcst.pack(side=TOP)


##MISSING FIELDS
    #STATES
e1=[]
e2=[]
e3=[]
e4=[]
e5=[]
e6=[]
e7=[]


def empty_chosen_label(label):
  def empty_chosen():
    label.config(text=e1)
    label.after(1000, empty_chosen)
    label.pack(side=LEFT)
  empty_chosen()
 
label_1e = Label(state, fg="red")


    #MIN SAT
def empty_MIN_SAT_label(label):
  def empty_MIN_SAT():
    label.config(text=e2)
    label.after(1000, empty_MIN_SAT)
    label.pack(side=LEFT)
  empty_MIN_SAT()
 
label_2e = Label(minsat, fg="red")


    #MAX SAT
def empty_MAX_SAT_label(label):
  def empty_MAX_SAT():
    label.config(text=e3)
    label.after(1000, empty_MAX_SAT)
    label.pack(side=LEFT)
  empty_MAX_SAT()
 
label_3e = Label(maxsat, fg="red")


    #MIN ADM
def empty_MIN_ADM_label(label):
  def empty_MIN_ADM():
    label.config(text=e4)
    label.after(1000, empty_MIN_ADM)
    label.pack(side=LEFT)
  empty_MIN_ADM()
 
label_4e = Label(minadm, fg="red")


    #MAX ADM
def empty_MAX_ADM_label(label):
  def empty_MAX_ADM():
    label.config(text=e5)
    label.after(1000, empty_MAX_ADM)
    label.pack(side=LEFT)
  empty_MAX_ADM()
 
label_5e = Label(maxadm, fg="red")


    #MIN CST
def empty_MIN_CST_label(label):
  def empty_MIN_CST():
    label.config(text=e6)
    label.after(1000, empty_MIN_CST)
    label.pack(side=LEFT)
  empty_MIN_CST()
 
label_6e = Label(mincst, fg="red")


    #MAX CST
def empty_MAX_CST_label(label):
  def empty_MAX_CST():
    label.config(text=e7)
    label.after(1000, empty_MAX_CST)
    label.pack(side=LEFT)
  empty_MAX_CST()
 
label_7e = Label(maxcst, fg="red")



def Submit():
    fields=0
    e1.clear()
    e2.clear()
    e3.clear()
    e4.clear()
    e5.clear()
    e6.clear()
    e7.clear()
    
    if CHOSEN_STATES:
        fields=fields+1
    else:
        e1.append("*")
        label_1e.pack(side=LEFT)
        empty_chosen_label(label_1e)


    if MIN_SAT.get():
        fields=fields+1
    elif MIN_SAT.get() > MAX_SAT.get():
        e2.append("MIN>MAX")
        label_2e.pack(side=LEFT)
        empty_MIN_SAT_label(label_2e)
    else:
        e2.append("*")
        label_2e.pack(side=LEFT)
        empty_MIN_SAT_label(label_2e)

        
    if MAX_SAT.get():
        fields=fields+1
    else:
        e3.append("*")
        label_3e.pack(side=LEFT)
        empty_MAX_SAT_label(label_3e)

        
    if MIN_ADM.get():
        fields=fields+1
    else:
        e4.append("*")
        label_4e.pack(side=LEFT)
        empty_MIN_ADM_label(label_4e)

        
    if MAX_ADM.get():
        fields=fields+1
    else:
        e5.append("*")
        label_5e.pack(side=LEFT)
        empty_MAX_ADM_label(label_5e)

        
    if MIN_CST.get():
        fields=fields+1
    else:
        e6.append("*")
        label_6e.pack(side=LEFT)
        empty_MIN_CST_label(label_6e)

        
    if MAX_CST.get():
        fields=fields+1
    else:
        e7.append("*")
        label_7e.pack(side=LEFT)
        empty_MAX_CST_label(label_7e)

        
        
    if fields == 7:
        if variabley.get() == '06-07':
            reader = csv.reader(open("data/MERGED2006_07_PP.csv"))
        elif variabley.get() == '07-08':
            reader = csv.reader(open("data/MERGED2007_08_PP.csv"))
        elif variabley.get() == '08-09':
            reader = csv.reader(open("data/MERGED2008_09_PP.csv"))
        elif variabley.get() == '09-10':
            reader = csv.reader(open("data/MERGED2009_10_PP.csv"))
        elif variabley.get() == '10-11':
            reader = csv.reader(open("data/MERGED2010_11_PP.csv"))
        elif variabley.get() == '11-12':
            reader = csv.reader(open("data/MERGED2011_12_PP.csv"))
        elif variabley.get() == '12-13':
            reader = csv.reader(open("data/MERGED2012_13_PP.csv"))
        elif variabley.get() == '13-14':
            reader = csv.reader(open("data/MERGED2013_14_PP.csv"))
        elif variabley.get() == '14-15':
            reader = csv.reader(open("data/MERGED2014_15_PP.csv"))
        elif variabley.get() == '15-16':
            reader = csv.reader(open("data/MERGED2015_16_PP.csv"))
        else:
            reader = csv.reader(open("data/MERGED2016_17_PP.csv"))

        with open("data/newfile.csv", mode='w', newline='') as newfile:
            for data in reader:
                file_write = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if data[5] == "STABBR":
                    file_write.writerow([data[0]]+[data[3]]+[data[59]]+[data[36]]+[data[376]])
                for x in CHOSEN_STATES:
                    if data[5] == x and data[59] > MIN_SAT.get() and data[59] < MAX_SAT.get() and data[36] > MIN_ADM.get() and data[36] < MAX_ADM.get() and data[376] > MIN_CST.get() and data[376] < MAX_CST.get():
                        file_write.writerow([data[0]]+[data[3]]+[data[59]]+[data[36]]+[data[376]])
        newfile.close()
        subprocess.Popen("python main.py " + 
							"newfile.csv " + 
							str(v.get())+ " " + 
							str(variabley.get())  
							)
        quit()

Button(master, text="SAVE AND QUIT", command=Submit).pack(side=TOP)


#Button(master, text="QUIT", command = quit).place(x=460, y=470)

mainloop()
