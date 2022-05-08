# This Restaurant Software Autmotion was created in python to replace the pencil/paper method most restaurants use to take orders.
# @authors: Malcolm Holden (Host), Drew Rado (Cook), Lileah Tunno (Wait Staff), Brandan Murphy (Busser)

# Imports
import tkinter
from tkinter import *
from tkinter import ttk
import csv
import os
from PIL import ImageTk, Image


#HOST------------------------------------------------------------------------------------------------------------------------------------------------
# Shows the host all tables and their state:
def hostTables():
    tableStatus=Toplevel(root)
    tableStatus.title("Host Table View")
    tableStatus.geometry("450x330")
    ttk.Label(tableStatus, text="All Tables: ").grid(sticky="W", column=0, row=0)
    # table buttons open up new windows that show table status
    Button(tableStatus, text="Table 1", command=(lambda: tbStatWindow(1)), height = 5, width=20).grid(column=0, row=1)
    Button(tableStatus, text="Table 2", command=(lambda: tbStatWindow(2)), height = 5, width=20).grid(column=0, row=2)
    Button(tableStatus, text="Table 3", command=(lambda: tbStatWindow(3)), height = 5, width=20).grid(column=0, row=3)
    Button(tableStatus, text="Table 4", command=(lambda: tbStatWindow(4)), height = 5, width=20).grid(column=1, row=1)
    Button(tableStatus, text="Table 5", command=(lambda: tbStatWindow(5)), height = 5, width=20).grid(column=1, row=2)
    Button(tableStatus, text="Table 6", command=(lambda: tbStatWindow(6)), height = 5, width=20).grid(column=1, row=3)
    Button(tableStatus, text="Table 7", command=(lambda: tbStatWindow(7)), height = 5, width=20).grid(column=2, row=1)
    Button(tableStatus, text="Table 8", command=(lambda: tbStatWindow(8)), height = 5, width=20).grid(column=2, row=2)
    Button(tableStatus, text="Table 9", command=(lambda: tbStatWindow(9)), height = 5, width=20).grid(column=2, row=3)
    ttk.Label(tableStatus, text="").grid(column=2, row=4)
    ttk.Button(tableStatus, text="Exit",command=tableStatus.destroy).place(x=185,y=295)

# opens table status window with parameter of table id
def tbStatWindow(tbid):

    tableStat=Toplevel(root)
    tableStat.title('Table ' + str(tbid))
    ttk.Label(tableStat, text="Status: " + \
              str(printTBstat(tbid-1))).grid(column=0, row=0)

    # if the table is available, allow host to assign waitstaff to table
    if str(printTBstat(tbid-1)) == "Available":
        empList=["John", "George", "Paul", "Ringo"]
        ttk.Label(tableStat, text="Select Waitstaff: ").grid(column=0, row=3)
        wsMenu=StringVar(tableStat)
        wsMenu.set("John")

        wsmenu1=ttk.OptionMenu(tableStat, wsMenu, * \
                               empList).grid(column=1, row=3)

        ttk.Button(tableStat, text="Submit", command=(
            lambda: assignWaitstaff(wsMenu.get()))).grid(column=1, row=4)
    
    # if table is occupied, only option can be to reset the table. This is when a customer finishes eating and goes to pay their bill.
    elif str(printTBstat(tbid-1)) == "Occupied":
        ttk.Button(tableStat, text="Reset Table", command=(
            lambda: resetTable())).grid(column=1, row=4)

    # resets the table back to being Dirty and Empty
    def resetTable():
        newFile=open("tempCSV.csv", 'w', newline="")
        file=open("hostTableCSV.csv")
        csvreader=csv.reader(file)
        csvWriter=csv.writer(newFile)
        rows=[]
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][2]="Empty"
        rows[tbid-1][1]="Dirty"
        for row in rows:
            csvWriter.writerow(row)

        file.close()
        newFile.close()
        os.remove("hostTableCSV.csv")
        old_name=r"tempCSV.csv"
        new_name=r"hostTableCSV.csv"
        os.rename(old_name, new_name)
        tableStat.destroy()
    
    def assignWaitstaff(waitstaffName):
        newFile=open("tempCSV.csv", 'w', newline="")
        file=open("hostTableCSV.csv")
        csvreader=csv.reader(file)
        csvWriter=csv.writer(newFile)
        rows=[]
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][2]=waitstaffName
        rows[tbid-1][1]="Occupied"
        for row in rows:
            csvWriter.writerow(row)

        file.close()
        newFile.close()
        os.remove("hostTableCSV.csv")
        old_name=r"tempCSV.csv"
        new_name=r"hostTableCSV.csv"
        os.rename(old_name, new_name)
        tableStat.destroy()

def printTBstat(tbid):
    file=open("hostTableCSV.csv")
    csvreader=csv.reader(file)
    rows=[]
    for row in csvreader:
        rows.append(row)

    statusId=(rows[tbid][1])
    return statusId
    file.close()


#WAITSTAFF------------------------------------------------------------------------------------------------------------------------------------------------
# pizza Order
orders_array = []
class pizzaOrder():
    def __init__(self, crust, sauce=[], toppings=[], notesVar=""):
        self.crust = crust
        self.sauce = sauce
        self.toppings = toppings
        self.notesVar = notesVar

# Wait staff enters the customer's order:
def waiterOrder():
    submitOrder = Toplevel()
    submitOrder.geometry("850x240")
    submitOrder.title("Submit New Order")
    Label(submitOrder, text="New Pizza Order").grid(sticky="W", column=0, row=0)

    # Image
    image2 = Image.open('pizza1-1.png')
    test2 = ImageTk.PhotoImage(image2)
    label2 = tkinter.Label(submitOrder, image=test2)
    label2.image = test2
    label2.place(x=500, y=1)

    # Crust
    crust1 = StringVar()  # Any Crust

    ttk.Label(submitOrder, text="",).grid(sticky="W", column=0, row=1)
    ttk.Label(submitOrder, text="Please Select A Crust: ",).grid(sticky="W", column=0, row=2)
    ttk.Radiobutton(submitOrder, text="Regular", value="Regular",variable=crust1).grid(sticky="W", column=1, row=2)
    ttk.Radiobutton(submitOrder, text="Stuffed", value="Stuffed",variable=crust1).grid(sticky="W", column=2, row=2)
    ttk.Radiobutton(submitOrder, text="Gluten Free", value="Gulten Free",variable=crust1).grid(sticky="W", column=3, row=2)

    # Sauce
    cb1 = StringVar()  # Tomato
    cb2 = StringVar()  # Garlic
    cb3 = StringVar()  # Ranch
    cb4 = StringVar()  # BBQ

    ttk.Label(submitOrder, text="").grid(sticky="W", column=0, row=3)  # Empty Space
    ttk.Label(submitOrder, text="Please Select Sauces: ").grid(sticky="W", column=0, row=4)
    ttk.Checkbutton(submitOrder, text="Tomato",     variable=cb1,onvalue="Tomato, ",   offvalue="").grid(sticky="W", column=1, row=4)
    ttk.Checkbutton(submitOrder, text="Garlic",     variable=cb2,onvalue="Garlic, ",   offvalue="").grid(sticky="W", column=2, row=4)
    ttk.Checkbutton(submitOrder, text="Ranch",      variable=cb3,onvalue="Ranch, ",     offvalue="").grid(sticky="W", column=3, row=4)
    ttk.Checkbutton(submitOrder, text="BBQ",        variable=cb4,onvalue="BBQ, ",         offvalue="").grid(sticky="W", column=4, row=4)

    # Toppings
    top1 = StringVar()  # Bacon
    top2 = StringVar()  # Pepperoni
    top3 = StringVar()  # Ham
    top4 = StringVar()  # Sausage

    ttk.Label(submitOrder, text="").grid(sticky="W", column=0, row=5)  # Empty Space
    ttk.Label(submitOrder, text="Please Select Toppings: ").grid(sticky="W", column=0, row=6)
    ttk.Checkbutton(submitOrder, text="Bacon",     variable=top1,onvalue="Bacon, ",     offvalue="").grid(sticky="W", column=1, row=6)
    ttk.Checkbutton(submitOrder, text="Pepperoni", variable=top2,onvalue="Pepperoni, ", offvalue="").grid(sticky="W", column=2, row=6)
    ttk.Checkbutton(submitOrder, text="Ham",       variable=top3,onvalue="Ham, ",       offvalue="").grid(sticky="W", column=3, row=6)
    ttk.Checkbutton(submitOrder, text="Sausage",   variable=top4,onvalue="Sausage, ",   offvalue="").grid(sticky="W", column=4, row=6)

    # Additional Notes
    ttk.Label(submitOrder, text="").grid(
        sticky="W", column=0, row=7)  # Empty Space
    ttk.Label(submitOrder, text="Additional Notes:").grid(
        sticky="W", column=0, row=8)

    notesVar = StringVar()
    ttk.Entry(submitOrder, textvariable=notesVar, width=50).grid(
        column=1, row=8, columnspan=4)

    # Submit order
    ttk.Label(submitOrder, text="",).grid(
        sticky="W", column=0, row=10)  # Empty Space

    def Submitted():
        submitOrder.destroy()
        orderConfirm = Toplevel()
        orderConfirm.title("Order Submitted")
        Label(orderConfirm, text="Order Successfully Submitted!").grid(sticky="W", column=0, row=0)
        ttk.Button(orderConfirm, text="Ok", command=(orderConfirm.destroy)).grid(column=0, row=1)

        # sends the order to the cook
        toppingsArray=[top1.get(), top2.get(), top3.get(), top4.get()]
        sauceArray=[cb1.get(), cb2.get(), cb3.get(), cb4.get()]
        orders_array.append(pizzaOrder(crust1.get(), sauceArray, toppingsArray, notesVar.get()))

        print(orders_array.__len__())
        print(orders_array[0].crust)
        print(orders_array[0].sauce)
        print(orders_array[0].toppings)
        print(orders_array[0].notesVar)


    # Submit Button, calls on def submitted
    ttk.Button(submitOrder, text="Submit Order >",
        command=Submitted).grid(sticky="W", column=4, row=11)


#COOK------------------------------------------------------------------------------------------------------------------------------------------------
# Shows the cooks what needs to be made next:
def cookOrders():
    cookOrder=Toplevel(root)
    cookOrder.title("Cook's Orders")
    cookOrder.geometry("400x150")
    ttk.Label(cookOrder, text="Current Orders: ").grid(column=0, row=0)

    numOfOrders = orders_array.__len__()
    colNumbner = 0
    while(numOfOrders >= 1):
        ttk.Label(cookOrder, text="Next Order: ").grid(sticky="W", column=colNumbner, row=1)
        ttk.Label(cookOrder, text="Crust: " + orders_array[colNumbner].crust).grid(sticky="W", column=colNumbner, row=2)
        ttk.Label(cookOrder, text="Sauce: " + "".join(orders_array[colNumbner].sauce)).grid(sticky="W", column=colNumbner, row=3)
        ttk.Label(cookOrder, text="Toppings: " + "".join(orders_array[colNumbner].toppings)).grid(sticky="W", column=colNumbner, row=4)
        ttk.Label(cookOrder, text="Additional Notes: " + "".join(orders_array[colNumbner].notesVar)).grid(sticky="W", column=colNumbner, row=5)
        colNumbner +=1
        numOfOrders -=1
        
    ttk.Button(cookOrder, text="Exit", command=(cookOrder.destroy)).grid(column=0, row=6)

    
#BUSSER------------------------------------------------------------------------------------------------------------------------------------------------
# Shows table status, once dirty the busser can ONLY mark to clean
def busserTables():
    tableStatus=Toplevel(root)
    tableStatus.title("Busser Table View")
    tableStatus.geometry("450x330")
    
    ttk.Label(tableStatus, text="All Tables: ").grid(sticky="W", column=0, row=0)
    Button(tableStatus, text="Table 1", command=(lambda: busWindow(1)), height = 5, width=20).grid(column=0, row=1)
    Button(tableStatus, text="Table 2", command=(lambda: busWindow(2)), height = 5, width=20).grid(column=0, row=2)
    Button(tableStatus, text="Table 3", command=(lambda: busWindow(3)), height = 5, width=20).grid(column=0, row=3)
    Button(tableStatus, text="Table 4", command=(lambda: busWindow(4)), height = 5, width=20).grid(column=1, row=1)
    Button(tableStatus, text="Table 5", command=(lambda: busWindow(5)), height = 5, width=20).grid(column=1, row=2)
    Button(tableStatus, text="Table 6", command=(lambda: busWindow(6)), height = 5, width=20).grid(column=1, row=3)
    Button(tableStatus, text="Table 7", command=(lambda: busWindow(7)), height = 5, width=20).grid(column=2, row=1)
    Button(tableStatus, text="Table 8", command=(lambda: busWindow(8)), height = 5, width=20).grid(column=2, row=2)
    Button(tableStatus, text="Table 9", command=(lambda: busWindow(9)), height = 5, width=20).grid(column=2, row=3)
    ttk.Label(tableStatus, text="").grid(column=2, row=4)
    ttk.Button(tableStatus, text="Exit",command=tableStatus.destroy).place(x=185,y=295)

def busWindow(tbid):
    tableStat=Toplevel(root)
    tableStat.title('Table ' + str(tbid))
    
    ttk.Label(tableStat, text="Status: " + \
              str(printTBstat(tbid-1))).grid(column=0, row=0)
    if str(printTBstat(tbid-1)) == "Dirty":
        ttk.Button(tableStat, text="Clean Table", command=(
            lambda: cleanTable(tbid))).grid(column=1, row=4)

    def cleanTable(tbid):
        newFile=open("tempCSV.csv", 'w', newline="")
        file=open("hostTableCSV.csv")
        csvreader=csv.reader(file)
        csvWriter=csv.writer(newFile)
        rows=[]
        for row in csvreader:
            rows.append(row)
        rows[tbid-1][1]="Available"
        for row in rows:
            csvWriter.writerow(row)

        file.close()
        newFile.close()
        os.remove("hostTableCSV.csv")
        old_name=r"tempCSV.csv"
        new_name=r"hostTableCSV.csv"
        os.rename(old_name, new_name)
        tableStat.destroy()


#MAIN------------------------------------------------------------------------------------------------------------------------------------------------
root=tkinter.Tk(className="Login")
root.title("Login")
root.geometry("600x535")

# What role everyone is
ttk.Label(root, text="Welcome Admin, please select who you would like to view the system as: ").place(x=4,y=0)
ttk.Label(root, text="").grid(sticky="W", column=0, row=0)
hostMenu = Button(root, text="Host", command=hostTables, height = 5, width=20).grid(sticky="W", column=0, row=1)            #Host
waiterMenu = Button(root, text="Wait Staff", command=waiterOrder, height = 5, width=20).grid(sticky="W", column=1, row=1)   #Wait Staff
cookMenu = Button(root, text="Cook", command=cookOrders, height = 5, width=20).grid(sticky="W", column=2, row=1)            #Cook
busserMenu = Button(root, text="Busser", command=busserTables, height = 5, width=20).grid(sticky="W", column=3, row=1)      #Busser


# Image
image1 = Image.open('pizzalogo1-1.png')
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=120, y=120)

ttk.Label(root, text="").grid(column=0, row=2)
exitForm=ttk.Button(root, text="Exit",command=root.destroy).place(x=256, y=485)

root.mainloop()