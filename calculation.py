from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math


GUI = Tk()
GUI.title('โปรแกรมคำนวณ Beam')
GUI.geometry('1000x600')
########################################


########################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = Frame(Tab)
T5 = Frame(Tab)
T6 = Frame(Tab)

Tab.pack(fill=BOTH,expand=1)
Tab.add(T1,text = 'Box')
Tab.add(T2,text = 'Sphere')
Tab.add(T3,text = 'Cylinder')
Tab.add(T4,text = 'Cube')
Tab.add(T5,text = 'Capsule')
Tab.add(T6,text = 'SquarePyramid')



#####################Tab1#######################
img_box = PhotoImage(file='box.png')
logo_box = ttk.Label(T1,text ='Box',image=img_box)
logo_box.pack()

F1 = Frame(T1)
F1.pack()

value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
FONT1 = ('TH Sarabun New',20,'bold')

############
E1 = ttk.Entry(F1,textvariable = value1)
E1.grid(column=1,row=0,pady=10)
L1 = ttk.Label(F1,text= 'ความกว้าง',font = FONT1)
L1.grid(column=0,row=0)
############
E2 = ttk.Entry(F1,textvariable = value2)
E2.grid(column=1,row=1,pady=10)
L2 = ttk.Label(F1,text= 'ความยาว',font = FONT1)
L2.grid(column=0,row=1)
############
E3 = ttk.Entry(F1,textvariable = value3)
E3.grid(column=1,row=2,pady=10)
L3 = ttk.Label(F1,text= 'ความสูง',font = FONT1)
L3.grid(column=0,row=2)

def Calc():
    v1 = float(value1.get())
    v2 = float(value2.get())
    v3 = float(value3.get())
    cal = v1 *v2 *v3
    textshow = f'กล่องชิ้นนี้มีปริมาตร : {cal:,.2f} ลบ.ม'
    v_result.set(textshow)

B1 = ttk.Button(T1,text = 'Calculate',command = Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

v_result =StringVar()
v_result.set('--------Result-------')
Result = ttk.Label(T1,textvariable =v_result,foreground = 'green',font =FONT1)
Result.pack()
#####################Tab1#######################


#####################Tab2#######################
img_sphere = PhotoImage(file='volumesphere.png')
logo1 = ttk.Label(T2,image=img_sphere)
logo1.pack()

F2 = Frame(T2)
F2.pack()

def Volumesphere():
    r = float(circle_value.get())
    cal = (4/3)*(22/7)*(r**3)
    textshow = f'รัศมีทรงกลมยาว{r}เมตร จะมีปริมาตร: {cal:,.2f} ลบ.ม'
    c_result.set(textshow)


circle_value = StringVar()
C1 = ttk.Entry(F2,textvariable = circle_value)
C1.grid(column=1,row=0,pady=10)
M1 = ttk.Label(F2,text= '(1) รัศมี : ',font = FONT1)
M1.grid(column=0,row=0)
B2 = ttk.Button(T2,text = 'Calculate',command = Volumesphere)
B2.pack(ipadx=20,ipady=10,pady=10)
c_result = StringVar()
c_result.set('--------Result-------')
Result1 = ttk.Label(T2,textvariable =c_result,foreground = 'green',font =FONT1)
Result1.pack()
#####################Tab2#######################

#####################Tab3#######################
img_cylinder = PhotoImage(file='vloumecylinder.png')
logo2 = ttk.Label(T3,image=img_cylinder)
logo2.pack()

F3 = Frame(T3)
F3.pack()

def Volumecylinder():
    r = float(cylinder_value.get())
    h = float(hight_valvue.get())
    cal = (22/7)*(r**2)*h
    textshow = f'ทรงกระบอกมีรัศมียาว{r}เมตร สูง{h}เมตร จะมีปริมาตร: {cal:,.2f} ลบ.ม'
    CY_result.set(textshow)


cylinder_value = StringVar()
hight_valvue = StringVar()
CY1 = ttk.Entry(F3,textvariable = cylinder_value)
CY1.grid(column=1,row=0,pady=10)
Ra1 = ttk.Label(F3,text= '(1) รัศมี : ',font = FONT1)
Ra1.grid(column=0,row=0)
CY2 = ttk.Entry(F3,textvariable = hight_valvue)
CY2.grid(column=1,row=1,pady=10)
Ra2 = ttk.Label(F3,text= '(2) ความสูง : ',font = FONT1)
Ra2.grid(column=0,row=1)
B3 = ttk.Button(T3,text = 'Calculate',command = Volumecylinder)
B3.pack(ipadx=20,ipady=10,pady=10)
CY_result = StringVar()
CY_result.set('--------Result-------')
Result2 = ttk.Label(T3,textvariable =CY_result,foreground = 'green',font =FONT1)
Result2.pack()
#####################Tab3#######################

#####################Tab4#######################
img_cube = PhotoImage(file='cube.png')
logo_cube = ttk.Label(T4,text ='Cube',image=img_cube)
logo_cube.pack()

F4 = Frame(T4)
F4.pack()

valuecube = StringVar()


############
ECB1 = ttk.Entry(F4,textvariable = valuecube)
ECB1.grid(column=1,row=0,pady=10)
LCB1 = ttk.Label(F4,text= 'ความยาวด้าน : ',font = FONT1)
LCB1.grid(column=0,row=0)


def CubeCalc():
    v1 = float(valuecube.get())

    cal = v1 *v1 *v1
    textshow = f'ลูกบาศก์ชิ้นนี้มีปริมาตร : {cal:,.2f} ลบ.ม'
    cube_result.set(textshow)

BCB1 = ttk.Button(T4,text = 'Calculate',command = CubeCalc)
BCB1.pack(ipadx=20,ipady=10,pady=10)

cube_result =StringVar()
cube_result.set('--------Result-------')
Resultcube = ttk.Label(T4,textvariable =cube_result,foreground = 'green',font =FONT1)
Resultcube.pack()
#####################Tab4#######################

#####################Tab5#######################
img_cap = PhotoImage(file='capsule.gif')
logo_cap = ttk.Label(T5,text ='Cap',image=img_cap)
logo_cap.pack()

F5 = Frame(T5)
F5.pack()

valuecap1 = StringVar()
valuecap2 = StringVar()


############
ECa1 = ttk.Entry(F5,textvariable = valuecap1)
ECa1.grid(column=1,row=0,pady=10)
LCa1 = ttk.Label(F5,text= 'ความยาว(a) : ',font = FONT1)
LCa1.grid(column=0,row=0)
ECa2 = ttk.Entry(F5,textvariable = valuecap2)
ECa2.grid(column=1,row=1,pady=10)
LCa2 = ttk.Label(F5,text= 'ความยาวรัศมี(r) : ',font = FONT1)
LCa2.grid(column=0,row=1)



def CapCalc():
    v1 = float(valuecap1.get())
    v2 = float(valuecap2.get())
 

    cal = math.pi*(v2*v2)*(((4/3)*v2)+v1)
    textshow = f'แคปซูลชิ้นนี้มีปริมาตร : {cal:,.2f} ลบ.ม'
    cap_result.set(textshow)

BCa1 = ttk.Button(T5,text = 'Calculate',command = CapCalc)
BCa1.pack(ipadx=20,ipady=10,pady=10)

cap_result =StringVar()
cap_result.set('--------Result-------')
Resultcap = ttk.Label(T5,textvariable =cap_result,foreground = 'green',font =FONT1)
Resultcap.pack()
#####################Tab5#######################

#####################Tab6#######################
img_pyramids = PhotoImage(file='pyramids.png')
logo_pyramids = ttk.Label(T6,text ='pyramids',image=img_pyramids)
logo_pyramids.pack()

F6 = Frame(T6)
F6.pack()

valueps1 = StringVar()
valueps2 = StringVar()


############
EPs1 = ttk.Entry(F6,textvariable = valueps1)
EPs1.grid(column=1,row=0,pady=10)
LPs1 = ttk.Label(F6,text= 'ความยาวฐาน : ',font = FONT1)
LPs1.grid(column=0,row=0)
EPs2 = ttk.Entry(F6,textvariable = valueps2)
EPs2.grid(column=1,row=1,pady=10)
LPs2 = ttk.Label(F6,text= 'ความสูง : ',font = FONT1)
LPs2.grid(column=0,row=1)



def PsCalc():
    v1 = float(valueps1.get())
    v2 = float(valueps2.get())


    cal = (1/3)* (v1 *v1) *v2
    textshow = f'พีระมิดชิ้นนี้มีปริมาตร : {cal:,.2f} ลบ.ม'
    Ps_result.set(textshow)

BPs1 = ttk.Button(T6,text = 'Calculate',command = PsCalc)
BPs1.pack(ipadx=20,ipady=10,pady=10)

Ps_result =StringVar()
Ps_result.set('--------Result-------')
Resultps= ttk.Label(T6,textvariable =Ps_result,foreground = 'green',font =FONT1)
Resultps.pack()
#####################Tab6#######################

GUI.mainloop()
