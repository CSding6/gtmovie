from tkinter import*
#from tkinter import messagebox
import urllib.request
import base64
import pymysql
import os
from datetime import date
import datetime

class cs4400:
    def __init__(self,win):
        self.db = pymysql.connect(host = "us-cdbr-azure-east-c.cloudapp.net",
                                  passwd = "c5f204a3",
                                  user = "bf47b538bf3d9a",
                                  db= "acsm_c3d83ab4ffcf1d9")
        self.cursor = self.db.cursor()
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
        self.passwordinput=Entry(self.frame2,width=30,state="normal", show = "*")
        self.passwordinput.grid(row=1,column=1)
        ##In Frame3, the two buttons
        self.loginbutton=Button(self.frame3,text="login", command = self.logincheck)
        self.loginbutton.grid(row=0,column=0)
        self.registerbutton=Button(self.frame3,text="Register", command = self.register)
        self.registerbutton.grid(row=0,column=1)
        ##Window: New User Registration
        # Page two register
        self.t1 = Toplevel()
        self.t1.title("New User Registration")
        self.t1.configure(background = "white")
        self.t1.withdraw();
        #title
        self.lt11 = Label(self.t1, text = "New User Registration", font = ("Helvetica",20), fg = "Orange")
        self.lt11.grid(row = 0, column = 0, columnspan = 2, sticky = W+E)
        #frame 1
        self.ft11 = Frame(self.t1)
        self.ft11.grid(row = 1, column = 0)
        #Username
        self.lt12 = Label(self.ft11,text = "Username" )
        self.lt12.grid(row = 0, column = 0, sticky = W+E, padx= 5, pady = 5)
        self.et12 = Entry(self.ft11, width = 30)
        self.et12.grid(row = 0, column = 1)
        #Email Address
        self.lt13 = Label(self.ft11,text = "Email Adress")
        self.lt13.grid(row = 1, column = 0, sticky = W+E, padx= 5, pady = 5)
        self.et13 = Entry(self.ft11, width = 30)
        self.et13.grid(row = 1, column = 1)
        #Password
        self.lt14 = Label(self.ft11, text = "Password")
        self.lt14.grid(row = 2, column = 0,sticky = W+E, padx= 5, pady = 5)
        self.et14 = Entry(self.ft11, width = 30, show= "*")
        self.et14.grid(row = 2, column = 1)
        #Confirm password
        self.lt15 = Label(self.ft11, text = "Confirm Password")
        self.lt15.grid(row = 3, column = 0, sticky = W+E, padx= 5, pady = 5)
        self.et15 = Entry(self.ft11, width = 30, show= "*")
        self.et15.grid(row = 3, column = 1)
        # Manage Password
        self.lt16 = Label(self.ft11, text = "Manager Password")
        self.lt16.grid(row = 4, column = 0, sticky = W+E, padx = 5, pady = 5)
        self.et13 = Entry(self.ft11, width = 30)
        self.et13.grid(row = 4, column = 1)
        # Create button
        self.ft12 = Frame(self.t1)
        self.ft12.grid(row = 2, column = 0, columnspan = 5, sticky = W+E)
        self.bt11 = Button(self.ft12, text = "Create", command = self.create)
        self.bt11.grid(row = 0, column = 0, sticky = W)
        self.bt12 = Button(self.ft12, text = "Cancel", command = self.backtologgin)
        self.bt12.grid(row = 0, column =1, sticky = E)
        
    def nowPlaying(self):
        #Nowplaying Page
        self.window.withdraw()
        self.nowplaying = Toplevel()
        self.nowplaying.title("Now Playing")
        self.nowplaying.configure(background = "white")
        self.nowplayingframe = Frame(self.nowplaying)
        self.nowplayingframe.grid(row = 0, column = 0)
        #Image
        self.photo1 = PhotoImage(file = "/Users/Jacksonfan/Desktop/Test/user.gif")
        self.image1 = Button(self.nowplayingframe, image = self.photo1,command = self.Me)
        self.image1.grid(row = 0, column = 0, sticky = W)
        self.nowplayinglabel1 = Label(self.nowplayingframe, text = "Now Playing", font = "Helvetica 20 bold italic", fg = "Orange")
        self.nowplayinglabel1.grid(row =0, column = 1,columnspan = 2, sticky = W+N+S+E)
        self.cursor.execute("SELECT title,EXTRACT(YEAR FROM release_date) as year, EXTRACT(MONTH FROM release_date) as month, EXTRACT(DAY FROM release_date) as day FROM movie")
        movie = self.cursor.fetchall()
        self.movietitle = []
        now = date.today()
        self.variable = IntVar()
        for i in movie:
            d1 = date(i[1],i[2],i[3])
            delta = d1 - now
            if (delta.days > -15):
                self.movietitle.append(i[0])
        print(self.movietitle)
        for i in self.movietitle[::2]:
            self.playingmovie = Radiobutton(self.nowplayingframe, text = i,variable = self.variable, value = self.movietitle.index(i), font = "Helvetica 20 bold italic", command = self.showmovie, indicatoron = 0, width = 15)
            self.playingmovie.grid(row = self.movietitle.index(i)+1, column = 1, columnspan = 1)
            if(self.movietitle.index(i)+1 < len(self.movietitle)):
                self.playingmovie2 = Radiobutton(self.nowplayingframe, text = self.movietitle[self.movietitle.index(i)+1],variable = self.variable, value = self.movietitle.index(i)+1,font = "Helvetica 20 bold italic", indicatoron = 0, command = self.showmovie, width = 15)
                self.playingmovie2.grid(row = self.movietitle.index(i)+1, column =2, columnspan = 1)
                self.playingmovie2.config(highlightbackground="Black")
            else:
                return;

    def register(self):
        self.window.withdraw()
        self.t1.update()
        self.t1.deiconify()
        
    def logincheck(self):
        userName = self.usernameinput.get()
        password = self.passwordinput.get()
        loginCheck = "SELECT username FROM customer WHERE username = %s AND password = %s"
        count = self.cursor.execute(loginCheck, (userName, password))
        if count > 0:
            messagebox.showinfo("Congratulations", "You have successfully logged in")
            self.nowPlaying()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
            return None

    def create(self):
        self.userName = self.et12.get()
        password = self.et14.get()
        email_address = self.et13.get()
        confirmpassword = self.et15.get()
        if(len(self.userName) == 0):
            messagebox.showerror("Error", "Please enter a Username")
            return None
        elif(password != confirmpassword) or (len(password) == 0):
            messagebox.showerror("Error", "Invalid password")
            return None
        else:
            reptitionCheck = "SELECT username FROM customer WHERE username = %s"
            count = self.cursor.execute(reptitionCheck, self.userName)
            if count > 0:
                messagebox.showinfo("Username Taken", "Please select a new Username")
            else:
                insert = "INSERT INTO customer (username, password, email) VALUES (%s,%s, %s)"
                self.cursor.execute(insert, (self.userName, password, email_address))
                messagebox.showinfo("Congratulations","You have successfully registered")
                self.t1.withdraw()
                self.window.update()
                self.window.deiconify()
            self.db.commit()
    def backtomain(self):
        self.me.withdraw()
        self.nowplaying.update()
        self.nowplaying.deiconify()
        
    
    def Me(self):
        ##Me Window
        self.window.withdraw()
        self.nowplaying.withdraw()
        self.me = Toplevel()
        self.me.title("Me")
        ##underlined labels
        Label(self.me,text="Me",font = "Helvetica 16 bold italic",fg = "Orange").grid(row=0,column=0)
        self.orderhist=Label(self.me,text="My Order History",underline=0,fg="blue")
        self.orderhist.grid(row=1,column=0)
        self.mypayinfo=Label(self.me,text="My Payment Information",underline=0,fg="blue")
        self.mypayinfo.grid(row=2,column=0)
        self.mypreferthea=Label(self.me,text="My Preferrred Theater",underline=0,fg="blue")
        self.mypreferthea.grid(row=3,column=0)
        self.meback=Button(self.me,text="Back",relief=RAISED, command = self.backtomain)
        self.meback.grid(row=4,column=0)
        
    def showmovie(self):
        print(self.variable.get())
        self.nowplaying.withdraw()
        self.movieshow = Toplevel()
        self.movieshow.title("Movie")
        #topside part
        self.movieshowframe0 = Frame(self.movieshow)
        self.movieshowframe0.grid(row = 0, column = 0, columnspan = 1)
        movietitle = Label(self.movieshowframe0, text = self.movietitle[self.variable.get()], font = "Helvetica 30 bold italic", fg = "Orange")
        movietitle.grid(row = 0, column = 0, sticky = W)
        print(self.movietitle[self.variable.get()])
        #leftside part
        self.movieshowframe = Frame(self.movieshow, bg = "black")
        self.movieshowframe.grid(row = 1, column = 0, sticky = W)
        released = Label(self.movieshowframe, text = "Released", font ="Times 20 italic", fg = "white", bg = "black" )
        released.grid(row = 0, column = 0,sticky = W+E)
        releasedatesql = "SELECT release_date FROM movie WHERE title = %s"
        self.cursor.execute(releasedatesql, self.movietitle[self.variable.get()])
        releasedate = self.cursor.fetchall()
        releasedatelabel = Label(self.movieshowframe, text = releasedate, font = "Helvetica 30 bold",fg = "white", bg = "black")
        releasedatelabel.grid(row =1, column = 0, sticky =W+E )
        generalinfosql = "SELECT rate, length, genre FROM movie WHERE title = %s"
        self.cursor.execute(generalinfosql, self.movietitle[self.variable.get()])
        generalinfo = self.cursor.fetchone()
        print(generalinfo)
        rating = generalinfo[0]
        if(int(generalinfo[1])% 60 < 10):
            length= str(int(generalinfo[1])//60) + ":" + "0"+str(int(generalinfo[1]) % 60) + ":00"
        else:
            length= str(int(generalinfo[1])//60) + ":" +str(int(generalinfo[1]) % 60) + ":00"
        genre = generalinfo[2]
        ratelengthlabel = Label(self.movieshowframe, text = str(rating) +", " + length,font ="Times 20 italic", fg = "white", bg = "black")
        ratelengthlabel.grid(row = 2, column = 0, sticky = W+E)
        genrelabel = Label(self.movieshowframe, text =genre, fg = "white",font ="Times 20 italic", bg = "black")
        genrelabel.grid(row = 3, column = 0, sticky = W+E)
        fanrating = "SELECT rating, COUNT(*) FROM review WHERE title = %s GROUP BY title"
        self.cursor.execute(fanrating, self.movietitle[self.variable.get()] )
        self.rating_info = self.cursor.fetchone()
        if(self.rating_info == None):
            pass
        else:
            self.star_rating = self.rating_info[0]
            self.fan_number = self.rating_info[1]
        ratinglabel = Label(self.movieshowframe, text = "Rating: " + str(self.star_rating) + "/5.0", fg = "white", font = "Times 20 italic", bg = "black")
        ratinglabel.grid(row = 4, column = 0, sticky = W+E)
        fannumberlabel = Label(self.movieshowframe, text = self.fan_number, fg = "white", font = "Times 30 italic", bg = "black")
        fannumberlabel.grid(row = 5, column = 0, sticky = W+E)
        
        
        
        
        #rightside part
        self.movieshowframe2 = Frame(self.movieshow)
        self.movieshowframe2.grid(row = 1, column =1)
        self.variableshowmovie = IntVar()
        overviewradiobutton = Radiobutton(self.movieshowframe2, text ="Overview", variable = self.variableshowmovie, font = "Helvetica 20 bold",value= 1, command = self.overview)
        overviewradiobutton.grid(row = 0, column = 0, sticky = W)
        moviereviewradiobutton = Radiobutton(self.movieshowframe2, text = "Movie Review", variable = self.variableshowmovie, font = "Helvetica 20 bold", value = 2, command = self.moviereview)
        moviereviewradiobutton.grid(row = 1, column = 0, sticky = W)
        buyticketradiobutton = Radiobutton(self.movieshowframe2, text = "Buy Ticket", variable = self.variableshowmovie, font = "Helvetica 20 bold italic", value = 3, command = self.buyticket)
        buyticketradiobutton.grid(row = 2, column = 0,sticky = W)
        
    def backtologgin(self):
        self.t1.withdraw()
        self.window.update()
        self.window.deiconify()


    def buyticket(self):
        self.movieshow.withdraw()

    def overview(self):

        self.movieshow.withdraw()
        self.overview = Toplevel()
        self.overview.title("Overview")
        titleframe = Frame(self.overview)
        titleframe.grid(row = 0, column = 0)
        movietitle = Label(titleframe, text = self.movietitle[self.variable.get()], fg = "Orange", font = "Helvetica 30 bold")
        movietitle.grid(row = 0, column = 0)
        synopsisstatement = "SELECT synopsis FROM movie WHERE title = %s LIMIT 5"
        self.cursor.execute(synopsisstatement, self.movietitle[self.variable.get()])
        synopsistxt = self.cursor.fetchall()
        print(synopsistxt)
        synopFrame = Frame(self.overview)
        synopFrame.grid(row = 1, column = 0)
        synoptitle = Label(synopFrame, text = "Synopsis", font = "Helvetica 20 bold")
        synoptitle.grid(row = 0, column = 0)
        synopLabel = Label(synopFrame, text = synopsistxt)
        synopLabel.grid(row =1, column = 0, columnspan = 3)
        castframe = Frame(self.overview)
        castframe.grid(row = 2, column = 0)
        castselect = "SELECT cast FROM movie WHERE title = %s"
        self.cursor.execute(castselect, self.movietitle[self.variable.get()])
        castname = self.cursor.fetchall()
        castLabel = Label(castframe, text = castname, fg = "Blue", font = "Helvetica 15 bold")
        castLabel.grid(row = 0, column = 0)
        back = Button(castframe, text = "Back", command = self.backtoshowmovie)
        back.grid(row = 1, column = 0)
        
    def backtoshowmovie(self):
        self.overview.withdraw()
        self.movieshow.update()
        self.movieshow.deiconify()
    def backtoshowmovie2(self):
        self.moviereview.withdraw()
        self.movieshow.update()
        self.movieshow.deiconify()

    def moviereview(self):
        self.movieshow.withdraw()
        self.moviereview = Toplevel()
 #       scrollbar = Scrollbar(self.moviereview)
#        scrollbar.pack(side=RIGHT, fill=Y)
        self.moviereview.title("Review")
        titleframe = Frame(self.moviereview)
        titleframe.grid(row = 0, column = 0)
        title = Label(titleframe, text = self.movietitle[self.variable.get()], fg = "Orange", font = "Helvetica 30 bold")
        title.grid(row = 0, column = 0)
        avgrating = Label(titleframe, text = str(self.star_rating) + "/5.0", font = "Helvetica 20")
        avgrating.grid(row = 0, column = 1)
        givereview = Frame(self.moviereview)
        givereview.grid(row = 1, column = 0)
        give = Button(givereview, text = "Give Review", width = 50, borderwidth = 1, command = self.givereview, highlightbackground = "Black")
        give.pack()
        main = Frame(self.moviereview)
        main.grid(row = 2, column = 0)
        review = "SELECT username, rating, comment FROM review WHERE title = %s"
        self.cursor.execute(review,  self.movietitle[self.variable.get()])
        reviewdata = self.cursor.fetchall()
        print(reviewdata)
        for i in range(len(reviewdata)):
            l = Label(main, text = "User: " + str(reviewdata[i][0]) + "\n" + "Rating: " + str(reviewdata[i][1]) + "\n" + "Comment: " + str(reviewdata[i][2]) + "\n", anchor = W, justify = LEFT,
                      width = 50, borderwidth = 2, highlightbackground = "Black")
            l.grid(row = i, column = 0, padx = 0.5, pady = 0.5)
        backframe = Frame(self.moviereview)
        backframe.grid(row = 3, column = 0)
        back = Button(backframe, text = "Back", width = 10, command = self.backtoshowmovie2, highlightbackground = "Black")
        back.grid(row = 0, column = 0, sticky = W)
                

    def givereview(self):
        self.moviereview.withdraw()
        self.giverevieew = Toplevel()
        self.givereview.title("")
        

        
        

#maincode
win = Tk()
win.resizable(width = False, height = False)
win.geometry("600x600")
run  = cs4400(win)
win.mainloop()


