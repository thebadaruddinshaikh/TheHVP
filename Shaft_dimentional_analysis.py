#Created By Badaruddin Shaikh
# Mrach 2  2019
#Hrasal vakhariya Project B.E
# Places for Improvement
# 1.The Repeated entering of the Values
# 2.Units of the answer to be displayed
# 4.Adding bling.

from tkinter import *
window = Tk()
window.title("Harshal Vakhariya Project")

#TORQUE TRANSMISSION CAPABILITY
shearstrength = StringVar()
Outerdiameter1 = StringVar()
Innerdiameter1 = StringVar()
def torque_1():
	val1.delete('1.0',END)
	torque = (3.14 * float(shearstrength.get()) * (float(Outerdiameter1.get())**4 - float(Innerdiameter1.get())**4)) / (16* float(Outerdiameter1.get()))
	if torque<3500:
		val1.insert(INSERT,"The Design is Not Safe ")    
	else:
		val1.insert(INSERT,"The Design Is Safe ")#how to make the new text delete the previous text


tag1 = Label(window,text="TORQUE TRANSMISSION CAPABILITY")
tag1.grid(row = 0, column = 2)
l1= Label(window,text="Shear Strength :")
l1.grid(row = 1,column = 0)
e1 = Entry(window,textvariable = shearstrength )
e1.grid(row = 1,column = 1)

l2= Label(window,text="Outer Diameter :")
l2.grid(row = 1,column = 2)
e2 = Entry(window,textvariable = Outerdiameter1)
e2.grid(row = 1,column = 3)

l3= Label(window,text="Inner Diameter :")
l3.grid(row = 2,column = 0)
e3 = Entry(window,textvariable = Innerdiameter1)
e3.grid(row = 2,column = 1)

b1 = Button(window,text = "Calculate", command = torque_1)
b1.grid(row = 3,column = 2)

res1 = Label(window,text= "The Torque Transmission Capability is : ")
res1.grid(row = 4, column = 1)
val1 = Text(window, height = 1 , width = 30)
val1.grid(row = 4, column = 2)


#MASS CALCULATION
Density = StringVar()
Outerdiameter2 = StringVar()
Innerdiameter2 = StringVar()
Lenght = StringVar()
def mass_1():
	val2.delete('1.0',END)
	mass = (float(Density.get()) * (float(Outerdiameter2.get())**2 - float(Innerdiameter2.get())**2) * float(Lenght.get()) * 3.14) / 4
	val2.insert(END,mass)

tag2 = Label(window,text="MASS CALCULATION")
tag2.grid(row = 6 , column = 2)

l4= Label(window,text="Enter Density :")
l4.grid(row = 7,column = 0)
e4 = Entry(window, textvariable = Density )
e4.grid(row = 7,column = 1)

l5= Label(window,text="Outer Diameter :")
l5.grid(row = 7,column = 2)
e5 = Entry(window, textvariable = Outerdiameter2)
e5.grid(row = 7,column = 3)

l6= Label(window,text="Inner Diameter :")
l6.grid(row = 8,column = 0)
e6 = Entry(window, textvariable = Innerdiameter2)
e6.grid(row = 8,column = 1)

l7= Label(window,text="Enter Lenght:")
l7.grid(row = 8,column = 2)
e7 = Entry(window, textvariable =Lenght )
e7.grid(row = 8,column = 3)

b2 = Button(window,text = "Calculate",command =mass_1)
b2.grid(row = 9,column = 2)

res2 = Label(window,text= "The Mass of the Shaft is:")
res2.grid(row = 10, column = 1)
val2 = Text(window, height = 1 , width = 20)
val2.grid(row = 10, column = 2)


#TORSIONAL BUCKLING CAPACITY CALCULATIONS
Poisions = StringVar()
Length1 = StringVar()
Thickness = StringVar()
MeanRadius = StringVar()
YM = StringVar()

def torsional_bukling():
	val5.delete('1.0',END)
	val3.delete('1.0',END)
	val6.delete('1.0',END)
	val4.delete('1.0',END)
	tb = (((float(Length1.get()))**2) * (float(Thickness.get())))/(((1-((float(Poisions.get()))**2))**0.5) * (2 * (float(MeanRadius.get())))**3)
	val3.insert(INSERT,tb)
	cs = ((float(YM.get())) / (3*2**0.5)*(1 - (float(Poisions.get()))**2)**0.75)*((float(Thickness.get()))/(float(MeanRadius.get())))**1.5
	val5.insert(END,cs)
	tbc = (cs)*2*3.14*(float(MeanRadius.get()))**2*(float(Thickness.get()))
	val6.insert(END,tbc)
	if tb > 5:
		val4.insert(INSERT,"Long")
	else:
		val4.insert(INSERT,"Medium or Short")




tag3 = Label(window,text="TORSIONAL BUCKLING CAPACITY CALCULATIONS")
tag3.grid(row = 11 , column = 2)

l8= Label(window,text="Enter Poisions Ratio:")
l8.grid(row = 12,column = 0)
e8 = Entry(window, textvariable = Poisions )
e8.grid(row = 12,column = 1)

l9= Label(window,text="Outer Length :")
l9.grid(row = 12,column = 2)
e9 = Entry(window, textvariable = Length1)
e9.grid(row = 12,column = 3)

l10= Label(window,text="Enter Thickness :")
l10.grid(row = 13,column = 0)
e10 = Entry(window, textvariable = Thickness)
e10.grid(row = 13,column = 1)

l11= Label(window,text="Enter Mean Radius :")
l11.grid(row = 13,column = 2)
e11 = Entry(window, textvariable =MeanRadius )
e11.grid(row = 13,column = 3)

l12= Label(window,text="Youngs Modulus :")
l12.grid(row = 14,column = 0)
e12 = Entry(window, textvariable =YM )
e12.grid(row = 14,column = 1)

b3 = Button(window,text = "Calculate",command = torsional_bukling)
b3.grid(row = 15,column = 2)

res3 = Label(window,text= "The Torsion Bukling is : ")
res3.grid(row = 16, column = 1)
val3 = Text(window, height = 1 , width = 20)
val3.grid(row = 16, column = 2)

res4 = Label(window,text= "The Shaft is: ")
res4.grid(row = 17, column = 1)
val4 = Text(window, height = 1 , width = 20)
val4.grid(row = 17, column = 2)

res5 = Label(window, text = "Critical Stress is :")
res5.grid(row = 18 , column = 1)
val5 = Text(window, height = 1 , width = 20)
val5.grid(row = 18,column = 2)

res6 = Label(window, text = "Torsional Bulking Capacity is :")
res6.grid(row = 19 , column = 1)
val6 = Text(window, height = 1 , width = 20)
val6.grid(row = 19,column = 2)


#Bending Natural Frequency Calculation

Outerdiameter3 = StringVar()
Innerdiameter3 = StringVar()
Density3 = StringVar()
Length3 = StringVar()
YM3 = StringVar()
GF3 = StringVar()

def n():
	val7.delete('1.0',END)
	I = ((3.14 / 64) * ((float(Outerdiameter3.get()))**4 - (float(Innerdiameter3.get()))**4))
	a = float((3.14/4) * ((float(Outerdiameter3.get()))**2 - (float(Innerdiameter3.get()))**2))
	w = ((float(Density3.get()))*a*(float(Length3.get())))
	natural_frequency = ((((float(GF3.get()))*(float(YM3.get()))*I) / (w*((float(Length3.get()))**4)))**0.5)*(3.14/2) 
	val7.insert(END,natural_frequency)


l13 = Label(window,text="BENDING NATURAL FREQUENCY CALCULATIONS")
l13.grid(row = 20 , column = 2)

l14 = Label(window,text = "Outer Diameter")
l14.grid(row = 21 , column = 0)
e14 = Entry(window, textvariable = Outerdiameter3)
e14.grid(row = 21 , column = 1)

l15 = Label(window,text = "Inner Diameter")
l15.grid(row = 21 , column = 2)
e15 = Entry(window, textvariable = Innerdiameter3)
e15.grid(row = 21 , column = 3)

l16 = Label(window,text = "Enter Density")
l16.grid(row = 22 , column = 0)
e16 = Entry(window, textvariable = Density3)
e16.grid(row = 22 , column = 1)

l17 = Label(window,text = "Youngs Modulus")
l17.grid(row = 22 , column = 2)
e17 = Entry(window, textvariable = YM3)
e17.grid(row = 22 , column = 3)

l17 = Label(window,text = "Gravitational Force")
l17.grid(row = 23 , column = 0)
e17 = Entry(window, textvariable = GF3)
e17.grid(row = 23 , column = 1)

l18 = Label(window,text = "Enter Length")
l18.grid(row = 23 , column = 2)
e18 = Entry(window, textvariable = Length3)
e18.grid(row = 23 , column = 3)

b4 = Button(window,text = "Calculate",command = n)
b4.grid(row = 24,column = 2)

res7 = Label(window, text = "The Natural Frequency is :" )
res7.grid(row = 25, column = 1)
val7 = Text(window, height = 1 , width = 20)
val7.grid(row = 25,column = 2)

creat = Label(window,text = "Badaruddin Shaikh\u00A9 2019",font=("Courier",9))
creat.grid(row = 27, column = 3)
window.mainloop()