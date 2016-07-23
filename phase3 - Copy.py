#CS4400 Phase 3
#Group #10
#Shuhao Fan	Section B 	jacksonfan1225@gatech.edu
#Ziwei Miao 	Section A 	zmiao9@gatech.edu
#Li Ding 	Section B	ding88@gatech.edu
from tkinter import*
from tkinter import messagebox
import pymysql
from datetime import datetime
class cs4400:
    def __init__(self,win):
        self.window=win
        ##login window
        ##"login" frame
        self.frame1=Frame(self.window)
        self.frame1.grid(row=0,column=0)
        ##"username and password" frame
        self.frame2=Frame(self.window)
        self.frame2.grid(row=1,column=0)
        ##two buttons: login, register frame
        self.frame3=Frame(self.window)
        self.frame3.grid(row=2,column=0)
        ##In Frame1, the login label
        Label(self.frame1,text="Login",font = "Helvetica 16 bold italic",fg = "Orange").grid(row=0,column=0)
        Label(self.frame2,text="Username").grid(row=0,column=0)
        Label(self.frame2,text="Password" ).grid(row=1,column=0)
        ##In Frame2, the two entires
        self.usernameinput=Entry(self.frame2, width=30,state="normal")
        self.usernameinput.grid(row=0,column=1)
        self.passwordinput=Entry(self.frame2,width=30,state="normal")
        self.passwordinput.grid(row=1,column=1)
        ##In Frame3, the two buttons
        self.loginbutton=Button(self.frame3,text="login")
        self.loginbutton.grid(row=0,column=0)
        self.registerbutton=Button(self.frame3,text="Register")
        self.registerbutton.grid(row=0,column=1)
        ##Window: New User Registration
        ##setup unitmovie price
        self.unitprice=10
        

    ##Movie playing list
    def playinglist(self):
        ##connect to database
        self.playdb=self.connect()
        self.playcursor=self.playdb.cursor()
        ##Create another window to display the Movies NOW
        ##after login as a customer
        self.window.withdraw()
        self.playlist.Toplevel()
    def Me(self):
        ##Me Window
        self.t2.withdraw()
        self.me.Toplevel()
        ##underlined labels
        Label(self.me,text="ME",font = "Helvetica 16 bold italic",fg = "Orange").grid(row=0,column=0)
        self.orderhist=Label(self.me,text="My Order History",underline=n,fg="blue")
        self.orderhist.grid(row=1,column=0)
        self.mypayinfo=Label(self.me,text="My Payment Information",underline=n,fg="blue")
        self.mypayinfo.grid(row=2,column=0)
        self.mypreferthea=Label(self.me,text="My Preferrred Theater",underline=n,fg="blue")
        self.mypreferthea.grid(row=3,column=0)
        self.meback=Button(self.me,text="Back",relief=RAISED)
        self.meback.grid(row=4,column=0)

    def get_systeminfo(self):
        systeminfosql="SELECT senior_discount,child_discount FROM System_info"
        self.cursor.execute(systeminfosql)
        self.seniordisc=float(self.cursor.fetchone()[0])
        self.childdisc=float(self.cursor.fetchone()[1])
        



    def Myorderhistory():
        self.me.withdraw()
        ##from me to my orderhistory window
        self.myorderhist.Toplevel()
        ##orderhistory title
        ##frame1: orderhistory 
        self.orderhistframe1=Frame(self.myorderhist)
        self.orderhistframe1.grid(row=0,column=0)
        ##frame2: order ID Search
        self.orderhistframe2=Frame(self.myorderhist)
        self.orderhistframe2.grid(row=1,column=0)
        ##frame3: retrieve from db, the orderhistory
        self.orderhistframe3=Frame(self.myorderhist,relief="SOLID")
        self.orderhistframe3.grid(row=2,column=0)
        ##frame4: view detail button
        self.orderhistframe4=Frame(self.myorderhist)
        self.orderhistframe4.grid(row=3,column=0)
     
        ##Order History
        Label(self.orderhistframe1,text="Order History",font = "Helvetica 16 bold italic",fg = "Orange")
        Label(self.ordderhistframe2,text="Order ID").grid(row=0,columu=0)
        ##Entry to search order
        self.searchentry=Entry(self.orderhistframe2,width=30,state="normal")
        self.searchentry.grid(row=0,column=1)
        self.searchbutton=Button(self.orderhistframe2,text="Search")
        self.searchbutton.grid(row=0,column=2)
        ##retrieve the order information
        orderhistsql="SELECT order_ID, title, status,num_of_child_ticket,num_of_adult_ticket,num_of_senior_ticket FROM order_information WHERE username=%s"
        self.cursor.execute(orderhistsql,self.username)
        ##create a orderinfolist which stores a list of lists
        self.orderinfolist=[]
        for i in self.cursor:
            ##Use the child disc and senior disc in def Get_Systeminfo
            ##calculate the total cost for ith order
            totalcost=float(i[2])*self.childdisc*self.unitprice+float(i[4])*self.seniordisc*self.unitprice+float(i[3])*self.unitprice
            ##append i orderinfo into orderinfolist 
            self.orderinfolist.append([i[0],i[1],i[2],'$'+str(totalcost)])
            totalcost=0
        ##In frame3:
        ##RadioButton
        self.selectval=IntVar()
        ##set a default value for select radio button
        self.selectval.set(0)
        k=1
        rb=[]
        for i in self.orderinfolist:
            self.orderselect=Radiobutton(self.orderhistframe3,text=i,variable=val,value=k)
            self.orderselect.grid(row=k,column=0)
            self.valuelist.append(k)
            k+=1
        ##Button in Frame4:
        self.viewdetail=Button(self.frame4,text="View Detail",relief=RAISED,command=self.view_detail)
        self.viewdetail.grid(row=0,column=0)
###########################VIEW ORDER DETAIL/CANCEL ORDER####################################
    def view_detail(self):
        ##check if the user selected the specific order
        ##get the value of the radiobutton
        self.selectvalcont=self.selectval.get()
        if self.selectval.get==0:
            ##which means the user didn't select any order or this is no order history displayed
            messagebox.showerror("Excuse Me!","You have no order selected!")
        else:
            ##Create a window of Order Detail
            self.myorderhist.withdraw()
            self.viewdetail=Toplevel()
            ##setup frame1
            viewdetailf1=Frame(self.viewdetail)
            viewdetailf1.grid(row=0,column=0)
            ##setup frame2
            viewdetailf2=Frame(self.viewdetail)
            viewdetailf2.grid(row=1,column=0)
            ##setup frame3
            viewdetailf3=Frame(self.viewdetail)
            viewdetailf3.grid(row=2,column=0)
            ##add title Order Detail to frame1
            Label(self.viewdetailf1,text="Order Detail")
            ## separate frame2 in to two small frames
            viewdetailf21=Frame(self.viewdetailf2)
            viewdetailf21.grid(row=0,column=0)
            viewdetailf22=Frame(self.viewdetailf2)
            viewdetailf22.grid(row=0,column=1)
            ##for the first frame in Frame2
            ##the title of the movie: match the value of the radiobutton to the db 
            self.ordermovie=self.orderinfolist[self.selectvalcont-1][1]
            self.orderdetailid=self.orderinfolist[self.selectvalcont-1][0]
            ## get the movie information from the database
            moviedetailsql="SELECT rate,length FROM Movie WHERE title=%s"
            self.cursor.execute(moviedetailsql,selfordermovie)
            ##get the level of the movie 
            self.orderdetailmrate=self.cursor()[0]
            ##get the length of the movie
            self.orderdetailmlength=self.cursor()[1]
            ##Label the length and the rate of the movie to small frame1 in Frame2
            Label(viewdetailf21,text=self.ordermovie,font = "Helvetica 12 bold italic").grid(row=0,column=0)
            Label(viewdetailf21,text=self.orderdetailmrate).grid(row=1,column=0)
            Label(viewdetailf21,text=self.orderdetailmlength).grid(row=2,column=0)
            ##get the ticket time of the specific order
            tickettimesql=" select s.show_time from Order_info as o left join Theater as t on o.theater_ID = o.theater_ID left join Movie as m on m.title = o.title left join Show_time  as s on s.theater_ID = o.theater_ID and m.title = o.title where o.order_id = %s"
            self.cursor.execute(tickettimesql,self.orderdetailid)
            self.orderdetailtime=self.cursor()
            Label(viewdetailf21,text=self.orderdetailtime).grid(row=3,column=0)
            ##the theater information from the specific order
            theatersql="select name,state,city,street,zip,num_of_adult_ticket,num_of_senior_ticket,num_of_child_ticket, from Order_info as o left join Theater    as t on o.theater_ID = o.theater_ID left join Movie as m on m.title = o.title left join Show_time  as s on s.theater_ID = o.theater_ID and m.title = o.title where o.order_id = %s"
            self.cursor.execute(theatersql,self.orderdetailid)
            self.ordertheainfo=self.cursor()
            ##Add the label to the f22 
            Label(viewdetailf22,text=self.cursor[0]).grid(row=0,column=0)
            Label(viewdetailf22,text=self.cursor[3]).grid(row=1,column=0)
            Label(viewdetailf22,text=self.cursor[2]+", "+self.cursor[1]+" "+self.cursor[4])
            if self.cursor[5]!="0":
                ##calculate the adult cost
                adultcost=int(self.cursor[5])*self.unitprice
                Label(viewdetailf22,text=self.cursor[5]+" adult ticket: $"+str(adultcost)).grid(row=2,column=0)
            if self.cursor[6]!="0":
                ##calculate the senior cost
                seniorcost=int(self.cursor[6])*self.unitprice*self.seniordisc
                Label(viewdetailf22,text=self.cursor[6]+" senior ticket: $"+str(seniorcost)).grid(row=3,column=0)
            if self.cursor[7]!="0":
                childcost=int(self.cursor[7])*self.unitprice*self.childdisc
                Label(viewdetailf22,text=self.cursor[7]+" child ticket: $" +str(childcost)).grid(row=4,column=0)
            
            ##Frame3: two buttons
            self.cancelthisorder=Button(self.viewdetailf3,text="Cancel This Order",relief=RAISED)
            self.cancelthisorder.grid(row=0,column=0,sticky=E)
            self.backorderinfo=Button(Self.viewdetailf3,text="Back",relief=RAISED,command=self.backorderinfo)
            self.backorderinfo.grid(row=0,column=1,sticky=E)
    def backorderinfo(self):
        ##after the user select "back", go back to the orderinformation page
        self.viewdetail.Withdraw()
        self.myorderhist=Toplevel()

    def cancelorder(self):
        ##get the current datetime
        timenow=str(datetime.now())
        
        cancelordersql="UPDATE Order_info SET status='Canceled' WHERE order_id=%s"
        
            
        
        


    
    
        
    def Movie(self):
        self.t2.withdraw()
        self.movie.Toplevel()
        ##create two frames
        self.movieframe1=Frame(self.movie)
        self.movieframe1.grid(row=0,column=0)
        self.movieframe2=Frame(self.movie)
        self.movieframe2.grid(row=0,column=1)
        ##the left frame
        ##the right frame
        ##overview,movie review, buy ticket
        self.overview=Button(self.movieframe1,text="Overview",relief=RAISED)
        self.overview.grid(row=0,column=0)
        self.moviereview=Button(self.movieframe1,text="Movie Review",relief=RAISED)
        self.moviereview.gird(row=1,column=0)
        self.buyticket=Button(self.movieframe1,text="Buy Ticket",relief=RAISED)
        self.buyticket.grid(row=2,column=0)
    def mypaymentinfo(self):
        self.me.withdraw()
        self.
        
        
        
        

        

