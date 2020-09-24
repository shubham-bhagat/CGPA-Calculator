from tkinter import *

def final():
	import manual.py

window=Toplevel()
window.title("LOGIN PAGE") #set a title of the Window
window.geometry('1360x1380')
frame1=Frame(window)
frame1.pack()

#images:
admin_logo=PhotoImage(file="sdh.gif")


# Adding label:

icon=PhotoImage(file="ezgif.com-gif-maker.gif")
label1=Label(frame1,image=icon)
label1.pack(anchor=CENTER)


#Adding label2 for backgrond:-
background=PhotoImage(file="aaaa.gif")
label2=Label(frame1,image=background,height="600")
label2.pack()


#Adding 3rd Label:
##
label3=Label(frame1,text="Click On Image To Enter",font=('Times',30,'bold'))
label3.pack()
label3.place(x=380,y=195)

label5=Label(window,text="INFORMATION",font=('Times',14,'bold'),fg='red')
label5.pack()
label5.place(x=950,y=490)

## Adding information box:-

info=Label(window,font=('time',9,'bold'),fg='blue',width=45,height=12)
info.pack()
info.place(x=950,y=510)
info.configure(text=" * By clicking in this image you will \nenter in the manual menu.In the top there is\n USER-FRIENDLY-ENVIRONMENT by clicking on this \nyou will enter user friendly menu.\nThere is submit button this will \nsubmit your record to database")  


# Adding button for Administraror:-

button1=Button(frame1,image=admin_logo,command=final,width=190,height=250)

button1.pack()
button1.place(x=500,y=250)


window.mainloop()







