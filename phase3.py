#CS4400 Phase 3
#Group #10
#Shuhao Fan	Section B 	jacksonfan1225@gatech.edu
#Ziwei Miao 	Section A 	zmiao9@gatech.edu
#Li Ding 	Section B	ding88@gatech.edu
from tkinter import*
from tkinter import messagebox
import pymysql
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
        for i in self.cursor:
            self.seniordisc=float(i[0])
            self.childdisc=float(i[1])
        



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
        self.orderhistframe3=Frame(self.myorderhist)
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
        orderhistsql="SELECT order_ID, title, status,num_of_child_ticket,num_of_adult_ticket,num_of_senior_ticket FROM order_information WHERE username=self.username"
            ##Get the discount info from system info
        systeminfosql="SELECT FROM System_info"
        self.cursor.execute(orderhistsql)
        self.orderinfolist=[]
        for i in self.cursor:
            totalcost=float(i[2])*self.childdisc*self.unitprice+float(i[4])*self.seniordisc*self.unitprice+i[3]*self.unitprice
            self.orderinfolist.append([i[0],i[1],i[2],totalcoast])
            totalcost=0
        ##In frame3:
        ##RadioButton
        val=IntVar()
        k=1
        rb=[]
        for i in self.orderinfolist:
            Radiobutton(self.orderhistframe3,variable=val,value=k)
            
            
        
        ##Button in Frame4:
        self.viewdetail=Button(self.frame4,text="View Detail",relief=RAISED)
        self.viewdetail.grid(row=0,column=0)
        
        


    
    
        
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
        
        
        
        

        

