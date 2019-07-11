from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Prototype Login System")
        #self.master.geometry('1350x750+0+0')
        self.master.config(bg= 'powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Prototype Login System', font=('arial',50,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row = 0, column = 0, columnspan=2, pady=40)
#-------------------------------------------------------------------------------
        self.LoginFrame1= LabelFrame(self.frame, width=1350, height=600,font=('arial', 20, 'bold'), relief='ridge',bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2= LabelFrame(self.frame, width=1000, height=600,font=('arial', 20, 'bold'), relief='ridge',bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

#-------------------------------------------------------------------------------
                            ##Label and Entry                    
        self.lblUsername=Label(self.LoginFrame1, text= 'Username: ', font = ('arial', 20,'bold'), bd=22, bg=
                               'cadet blue', fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername=Entry(self.LoginFrame1, font = ('arial', 20,'bold'), textvariable = self.Username)
        self.txtUsername.grid(row=0, column=1, padx = 10)

        self.lblPassword=Label(self.LoginFrame1, text= 'Password: ', font = ('arial', 20,'bold'),bd=22, bg=
                               'cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword=Entry(self.LoginFrame1, font = ('arial', 20,'bold'), show='*', textvariable = self.Password)
        self.txtPassword.grid(row=1, column=1, pady=10)
        
#----------------------------------------------------------------------------------
                            #Buttons label

        self.btnLogin = Button(self.LoginFrame2, text = "Login", width = 17,font = ('arial', 20,'bold'), command = self.Login_system)
        self.btnLogin.grid(row=3, column=0, pady = 22, padx=8)

        self.btnReset = Button(self.LoginFrame2, text = "Reset", width = 17,font = ('arial', 20,'bold'), command = self.Reset)
        self.btnReset.grid(row=3, column=1,pady = 22, padx=8)

        self.btnExit = Button(self.LoginFrame2, text = "Exit", width = 17,font = ('arial', 20,'bold'), command = self.iExit)
        self.btnExit.grid(row=3, column=2)

#==------------------------------------------------------------------------------
                            #Main Buttons 
    def Login_system(self):
        u=(self.Username.get())
        p=(self.Password.get())
        if (len(u) and len(p)) > 0:
            if (u == str(1212) and p == str(1212)):
                self.newWindow = Toplevel(self.master)
                self.app = Window2(self.newWindow)
            else:
                tkinter.messagebox.askretrycancel("Login systems", "Invalid Login Details!")
                self.Username.set("")
                self.Password.set("")
                self.txtUsername.focus()
        else:
            tkinter.messagebox.askretrycancel("Login System", "Please enter valid Input!")

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System", "Do you want to Exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

   

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Prototype Resturant Management System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg= 'Cadet blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
#===========================================================================
##        from tkinter import*
##        import random
##        import time;

##        root= Tk()
##        root.geometry("1600x800+0+0")
##        root.title("Name")

        text_Input=StringVar()

        Tops=Frame(self.master,width=1600, height=50, bg="powder blue", relief=SUNKEN)
        Tops.pack(side=TOP)

        f1=Frame(self.master,width=800, height=700, bg="powder blue", relief=SUNKEN)
        f1.pack(side=LEFT)

        cal=Frame(self.master,width=300, height=700, bg="powder blue", relief=SUNKEN)
        cal.pack(side=RIGHT)
        ################TIME##########################
        Localtime=time.asctime(time.localtime(time.time()))
        #=================================Info=============================

        lblinfo=Label(Tops, font=('arial', 50, 'bold'), text="UCA Meal Management system", fg="Steel Blue", bd=10, anchor='w')
        lblinfo.grid(row=0,column=0)

        lblDateTime=Label(Tops, font=('arial', 20, 'bold'), text=Localtime, fg="Steel Blue", bd=10, anchor='w')
        lblDateTime.grid(row=1,column=0)

        ####Calculator
        #========================================Calculator============================
        def btnClick(numbers):
            global operator
            operator=operator + str(numbers)
            text_Input.set(operator)

        def btnClearDisplay():
            global operator
            operator=""
            text_Input.set("")

        def btnEqualsInput():
            global operator
            sumup=str(eval(operator))
            text_Input.set(sumup)
            operator=""
        def Ref():
            x=random.randint(12908, 500876)
            randomRef = str(x)
            rand.set(randomRef)

            CoF=float(Fries.get())
            CoD=float(Drinks.get())
            CoFilet=float(Filet.get())
            CoBurger=float(Burger.get())
            CoChicBurger=float(Chicken_Burger.get())
            CoCheese_Burger=float(Cheese_Burger.get())

            CostofFries = CoF * 40
            CostofDrinks = CoD * 45
            CostofFilet = CoFilet * 120
            CostofBurger = CoBurger * 150
            CostofChicken_Burger = CoChicBurger * 120
            CostofCheese_Burger = CoCheese_Burger * 200

            CostofMeal = 'KGS', str('%.2f' % (CostofFries + CostofDrinks + CostofFilet
                                            + CostofBurger + CostofChicken_Burger
                                            + CostofCheese_Burger))

            PayTax = ((CostofFries + CostofDrinks + CostofFilet
                       + CostofBurger + CostofChicken_Burger
                       + CostofCheese_Burger) * 0.2)

            TotalCost = (CostofFries + CostofDrinks + CostofFilet
                                            + CostofBurger + CostofChicken_Burger
                         + CostofCheese_Burger)

            Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet
                                            + CostofBurger + CostofChicken_Burger
                          + CostofCheese_Burger)/99)

            Service_1 = "KGS", str('%.2f' % Ser_Charge)

            OverAllCost = "KGS", str('%.2f' % (PayTax + TotalCost + Ser_Charge ))

            PaidTax = "KGS", str('%.2f' % PayTax)

            Service.set(Service_1)

            Cost.set(CostofMeal)

            Tax.set(PaidTax)

            Subtotal.set(CostofMeal)

            Total.set(OverAllCost)
            

        def qExit():
            root.destroy()

        def Reset():
            rand.set("")
            Fries.set("")
            Burger.set("")
            Filet.set("")
            Subtotal.set("")
            Total.set("")
            Service.set("")
            Drinks.set("")
            Tax.set("")
            Cost.set("")
            Chicken_Burger.set("")
            Cheese_Bruger.set("")


        txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                           bg="powder blue", justify='right').grid(columnspan=4)

        btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="7", bg="powder blue",command=lambda:btnClick(7)).grid(row=1,column=0)
        btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=1,column=1)
        btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=1,column=2)
        Addition=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=1,column=3)
        #=======================================================================
        btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="4", bg="powder blue",command=lambda:btnClick(4)).grid(row=2,column=0)
        btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=2,column=1)
        btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=2,column=2)
        Subtraction=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
        #=================================================================
        btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="1", bg="powder blue",command=lambda:btnClick(1)).grid(row=3,column=0)
        btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=3,column=1)
        btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=3,column=2)
        Multiply=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=3,column=3)
        #=================================================================
        btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)
        btnClear=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="C",bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)
        btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="=",bg="powder blue",command=btnEqualsInput).grid(row=4,column=2)
        Division=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial', 20, 'bold'),
                    text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=4,column=3)


        #======================================Resturnat Info 1================================
        rand = StringVar()
        Fries = StringVar()
        Burger = StringVar()
        Filet = StringVar()
        Subtotal = StringVar()
        Total = StringVar()
        Service= StringVar()
        Drinks = StringVar()
        Tax = StringVar()
        Cost = StringVar()
        Chicken_Burger = StringVar()
        Cheese_Burger = StringVar()


        lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16, anchor='w')
        lblReference.grid(row=0,column=0)
        txtReference = Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtReference.grid(row=0,column=1)

        lblFries = Label(f1,font=('arial',16,'bold'),text="Large Fries",bd=16, anchor='w')
        lblFries.grid(row=1,column=0)
        txtFries = Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtFries.grid(row=1,column=1)

        lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16, anchor='w')
        lblBurger.grid(row=2,column=0)
        txtBurger = Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtBurger.grid(row=2,column=1)

        lblFilet = Label(f1,font=('arial',16,'bold'),text="Filet",bd=16, anchor='w')
        lblFilet.grid(row=3,column=0)
        txtFilet = Entry(f1,font=('arial',16,'bold'),textvariable=Filet,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtFilet.grid(row=3,column=1)


        lblChicken = Label(f1,font=('arial',16,'bold'),text="Chicken",bd=16, anchor='w')
        lblChicken.grid(row=4,column=0)
        txtChicken = Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtChicken.grid(row=4,column=1)

        lblCheese = Label(f1,font=('arial',16,'bold'),text="Cheese",bd=16, anchor='w')
        lblCheese.grid(row=5,column=0)
        txtCheese = Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger,bd=10,insertwidth=4,bg='powder blue', justify='right')
        txtCheese.grid(row=5,column=1)

        #======================Resturnat info 2======================================
        lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16, anchor='w')
        lblDrinks.grid(row=0,column=2)
        txtDrinks = Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtDrinks.grid(row=0,column=3)

        lblCost = Label(f1,font=('arial',16,'bold'),text="Cost",bd=16, anchor='w')
        lblCost.grid(row=1,column=2)
        txtCost = Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtCost.grid(row=1,column=3)

        lblService = Label(f1,font=('arial',16,'bold'),text="Service",bd=16, anchor='w')
        lblService.grid(row=2,column=2)
        txtService = Entry(f1,font=('arial',16,'bold'),textvariable=Service,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtService.grid(row=2,column=3)

        lblStateTax = Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16, anchor='w')
        lblStateTax.grid(row=3,column=2)
        txtStateTax = Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtStateTax.grid(row=3,column=3)

        lblSubtotal = Label(f1,font=('arial',16,'bold'),text="Subtotal",bd=16, anchor='w')
        lblSubtotal.grid(row=4,column=2)
        txtSubtotal = Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtSubtotal.grid(row=4,column=3)


        lblTotalCost = Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16, anchor='w')
        lblTotalCost.grid(row=5,column=2)
        txtTotalCost = Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg='#ffffff', justify='right')
        txtTotalCost.grid(row=5,column=3)

        #========================================Buttons==================================
        btnTotal=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Total", bg="powder blue", command = Ref).grid(row=7,column=1)

        btnReset=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Reset", bg="powder blue", command = Reset).grid(row=7,column=2)

        btnExit=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Exit", bg="powder blue", command = qExit).grid(row=7,column=3)


        root.mainloop()


if __name__ == '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()




