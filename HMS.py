#importing modules
import time
import datetime
import sys
import mysql.connector
from guietta import _, Gui, Quit
from guietta import Gui,B,E,L,HS,VS,HSeparator, VSeparator
from guietta import Yes, No, Ok, Cancel, Quit,_, III

#connection to database
mydb = mysql.connector.connect(host="localhost",user="root",
                               passwd="krishanu",database="hert")
mycursor = mydb.cursor() #cursor is a function that connects

#starting application
d=datetime.date.today()
t=datetime.datetime.now()
dd=d.strftime("%A, %d %B %Y")
tt=t.strftime("%H:%M:%S")
gui = Gui(
        [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],
        [_,"<H5><center><I>©Krishanu©",_,_,_],
        [HSeparator],
        ["<H4><B>DATE:-",dd,_,_,_],["<H4><B>TIME:-",tt,_,_,_],[HSeparator],
        ["<H4><B>LOGIN DETAILS:",_,_,_,_],
        ["<H4>USERNAME:","__uid__",_,_,_],
        ["<H4>PASSWORD:","__psw__",_,_,['LOGIN']],
        ["<H4>RESULT:-","result1",_,_,_],
	[_,_,_,_,Quit ]
)

gui1 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    ["<H4>Enter Choice(1-6):","__ch__",_,_,["SUBMIT"]],
    [_,"<H3><B>1.NEW PATIENT ENTRY",_,_,_],
    [_,"<H3><B>2.SEARCH PATIENT",_,_,_],
    [_,"<H3><B>3.UPDATE PATIENT",_,_,_],
    [_,"<H3><B>4.DELETE PATIENT",_,_,_],
    [_,"<H3><B>5.LIST OF DOCTORS",_,_,_],
    [_,"<H3><B>6.PRINT BILL",_,_,_],
    [_,_,_,_,Quit]
    
    )
gui2 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    [_,"<H2><B>NEW PATIENT ENTRY",_,_,_],
        [HSeparator],
    ["<H4>NAME OF PATIENT:","__name__",_,_,_],
    ["<H4>ENTER AGE OF PATIENT:","__age__",_,_,_],
    ["<H4>ENTER CITY:","__city__",_,_,_],
    ["<H4>ENTER PHONE NO:","__phone__",_,_,_],
    ["<H4>ENTER DISEASE:","__disease__",_,_,["PRESS_OK"]],
    [_,"status",_,_,Quit]
    )

gui3 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    [_,"<H2><B>SEARCH PATIENT",_,_,_],
        [HSeparator],
    
    ["<H4>ENTER REGISTERED PHONE NO:","__c__",_,_,["OK"]],
    [_,"status_",_,_,Quit]
    )

gui4 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    [_,"<H2><B>UPDATE PATIENT DATA",_,_,_],
        [HSeparator],
    
    ["<H4>ENTER REGISTERED PHONE NO:","__c__",_,_,_],
    [_,"<H2><B>WHAT DO YOU WANT TO UPDATE?",_,_,_],
        [HSeparator],
    ["<H4>Enter Choice(1-5):","__ch__",_,_,_],
    ["<H4>Enter Data to Update:","__v__",_,_,["CLICK"]],
    [_,"<H3><B>1.NAME",_,_,_],
    [_,"<H3><B>2.AGE",_,_,_],
    [_,"<H3><B>3.CITY",_,_,_],
    [_,"<H3><B>4.PHONE NO",_,_,_],
    [_,"<H3><B>5.DISEASE",_,_,_],
    
    [_,"<H3><B>*PRESS QUIT",_,_,Quit],[HSeparator],
    [_,"status",_,_,_]
    
    )

gui5 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    [_,"<H2><B>DELETE PATIENT DATA",_,_,_],
        [HSeparator],
    ["<H4>ENTER REGISTERED Ph.No. TO DELETE:","__c__",_,_,["DELETE"]],
    [_,_,_,_,Quit],[HSeparator],
    [_,"status",_,_,_]
    
    )

gui6 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    ["<H4>List of Doctors:",_,_,_,_],
    [_,"<H3><B>1.Dr Anil Kumar  MBBS, MD(Cardiology)8:00 am - 11:00 am",_,_,_],
    [_,"<H3><B>2.Dr Sunil Singh, MBBS, MD(Cardiology)11:00 am -1:00 pm",_,_,_],
    [_,"<H3><B>3.Dr Md. Kamal, MBBS, MD(Surgeryy)11:30 am - 3:00 pm",_,_,_],
    [_,"<H3><B>4.Dr Arup Das, MBBS, MD(Cardiology)4:00 pm - 7:30 am",_,_,_],
    [_,"<H3><B>5.Dr Anil Kumar, MBBS, MD(Cardiology)8:00 am - 11am",_,_,_],
    [HSeparator],
    [_,"<H3><B>*PLEASE CONTACT THE RECEPTION FOR DOCTOR'S APPOINTMENT",_,_,_],
    [_,_,_,_,Quit]
    
    )

gui7 = Gui(
    [_,"<H1><B>HEART BEATZ CARDIAC HOSPITAL","hos.png",_,_],
        [HSeparator],[HSeparator],
    [_,"<H2><B>BILL CALCULATOR",_,_,_],
        [HSeparator],
    ["<H4>ENTER REGISTERED PHONE NO:","__c__","DAYS:","__n__",["GENERATE"]],
    [_,_,_,_,Quit],[HSeparator],
    [_,"status",_,_,_]
    
    )

#####################################################       
with gui.LOGIN:
    if str(gui.uid)=="admin" and str(gui.psw)=="pass":
        gui.result1=str("LOGIN SUCCESSFUL")
        time.sleep(1)
        #gui.result1=gui1
        gui1.run()
    else:
        gui.result1=str("LOADING........")

with gui1.SUBMIT:
    if int(gui1.ch)==1:
        gui2.run()
    elif int(gui1.ch)==2:
        gui3.run()
    elif int(gui1.ch)==3:
        gui4.run()
    elif int(gui1.ch)==4:
        gui5.run()
    elif int(gui1.ch)==5:
        gui6.run()
    elif int(gui1.ch)==6:
        gui7.run()

with gui2.PRESS_OK:
    sqlform = "insert into patients(name,age,city,phno,disease)values(%s,%s,%s,%s,%s)"
    patients = [str(gui2.name),str(gui2.age),str(gui2.city),str(gui2.phone),str(gui2.disease)]
    mycursor.execute(sqlform,patients)
    mydb.commit()
    gui2.status = "NEW PATIENT ADMITTED SUCCESSFULLY"

with gui3.OK:
    cc = str(gui3.c)
    mycursor.execute("select * from patients where phno = '"+cc+"'")
    for x in mycursor:
        gui3.status_ = str("PATIENT DETAILS:--"+str(x))

with gui4.CLICK:
    idd = str(gui4.c)
    if int(gui4.ch)==1:
        name = str(gui4.v)
        sql = "update patients set name= '"+name+"' where phno='"+idd+"'  "
        mycursor.execute(sql)
        mydb.commit()
        gui4.status = "UPDATED SUCCESSFULLY"
    elif int(gui4.ch)==2:
        age = str(gui4.v)
        sql = "update patients set age= '"+age+"' where phno='"+idd+"'  "
        mycursor.execute(sql)
        mydb.commit()
        gui4.status = "UPDATED SUCCESSFULLY"
    elif int(gui4.ch)==3:
        city = str(gui4.v)
        sql = "update patients set city= '"+city+"' where phno='"+idd+"'  "
        mycursor.execute(sql)
        mydb.commit()
        gui4.status = "UPDATED SUCCESSFULLY"
    elif int(gui4.ch)==4:
        phone = str(gui4.v)
        sql = "update patients set phno= '"+phone+"' where phno='"+idd+"'  "
        mycursor.execute(sql)
        mydb.commit()
        gui4.status = "UPDATED SUCCESSFULLY"
    elif int(gui4.ch)==5:
        disease = str(gui4.v)
        sql = "update patients set disease= '"+disease+"' where phno='"+idd+"'  "
        mycursor.execute(sql)
        mydb.commit()
        gui4.status = "UPDATED SUCCESSFULLY"

with gui5.DELETE:
    try:
        idd = str(gui5.c)
        sql = "delete from patients where phno= '"+idd+"' "
        mycursor.execute(sql)
        mydb.commit()
        gui5.status = str("Loading...")
    except:
        gui5.status = str("does not exist. try again")

with gui7.GENERATE:
    cc = str(gui7.c)
    nn = int(gui7.n)
    mycursor.execute("select * from patients where phno = '"+cc+"'")
    for x in mycursor:
        fee = 500
        T = fee*nn
        gui7.status =str("PATIENT DATA:--\n"+str(x)+"\nRATE=500\nTOTAL BILL AMOUNT ="
            +str(T)+"\tfor Days:"+str(nn)+"\n\t\tBill Generated!")
        f = open("bill.txt","w")
        f.write(gui7.status)
        f.close()

gui.run()



