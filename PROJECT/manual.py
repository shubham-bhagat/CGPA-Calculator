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
        

######################## Functions :-############################
# To user-friendly-environment:
def other_m():
    import user_friendly.py




### Function 1 (for 1st semester) :-

def calculate1():
       if(entry1.get()!=' ' and entry2.get()!=' ' and entry3.get()!=' ' and entry4.get()!=' '  and entry5.get()!=' ' and entry6.get()!=' ' and entry7.get()=='3' and  entry7.get()!=" " and entry8.get()=='4' and
       entry8.get() !=' ' and entry9.get()=='4' and entry9.get() !=' ' and entry10.get()=='4' and
       entry10.get()!=" " and entry11.get()=='1' and entry11.get()!=" " and entry12.get()=='3' and entry12.get() !=" " and
       entry1.get()=='A+' or entry1.get()=='A' or entry1.get()=='B' or entry1.get()=='C' or entry1.get()=='D' or entry1.get()=='E' or entry1.get()=='O' or entry1.get()=='O+' or entry1.get=='A+' or entry1.get()=='B+' or entry1.get()=='C+' or entry1.get()=='D+' or entry1.get()=='E+' and
       entry2.get()=='A' or entry2.get()=='B' or entry2.get()=='C' or entry2.get()=='D' or
       entry2.get()=='E' or entry2.get()=='O' or entry2.get()=='O+' or entry2.get=='A+' or entry2.get()=='B+' or entry2.get()=='C+' or
       entry2.get()=='D+' or entry2.get()=='E+' and
       entry3.get()=='A' or entry3.get()=='B' or entry3.get()=='C' or entry3.get()=='D' or entry3.get()=='E' or entry3.get()=='O' or entry3.get()=='O+' or entry3.get=='A+' or entry3.get()=='B+' or entry3.get()=='C+' or entry3.get()=='D+' or entry3.get()=='E+' and
       entry4.get()=='A' or entry4.get()=='B' or entry4.get()=='C' or entry4.get()=='D' or entry4.get()=='E' or entry4.get()=='O' or entry4.get()=='O+' or entry4.get=='A+' or entry4.get()=='B+' or entry4.get()=='C+' or entry4.get()=='D+' or entry4.get()=='E+' and
       entry5.get()=='A' or entry5.get()=='B' or entry5.get()=='C' or entry5.get()=='D' or entry5.get()=='E' or entry5.get()=='O' or entry5.get()=='O+' or entry5.get=='A+' or entry5.get()=='B+' or entry5.get()=='C+' or entry5.get()=='D+' or entry5.get()=='E+' and
       entry6.get()=='A' or entry6.get()=='B' or entry6.get()=='C' or entry6.get()=='D' or entry6.get()=='E' or entry6.get()=='O' or entry6.get()=='O+' or entry6.get=='A+' or entry6.get()=='B+' or entry6.get()=='C+' or entry6.get()=='D+' or entry6.get()=='E+' ):
            
        
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
            
               credit1=int(entry7.get())
               credit2=int(entry8.get())
               credit3=int(entry9.get())
               credit4=int(entry10.get())
               credit5=int(entry11.get())
               credit6=int(entry12.get())

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
    if(entry14.get()!=' ' and entry15.get()!=' ' and entry16.get()!=' ' and entry17.get()!=' '  and entry18.get()!=' 'and entry19.get()!=' ' and entry20.get()=='1' and  entry20.get()!=" " and entry21.get()=='4' and
       entry21.get()!=" " and entry22.get()=='4' and entry22.get() !=" " and entry23.get()=='4' and
       entry23.get()!=" " and entry24.get()=='4' and entry24.get()!=" " and entry25.get()=='4' and entry25.get() !=" " and
       entry14.get()=='A' or entry14.get()=='A+' or entry14.get()=='B' or entry14.get()=='C' or entry14.get()=='D' or entry14.get()=='E' or entry14.get()=='O' or entry14.get()=='O+' or entry14.get=='A+' or entry14.get()=='B+' or entry14.get()=='C+' or entry14.get()=='D+' or entry14.get()=='E+' and
       entry15.get()=='A' or entry15.get()=='B' or entry15.get()=='C' or entry15.get()=='D' or
       entry15.get()=='E' or entry15.get()=='O' or entry15.get()=='O+' or entry15.get=='A+' or entry15.get()=='B+' or entry15.get()=='C+' or
       entry15.get()=='D+' or entry15.get()=='E+' and
       entry16.get()=='A' or entry16.get()=='B' or entry16.get()=='C' or entry16.get()=='D' or entry16.get()=='E' or entry16.get()=='O' or entry16.get()=='O+' or entry16.get=='A+' or entry16.get()=='B+' or entry16.get()=='C+' or entry16.get()=='D+' or entry16.get()=='E+' and
       entry17.get()=='A' or entry17.get()=='B' or entry17.get()=='C' or entry17.get()=='D' or entry17.get()=='E' or entry17.get()=='O' or entry17.get()=='O+' or entry17.get=='A+' or entry17.get()=='B+' or entry17.get()=='C+' or entry17.get()=='D+' or entry17.get()=='E+' and
       entry18.get()=='A' or entry18.get()=='B' or entry18.get()=='C' or entry18.get()=='D' or entry18.get()=='E' or entry18.get()=='O' or entry18.get()=='O+' or entry18.get=='A+' or entry18.get()=='B+' or entry18.get()=='C+' or entry18.get()=='D+' or entry18.get()=='E+' and
       entry19.get()=='A' or entry19.get()=='B' or entry19.get()=='C' or entry19.get()=='D' or entry19.get()=='E' or entry19.get()=='O' or entry19.get()=='O+' or entry19.get=='A+' or entry19.get()=='B+' or entry19.get()=='C+' or entry19.get()=='D+' or entry19.get()=='E+' ):
            

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
            
               credit1=int(entry20.get())
               credit2=int(entry21.get())
               credit3=int(entry22.get())
               credit4=int(entry23.get())
               credit5=int(entry24.get())
               credit6=int(entry25.get())

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
             entry26.configure(text="Not valid")

####################

## function for CGPA :-

def calculate3():

    
    
    if(entry7.get() and entry8.get() and entry9.get() and entry10.get() and entry11.get() and entry12.get()  and entry20.get() and entry21.get() and entry22.get() and entry23.get() and entry24.get() and entry25.get() !=" "):
    
         try:

             credit1=int(entry7.get())
             credit2=int(entry8.get())
             credit3=int(entry9.get())
             credit4=int(entry10.get())
             credit5=int(entry11.get())
             credit6=int(entry12.get())
             credit7=int(entry20.get())
             credit8=int(entry21.get())
             credit9=int(entry22.get())
             credit10=int(entry23.get())
             credit11=int(entry24.get())
             credit12=int(entry25.get())

             first=entry13['text']
             second=entry26['text']

             credit_all=int(credit1+credit2+credit3+credit4+credit5+credit6+credit7+credit8+credit9+credit10+credit11+credit12)
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
                 
             elif(CGPA<9 or CGPA==9.5 ):
                 entry28.configure(text="Very good keep it up",fg="green")
             elif(CGPA>9.5):
                 entry28.configure(text="Awesome very good",fg="green")
             else:
                 entry28.configure(text="Awesome very good",fg="green")

             if(CGPA <1 or CGPA==1):
                 entry30.configure(text="E",fg="black",bg="red")
             elif(CGPA<2 or CGPA==2):
                 entry30.configure(text="D",fg="red",bg="red")
             elif(CGPA<3 or CGPA==3):
                 entry30.configure(text="D+",fg="red",bg="red")
             elif(CGPA<4 or CGPA==4):
                 entry30.configure(text="C",fg="red")
             elif(CGPA<5 or CGPA==5):
                 entry30.configure(text="C+",fg="blue")
             elif(CGPA<7 or CGPA==7):
                 entry30.configure(text="B",fg="green")
             elif(CGPA<8 or CGPA==8):
                 entry30.configure(text="B+",fg="green")
             elif(CGPA<9 or CGPA==9.5 ):
                 entry30.configure(text="A",fg="green")   
             elif(CGPA>9.5):
                 entry30.configure(text="A+",fg="green")
             else:
                 entry30.configure(text="A+",fg="green")

             
         except:
             entry27.configure(text="invalid")
             
         
    else:
        entry27.configure(text="fill value")
    

############ Functions for caps entry :-

def caps(event):
    sub1.set(sub1.get().upper())
    sub2.set(sub2.get().upper())
    sub3.set(sub3.get().upper())
    sub4.set(sub4.get().upper())
    sub5.set(sub5.get().upper())
    sub6.set(sub6.get().upper())
    sub7.set(sub7.get().upper())
    sub8.set(sub8.get().upper())
    sub9.set(sub9.get().upper())
    sub10.set(sub10.get().upper())
    sub11.set(sub11.get().upper())
    sub12.set(sub12.get().upper())


################ Function for reset :-

def reset():
 
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    entry12.delete(0, 'end')
    entry14.delete(0, 'end')
    entry15.delete(0, 'end')
    entry16.delete(0, 'end')
    entry17.delete(0, 'end')
    entry18.delete(0, 'end')
    entry19.delete(0, 'end')
    entry20.delete(0, 'end')
    entry21.delete(0, 'end')
    entry22.delete(0, 'end')
    entry23.delete(0, 'end')
    entry24.delete(0, 'end')
    entry25.delete(0, 'end')
    name_entry.delete(0, 'end')
    entry26.configure(text=' ')
    entry13.configure(text=' ')
    entry27.configure(text=' ')
    entry28.configure(text=' ')
#########################################################################################################################
########################### Entry variable #######################

### Semester 1 :-

sub1=StringVar()
sub2=StringVar()
sub3=StringVar()
sub4=StringVar()
sub5=StringVar()
sub6=StringVar()

#### Semester 2:-

sub7=StringVar()
sub8=StringVar()
sub9=StringVar()
sub10=StringVar()
sub11=StringVar()
sub12=StringVar()

#################################################################


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

label2=Label(window,text="SEMESTER 1",font=(' Times',15,'bold','italic'),bg='#6262ff',fg='yellow')
label2.pack()
label2.place(x=255,y=160)

label3=Label(window,text="Grade",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label3.pack()
label3.place(x=265,y=220)

label4=Label(window,text="Credit",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label4.pack()
label4.place(x=410,y=220)


label5=Label(window,text="Physics",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label5.pack()
label5.place(x=100,y=260)


label6=Label(window,text="Maths",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label6.pack()
label6.place(x=100,y=300)


label7=Label(window,text="C programming",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label7.pack()
label7.place(x=100,y=340)


label8=Label(window,text="C++",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label8.pack()
label8.place(x=100,y=380)


label9=Label(window,text="Python",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label9.pack()
label9.place(x=100,y=420)

label10=Label(window,text="ECE 132",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label10.pack()
label10.place(x=100,y=460)


# entry for subject and credit

entry1=Entry(window,justify=CENTER,textvariable=sub1)
entry1.bind("<KeyRelease>", caps)
entry1.pack()
entry1.place(x=225,y=260)

entry2=Entry(window,justify=CENTER,textvariable=sub2,)
entry2.bind("<KeyRelease>", caps)
entry2.pack()
entry2.place(x=225,y=300)

entry3=Entry(window,justify=CENTER,textvariable=sub3)
entry3.bind("<KeyRelease>", caps)
entry3.pack()
entry3.place(x=225,y=340)

entry4=Entry(window,justify=CENTER,textvariable=sub4)
entry4.bind("<KeyRelease>", caps)
entry4.pack()
entry4.place(x=225,y=380)


entry5=Entry(window,justify=CENTER,textvariable=sub5)
entry5.bind("<KeyRelease>", caps)
entry5.pack()
entry5.place(x=225,y=420)

entry6=Entry(window,justify=CENTER,textvariable=sub6)
entry6.pack()
entry6.bind("<KeyRelease>", caps)
entry6.place(x=225,y=460)


# Credit

entry7=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry7.pack()
entry7.place(x=400,y=260)

entry8=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry8.pack()
entry8.place(x=400,y=300)

entry9=Entry(window,width=8,font=('Times',11,'bold'),justify=CENTER)
entry9.pack()
entry9.place(x=400,y=340)

entry10=Entry(window,width=8,font=('Times',11,'bold'),justify=CENTER)
entry10.pack()
entry10.place(x=400,y=380)


entry11=Entry(window,width=8,font=('Times',11,'bold'),justify=CENTER)
entry11.pack()
entry11.place(x=400,y=420)

entry12=Entry(window,width=8,font=('Times',11,'bold'),justify=CENTER)
entry12.pack()
entry12.place(x=400,y=460)


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

label4=Label(window,bg="#e2e2e2",height="8",font=('Times',30,'bold'),width="20",borderwidth=2,relief="groove")
label4.pack()
label4.place(x=755,y=200)


label11=Label(window,text="SEMESTER 2",font=(' Times',15,'bold','italic'),bg='light blue',fg="yellow")
label11.pack()
label11.place(x=925,y=160)

label12=Label(window,text="Grade",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label12.pack()
label12.place(x=900,y=220)

label13=Label(window,text="Credit",font=('Times',15,'bold'),bg='#e2e2e2',fg='black')
label13.pack()
label13.place(x=1100,y=220)


label14=Label(window,text="HTML",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label14.pack()
label14.place(x=768,y=260)


label15=Label(window,text="EVS",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label15.pack()
label15.place(x=768,y=300)


label16=Label(window,text="English",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label16.pack()
label16.place(x=768,y=340)


label17=Label(window,text="MEC",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label17.pack()
label17.place(x=768,y=380)


label18=Label(window,text="Eng.drawing",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label18.pack()
label18.place(x=768,y=420)

label19=Label(window,text="CSE211",font=('Times',12,'bold'),bg='#e2e2e2',fg='black')
label19.pack()
label19.place(x=768,y=460)


# entry for subject and credit

entry14=Entry(window,justify=CENTER,textvariable=sub7)
entry14.bind("<KeyRelease>", caps)
entry14.pack()
entry14.place(x=875,y=260)

entry15=Entry(window,justify=CENTER,textvariable=sub8)
entry15.bind("<KeyRelease>", caps)
entry15.pack()
entry15.place(x=875,y=300)

entry16=Entry(window,justify=CENTER,textvariable=sub9)
entry16.bind("<KeyRelease>", caps)
entry16.pack()
entry16.place(x=875,y=340)

entry17=Entry(window,justify=CENTER,textvariable=sub10)
entry17.bind("<KeyRelease>", caps)
entry17.pack()
entry17.place(x=875,y=380)


entry18=Entry(window,justify=CENTER,textvariable=sub11)
entry18.bind("<KeyRelease>", caps)
entry18.pack()
entry18.place(x=875,y=420)

entry19=Entry(window,justify=CENTER,textvariable=sub12)
entry19.bind("<KeyRelease>", caps)
entry19.pack()
entry19.place(x=875,y=460)


# Credit
entry20=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry20.pack()
entry20.place(x=1080,y=260)

entry21=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry21.pack()
entry21.place(x=1080,y=300)

entry22=Entry(window,width=8,font=('Times',11,'bold'),justify=CENTER)
entry22.pack()
entry22.place(x=1080,y=340)

entry23=Entry(window,justify=CENTER,width=8,font=('Times',11,'bold'))
entry23.pack()
entry23.place(x=1080,y=380)


entry24=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry24.pack()
entry24.place(x=1080,y=420)

entry25=Entry(window,width=8,justify=CENTER,font=('Times',11,'bold'))
entry25.pack()
entry25.place(x=1080,y=460)


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

button3=Button(window,text="CGPA",command=calculate3,borderwidth=2,font=('Times',10,'bold'),bg='gray',fg='black')
button3.pack()
button3.place(x=620,y=605)

entry30=Label(window,width=5,font=('Times',14,'bold'))
entry30.pack()
entry30.place(x=735,y=605)

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





####################  USER INFORMATION :-

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
button44.place(x=613,y=350)
    
button45=Button(window,bg="red",text="Reset",command=reset)
button45.pack()
button45.place(x=675,y=350)

########################## Credit reference ##



c1=Label(window,text=" /  3 ",bg="white",font=('times',10,'bold'))
c1.pack()
c1.place(x=470,y=260)

c2=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c2.pack()
c2.place(x=470,y=300)

c3=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c3.pack()
c3.place(x=470,y=340)

c4=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c4.pack()
c4.place(x=470,y=380)

c5=Label(window,text=" /  1 ",bg="white",font=('times',10,'bold'))
c5.pack()
c5.place(x=470,y=420)

c6=Label(window,text=" /  3 ",bg="white",font=('times',10,'bold'))
c6.pack()
c6.place(x=470,y=460)

c7=Label(window,text=" /  1 ",bg="white",font=('times',10,'bold'))
c7.pack()
c7.place(x=1150,y=260)

c8=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c8.pack()
c8.place(x=1150,y=300)

c9=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c9.pack()
c9.place(x=1150,y=340)

c10=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c10.pack()
c10.place(x=1150,y=380)

c11=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c11.pack()
c11.place(x=1150,y=420)

c12=Label(window,text=" /  4 ",bg="white",font=('times',10,'bold'))
c12.pack()
c12.place(x=1150,y=460)

other=Button(window,command=other_m,width=40,text="ENTER-USER-FRIENDLY-ENVIRONMENT",bg="orange")
other.pack()
other.place(x=1025,y=100)

window.mainloop()
