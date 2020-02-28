import math
import matplotlib.pyplot as plt
from Tkinter import *
import Tkinter



    
master=Tk()
Label(master, text="Firing Angle:").grid(row=0)
Label(master, text="Firing Speed:").grid(row=1)
Label(master, text="Initial Height:").grid(row=2)

e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
e4=Entry(master)
e5=Entry(master)
e6=Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
master.title("Modelling Projectile Motion")

def Error_velocity():
    ErrorGUI=Tk()
    ErrorGUI.title("Error")
    ErrorGUI.geometry

    label=Label(ErrorGUI, text="Invalid Value for Firing Speed, please input a correct value.")
    label.grid(row=0)

def Error_degrees():
    ErrorGUI=Tk()
    ErrorGUI.title("Error")
    ErrorGUI.geometry

    label=Label(ErrorGUI, text="Invalid Value for Firing Angle, please input a correct value.")
    label.grid(row=0)

def Error_initial_height():
    ErrorGUI=Tk()
    ErrorGUI.title("Error")
    ErrorGUI.geometry

    label=Label(ErrorGUI, text="Invalid Value for Initial Height, please input a correct value.")
    label.grid(row=0)

#--------------------Calculations for values x,y-------------------------------------
def calculate_projectile_xy (velocity, angle, initial_height, gravity=9.81):
    data_xy = []
    time = 0.0
    d=1
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        data_xy.append((x, y))
        time+=0.1
    return data_xy
#------------------Puts values for x and y into an array------------------------------


def projectile_xy (velocity, angle, graphx, graphy,initial_height, gravity=9.81 ):
    data_xy = []
    time = 0.0
    d=1
    plt.rcParams['toolbar'] = 'None'
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        data_xy.append((x, y))
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity
###--------------------adjusts refresh rate of animation----------------------------------------
        if time_taken>30: 
            time_pause=0.00001
        else:
            time_pause=0.01
#---------------------------------------------------------------------------------
        if initial_height <=12:
            graphx=graphx+0.1
        elif initial_height >=20:
            graphx=graphx+1
        else:
            graphx=graphx
        
#------------------Animation------------------------------------------------------------- 

        plt.axis([0, graphx*2+20, 0, graphy+10])
        plt.ion()
        pos=0
        xlist =[x]
        ylist =[y]
       
        
        
        plt.plot(xlist, ylist, 'ro', color = "red")
        plt.pause(time_pause)
        pos=pos+1
        xlist.insert(pos,x)
        ylist.insert(pos,y)
        plt.xlabel("Horizontal Distance/m")
        plt.ylabel("Vertical Distance/m")
        plt.title("Projectile Motion Animation")

    
        
    master2=Tk()
    master2.title("Extra Information")
    
    firing_angle=round(math.degrees(angle))
    str4=str(firing_angle)
    firing_speed=round(velocity)
    str5=str(firing_speed)
    max_height=round(initial_height + (velocity**2 * math.sin(angle)**2)/(2*gravity),2)
    str1=str(max_height)
    distance_max_height=round((velocity * math.cos(angle) * time)/2,2)
    str2=str(distance_max_height)
    time_taken=round((2*(velocity*math.cos(angle)))/gravity,2)
    str3=str(time_taken)
    Horizontal_Distance=round((velocity * math.cos(angle) * time),2)
    str6=str(Horizontal_Distance)
    str7=str(initial_height)
    Label(master2, text="Initial Height: "+str7+" Metres").grid(row=6)
    Label(master2, text="Firing Angle: "+str4+" Degrees").grid(row=0)
    Label(master2, text="Firing Speed: "+str5+" Metres per Second").grid(row=2)
    Label(master2, text="Time Taken: "+str3+" Seconds").grid(row=4)
    Label(master2, text="Maximum Height Reached: "+str1+" Metres").grid(row=8)
    Label(master2, text="Hoizontal Distance Maximum Height Reached: "+str2+" Metres").grid(row=10)
    Label(master2, text="Hoizontal Distance: "+str6+" Metres").grid(row=12)

        
    return data_xy
#------------------------------------------------------------------------------------------

#------------------------------Graph-------------------------------------------------------

#--------------------Calculations for values x,y-------------------------------------
def calculate_projectile_xy_graph (velocity, angle, initial_height, gravity=9.81):
    data_xy = []
    time = 0.0
    d=1
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        data_xy.append((x, y))
        time+=0.1
    return data_xy
#------------------Puts values for x and y into an array------------------------------


def projectile_xy_graph (velocity, angle, graphx, graphy,initial_height, gravity=9.81 ):
    data_xy = []
    time = 0.0
    d=1
    f=True
    a=0
    while f==True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        data_xy.append((x, y))
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity

#------------------Graph-Distance/Distance------------------------------------------------------------- 


        plt.axis([0, graphx*2+20, 0, graphy+10])
        plt.ion()
        pos=0
        xlist =[x]
        ylist =[y]
       
        
        
        
        
        if a==1:
            if y==0:
                f=False
        else:
            a=1
        
                 
        plt.plot(xlist,ylist,'ro')
        
        pos=pos+1
        xlist.insert(pos,x)
        ylist.insert(pos,y)
        plt.xlabel("Horizontal Distance/m")
        plt.ylabel("Vertical Distance/m")
        plt.title("Distance-Distance Graph")

    master3=Tk()

    master3.title("Extra Information")
    firing_angle=round(math.degrees(angle))
    str4=str(firing_angle)
    firing_speed=round(velocity)
    str5=str(firing_speed)
    max_height=round(initial_height + (velocity**2 * math.sin(angle)**2)/(2*gravity),2)
    str1=str(max_height)
    distance_max_height=round((velocity * math.cos(angle) * time)/2,2)
    str2=str(distance_max_height)
    time_taken=round((2*(velocity*math.cos(angle)))/gravity,2)
    str3=str(time_taken)
    Horizontal_Distance=round((velocity * math.cos(angle) * time),2)
    str6=str(Horizontal_Distance)
    str4=str(initial_height)
    Label(master3, text="Firing Angle: "+str4+" Degrees").grid(row=0)
    Label(master3, text="Firing Speed: "+str5+" Metres per Second").grid(row=2)
    Label(master3, text="Time Taken: "+str3+" Seconds").grid(row=4)
    Label(master3, text="Initial Height: "+str4+" Metres").grid(row=6)
    Label(master3, text="Maximum Height Reached: "+str1+" Metres").grid(row=8)
    Label(master3, text="Hoizontal Distance Maximum Height Reached: "+str2+" Metres").grid(row=10)
    Label(master3, text="Hoizontal Distance: "+str6+" Metres").grid(row=12)
        

    return data_xy
#------------------------------------------------------------------------------------------
#------------------------------Graph-------------------------------------------------------

#--------------------Calculations for values x,y-------------------------------------
def calculate_projectile_xy_graph_dt (velocity, angle, initial_height, gravity=9.81):
    data_xt = []
    time = 0.0
    d=1
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_xt.append((x,time))
    return data_xt
#------------------Puts values for x and y into an array------------------------------


def projectile_xy_graph_dt (velocity, angle, graphx, grapht,initial_height, gravity=9.81 ):
    data_xt = []
    time = 0.0
    d=1
    g=True
    a=0
    while g==True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_xt.append((x, time))
        
        
#------------------Graph-Distance/Time------------------------------------------------------------- 


        plt.axis([0, x*2+10, 0, grapht*2])
        plt.ion()
        pos=0
        xlist =[x]
        ylist =[time]
       
        
        
        
        
        if a==1:
            if y==0:
                f=False
        else:
            a=1
        
                 
        plt.plot(xlist,ylist,'ro')
        
        pos=pos+1
        xlist.insert(pos,x)
        ylist.insert(pos,time)
        plt.xlabel("Horizontal Distance/m")
        plt.ylabel("Time Taken/s")
        plt.title("Time-Distance Graph")
        plt.show()

    master4=Tk()

    master4.title("Extra Information")
    firing_angle=round(math.degrees(angle))
    str1a=str(firing_angle)
    firing_speed=round(velocity)
    str2a=str(firing_speed)
    time_taken=round((2*(velocity*math.cos(angle)))/gravity,2)
    str3a=str(time_taken)
    Horizontal_Distance=round((velocity * math.cos(angle) * time),2)
    str4a=str(Horizontal_Distance)
    str5a=str(initial_height)
    Label(master4, text="Firing Angle: "+str1a+" Degrees").grid(row=0)
    Label(master4, text="Firing Speed: "+str2a+" Metres per Second").grid(row=2)
    Label(master4, text="Initial Height: "+str5a+" Metres").grid(row=4)
    Label(master4, text="Time Taken: "+str3a+" Seconds").grid(row=6)
    Label(master4, text="Hoizontal Distance: "+str4a+" Metres").grid(row=8)
        

    return data_xt

#------------------------------Graph-------------------------------------------------------

#--------------------Calculations for values x,y-------------------------------------
def calculate_projectile_xy_graph_yt (velocity, angle, initial_height, gravity=9.81):
    data_yt = []
    time = 0.0
    d=1
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_xt.append((y,time))
    return data_xt
#------------------Puts values for x and y into an array------------------------------


def projectile_xy_graph_yt (velocity, angle, graphx, grapht,initial_height, gravity=9.81 ):
    data_yt = []
    time = 0.0
    d=1
    g=True
    a=0
    while g==True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        time+=0.1
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_xt.append((y, time))
        
        
#------------------Graph-Distance/Time------------------------------------------------------------- 


        plt.axis([0, y+10, 0, grapht*2])
        plt.ion()
        pos=0
        xlist =[y]
        ylist =[time]
       
        
        
        
        
        if a==1:
            if y==0:
                f=False
        else:
            a=1
        
                 
        plt.plot(xlist,ylist,'ro')
        
        pos=pos+1
        xlist.insert(pos,y)
        ylist.insert(pos,time)
        plt.xlabel("Vertical Distance/m")
        plt.ylabel("Time Taken/s")
        plt.title("Time-Distance Graph")
        plt.show()

    master6=Tk()

    master4.title("Extra Information")
    firing_angle=round(math.degrees(angle))
    str1a=str(firing_angle)
    firing_speed=round(velocity)
    str2a=str(firing_speed)
    time_taken=round((2*(velocity*math.cos(angle)))/gravity,2)
    str3a=str(time_taken)
    Vertical_Distance=round((initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2),2)
    str4a=str(Vertical_Distance)
    str5a=str(initial_height)
    Label(master4, text="Firing Angle: "+str1a+" Degrees").grid(row=0)
    Label(master4, text="Firing Speed: "+str2a+" Metres per Second").grid(row=2)
    Label(master4, text="Initial Height: "+str5a+" Metres").grid(row=4)
    Label(master4, text="Time Taken: "+str3a+" Seconds").grid(row=6)
    Label(master4, text="Vertical Distance: "+str4a+" Metres").grid(row=8)
        

    return data_yt
#------------------------------------------------------------------------------------------
#------------------------------Graph-------------------------------------------------------

#--------------------Calculations for values x,y-------------------------------------
def calculate_projectile_xy_graph_vt (velocity, angle, initial_height, gravity=9.81):
    data_vt = []
    time = 0.0
    d=1
    while True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time#this is the equation used to work out the horizontal distance
        
        time+=0.1
        f_velocity=((2*x)/time)-velocity
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_vt.append((time,f_velocity))
    return data_vt
#------------------Puts values for x and y into an array------------------------------


def projectile_xy_graph_vt (velocity, angle, graphx, grapht,initial_height, gravity=9.81 ):
    data_vt = []
    time = 0.0
    d=1
    g=True
    a=0
    
    while g==True:
        y = initial_height + (time * velocity * math.sin(angle)) - (gravity * time**2)/2#this is the equation used to work out the vertical distance.
        if y < 0:            
            break #if y<0 the program wont be able to map the projectile as the projectile wouldnt have gone anywhere.
        
        x = velocity * math.cos(angle) * time
        time+=0.1
        f_velocity=((2*x)/time)-velocity#this is the equation used to work out the horizontal distance
        
        time_taken=(2*(velocity*math.cos(angle)))/gravity
        data_vt.append((time,f_velocity))
        
        
#------------------Graph-Velocity/Time------------------------------------------------------------- 


        plt.axis([0, x*2+20, 0, grapht+10])
        plt.ion()
        pos=0
        xlist =[time]
        ylist =[f_velocity]
       
        
        
        
        
        
        
                 
        plt.plot(xlist,ylist,'ro')
        
        pos=pos+1
        xlist.insert(pos,time)
        ylist.insert(pos,f_velocity)
        plt.xlabel("Time Taken/s")
        plt.ylabel("Velocity/metres per second")
        plt.title("Velocity-Time Graph")
        plt.show()

    master5=Tk()

    master5.title("Extra Information")
    firing_angle=round(math.degrees(angle))
    str1b=str(firing_angle)
    firing_speed=round(velocity)
    str2b=str(firing_speed)
    time_taken=round((2*(velocity*math.cos(angle)))/gravity,2)
    str3b=str(time_taken)
    Horizontal_Distance=round((velocity * math.cos(angle) * time),2)
    str4b=str(Horizontal_Distance)
    str5b=str(initial_height)
    Label(master5, text="Firing Angle: "+str1b+" Degrees").grid(row=0)
    Label(master5, text="Firing Speed: "+str2b+" Metres per Second").grid(row=2)
    Label(master5, text="Initial Height: "+str5b+" Metres").grid(row=4)
    Label(master5, text="Time Taken: "+str3b+" Seconds").grid(row=6)
    Label(master5, text="Hoizontal Distance: "+str4b+" Metres").grid(row=8)
        

    return data_vt
#------------------------------------------------------------------------------------------

        
        
#-----------------Functions to run graphs/animations---------------------------------------

def run_graph_vt():
    degrees=float(e1.get())
    velocity=float(e2.get())
    gravity=9.81
    initial_height=float(e3.get())
    angle=math.radians(degrees)
    

#--------------Validation----------------------------------------------------------------------

    
    try:
        velocity=float(e2.get())
        if velocity >=0 and velocity<=370:
            validvt=2
            
        else:
            validvt=1
            Error_velocity()
            
    except ValueError:
        validvt=1
        Error_velocity()
    if validvt==2:
        
        try:
            degrees=float(e1.get())
            if degrees >=0 and degrees<=90:
                validvt=2
                
            else:
                validvt=1
                Error_degrees()
                
        except ValueError:
            validvt=1
            Error_degrees()
    if validvt==2:
        try:
            initial_height=float(e3.get())
            if initial_height >=0 and initial_height<=100:
                validvt=2
                
            else:
                validvt=1
                Error_initial_height()
                
        except ValueError:
                validvt=1
                Error_initial_height()
    if validvt==2:
        time_taken=((2*(velocity*math.cos(angle)))/gravity)
        data_45=calculate_projectile_xy_graph_vt(velocity, angle, initial_height)
        point_height_max = max(data_45, key = lambda q: q[1])
        velocity, time_taken = point_height_max
        data_45 = projectile_xy_graph_vt(velocity, angle, initial_height,time_taken,gravity)

#------------------------------------------------------------------------------------------

def run_graph_dt():
    degrees=float(e1.get())
    velocity=float(e2.get())
    gravity=9.81
    initial_height=float(e3.get())
    angle=math.radians(degrees)
    time_taken=((2*(velocity*math.cos(angle)))/gravity)
   
#--------------Validation----------------------------------------------------------------------

    
    try:
        velocity=float(e2.get())
        if velocity >=0 and velocity<=370:
            validdt=2
            
        else:
            validdt=1
            Error_velocity()
            
    except ValueError:
        validdt=1
        Error_velocity()
    if validdt==2:
        
        try:
            degrees=float(e1.get())
            if degrees >=0 and degrees<=90:
                validdt=2
                
            else:
                validdt=1
                Error_degrees()
                
        except ValueError:
            validdt=1
            Error_degrees()
    if validdt==2:
        try:
            initial_height=float(e3.get())
            if initial_height >=0 and initial_height<=100:
                validdt=2
                
            else:
                validdt=1
                Error_initial_height()
                
        except ValueError:
                validdt=1
                Error_initial_height()
    if validdt==2:
         data_45=calculate_projectile_xy_graph_dt(velocity, angle, initial_height)
         point_height_max = max(data_45, key = lambda q: q[1])
         x, time_taken = point_height_max
         data_45 = projectile_xy_graph_dt(velocity, angle, x, time_taken, initial_height)

#-----------------------------------------------------------------------------------------
def run_graph_yt():
    degrees=float(e1.get())
    velocity=float(e2.get())
    gravity=9.81
    initial_height=float(e3.get())
    angle=math.radians(degrees)
    time_taken=((2*(velocity*math.cos(angle)))/gravity)
   
#--------------Validation----------------------------------------------------------------------

    
    try:
        velocity=float(e2.get())
        if velocity >=0 and velocity<=370:
            validyt=2
            
        else:
            validyt=1
            Error_velocity()
            
    except ValueError:
        validyt=1
        Error_velocity()
    if validyt==2:
        
        try:
            degrees=float(e1.get())
            if degrees >=0 and degrees<=90:
                validyt=2
                
            else:
                validyt=1
                Error_degrees()
                
        except ValueError:
            validyt=1
            Error_degrees()
    if validyt==2:
        try:
            initial_height=float(e3.get())
            if initial_height >=0 and initial_height<=100:
                validyt=2
                
            else:
                validyt=1
                Error_initial_height()
                
        except ValueError:
                validyt=1
                Error_initial_height()
    if validyt==2:
         data_45=calculate_projectile_xy_graph_yt(velocity, angle, initial_height)
         point_height_max = max(data_45, key = lambda q: q[1])
         y, time_taken = point_height_max
         data_45 = projectile_xy_graph_yt(velocity, angle, x, time_taken, initial_height)
#----------------------------------------------------------------------------------------------
    
def run_graph():
    degrees=float(e1.get())
    velocity=float(e2.get())
    gravity=9.81
    initial_height=float(e3.get())
    angle = math.radians(degrees)
    

#--------------Validation----------------------------------------------------------------------

    
    try:
        velocity=float(e2.get())
        if velocity >=0 and velocity<=370:
            valid_graph=2
            
        else:
            valid_graph=1
            Error_velocity()
            
    except ValueError:
        valid_graph=1
        Error_velocity()
    if valid_graph==2:
        
        try:
            degrees=float(e1.get())
            if degrees >=0 and degrees<=90:
                valid_graph=2
                
            else:
                valid_graph=1
                Error_degrees()
                
        except ValueError:
            valid_graph=1
            Error_degrees()
    if valid_graph==2:
        try:
            initial_height=float(e3.get())
            if initial_height >=0 and initial_height<=100:
                valid_graph=2
                
            else:
                valid_graph=1
                Error_initial_height()
                
        except ValueError:
                valid_graph=1
                Error_initial_height()
    if valid_graph==2:
        data_45 = calculate_projectile_xy_graph(velocity, angle, initial_height)
        point_height_max = max(data_45, key = lambda q: q[1])
        xm, ym = point_height_max
        time_taken=(2*(velocity*math.cos(angle)))/gravity


        data_45 = projectile_xy_graph(velocity, angle, xm, ym, initial_height)

#----------------------------------------------------------------------------------------        
    




def run_animation():
    degrees=float(e1.get())
    velocity=float(e2.get())
    gravity=9.81
    initial_height=float(e3.get())
    angle = math.radians(degrees)

#--------------Validation----------------------------------------------------------------------

    try:
        velocity=float(e2.get())
        if velocity >=0 and velocity<=370:
            valid_animation=2
            
        else:
            valid_animation=1
            Error_velocity()
            
    except ValueError:
        valid_animation=1
        Error_velocity()
    if valid_animation==2:
        
        try:
            degrees=float(e1.get())
            if degrees >=0 and degrees<=90:
                valid_animation=2
                
            else:
                valid_animation=1
                Error_degrees()
                
        except ValueError:
            valid_animation=1
            Error_degrees()
    if valid_animation==2:
        try:
            initial_height=float(e3.get())
            if initial_height >=0 and initial_height<=100:
                valid_animation=2
                
            else:
                valid_animation=1
                Error_initial_height()
                
        except ValueError:
                valid_animation=1
                Error_initial_height()
    if valid_animation==2:
        data_45 = calculate_projectile_xy(velocity, angle, initial_height) 
        point_height_max = max(data_45, key = lambda q: q[1])
        xm, ym = point_height_max
        time_taken=(2*(velocity*math.cos(angle)))/gravity

        
        data_45 = projectile_xy(velocity, angle, xm, ym, initial_height)



    


#-------------------------------------------------------------------------------------------------------        
    


Button(master, text='Animation', command=run_animation).grid(row=4, column=2, sticky=W, pady=4)
Button(master, text='Distance-Distance Graph', command=run_graph).grid(row=5, column=2, sticky=W, pady=4)
Button(master, text='Horizontal Distance-Time Graph', command=run_graph_dt).grid(row=6, column=2, sticky=W, pady=4)
Button(master, text='Vertical Distance-Time Graph', command=run_graph_dt).grid(row=7, column=2, sticky=W, pady=4)
Button(master, text='Velocity-Time Graph (Currently Under Development)', command=run_graph_vt).grid(row=8, column=2, sticky=W, pady=4)

mainloop()

