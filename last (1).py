from tkinter import*
import random
import time;
import datetime
root = Tk()
root.geometry("1350x750+0+0")
root.title("TASTY")
root.configure(background = 'black')

Tops = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
Tops.pack(side=TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 440, height = 650, bd = 8, relief = "raise")
f2.pack(side=RIGHT)

ft2 = Frame(f2, width = 440, height = 650, bd = 12, relief = "raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width = 440, height = 50, bd = 16, relief = "raise")
fb2.pack(side=BOTTOM)

f1a = Frame(f1, width = 900, height = 330, bd = 8, relief = "raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width = 900, height = 320, bd = 6, relief = "raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width = 400, height = 330, bd = 16, relief = "raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd = 14, relief = "raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width = 450, height = 330, bd = 14, relief = "raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

#========================Cost========================================
def CostofItem():
    Item1=float(l_atte.get())
    Item2=float(L_att.get())
    Item3=float(L_at.get())
    Item4=float(L_a.get())
    Item5=float(L_.get())
    Item6=float(L_e.get())
    Item7=float(L_te.get())
    Item8=float(L_tte.get())

    Item9=float(C_offe.get())
    Item10=float(C_off.get())
    Item11=float(C_of.get())
    Item12=float(C_ofee.get())
    Item13=float(C_ofee.get())
    Item14=float(C_ffee.get())
    Item15=float(C_fee.get())
    Item16=float(C_ofe.get())

    PriceofDrinks = (Item1 * 350) + (Item2 * 350) + (Item3 * 300) \
                    + (Item4 * 250) + (Item5 * 200)+ (Item6 * 200) + (Item7 * 280) + (Item8 * 220)
    
    PriceofFoods = (Item9 * 40) + (Item10 * 250) + (Item11 * 150) \
                    + (Item12 * 150) + (Item13 * 200)+ (Item14 * 200) + (Item15 * 230) + (Item16 * 250)

    DrinksPrice ="Som",str('%.2f'%(PriceofDrinks))
    FoodsPrice ="Som",str('%.2f'%(PriceofFoods))
    CostofDrinks.set(DrinksPrice)
    CostofFoods.set(FoodsPrice)
    SC="Som",str('%.2f'%(60))
    ServiceCharge.set(SC)

    SubTotalofITEMS="Som",str('%.2f'%(PriceofDrinks+PriceofFoods+60))
    SubTotal.set(SubTotalofITEMS)

    Tax="Som",str('%.2f'%((PriceofDrinks+PriceofFoods+60)*0))
    PaidTax.set(Tax)
    TT=((PriceofDrinks+PriceofFoods+60)*0)
    TC="Som",str('%.2f'%(PriceofDrinks+PriceofFoods+60+TT))
    TotalCost.set(TC)
    


def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFoods.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    l_atte.set("0")
    L_att.set("0")
    L_at.set("0")
    L_a.set("0")
    L_.set("0")
    L_e.set("0")
    L_te.set("0")
    L_tte.set("0")

    C_offe.set("0")
    C_off.set("0")
    C_of.set("0")
    C_ofee.set("0")
    C_ofee.set("0")
    C_ffee.set("0")
    C_fee.set("0")
    C_ofe.set("0")

    varl.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.confiure(state=DISABLED)
    txtLatt.confiure(state=DISABLED)
    txtLat.confiure(state=DISABLED)
    txtLa.confiure(state=DISABLED)
    txtL.confiure(state=DISABLED)
    txtLe.confiure(state=DISABLED)
    txtLte.confiure(state=DISABLED)
    txtLtte.confiure(state=DISABLED)
    txtCoffe.confiure(state=DISABLED)
    txtCoff.confiure(state=DISABLED)
    txtCof.confiure(state=DISABLED)
    txtCofee.confiure(state=DISABLED)
    txtCoee.confiure(state=DISABLED)
    txtCffee.confiure(state=DISABLED)
    txtCfee.confiure(state=DISABLED)
    txtCofe.confiure(state=DISABLED)


def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL"+randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t\t'+Dateforder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t\t\t'+"Cost Of Items \n\n")
    txtReceipt.insert(END, 'Grilled meat:\t\t\t\t\t'+l_atte.get()+"\n")
    txtReceipt.insert(END, 'Grilled fish:\t\t\t\t\t'+L_att.get()+"\n")
    txtReceipt.insert(END, 'Chicken and rice:\t\t\t\t\t'+L_at.get()+"\n")
    txtReceipt.insert(END, 'Roast Chicken:\t\t\t\t\t'+L_a.get()+"\n")
    txtReceipt.insert(END, 'Onion Soup:\t\t\t\t\t'+L_.get()+"\n")
    txtReceipt.insert(END, 'Tomato Soup:\t\t\t\t\t'+L_e.get()+"\n")
    txtReceipt.insert(END, 'Chicken Salad:\t\t\t\t\t'+L_te.get()+"\n")
    txtReceipt.insert(END, 'Vegetable omlette:\t\t\t\t\t'+L_tte.get()+"\n")
    txtReceipt.insert(END, 'Mineral water:\t\t\t\t\t'+C_offe.get()+"\n")
    txtReceipt.insert(END, 'Fresh juice:\t\t\t\t\t'+C_off.get()+"\n")
    txtReceipt.insert(END, 'Green Tea:\t\t\t\t\t'+C_of.get()+"\n")
    txtReceipt.insert(END, 'Black Tea:\t\t\t\t\t'+C_ofee.get()+"\n")
    txtReceipt.insert(END, 'English Tea:\t\t\t\t\t'+C_oee.get()+"\n")
    txtReceipt.insert(END, 'Latte:\t\t\t\t\t'+C_ffee.get()+"\n")
    txtReceipt.insert(END, 'Espresso:\t\t\t\t\t'+C_fee.get()+"\n")
    txtReceipt.insert(END, 'Cappuccino:\t\t\t\t\t'+C_ofe.get()+"\n")
    txtReceipt.insert(END, 'Cost of Drinks:\t\t'+CostofDrinks.get()+'\tTax Paid:\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Cost of Foods:\t\t'+CostofFoods.get()+'\tSubTotal Paid:\t\t'+SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Service Charge:\t\t'+ServiceCharge.get()+'\tTotal Cost:\t\t'+TotalCost()+"\n")
    
lblInfo=Label(Tops,font=('arial',70,'bold'),text="        TASTY        ", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

def chkbutton_value():
    if (varl.get() == 1):
        txtLatte.confiure(state=NORMAL)
    elif varl.get() == 0:
         txtLatte.confiure(state=DISABLED)
         l_atte.set("0")
    if (var2.get() == 1):
        txtLatt.confiure(state=NORMAL)
    elif var2.get() == 0:
         txtLatt.confiure(state=DISABLED)
         L_att.set("0")
    if (var3.get() == 1):
        txtLat.confiure(state=NORMAL)
    elif var3.get() == 0:
         txtLat.confiure(state=DISABLED)
         L_at.set("0")
    if (var4.get() == 1):
        txtLa.confiure(state=NORMAL)
    elif var4.get() == 0:
         txtLa.confiure(state=DISABLED)
         L_a.set("0")
    if (var5.get() == 1):
        txtL.confiure(state=NORMAL)
    elif var5.get() == 0:
         txtL.confiure(state=DISABLED)
         L_.set("0")
    if (var6.get() == 1):
        txtLe.confiure(state=NORMAL)
    elif var6.get() == 0:
         txtLe.confiure(state=DISABLED)
         L_e.set("0")
    if (var7.get() == 1):
        txtLte.confiure(state=NORMAL)
    elif var7.get() == 0:
         txtLte.confiure(state=DISABLED)
         L_te.set("0")
    if (var8.get() == 1):
        txtLtte.confiure(state=NORMAL)
    elif var8.get() == 0:
         txtLtte.confiure(state=DISABLED)
         L_tte.set("0")
    if (var9.get() == 1):
        txtCoffe.confiure(state=NORMAL)
    elif var9.get() == 0:
         txtCoffe.confiure(state=DISABLED)
         C_offe.set("0")
    if (var10.get() == 1):
        txtCoff.confiure(state=NORMAL)
    elif var10.get() == 0:
         txtCoff.confiure(state=DISABLED)
         C_off.set("0")
    if (var11.get() == 1):
        txtCof.confiure(state=NORMAL)
    elif var11.get() == 0:
         txtCof.confiure(state=DISABLED)
         C_of.set("0")
    if (var12.get() == 1):
        txtCofee.confiure(state=NORMAL)
    elif var12.get() == 0:
         txtCofee.confiure(state=DISABLED)
         C_ofee.set("0")
    if (var13.get() == 1):
        txtCoee.confiure(state=NORMAL)
    elif var13.get() == 0:
         txtCoee.confiure(state=DISABLED)
         C_ofee.set("0")
    if (var14.get() == 1):
        txtCffee.confiure(state=NORMAL)
    elif var14.get() == 0:
         txtCffee.confiure(state=DISABLED)
         C_ffee.set("0")
    if (var15.get() == 1):
        txtCfee.confiure(state=NORMAL)
    elif var15.get() == 0:
         txtCfee.confiure(state=DISABLED)
         C_fee.set("0")
    if (var16.get() == 1):
        txtCofe.confiure(state=NORMAL)
    elif var16.get() == 0:
         txtCofe.confiure(state=DISABLED)
         C_ofe.set("0")


#========================Variables========================================

varl= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

Dateforder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofFoods=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

l_atte=StringVar()
L_att=StringVar()
L_at=StringVar()
L_a=StringVar()
L_=StringVar()
L_e=StringVar()
L_te=StringVar()
L_tte=StringVar()

C_offe=StringVar()
C_off=StringVar()
C_of=StringVar()
C_ofee=StringVar()
C_oee=StringVar()
C_ffee=StringVar()
C_fee=StringVar()
C_ofe=StringVar()


l_atte.set("0")
L_att.set("0")
L_at.set("0")
L_a.set("0")
L_.set("0")
L_e.set("0")
L_te.set("0")
L_tte.set("0")

C_offe.set("0")
C_off.set("0")
C_of.set("0")
C_ofee.set("0")
C_oee.set("0")
C_ffee.set("0")
C_fee.set("0")
C_ofe.set("0")

Dateforder.set(time.strftime("%d/%m/Y"))


#========================Drinks============================
Water = Checkbutton(f1ab,text="Mineral water \t", variable = var9, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

Juice = Checkbutton(f1ab,text="Fresh juice \t", variable = var10, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

Black_Tea = Checkbutton(f1ab,text="Black Tea \t", variable = var11, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

Green_Tea = Checkbutton(f1ab,text="Green Tea \t", variable = var12, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

English_Tea = Checkbutton(f1ab,text="English Tea \t", variable = var13, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

Latte = Checkbutton(f1ab,text="Latte \t", variable = var14, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

Espresso = Checkbutton(f1ab,text="Espresso \t", variable = var15, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

Cappuccino = Checkbutton(f1ab,text="Cappuccino \t", variable = var16, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#========================Foods============================
A = Checkbutton(f1aa,text="Grilled meat \t", variable = var9, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=0,sticky=W)

B = Checkbutton(f1aa,text="Grilled fish \t\t", variable = var10, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=1,sticky=W)

C = Checkbutton(f1aa,text="Chicken and rice \t\t", variable = var11, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=2,sticky=W)

D = Checkbutton(f1aa,text="Roast Chicken \t\t", variable = var12, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=3,sticky=W)

E = Checkbutton(f1aa,text="Onion Soup \t\t", variable = var13, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=4,sticky=W)

F = Checkbutton(f1aa,text= "Tomato Soup \t\t", variable = var14, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=5,sticky=W)

G = Checkbutton(f1aa,text="Chicken Salad \t\t", variable = var15, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=6,sticky=W)

H = Checkbutton(f1aa,text="Vegetable omlette \t\t", variable = var16, onvalue=1,offvalue=0,
                    font=('arial',18,'bold'),command=chkbutton_value).grid(row=7,sticky=W)

#========================Entre Widget for Foods============================
txtLatte = Entry(f1aa,font=('arial',16,'bold'),textvariable=l_atte, bd=8,
                 width=6, justify='left',state= NORMAL)
txtLatte.grid(row=0, column=1)

txtLatt = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_att,bd=8,
                width=6, justify='left',state= NORMAL)
txtLatt.grid(row=1, column=1)

txtLat = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_at,bd=8,
               width=6, justify='left',state= NORMAL)
txtLat.grid(row=2, column=1)

txtLa = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_a,bd=8,
              width=6, justify='left',state= NORMAL)
txtLa.grid(row=3, column=1)

txtL = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_,bd=8,
             width=6, justify='left',state= NORMAL)
txtL.grid(row=4, column=1)

txtLe = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_e,bd=8,
              width=6, justify='left',state= NORMAL)
txtLe.grid(row=5, column=1)

txtLte = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_te,bd=8,
               width=6, justify='left',state= NORMAL)
txtLte.grid(row=6, column=1)

txtLtte = Entry(f1aa,font=('arial',16,'bold'),textvariable=L_tte,bd=8,
                width=6, justify='left',state= NORMAL)
txtLtte.grid(row=7, column=1)


#========================Entre Widget for Drinks============================
txtCoffe = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_offe,bd=8,
                 width=6, justify='left',state= NORMAL)
txtCoffe.grid(row=0, column=1)

txtCoff = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_off,bd=8,
                width=6, justify='left',state= NORMAL)
txtCoff.grid(row=1, column=1)

txtCof = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_of,bd=8,
               width=6, justify='left',state= NORMAL)
txtCof.grid(row=2, column=1)

txtCofee = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_ofee,bd=8,
                 width=6, justify='left',state= NORMAL)
txtCofee.grid(row=3, column=1)

txtCoee = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_oee,bd=8,
                width=6, justify='left',state= NORMAL)
txtCoee.grid(row=4, column=1)

txtCffee = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_ffee,bd=8,
                 width=6, justify='left',state= NORMAL)
txtCffee.grid(row=5, column=1)

txtCfee = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_fee,bd=8,
                width=6, justify='left',state= NORMAL)
txtCfee.grid(row=6, column=1)

txtCofe = Entry(f1ab,font=('arial',16,'bold'),textvariable=C_ofe,bd=8,
                width=6, justify='left',state= NORMAL)
txtCofe.grid(row=7, column=1)

#========================Cost of Items Information========================================
lblCostofFoods=Label(f2aa,font=('arial',16,'bold'),text="Cost of Drinks", bd=8, anchor='w')
lblCostofFoods.grid(row=2,column=0,sticky=W)
txtCostofFoods=Entry(f2aa,font=('arial',16,'bold'),textvariable=CostofFoods, bd=8,
                      insertwidth=2,justify='left')
txtCostofFoods.grid(row=2,column=1)

lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'),text="Cost of Foods", bd=8, anchor='w')
lblCostofDrinks.grid(row=3,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'),textvariable=CostofDrinks,bd=8,
                      insertwidth=2,justify='left')
txtCostofDrinks.grid(row=3,column=1)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge", bd=8, anchor='w')
lblServiceCharge.grid(row=4,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'),textvariable=ServiceCharge,bd=8,
                      insertwidth=2,justify='left')
txtServiceCharge.grid(row=4,column=1)

#========================Payment Information========================================
lblPaidTax=Label(f2ab,font=('arial',16,'bold'),text="Paid Tax", bd=8)
lblPaidTax.grid(row=2,column=0,sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'),textvariable=PaidTax,bd=8,
                 insertwidth=2,justify='left')
txtPaidTax.grid(row=2,column=1)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total", bd=8)
lblSubTotal.grid(row=3,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'),textvariable=SubTotal,bd=8,
                 insertwidth=2,justify='left')
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'),text="Total Cost", bd=8)
lblTotalCost.grid(row=4,column=0,sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'),textvariable=TotalCost,bd=8,
                 insertwidth=2,justify='left')
txtTotalCost.grid(row=4,column=1)

#========================Information========================================
lblReceipt = Label(ft2,font=('arial',12,'bold'), text="Receipt:", bd=2, anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(ft2, width=59,height=22,bg="white",bd=8,
                  font=('arial',11,'bold'))
txtReceipt.grid(row=1, column=0)

#========================Button========================================
btnTotal=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Total ",command = CostofItem).grid(row=0, column=0)

btnReceipt=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Receipt ",command = Receipt).grid(row=0, column=1)

btnReset=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Reset",command = Reset).grid(row=0, column=2)

btnExit=Button(fb2,padx=16,pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5,
                text="Exit",command = qExit).grid(row=0, column=3)



root.mainloop()


