from tkinter import *
import sqlite3
window=Toplevel()
window.geometry('1360x800')
window.config(bg='white')
window.title("Calculator")

frame1=Frame(window,bg="white")
frame1.pack()


background=PhotoImage(file='aaaa.gif')
label88=Label(window,image=background)
label88.pack()



############################# Database #########################
Student_name=StringVar()
tgpa1st=StringVar()
tgpa2nd=StringVar()
cgpa_all=StringVar()

####

######Functions:-
def database():
    name=Student_name.get()
    tgpa_1=entry13['text']
    tgpa_2=entry26['text']
    cgpa_f=entry27['text']
    con=sqlite3.connect("Datbase information.db")
    #con.execute("CREATE TABLE STUDENT_CGPA_Details(Student_name varchar(40),TGPA_1st_Sem int not null,TGPA_2nd_Sem int not null,CGPA int not null);")
    con.execute("insert into STUDENT_CGPA_Details(Student_name,TGPA_1st_Sem,TGPA_2nd_Sem,CGPA)values(?,?,?,?)",(name,tgpa_1,tgpa_2,cgpa_f))
    c=con.execute("select * from STUDENT_CGPA_Details")
    for i in c:
        print("name",i[0])
        print("tgpa_1",i[1])
        print("tgpa_2",i[2])
        print("cgpa_f",i[3])
        con.commit()


#### calculation entry :-

entry88=Entry(window)
entry89=Entry(window)
entry90=Entry(window)
entry91=Entry(window)
entry92=Entry(window)
entry93=Entry(window)
        
#################
######################## Functions :-############################

### Function 1 (for 1st semester) :-

def calculate1():
    
    if(label5.get()!="Please   select   the   subject" and label6.get()!="Please   select   the   subject" and label7.get()!="Please   select   the   subject" and label8.get()!="Please   select   the   subject" and label9.get()!="Please   select   the   subject" and label10.get()!="Please   select   the   subject" and entry1.get()!="select" and entry2.get()!="select" and entry3.get()!="select" and entry4.get()!="select" and entry5.get()!="select"  and entry6.get()!="select"   and credit_1.get()!="select" and credit_2.get()!="select" and credit_3.get()!="select" and credit_4.get()!="select" and credit_5.get()!="select" and credit_6.get()!="select"):
      
           try:
               O=int(10)
               A_plus=int(9)
               A=int(8)
               B_plus=int(7)
               B=int(6)
               C_plus=int(5)
               C=int(4)
               D_plus=int(3)
               D=int(3)
               E_plus=int(0)
               E=int(0)

               point1=int(0)
               point2=int(0)
               point3=int(0)
               point4=int(0)
               point5=int(0)
               point6=int(0)
            
               credit1=int(credit_1.get())
               credit2=int(credit_2.get())
               credit3=int(credit_3.get())
               credit4=int(credit_4.get())
               credit5=int(credit_5.get())
               credit6=int(credit_6.get())

               if entry1.get()=='A+':
                  point1=int(point1+A_plus)
               elif entry1.get()=='A':
                  point1=int(point1+A)
               elif entry1.get()=='B+':
                   point1=int(point1+B_plus)
               elif entry1.get()=='B':
                    point1=int(point1+B)
               elif entry1.get()=='C+':
                    point1=int(point1+C_plus)
               elif entry1.get()=='C':
                    point1=int(point1+C)
               elif entry1.get()=='D+':
                    point1=int(point1+D_plus)
               elif entry1.get()=='D':
                    point1=int(point1+D)
               elif entry1.get()=='E+':
                    point1=int(point1+E_plus)
               elif entry1.get()=='E':
                    point1=int(point1+E)
               else:
                     entry13.configure(text="invalid")

               value1=float(point1*credit1)

               if entry2.get()=='A+':
                    point2=int(point2+A_plus)
               elif entry2.get()=='A':
                    point2=int(point2+A)
               elif entry2.get()=='B+':
                    point2=int(point3+B_plus)
               elif entry2.get()=='B':
                    point2=int(point2+B)
               elif entry2.get()=='C+':
                    point2=int(point3+C_plus)
               elif entry2.get()=='C':
                    point2=int(point4+C)
               elif entry2.get()=='D+':
                    point2=int(point5+D_plus)
               elif entry2.get()=='D':
                    point2=int(point2+D)
               elif entry2.get()=='E+':
                    point2=int(point2+E_plus)
               elif entry2.get()=='E':
                    point2=int(point2+E)
               else:
                     entry13.configure(text="invalid")

               value2=float(point2*credit2)

               if entry3.get()=='A+':
                    point3=int(point3+A_plus)
               elif entry3.get()=='A':
                    point3=int(point3+A)
               elif entry3.get()=='B+':
                    point3=int(point3+B_plus)
               elif entry3.get()=='B':
                    point3=int(point3+B)
               elif entry3.get()=='C+':
                    point3=int(point3+C_plus)
               elif entry3.get()=='C':
                    point3=int(point3+C)
               elif entry3.get()=='D+':
                    point3=int(point3+D_plus)
               elif entry3.get()=='D':
                    point3=int(point3+D)
               elif entry3.get()=='E+':
                    point3=int(point3+E_plus)
               elif entry3.get()=='E':
                    point3=int(point3+E)
               else:
                     entry13.configure(text="invalid")

               value3=float(point3*credit3)
            
               if entry4.get()=='A+':
                    point4=int(point4+A_plus)
               elif entry4.get()=='A':
                    point4=int(point4+A)
               elif entry4.get()=='B+':
                    point4=int(point4+B_plus)
               elif entry4.get()=='B':
                    point4=int(point4+B)
               elif entry4.get()=='C+':
                    point4=int(point4+C_plus)
               elif entry4.get()=='C':
                    point4=int(point4+C)
               elif entry4.get()=='D+':
                    point4=int(point4+D_plus)
               elif entry4.get()=='D':
                    point4=int(point4+D)
               elif entry4.get()=='E+':
                    point4=int(point4+E_plus)
               elif entry4.get()=='E':
                    point4=int(point4+E)
               else:
                     entry13.configure(text="invalid")


               value4=float(point4*credit4)
            
               if entry5.get()=='A+':
                    point5=int(point5+A_plus)
               elif entry5.get()=='A':
                    point5=int(point5+A)
               elif entry5.get()=='B+':
                   point5=int(point5+B_plus)
               elif entry5.get()=='B':
                   point5=int(point5+B)
               elif entry5.get()=='C+':
                    point5=int(point5+C_plus)
               elif entry5.get()=='C':
                    point5=int(point5+C)
               elif entry5.get()=='D+':
                    point5=int(point5+D_plus)
               elif entry5.get()=='D':
                    point5=int(point5+D)
               elif entry5.get()=='E+':
                    point5=int(point5+E_plus)
               elif entry5.get()=='E':
                    point5=int(point5+E)
               else:
                    entry13.configure(text="invalid")
               value5=float(point5*credit6)

               if entry6.get()=='A+':
                    point6=int(point6+A_plus)
               elif entry6.get()=='A':
                    point6=int(point6+A)
               elif entry6.get()=='B+':
                    point6=int(point6+B_plus)
               elif entry6.get()=='B':
                    point6=int(point6+B)
               elif entry6.get()=='C+':
                    point6=int(point6+C_plus)
               elif entry6.get()=='C':
                    point6=int(point6+C)
               elif entry6.get()=='D+':
                    point6=int(point6+D_plus)
               elif entry6.get()=='D':
                   point6=int(point6+D)
               elif entry6.get()=='E+':
                    point6=int(point6+E_plus)
               elif entry6.get()=='E':
                    point6=int(point6+E)
               else:
                    entry13.configure(text="invalid")

               value6=float(point6*credit6)
               print(value1,value2,value3,value4,value5,value6)
               value_1st=float(value1+value2+value3+value4+value5+value6)
               credit_1st=float(credit1+credit2+credit3+credit4+credit5+credit6)
               tgpa1=float(value_1st/credit_1st)
               TGPA1=float("{0:.2f}".format(tgpa1))
               print(tgpa1)
               entry13.configure(text=TGPA1)
               

           except:
                    entry13.configure(text="Fill all")
    else:
             entry13.configure(text="Invalid")


            
##################################

## Function 2 ( for 2nd semester) :-

def calculate2():
 
    if(label14.get()!="Please   select   the   subject" and label15.get()!="Please   select   the   subject" and label16.get()!="Please   select   the   subject" and label17.get()!="Please   select   the   subject" and label18.get()!="Please   select   the   subject" and label19.get()!="Please   select   the   subject" and entry14.get()!="select" and entry15.get()!="select" and entry16.get()!="select" and entry17.get()!="select" and entry18.get()!="select"  and entry19.get()!="select"   and credit_8.get()!="select" and credit_9.get()!="select" and credit_10.get()!="select" and credit_11.get()!="select" and credit_12.get()!="select" and credit_13.get()!="select"):
  
         try:
             
               O=int(10)
               A_plus=int(9)
               A=int(8)
               B_plus=int(7)
               B=int(6)
               C_plus=int(5)
               C=int(4)
               D_plus=int(3)
               D=int(3)
               E_plus=int(0)
               E=int(0)

               point1=int(0)
               point2=int(0)
               point3=int(0)
               point4=int(0)
               point5=int(0)
               point6=int(0)
            
               credit1=int(credit_8.get())
               credit2=int(credit_9.get())
               credit3=int(credit_10.get())
               credit4=int(credit_11.get())
               credit5=int(credit_12.get())
               credit6=int(credit_13.get())

               if entry14.get()=='A+':
                  point1=int(point1+A_plus)
               elif entry14.get()=='A':
                  point1=int(point1+A)
               elif entry14.get()=='B+':
                   point1=int(point1+B_plus)
               elif entry14.get()=='B':
                    point1=int(point1+B)
               elif entry14.get()=='C+':
                    point1=int(point1+C_plus)
               elif entry14.get()=='C':
                    point1=int(point1+C)
               elif entry14.get()=='D+':
                    point1=int(point1+D_plus)
               elif entry14.get()=='D':
                    point1=int(point1+D)
               elif entry14.get()=='E+':
                    point1=int(point1+E_plus)
               elif entry14.get()=='E':
                    point1=int(point1+E)
               else:
                     entry26.configure(text="invalid")

               value1=float(point1*credit1)

               if entry15.get()=='A+':
                    point2=int(point2+A_plus)
               elif entry15.get()=='A':
                    point2=int(point2+A)
               elif entry15.get()=='B+':
                    point2=int(point3+B_plus)
               elif entry15.get()=='B':
                    point2=int(point2+B)
               elif entry15.get()=='C+':
                    point2=int(point3+C_plus)
               elif entry15.get()=='C':
                    point2=int(point4+C)
               elif entry15.get()=='D+':
                    point2=int(point5+D_plus)
               elif entry15.get()=='D':
                    point2=int(point2+D)
               elif entry15.get()=='E+':
                    point2=int(point2+E_plus)
               elif entry15.get()=='E':
                    point2=int(point2+E)
               else:
                     entry26.configure(text="invalid")

               value2=float(point2*credit2)

               if entry16.get()=='A+':
                    point3=int(point3+A_plus)
               elif entry16.get()=='A':
                    point3=int(point3+A)
               elif entry16.get()=='B+':
                    point3=int(point3+B_plus)
               elif entry16.get()=='B':
                    point3=int(point3+B)
               elif entry16.get()=='C+':
                    point3=int(point3+C_plus)
               elif entry16.get()=='C':
                    point3=int(point3+C)
               elif entry16.get()=='D+':
                    point3=int(point3+D_plus)
               elif entry16.get()=='D':
                    point3=int(point3+D)
               elif entry16.get()=='E+':
                    point3=int(point3+E_plus)
               elif entry16.get()=='E':
                    point16=int(point3+E)
               else:
                     entry26.configure(text="invalid")

               value3=float(point3*credit3)
            
               if entry17.get()=='A+':
                    point4=int(point4+A_plus)
               elif entry17.get()=='A':
                    point4=int(point4+A)
               elif entry17.get()=='B+':
                    point4=int(point4+B_plus)
               elif entry17.get()=='B':
                    point4=int(point4+B)
               elif entry17.get()=='C+':
                    point4=int(point4+C_plus)
               elif entry17.get()=='C':
                    point4=int(point4+C)
               elif entry17.get()=='D+':
                    point4=int(point4+D_plus)
               elif entry17.get()=='D':
                    point4=int(point4+D)
               elif entry17.get()=='E+':
                    point4=int(point4+E_plus)
               elif entry17.get()=='E':
                    point4=int(point4+E)
               else:
                     entry26.configure(text="invalid")


               value4=float(point4*credit4)
            
               if entry18.get()=='A+':
                    point5=int(point5+A_plus)
               elif entry18.get()=='A':
                    point5=int(point5+A)
               elif entry18.get()=='B+':
                   point5=int(point5+B_plus)
               elif entry18.get()=='B':
                   point5=int(point5+B)
               elif entry18.get()=='C+':
                    point5=int(point5+C_plus)
               elif entry18.get()=='C':
                    point5=int(point5+C)
               elif entry18.get()=='D+':
                    point5=int(point5+D_plus)
               elif entry18.get()=='D':
                    point5=int(point5+D)
               elif entry18.get()=='E+':
                    point5=int(point5+E_plus)
               elif entry18.get()=='E':
                    point18=int(point5+E)
               else:
                    entry26.configure(text="invalid")
               value5=float(point5*credit6)

               if entry19.get()=='A+':
                    point6=int(point6+A_plus)
               elif entry19.get()=='A':
                    point6=int(point6+A)
               elif entry19.get()=='B+':
                    point6=int(point6+B_plus)
               elif entry19.get()=='B':
                    point6=int(point6+B)
               elif entry19.get()=='C+':
                    point6=int(point6+C_plus)
               elif entry19.get()=='C':
                    point6=int(point6+C)
               elif entry19.get()=='D+':
                    point6=int(point6+D_plus)
               elif entry19.get()=='D':
                   point6=int(point6+D)
               elif entry19.get()=='E+':
                    point6=int(point6+E_plus)
               elif entry19.get()=='E':
                    point6=int(point6+E)
               else:
                    entry26.configure(text="invalid")

               value6=float(point6*credit6)
               print(value1,value2,value3,value4,value5,value6)
               value_1st=float(value1+value2+value3+value4+value5+value6)
               credit_1st=float(credit1+credit2+credit3+credit4+credit5+credit6)
               tgpa2=float(value_1st/credit_1st)
               TGPA2=float("{0:.2f}".format(tgpa2))
               print(TGPA2)
               entry26.configure(text=TGPA2)
               

         except:
                    entry26.configure(text="Fill all")
    else:
             entry26.configure(text="Invalid")

####################

## function for CGPA :-

def calculate3():

    
    
    if(entry1.get() and entry2.get() and entry3.get() and entry4.get() and entry5.get()  and entry6.get() and entry14.get() and entry15.get() and entry16.get() and entry17.get() and entry18.get() and entry19.get() and credit_1.get() and credit_2.get() and credit_3.get() and credit_4.get() and credit_5 and credit_6  and credit_8.get() and credit_9.get() and credit_10.get() and credit_11.get() and credit_12.get() and credit_13.get() !=" select" ):
    
         try:


             first=entry13['text']
             second=entry26['text']
             value=first+second
             cgpa=float(value/2)
             CGPA=float("{0:.2f}".format(cgpa))
             entry27.configure(text=CGPA)
             print(CGPA)
             if(CGPA <1 or CGPA==1):
                 entry28.configure(text="Reappear",fg="white",bg="red")
                
             elif(CGPA<2 or CGPA==2):
                 entry28.configure(text="Reappear",fg="white",bg="red") 
                 
             elif(CGPA<3 or CGPA==3):
                 entry28.configure(text="Reappear",fg="white",bg="red")
                 
             elif(CGPA<4 or CGPA==4):
                 entry28.configure(text="Need very hard work and improvement",fg="red")
                 
             elif(CGPA<5 or CGPA==5):
                 entry28.configure(text="Need very hard work and improvement",fg="red")
                 
             elif(CGPA<6 or CGPA==6):
                 entry28.configure(text="Need Hardwork and more effort",fg="blue")
                 
             elif(CGPA<7 or CGPA==7):
                 entry28.configure(text="Need Hardwork and more effort",fg="blue")
                 
             elif(CGPA<8 or CGPA==8):
                 entry28.configure(text="Average , need improvement",fg="blue")
                 
             elif(CGPA<9 or CGPA==9.4 ):
                 entry28.configure(text="Very good keep it up",fg="green")
             elif(CGPA>9.4):
                 entry28.configure(text="Awesome very good",fg="green")
             else:
                 print()

             if(CGPA <1 or CGPA==1):
                 entry30.configure(text="E",fg="black",bg="red")
             elif(CGPA<1 or CGPA==2 ):
                 entry30.configure(text="E",fg="red",bg="red")
             elif(CGPA<2 or CGPA==3):
                 entry30.configure(text="D",fg="red",bg="red")
             elif(CGPA<3 or CGPA==4):
                 entry30.configure(text="D+",fg="red")
             elif(CGPA<4 or CGPA==5):
                 entry30.configure(text="C",fg="blue")
             elif(CGPA<5 or CGPA==6):
                 entry30.configure(text="C+",fg="green")
             elif(CGPA<7 or CGPA==7):
                 entry30.configure(text="B",fg="green")
             elif(CGPA<8 or CGPA==8.5):
                 entry30.configure(text="B+",fg="green")
             elif(CGPA<8.5 or CGPA==10):
                 entry30.configure(text="A",fg="green")   
             else:
                 entry30.configure(text="A+",fg="green")
            
         except:
             entry27.configure(text="invalid")
    else:
        entry27.configure(text="fill value")
    
################ Function for reset :-

def exit():
    window.destroy()
    


#########################################################################################################################

icon=PhotoImage(file="ezgif.com-crop.gif")
label1=Label(frame1,image=icon,width=1360,bg="White")
label1.pack()


blank=Label(frame1,bg="red",width='1360',borderwidth=1,relief="groove")
blank.pack(fill=X)


label4=Label(window,bg="#e2e2e2",height="8",font=('Times',30,'bold'),width="20",borderwidth=2,relief="groove")
label4.pack()
label4.place(x=85,y=200)

######################################
#  label for subject , grade and marks and tgpa and cgpa :-

sub_option=[
"Please   select   the   subject",
"COMPUTER PROGRAMMING",
"COMPUTER PROGRAMMING LABORATORY",
"BASIC ELECTRICAL AND ELECTRONICS ENG",
"BASIC ELECTRICAL AND ELECTRONICS ENG LAB",
"ENGINEERING GRAPHICS",
"MATHEMATICS FOR ENGINEERS",
"COMMUNICATION SKILLS-I",
"ENGINEERING PHYSICS",
"ENGINEERING PHYSICS LABORATORY",
"ENVIRONMENTAL STUDIES",
"OBJECT ORIENTED PROGRAMMING",
"INTERNET PROGRAMMING LABORATORY",
"DIGITAL ELECTRONICS",
"DIGITAL ELECTRONICS LABORATORY",
"BASIC ENGINEERING MECHANICS",
"DIFFERENTIAL EQ AND VECTOR CALCULUS",
"COMMUNICATION SKILLS-II",
]

label5=StringVar(window)
label6=StringVar(window)
label7=StringVar(window)
label8=StringVar(window)
label9=StringVar(window)
label10=StringVar(window)


label5.set(sub_option[0])
label6.set(sub_option[0])
label7.set(sub_option[0])
label8.set(sub_option[0])
label9.set(sub_option[0])
label10.set(sub_option[0])



label2=Label(window,text="SEMESTER 1",font=(' Times',15,'bold','italic'),bg='#6262ff',fg='yellow')
label2.pack()
label2.place(x=255,y=160)

label3=Label(window,text="Grade",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label3.pack()
label3.place(x=395,y=220)

label4=Label(window,text="Credit",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label4.pack()
label4.place(x=475,y=220)

label_sub=Label(window,text="Subject",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label_sub.pack()
label_sub.place(x=200,y=220)


sub5=OptionMenu(window,label5,*sub_option)
sub5.pack()
sub5.place(x=100,y=260)
sub5.configure(width=40,bg="white")

sub6=OptionMenu(window,label6,*sub_option)
sub6.pack()
sub6.place(x=100,y=300)
sub6.configure(width=40,bg="white")

sub7=OptionMenu(window,label7,*sub_option)
sub7.pack()
sub7.place(x=100,y=340)
sub7.configure(width=40,bg="white")

sub8=OptionMenu(window,label8,*sub_option)
sub8.pack()
sub8.place(x=100,y=380)
sub8.configure(width=40,bg="white")

sub9=OptionMenu(window,label9,*sub_option)
sub9.pack()
sub9.place(x=100,y=420)
sub9.configure(width=40,bg="white")

sub10=OptionMenu(window,label10,*sub_option)
sub10.pack()
sub10.place(x=100,y=460)
sub10.configure(width=40,bg="white")

# entry for subject and credit

entry1=StringVar(window)
entry2=StringVar(window)
entry3=StringVar(window)
entry4=StringVar(window)
entry5=StringVar(window)
entry6=StringVar(window)

option=[
"select",
"A+",
"A",
"B+",
"B",
"C+",
"C",
"D+",
"D",
"E+",
"E",
]

entry1.set(option[0])
entry2.set(option[0])
entry3.set(option[0])
entry4.set(option[0])
entry5.set(option[0])
entry6.set(option[0])



en1=OptionMenu(window,entry1,*option)
en1.pack()
en1.place(x=388,y=260)
en1.configure(width=4,bg="white")

en2=OptionMenu(window,entry2,*option)
en2.pack()
en2.place(x=388,y=300)
en2.configure(width=4,bg="white")

en3=OptionMenu(window,entry3,*option)
en3.pack()
en3.place(x=388,y=340)
en3.configure(width=4,bg="white")

en4=OptionMenu(window,entry4,*option)
en4.pack()
en4.place(x=388,y=380)
en4.configure(width=4,bg="white")


en5=OptionMenu(window,entry5,*option)
en5.pack()
en5.place(x=388,y=420)
en5.configure(width=4,bg="white")

en6=OptionMenu(window,entry6,*option)
en6.pack()
en6.place(x=388,y=460)
en6.configure(width=4,bg="white")


# Credit

OPTIONS = [
"select",
"4",
"3",
"2",
"1"
]

credit_1=StringVar(window)
credit_2=StringVar(window)
credit_3=StringVar(window)
credit_4=StringVar(window)
credit_5=StringVar(window)
credit_6=StringVar(window)

credit_1.set(OPTIONS[0])
credit_2.set(OPTIONS[0])
credit_3.set(OPTIONS[0])
credit_4.set(OPTIONS[0])
credit_5.set(OPTIONS[0])
credit_6.set(OPTIONS[0])





entry7=OptionMenu(window,credit_1,*OPTIONS)
entry7.pack()
entry7.place(x=470,y=260)
entry7.configure(width=4,bg="white")

entry8=OptionMenu(window,credit_2,*OPTIONS)
entry8.pack()
entry8.place(x=470,y=300)
entry8.configure(width=4,bg="white")

entry9=OptionMenu(window,credit_3,*OPTIONS)
entry9.pack()
entry9.place(x=470,y=340)
entry9.configure(width=4,bg="white")

entry10=OptionMenu(window,credit_4,*OPTIONS)
entry10.pack()
entry10.place(x=470,y=380)
entry10.configure(width=4,bg="white")

entry11=OptionMenu(window,credit_5,*OPTIONS)
entry11.pack()
entry11.place(x=470,y=420)
entry11.configure(width=4,bg="white")

entry12=OptionMenu(window,credit_6,*OPTIONS)
entry12.pack()
entry12.place(x=470,y=460)
entry12.configure(width=4,bg="white")


# TGPA
button1=Button(window,text="TGPA",command=calculate1 or cal,borderwidth=2,relief="ridge",font=('Times',10,'bold'),bg='gray',fg='black')
button1.pack()
button1.place(x=280,y=500)


entry13=Label(window,width=6,font=('Times',14,'bold'),justify=LEFT)
entry13.pack()
entry13.place(x=330,y=500)




#*******************************************************************************************************************************************************************
#*******************************************************************************************************************************************************************
#*******************************************************************************************************************************************************************



####  For semester 2 ############


label14=StringVar(window)
label15=StringVar(window)
label16=StringVar(window)
label17=StringVar(window)
label18=StringVar(window)
label19=StringVar(window)


label14.set(sub_option[0])
label15.set(sub_option[0])
label16.set(sub_option[0])
label17.set(sub_option[0])
label18.set(sub_option[0])
label19.set(sub_option[0])



label4=Label(window,bg="#e2e2e2",height="8",font=('Times',30,'bold'),width="20",borderwidth=2,relief="groove")
label4.pack()
label4.place(x=755,y=200)

label_sub2=Label(window,text="Subject",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label_sub2.pack()
label_sub2.place(x=890,y=220)

label11=Label(window,text="SEMESTER 2",font=(' Times',15,'bold','italic'),bg='light blue',fg="yellow")
label11.pack()
label11.place(x=925,y=160)

label12=Label(window,text="Grade",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label12.pack()
label12.place(x=1065,y=220)

label13=Label(window,text="Credit",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label13.pack()
label13.place(x=1145,y=220)


sub14=OptionMenu(window,label14,*sub_option)
sub14.pack()
sub14.place(x=768,y=260)
sub14.configure(width=40,bg="white")

sub15=OptionMenu(window,label15,*sub_option)
sub15.pack()
sub15.place(x=768,y=300)
sub15.configure(width=40,bg="white")


sub16=OptionMenu(window,label16,*sub_option)
sub16.pack()
sub16.place(x=768,y=340)
sub16.configure(width=40,bg="white")


sub17=OptionMenu(window,label17,*sub_option)
sub17.pack()
sub17.place(x=768,y=380)
sub17.configure(width=40,bg="white")


sub18=OptionMenu(window,label18,*sub_option)
sub18.pack()
sub18.place(x=768,y=420)
sub18.configure(width=40,bg="white")

sub19=OptionMenu(window,label19,*sub_option)
sub19.pack()
sub19.place(x=768,y=460)
sub19.configure(width=40,bg="white")


# entry for subject and credit

entry14=StringVar(window)
entry15=StringVar(window)
entry16=StringVar(window)
entry17=StringVar(window)
entry18=StringVar(window)
entry19=StringVar(window)

option2=[
"select",
"A+",
"A",
"B+",
"B",
"C+",
"C",
"D+",
"D",
"E+",
"E",
]

entry14.set(option[0])
entry15.set(option[0])
entry16.set(option[0])
entry17.set(option[0])
entry18.set(option[0])
entry19.set(option[0])


en14=OptionMenu(window,entry14,*option2)
en14.pack()
en14.place(x=1058,y=260)
en14.configure(width=4,bg="white")

en15=OptionMenu(window,entry15,*option2)
en15.pack()
en15.place(x=1058,y=300)
en15.configure(width=4,bg="white")

en16=OptionMenu(window,entry16,*option2)
en16.pack()
en16.place(x=1058,y=340)
en16.configure(width=4,bg="white")

en17=OptionMenu(window,entry17,*option2)
en17.pack()
en17.place(x=1058,y=380)
en17.configure(width=4,bg="white")

en18=OptionMenu(window,entry18,*option2)
en18.pack()
en18.place(x=1058,y=420)
en18.configure(width=4,bg="white")

en19=OptionMenu(window,entry19,*option2)
en19.pack()
en19.place(x=1058,y=460)
en19.configure(width=4,bg="white")

# Credit

OPTIONS1 = [
"select",
"4",
"3",
"2",
"1"
]

credit_8=StringVar()
credit_9=StringVar()
credit_10=StringVar()
credit_11=StringVar()
credit_12=StringVar()
credit_13=StringVar()

credit_8.set(OPTIONS1[0])
credit_9.set(OPTIONS1[0])
credit_10.set(OPTIONS1[0])
credit_11.set(OPTIONS1[0])
credit_12.set(OPTIONS1[0])
credit_13.set(OPTIONS1[0])





entry20=OptionMenu(window,credit_8,*OPTIONS1)
entry20.pack()
entry20.place(x=1140,y=260)
entry20.configure(width=4,bg="white")

entry21=OptionMenu(window,credit_9,*OPTIONS1)
entry21.pack()
entry21.place(x=1140,y=300)
entry21.configure(width=4,bg="white")

entry22=OptionMenu(window,credit_10,*OPTIONS1)
entry22.pack()
entry22.place(x=1140,y=340)
entry22.configure(width=4,bg="white")

entry23=OptionMenu(window,credit_11,*OPTIONS1)
entry23.pack()
entry23.place(x=1140,y=380)
entry23.configure(width=4,bg="white")

entry24=OptionMenu(window,credit_12,*OPTIONS1)
entry24.pack()
entry24.place(x=1140,y=420)
entry24.configure(width=4,bg="white")

entry25=OptionMenu(window,credit_13,*OPTIONS1)
entry25.pack()
entry25.place(x=1140,y=460)
entry25.configure(width=4,bg="white")

# TGPA
button2=Button(window,text="TGPA",command=calculate2,borderwidth=2,relief="ridge",font=('Times',10,'bold'),bg='gray',fg='black')
button2.pack()
button2.place(x=980,y=500)


entry26=Label(window,width=6,font=('Times',14,'bold'))
entry26.pack()
entry26.place(x=1030,y=500)



###CGPA



label4=Label(window,bg="#e2e2e2",height="2",font=('Times',30,'bold'),width="20",borderwidth=2,relief="groove")
label4.pack()
label4.place(x=455,y=600)

button3=Button(window,text="CGPA",command=calculate3,borderwidth=2,relief="ridge",font=('Times',10,'bold'),bg='gray',fg='black')
button3.pack()
button3.place(x=620,y=605)


entry27=Label(window,width=5,font=('Times',14,'bold'))
entry27.pack()
entry27.place(x=665,y=605)

## Remarks:

label20=Label(window,text="Remarks",borderwidth=2,relief="groove",font=('Times',14,'bold'),bg='powderblue',fg='black')
label20.pack()
label20.place(x=460,y=635)


entry28=Label(window,width=30,font=('Times',14,'bold'))
entry28.pack()
entry28.place(x=550,y=635)


entry30=Label(window,width=5,font=('Times',14,'bold'))
entry30.pack()
entry30.place(x=735,y=605)

###################  USER INFORMATION :-

USER=Label(window,bg="#e2e2e2",height="5",font=('Times',10,'bold'),width="20",borderwidth=2,relief="groove")
USER.pack()
USER.place(x=590,y=300)

name1=Label(window,bg="#e2e2e2",text="Name",font=('Times',11,'bold'))
name1.pack()
name1.place(x=635,y=302)

name_entry=Entry(window,textvar=Student_name)
name_entry.pack()
name_entry.place(x=600,y=324)

button44=Button(window,bg="green",text="Submit",command=database)
button44.pack()
button44.place(x=640,y=350)
    
button45=Button(window,width=20,bg="red",text="Close",command=exit)
button45.pack()
button45.place(x=1200,y=100)

########################## 


window.mainloop()
