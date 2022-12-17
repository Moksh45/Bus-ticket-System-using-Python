from tkinter import *
from tkinter import messagebox
import sqlite3
with sqlite3.connect('Bus_Booking.db') as db:
    cur = db.cursor()

class Bus_Ticket:
    def home_Page():
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8)
        Label(root , text="Name : Moksh Gupta",font = "Arial 14 bold",fg = "blue2").grid(row = 2 , column = 0,pady = 35)
        Label(root , text="Er : 211B185",font = "Arial 14 bold",fg = "blue2").grid(row = 3 , column = 0,pady = 20)
        Label(root , text="Mobile : 9451744774",font = "Arial 14 bold",fg = "blue2").grid(row = 4 , column = 0,pady = 20)

        Label(root , text="Submitted To : Dr. Mahesh Kumar",font = "Arial 20 bold",fg = "red",bg="sky blue").grid(row = 5, column = 0,pady = 35)
        Label(root , text="Project Based Learning",font = "Arial 14 bold",fg = "red").grid(row = 6, column = 0)

        def fun(e=0):
            root.destroy()
            a.second_Screen()
        root.bind('<KeyPress>',fun)
        root.mainloop()

    def second_Screen():
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)
        def first_screen():
            root.destroy()
            a.Journey_details()
        def second_screen():
            root.destroy()
            a.check_your_booking()
        def third_screen():
            root.destroy()
            a.four_button()
        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=40)
        frame2=Frame(root)
        frame2.grid(row=2,column = 0, columnspan =10)
        Button (frame2, text= "Seat Booking",command=first_screen,bg="spring Green2",font = "Arial 15 bold").grid(row = 2 , column = 0,pady = 20,padx=20)
        Button (frame2, text= "Check Booked Seat",command=second_screen,bg="Green3",font = "Arial 15 bold").grid(row = 2 , column = 1,padx=20)
        Button (frame2, text= "Add Bus Details",command=third_screen,bg="Green4",font = "Arial 15 bold").grid(row = 2 , column = 2,padx=20)
        Label(frame2, text = "For Admin Only",fg="Red",font = "Arial 10 bold").grid(row = 3, column = 2)
        root.mainloop()

    def Journey_details():
        cur.execute("create table IF NOT EXISTS user_info(User_name varchar(100),Gender varchar(100),No_Of_Seats varchar(200),Mobile_No varchar(20),age Varchar(3),bID varchar(100),refer INTEGER PRIMARY KEY AUTOINCREMENT);")
    
        def show_bus():
            def PTB():
                def box():
                    newname = userName.get()
                    newgender = bus_type.get()
                    newSeat_Number = Seat_Number.get()
                    newMobile_Number = Mobile_Number.get()
                    newAge = Age.get()
                    newratio=radio.get()
                    # if newname =="" or newSeat_Number == "" or newMobile_Number == "" or newAge == "" or int(newAge)>0 or int(newAge)<100:
                    #     messagebox.showinfo("Error", "Some information is missing in User Details or age invalid")
                    if int(len(Mobile_Number.get()))<10 :
                        messagebox.showinfo("info","Number Count Less then 10")
                    else:
                        cur.execute("select Seat_available from add_bus_running_details where b_id ='" + newratio + "' ")
                        number =cur.fetchone()
                        total = str(int(number[0])-int(newSeat_Number))
                        if int(total) < 0:
                            messagebox.showinfo("Error","Seat Not Available")
                        else:
                            cur.execute("update add_bus_running_details set Seat_available  = '" + total + "' where b_id = '" + newratio + "'")
                            cur.execute("INSERT INTO user_info(User_name ,Gender ,No_Of_Seats ,Mobile_No ,age, bID)VALUES(?,?,?,?,?,?)",(newname,newgender,newSeat_Number,newMobile_Number,newAge,newratio))
                            db.commit()
                            cur.execute("select Fare_rs from add_bus_details where Bus_id = '" + radio.get() + "'")
                            check = cur.fetchone()
                            sum = str(int(newSeat_Number)*int(check[0]))
                            sum = "Your Seat is SuccessFully Booked Your Fare is " + sum
                            # print(sum)
                            choose = messagebox.askyesno("Info" ,sum)
                            if choose:
                                root.destroy()
                                a.bus_ticket(newMobile_Number,radio.get(),newJourney)

                Label(frame4 , text="Fill Passenger Detail To Book The Bus Ticket",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 7, column = 5,pady=20)
                frame5=Frame(frame4)
                frame5.grid(row=8,column = 0, columnspan =10)
                Label(frame5, text = "Name",font = "5").grid(row = 8, column = 0,padx=20)
                userName = Entry(frame5)
                userName.grid(row =8, column = 1,pady=10)
                Label(frame5, text = "Gender",font = "5").grid(row = 8, column = 2)
                bus_type = StringVar()
                bus_type.set('Male')
                option = ["Male","Female" , "Third Gender"]
                Gender_Menu=OptionMenu(frame5,bus_type,*option)
                Gender_Menu.grid(row = 8, column = 3)
                Label(frame5, text = "No of Seats",font = "5").grid(row =8, column = 4)
                Seat_Number = Entry(frame5)
                Seat_Number.grid(row = 8, column = 5)
                Label(frame5, text = "Mobile No",font = "5").grid(row = 8, column = 6)
                Mobile_Number = Entry(frame5)
                Mobile_Number.grid(row = 8, column = 7)
                
                Label(frame5, text = "Age",font = "5").grid(row = 8, column = 8)
                Age = Entry(frame5)
                Age.grid(row = 8, column = 9)
                Button(frame5,command=box,text="Book Seat",font = "8",bg="SpringGreen2").grid(row = 8, column = 10) 

            newTo = To.get()
            newFrom = From.get()
            newJourney = Journey.get()
    
            cur.execute("select bus_id,name,bus_type,seat_available,fare_rs from operator ,add_bus_route_details , add_bus_running_details ,add_bus_details where station_from='" + newTo + "' and station_to='" + newFrom + "' and R_id=route_id and O_id=operator_id and bus_id=b_id and running_data='" + newJourney + "'")
            res = cur.fetchall()
            cur.execute("select count(*) from operator ,add_bus_route_details , add_bus_running_details ,add_bus_details where station_from='" + newTo + "' and station_to='" + newFrom + "' and R_id=route_id and O_id=operator_id and bus_id=b_id and running_data='" + newJourney + "'")
            count = cur.fetchall()
            if count[0][0]==2:
                Label(frame2, text = "Select Bus",font = "Arial 10 bold",fg="green").grid(row = 4, column = 0,padx=30,pady=30)
                radio = StringVar()
                R1 = Radiobutton(frame2, text="Bus1", variable=radio, value=res[0][0])
                R1.grid(row = 5, column = 0,padx=30,pady=10)
                R2 = Radiobutton(frame2, text="Bus2", variable=radio, value=res[1][0])
                R2.grid(row = 6, column = 0,padx=30,pady=10)

                Label(frame2, text = "Operator",font = "Arial 10 bold",fg="green").grid(row = 4, column = 1,padx=40,pady=30)
                Label(frame2, text = "Bus Type",font = "Arial 10 bold",fg="green").grid(row = 4, column = 2,padx=50,pady=30)
                Label(frame2, text = "Available Capacity",font = "Arial 10 bold",fg="green").grid(row = 4, column = 3,padx=60,pady=30)
                Label(frame2, text = "Fare",font = "Arial 10 bold",fg="green").grid(row = 4, column = 4,padx=60,pady=30)
                # bus_select = IntVar()
                # Radiobutton = (frame2 , text = "Select Bus").grid(row = 5, column = 0,padx=30,pady=30)
                Label(frame2, text = res[0][1]).grid(row = 5, column = 1,padx=40,pady=30)
                Label(frame2, text = res[1][1]).grid(row = 6, column = 1,padx=40,pady=30)

                Label(frame2, text = res[0][2]).grid(row = 5, column = 2,padx=40,pady=30)
                Label(frame2, text = res[1][2]).grid(row = 6, column = 2,padx=40,pady=30)

                Label(frame2, text = res[0][3]).grid(row = 5, column = 3,padx=40,pady=30)
                Label(frame2, text = res[1][3]).grid(row = 6, column = 3,padx=40,pady=30)

                Label(frame2, text = res[0][4]).grid(row = 5, column = 4,padx=40,pady=30)
                Label(frame2, text = res[1][4]).grid(row = 6, column = 4,padx=40,pady=30)

                

                Button(frame2,command=PTB,text="Proceed to Book",font = "8",bg="SpringGreen2").grid(row = 5, column = 7,pady = 15) 
            elif count[0][0]==0:
                messagebox.showinfo("Error","Some Information is Missing or Date Format Should Wrong Data Format like DD/MM/YY")  
            else:
                radio = StringVar()  
                Label(frame2, text = "Select Bus",font = "Arial 10 bold",fg="green").grid(row = 4, column = 0,padx=30,pady=30)
                R1 = Radiobutton(frame2, text="Bus1", variable=radio, value =res[0][0])  
                R1.grid(row = 5, column = 0,padx=30,pady=5)
                Label(frame2, text = "Operator",font = "Arial 10 bold",fg="green").grid(row = 4, column = 1,padx=40,pady=30)
                Label(frame2, text = "Bus Type",font = "Arial 10 bold",fg="green").grid(row = 4, column = 2,padx=50,pady=30)
                Label(frame2, text = "Available Capacity",font = "Arial 10 bold",fg="green").grid(row = 4, column = 3,padx=60,pady=30)
                Label(frame2, text = "Fare",font = "Arial 10 bold",fg="green").grid(row = 4, column = 4,padx=60,pady=30)
                Label(frame2, text = res[0][1]).grid(row = 5, column = 1,padx=40,pady=30)
                #Label(frame2, text = res[1][1]).grid(row = 6, column = 1,padx=40,pady=30)

                Label(frame2, text = res[0][2]).grid(row = 5, column = 2,padx=40,pady=30)
                #Label(frame2, text = res[1][2]).grid(row = 6, column = 2,padx=40,pady=30)

                Label(frame2, text = res[0][3]).grid(row = 5, column = 3,padx=40,pady=30)
                #Label(frame2, text = res[1][3]).grid(row = 6, column = 3,padx=40,pady=30)

                Label(frame2, text = res[0][4]).grid(row = 5, column = 4,padx=40,pady=30)
                #Label(frame2, text = res[1][4]).grid(row = 6, column = 4,padx=40,pady=30)

                Button(frame2,command=PTB,text="Proceed to Book",font = "8",bg="SpringGreen2").grid(row = 5, column = 7,pady = 15)


        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        

        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)
        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Enter Journey Details",fg="green4",bg="palegreen1",font = "Arial 16 bold").grid(row = 2, column = 0)

        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Label(frame2, text = "To",font = "5").grid(row = 3, column = 0,pady=0)
        To = Entry(frame2)
        To.grid(row = 3, column = 1)
        Label(frame2, text = "From",font = "5").grid(row = 3, column = 2)
        From = Entry(frame2)
        From.grid(row = 3, column = 3)
        Label(frame2, text = "Journey Date",font = "5").grid(row = 3, column = 4)
        Journey = Entry(frame2)
        Journey.grid(row = 3, column = 5)

        frame3=Frame(root)
        frame3.grid(row=5,column = 0, columnspan =10)
        frame4=Frame(frame3)
        frame4.grid(row=6,column = 0, columnspan =10)
        Button(frame2,command= show_bus, text="Show Bus",font = "9",bg="SpringGreen2").grid(row = 3, column = 6,padx=20)
        img2 = PhotoImage(file = '.\\home.png')
        Label(frame2,image=img2).grid(row = 3, column =7)
        root.mainloop()

    def bus_ticket(phone,busID,date):
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        messagebox.showinfo("Success", "seat Booked...")
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)
        frame2=Frame(root,relief="groove",bd=5)
        frame2.grid(row=3,column = 0, columnspan =10)
        cur.execute("select User_name , Gender , No_Of_Seats, age , refer from user_info where Mobile_No = '" + phone + "'")
        res1 = cur.fetchall()
        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=20)
        Label(root, text = "Bus Ticket",font = "Arial 15 bold").grid(row = 2, column = 0)
        Label(frame2, text = "Passengers : " + str(res1[0][0]),font = "Arial 10 bold").grid(row = 3, column = 2)
        Label(frame2, text = "Gender : " + str(res1[0][1]),font = "Arial 10 bold").grid(row = 3, column = 4)
        Label(frame2, text = "No of Seats : " + str(res1[0][2]),font = "Arial 10 bold").grid(row = 4, column = 2)
        Label(frame2, text = "Mobile Number: " + str(phone),font = "Arial 10 bold").grid(row = 4, column = 4)
        Label(frame2, text = "Age : " + str(res1[0][3]),font = "Arial 10 bold").grid(row = 5, column = 2)
        cur.execute("select Fare_Rs,O_id,route_id from add_bus_details where Bus_id = '" + busID + "'")
        res2 = cur.fetchall()
        Label(frame2, text = "Fare Rs : " + str(res2[0][0]),font = "Arial 15 bold").grid(row = 5, column = 4)
        Label(frame2, text = "Booking Ref " + str(res1[0][4]),font = "Arial 15 bold").grid(row = 6, column = 2)  #as it is
        cur.execute("select name from operator where Operator_id = '" + res2[0][1] + "'")
        res3 = cur.fetchone()
        Label(frame2, text = "Bus Details : " + str(res3[0]),font = "Arial 10 bold").grid(row = 6, column = 4)
        cur.execute("select date('now')")
        da_te = cur.fetchone()
        Label(frame2, text = "Booked on : " + str(da_te[0]),font = "Arial 10 bold").grid(row = 7, column = 2)  #as it is
        #cur.execute("select Station_from from add_bus_running_details where R_id = '" + res2[2] + "'")  
        # res4 = cur.fetchall()
        Label(frame2, text = "Travel On : " + str(date),font = "Arial 10 bold").grid(row = 7, column = 4)
        Label(frame2, text = "No of Seats : " + str(res1[0][2]),font = "Arial 10 bold").grid(row = 8, column = 2)
        cur.execute("select Station_from from add_bus_route_details where R_id = '" + res2[0][2] + "'")   #guna
        res5 = cur.fetchone()
        Label(frame2, text = "Boarding Point : " + str(res5[0]),font = "Arial 10 bold").grid(row = 8, column = 4)
        total = str(int(res2[0][0])*int(res1[0][2]))
        frame3=Frame(frame2,relief="groove",bd=5)
        frame3.grid(row=3,column = 0, columnspan =10)
        Label(frame3, text = "Total amount Rs : " + total + ".00 /- to be paid at the time of boarding the bus",font = "Arial 10 bold").grid(row = 9, column = 2)
        #value from another table
        i=i+1
        

        root.mainloop()


    def check_your_booking():
        
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)

        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)

        def fun2():
            phone=phone1.get()
            frame3=Frame(root,relief="groove",bd=5)
            frame3.grid(row=4,column = 0, columnspan =10)
            cur.execute("select User_name , Gender , No_Of_Seats, age,bID from user_info where Mobile_No = '" + phone + "'")
            res1 = cur.fetchall()
            Label(frame3, text = "Passengers : " + str(res1[0][0]),font = "Arial 10 bold").grid(row = 3, column = 1)
            Label(frame3, text = "Gender : " + str(res1[0][1]),font = "Arial 10 bold").grid(row = 3, column = 2)
            Label(frame3, text = "No of Seats : " + str(res1[0][2]),font = "Arial 10 bold").grid(row = 4, column = 1)
            Label(frame3, text = "Mobile Number : " + str(phone),font = "Arial 10 bold").grid(row = 4, column = 2)
            Label(frame3, text = "Age : " + str(res1[0][3]),font = "Arial 10 bold").grid(row = 5, column = 1)
            cur.execute("select running_data from add_bus_running_details where b_id = '" + res1[0][4] + "'")
            res2 = cur.fetchone()
            Label(frame3, text = "Tavel on : " + str(res2[0]),font = "Arial 10 bold").grid(row = 5, column = 2)
            cur.execute("select route_id, fare_rs from add_bus_details where bus_id = '" + res1[0][4] + "'")
            res3 = cur.fetchall()
            cur.execute("select station_from,station_to from add_bus_route_details where r_id = '" + res3[0][0] + "'")
            res4 = cur.fetchall()
            Label(frame3, text = "Boarding Point : " + str(res4[0][0]),font = "Arial 10 bold").grid(row = 6, column = 1)
            Label(frame3, text = "Destination Point : " + str(res4[0][1]),font = "Arial 10 bold").grid(row = 6, column = 2)
            Label(frame3, text = "Fare Rs : " + str(res3[0][1]),font = "Arial 10 bold").grid(row = 7, column = 1)

        Label(root, text = "Check Your Booking",fg="green4",bg="palegreen1",font = "Arial 16 bold").grid(row = 2, column = 0)
        Label(frame2, text = "Enter Your Mobile No : ",font = "Arial 16 bold").grid(row = 3, column = 0,pady=30)
        phone1 = Entry(frame2)
        phone1.grid(row = 3, column = 1)
        Button(frame2,text="Check Booking",command=fun2,font = "Arial 10 bold").grid(row = 3, column = 2,padx=3)
        root.mainloop()

    def four_button():
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Add New Details to DataBase",fg="green4",font = "Arial 16 bold").grid(row = 2, column = 0,pady=20)

        #calling Function
        def call_operator():
            root.destroy()
            a.operator()


        def call_new_bus():
            root.destroy()
            a.add_bus_details()


        def call_new_route():
            root.destroy()
            a.bus_route()


        def call_new_run():
            root.destroy()
            a.bus_running_details()


        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Button(frame2,text="New Operator",command=call_operator,bg = "Pale Green1").grid(row=3,column = 0,padx =20,pady=20)
        Button(frame2,text="New Bus",command=call_new_bus,bg = "tomato").grid(row=3,column = 1,padx =20)
        Button(frame2,text="New Route",command=call_new_route,bg = "skyBlue2").grid(row=3,column = 2,padx =20)
        Button(frame2,text="New Run",command=call_new_run,bg = "Lightpink3").grid(row=3,column = 3,padx =20)
        root.mainloop()

    def operator():
        cur.execute("create table IF NOT EXISTS operator(Operator_id varchar(100) NOT NULL PRIMARY KEY,Name varchar(100),Address varchar(200),Mobile_Number varchar(20),Email Varchar(50));")

        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)
        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Add Bus Operator Details",fg="green4",font = "Arial 16 bold").grid(row = 2, column = 0,pady=20)


        # Function
        def fun1():
            newOPI = OPI.get()
            newO_Name = O_Name.get()
            newO_Address = O_Address.get()
            newO_Phone = O_Phone.get()
            newO_Email = O_Email.get()
            cur.execute("SELECT COUNT(*) from operator WHERE Operator_id = '" + newOPI + "' ")
            result = cur.fetchone()
            if int(result[0]) > 0:
                messagebox.showerror("Error","Operator_id Already exists in database")
            else:
                messagebox.showinfo("Operator Entry", "Operator record added")
                cur.execute("INSERT INTO operator(Operator_id,Name,Address,Mobile_Number,Email)VALUES(?,?,?,?,?)",(newOPI,newO_Name,newO_Address,newO_Phone,newO_Email))
                db.commit()
            Label(frame2,text=OPI.get() + " "+ O_Name.get()+" " + O_Address.get()+ " " + O_Phone.get() +" "+O_Email.get()).grid(row=4,column = 0, columnspan =10)


        def update():
            newOPI = OPI.get()
            newO_Name = O_Name.get()
            newO_Address = O_Address.get()
            newO_Phone = O_Phone.get()
            newO_Email = O_Email.get()
            cur.execute("SELECT COUNT(*) from operator WHERE Operator_id = '" + newOPI + "' ")
            result = cur.fetchone()
            if int(result[0]) == 0:
                messagebox.showerror("Error","Operator_id Not Present in database Your can't Edit it")
            else:
                messagebox.showinfo("Operator Entry", "Operator record Updated Succesfully")
                cur.execute("DELETE FROM operator WHERE Operator_id = '" + newOPI + "' ")
                cur.execute("INSERT INTO operator(Operator_id,Name,Address,Mobile_Number,Email)VALUES(?,?,?,?,?)",(newOPI,newO_Name,newO_Address,newO_Phone,newO_Email))
                db.commit()
            Label(frame2,text=OPI.get() + " "+ O_Name.get()+" " + O_Address.get()+ " " + O_Phone.get() +" "+O_Email.get()).grid(row=4,column = 0, columnspan =10)

            #set all entry empty


        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Label(frame2, text = "Operator id",font = "5").grid(row = 3, column = 0,pady=10)
        OPI = Entry(frame2)
        OPI.grid(row = 3, column = 1)
        Label(frame2, text = "Name",font = "5").grid(row = 3, column = 2)
        O_Name = Entry(frame2)
        O_Name.grid(row = 3, column = 3)
        Label(frame2, text = "Address",font = "5").grid(row = 3, column = 4)
        O_Address = Entry(frame2)
        O_Address.grid(row = 3, column = 5)
        Label(frame2, text = "Mobile_Number",font = "5").grid(row = 3, column = 6)
        O_Phone = Entry(frame2)
        O_Phone.grid(row = 3, column = 7)
        # if int(len(O_Phone.get()))<10:
        #     messagebox.showinfo("info","Number Count Less then 10")
        Label(frame2, text = "Email",font = "5").grid(row = 3, column = 8)
        O_Email = Entry(frame2)
        O_Email.grid(row = 3, column = 9)


        Button(frame2,text="Add",command=fun1,bg = "spring green1",font="Arial 12").grid(row = 3, column = 10,padx=8)
        Button(frame2,text="Edit",command = update,bg = "spring green1",font="Arial 12").grid(row = 3, column = 11)


        img1 = PhotoImage(file = '.\\home.png')
        Label(frame2,image=img1).grid(row = 5, column = 8,pady=70)
        root.mainloop()

    def bus_route():
        cur.execute("create table IF NOT EXISTS add_bus_route_details(R_id varchar(10) NOT NULL PRIMARY KEY, Station_from varchar(100), Station_to varchar(100));")
        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Add Bus Route Details",fg="green4",font = "Arial 16 bold").grid(row = 2, column = 0,pady=20)

        def fun1():
            newroute_id = route_id.get()
            newbus_to= bus_from.get()
            newbus_from = bus_to.get()
            cur.execute("SELECT COUNT(*) from add_bus_route_details WHERE R_id = '" + newroute_id + "' ")
            result = cur.fetchone()
            if int(result[0]) > 0:
                messagebox.showerror("Error","route_id Already exists in database")
            messagebox.showinfo("Operator Entry", "Operator Entry ")
            cur.execute("INSERT INTO add_bus_route_details(R_id, Station_from, Station_to)VALUES(?,?,?)",(newroute_id,newbus_to,newbus_from))
            db.commit()
            Label(frame2,text=newroute_id + " "+ newbus_to+" " + newbus_from ,font = "Arial 10 bold",).grid(row=4,column = 0, columnspan =10)


        def action():
            newroute_id = route_id.get()
            newbus_to= bus_from.get()
            newbus_from = bus_to.get()
            cur.execute("SELECT COUNT(*) from add_bus_route_details WHERE R_id = '" + newroute_id + "' ")
            result = cur.fetchone()
            if int(result[0]) == 0:
                messagebox.showerror("Error","bus route Details Not Present in database Your can't delete it")
            else:
                messagebox.showinfo("Running Details", "SuccessFully Deleted From Database")
                cur.execute("DELETE FROM operator WHERE Route_id = '" + newroute_id + "' ")


        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Label(frame2, text = "Route Id",font = "5").grid(row = 3, column = 0,pady=10)
        route_id = Entry(frame2)
        route_id.grid(row = 3, column = 1)
        Label(frame2, text = "From",font = "5").grid(row = 3, column = 2)
        bus_from = Entry(frame2)
        bus_from .grid(row = 3, column = 3)
        Label(frame2, text = "To",font = "5").grid(row = 3, column = 4)
        bus_to = Entry(frame2)
        bus_to.grid(row = 3, column = 5)

        Button(frame2,text="Add Route",command=fun1,bg = "spring green1",font="Arial 12").grid(row = 3, column = 6,padx=50)
        Button(frame2,text="Delete Route",command=action,bg = "spring green1",font="Arial 12",fg="red").grid(row = 3, column = 7)


        img1 = PhotoImage(file = '.\\home.png')
        Label(frame2,image=img1).grid(row = 4, column = 6,pady=70)

        root.mainloop()

    def bus_running_details():
        cur.execute("create table IF NOT EXISTS add_bus_running_details(b_id varchar(50) NOT NULL PRIMARY KEY,Running_Data varchar(100),Seat_available varchar(20));")

        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Add Bus Running Details",fg="green4",font = "Arial 16 bold").grid(row = 2, column = 0,pady=20)

        def fun1():
            newbus_id = Bus_ID.get()
            newRunning_date = Running_date.get()
            newSeat_available = seat_available.get()
            messagebox.showinfo("Running Details", "SuccessFully Added")
            cur.execute("INSERT INTO add_bus_running_details(b_id ,Running_Data ,Seat_available )VALUES(?,?,?)",(newbus_id,newRunning_date,newSeat_available))
            db.commit()
            cur.execute("SELECT COUNT(*) from add_bus_running_details WHERE b_id = '" + newbus_id + "' ")
            result = cur.fetchone()
            if int(result[0]) > 0:
                messagebox.showerror("Error","Operator_id Already exists in database")
            Label(frame2,text=newbus_id + " " + newRunning_date +" "+newSeat_available,font="Arial 12").grid(row=4,column = 0, columnspan =10)

        def action():
            newbus_id = Bus_ID.get()
            newRunning_date = Running_date.get()
            newSeat_available = seat_available.get()
            cur.execute("SELECT COUNT(*) from add_bus_running_details WHERE b_id = '" + newbus_id + "' ")
            result = cur.fetchone()
            if int(result[0]) == 0:
                messagebox.showerror("Error","bus Running Details Not Present in database Your can't delete it")
            else:
                messagebox.showinfo("Running Details", "SuccessFully Deleted From Database")
                cur.execute("DELETE FROM add_bus_running_details WHERE b_id = '" + newbus_id + "' ")

        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Label(frame2, text = "Bus ID",font = "5").grid(row = 3, column = 0,pady=10)
        Bus_ID = Entry(frame2)
        Bus_ID.grid(row = 3, column = 1)
        Label(frame2, text = "Running Date",font = "5").grid(row = 3, column = 2)
        Running_date = Entry(frame2)
        Running_date .grid(row = 3, column = 3)
        Label(frame2, text = "Seat Available",font = "5").grid(row = 3, column = 4)
        seat_available = Entry(frame2)
        seat_available.grid(row = 3, column = 5)

        Button(frame2,text="Add Run",command=fun1,bg = "spring green1",font="Arial 12").grid(row = 3, column = 6,padx=50)
        Button(frame2,text="Delete Run",command=action,bg = "spring green1",font="Arial 12").grid(row = 3, column = 7)


        img1 = PhotoImage(file = '.\\home.png')
        Label(frame2,image=img1).grid(row = 4, column = 6,pady=70)
        root.mainloop()

    def add_bus_details():
        cur.execute("create table IF NOT EXISTS add_bus_details(Bus_id varchar(100) NOT NULL PRIMARY KEY,Bus_type varchar(100),Capacity varchar(200),Fare_Rs varchar(20),O_id Varchar(50), Route_id Varchar(50),FOREIGN KEY (O_id) REFERENCES operator(Operator_id),FOREIGN KEY (Route_id) REFERENCES add_bus_route_details(Route_id));")

        root = Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        root.title("Online bus Booking System")
        frame1=Frame(root)
        frame1.grid(row=0,column = 0, columnspan =10)
        img = PhotoImage(file = '.\\Bus_for_project.png')
        Label(frame1,image=img).grid(row = 0 , column = 0,padx = w//2.8)

        Label(root , text="Online Bus Booking System",bg="sky blue",font = "Arial 25 bold",fg = "red").grid(row = 1 , column = 0,padx = w//2.8,pady=30)
        Label(root, text = "Add Bus Details",fg="green4",font = "Arial 16 bold").grid(row = 2, column = 0,pady=20)

        def fun2():
            newbus_id = bus_id.get()
            newbus_type = bus_type.get()
            newCapacity = Capacity.get()
            newfare_id = Fare_Rs.get()
            newOperator_id = Operator_ID.get()
            newRoute_id = Route_id.get()

            cur.execute("SELECT COUNT(*) from add_bus_details WHERE bus_id = '" + newbus_id + "' ")
            result = cur.fetchone()
            if int(result[0]) > 0:
                messagebox.showerror("Error","Bus_id Already exists in database") #some thig missing operator id = operator table operator id
            else:
                messagebox.showinfo("Bus Entry", "Bus Record Added ")
                cur.execute("INSERT INTO add_bus_details(Bus_id,Bus_type,Capacity,Fare_Rs,O_id, Route_id)VALUES(?,?,?,?,?,?)",(newbus_id,newbus_type,newCapacity,newfare_id,newOperator_id,newRoute_id))
                db.commit()
            Label(frame2,text=newbus_id + " "+newbus_type+" " +  newCapacity+ " " + newfare_id +" "+newOperator_id +" " +newRoute_id,font = "Arial 10 bold").grid(row=5,column = 0, columnspan =10)

        def update():
            newbus_id = bus_id.get()
            newbus_type = bus_type.get()
            newCapacity = Capacity.get()
            newfare_id = Fare_Rs.get()
            newOperator_id = Operator_ID.get()
            newRoute_id = Route_id.get()

            cur.execute("SELECT COUNT(*) from add_bus_details WHERE bus_id = '" + newbus_id + "' ")
            result = cur.fetchone()
            if int(result[0]) == 0:
                messagebox.showerror("Error","Bus_id Not Present in database Your can't Edit it") #some thig missing operator id = operator table operator id
            else:
                messagebox.showinfo("Bus Entry", "Bus Record record Updated Succesfully ")
                cur.execute("DELETE FROM operator WHERE Bus_id = '" + newbus_id + "' ")
                cur.execute("INSERT INTO add_bus_details(Bus_id,Bus_type,Capacity,Fare_Rs,Operator_id, Route_id)VALUES(?,?,?,?,?,?)",(newbus_id,newbus_type,newCapacity,newfare_id,newOperator_id,newRoute_id))
                db.commit()
            Label(frame2,text=newbus_id + " "+newbus_type+" " +  newCapacity+ " " + newfare_id +" "+newOperator_id +" " +newRoute_id,font = "Arial 10 bold").grid(row=5,column = 0, columnspan =10)


        frame2=Frame(root)
        frame2.grid(row=3,column = 0, columnspan =10)
        Label(frame2, text = "Bus ID",font = "5").grid(row = 3, column = 0,pady=10)
        bus_id = Entry(frame2)
        bus_id.grid(row = 3, column = 1)
        Label(frame2, text = "Bus Type",font = "5").grid(row = 3, column = 2)
        bus_type = StringVar()
        bus_type.set('Bus Type')
        option = ["AC f2","AC 3X2" , "Non AC 2X2","Non AC 3X2", "AC-Sleeper 2X1" , "Non-AC Sleeper 2X1"]
        d_Menu=OptionMenu(frame2,bus_type,*option)
        d_Menu.grid(row = 3, column = 3)
        Label(frame2, text = "Capacity",font = "5").grid(row = 3, column = 4)
        Capacity = Entry(frame2)
        Capacity.grid(row = 3, column = 5)
        Label(frame2, text = "Fare Rs",font = "5").grid(row = 3, column = 6)
        Fare_Rs=Entry(frame2)
        Fare_Rs.grid(row = 3, column = 7)
        Label(frame2, text = "Operator ID",font = "5").grid(row = 3, column = 8)
        Operator_ID = Entry(frame2)
        Operator_ID.grid(row = 3, column = 9)
        Label(frame2, text = "Route ID",font = "5").grid(row = 3, column = 10)
        Route_id = Entry(frame2)
        Route_id.grid(row = 3, column = 11)
        Button(frame2,text="Add Bus",command=fun2,bg = "spring green1",font="Arial 12").grid(row = 9, column = 7,pady=60)
        Button(frame2,text="Edit Bus",command=update,bg = "spring green1",font="Arial 12").grid(row = 9, column = 8)


        img1 = PhotoImage(file = '.\\home.png')
        Label(frame2,image=img1).grid(row = 9, column = 9,pady=70)
        root.mainloop()




a=Bus_Ticket
a.home_Page()
