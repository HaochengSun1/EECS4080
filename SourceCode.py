import viz
import vizact
import vizproximity
import viztask
import vizinfo
import math


viz.setMultiSample(4)
viz.fov(60)

#Turn on the physics engine
viz.phys.enable()


viz.MainView.setPosition([2,5+5,-15])


# Create a Vizard window
import vizshape

#3rd
sphere1 = vizshape.addSphere()
sphere1.setPosition(5+5,5+5,0)

#first
sphere2 = vizshape.addSphere()
sphere2.setPosition(0+5,10+5,0)

#fifth 
sphere3 = vizshape.addSphere()
sphere3.setPosition(-5+5,5+5,0)

sphere4 = vizshape.addSphere()
sphere4.setPosition(0+5,0+5,0)

#second bot right
sphere5 = vizshape.addSphere()
sphere5.setPosition(3.54+5,1.46+5,0)

#4th top right
sphere6 = vizshape.addSphere()
sphere6.setPosition(3.54+5,8.54+5,0)

sphere7 = vizshape.addSphere()
sphere7.setPosition(-3.54+5,1.46+5,0)

#top left
sphere8 = vizshape.addSphere()
sphere8.setPosition(-3.54+5,8.54+5,0)


cone = vizshape.addCylinder()
cone.setPosition(-0,5,-5)
cone.setEuler(0,-100,0)
cone.setScale([3,13,3])

number_text1 = viz.addText('1', parent=sphere1, pos=[1, 0, 0])
number_text1.color(viz.YELLOW)

number_text2 = viz.addText('2', parent=sphere5, pos=[1, 0, 0])
number_text2.color(viz.YELLOW)

number_text3 = viz.addText('3', parent=sphere4, pos=[1, 0, 0])
number_text3.color(viz.YELLOW)

number_text4 = viz.addText('4', parent=sphere7, pos=[1, 0, 0])
number_text4.color(viz.YELLOW)

number_text5 = viz.addText('5', parent=sphere3, pos=[1, 0, 0])
number_text5.color(viz.YELLOW)

number_text6 = viz.addText('6', parent=sphere8, pos=[1, 0, 0])
number_text6.color(viz.YELLOW)

number_text7 = viz.addText('7', parent=sphere6, pos=[1, 0, 0])
number_text7.color(viz.YELLOW)

number_text8 = viz.addText('8', parent=sphere2, pos=[1, 0, 0])
number_text8.color(viz.YELLOW)


#Turn off mouse navigation.
viz.mouse.setOverride(viz.ON)
#Turn it back on.
viz.mouse.setOverride(viz.OFF)
#Print out the current state of mouse navigation.
print( viz.mouse.getOverride())

def onMouseMove(e):
    x,y= viz.mouse.getPosition()
    cone.setPosition(20*x,20*y,0)
viz.callback(viz.MOUSE_MOVE_EVENT,onMouseMove)

# Set the color of sphere2 to red
sphere2.color(1, 0, 0)

# Global variables for collision flags
collide = False
collide2 = False
collide3 = False
collide4 = False
collide5 = False
collide6 = False
collide7 = False
collide8 = False

start_time = 0
print(cone.getPosition)

# Function to check the first intersection
def check_collision():
    global collide
    info = viz.intersect([3 + 1, 15 - 1, 0], [3.9 + 1, 15 - 1, 0])
    if info.valid:
        collide = True
        print('First intersection success!!')
        sphere2.color(1, 1, 1)  # Set the color to white
        stop_timer()
        global elapsed_time
        elapsed_time = viz.tick() - start_time
        print(f'Time taken for first collision: {elapsed_time} seconds')
        distance1 = 5
        print(f'Distance traveled: ' ,distance1)
        print('IP = ', round(math.log2(2 * distance1 / elapsed_time), 2))
        start_second_timer()
        print()
        print('move from 8 to 2')

# Create a timer for the first intersection check
print()
print('move to 8')
print()
timer = vizact.ontimer(0.01, check_collision)

# Function to stop the first timer
def stop_timer():
    global timer
    timer.setEnabled(False)

# Function to start the second timer
def start_second_timer():
    global timer2
    timer2.setEnabled(True)

# Function to check the second intersection
def second_intersection_check():
    sphere5.color(1, 0, 0)

    info = viz.intersect([3.54 + 4, 1.46 + 5 + 1, 0], [3.54 + 4, 1.46 + 5 + 1.1, 0])

    if info.valid:
        global collide2
        collide2 = True
        sphere5.color(1, 1, 1)  # Set the color to white
        print()
        print( 'Second intersection success!!')
        stop_timer2()
        global elapsed_time2
        elapsed_time2 = viz.tick() - elapsed_time
        print(f'Time taken for second collision: {elapsed_time2} seconds')
        distance2 = 9.24
        print(f'Distance traveled: ' ,distance2)
        print('IP = ', round(math.log2(2 * distance2 / elapsed_time2), 2))
        start_third_timer()
        print()
        print('move from 2 to 1')

# Create a timer for the second intersection check, initially disabled

timer2 = vizact.ontimer(0.01, second_intersection_check)
timer2.setEnabled(False)

# Function to stop the second timer
def stop_timer2():
    global timer2
    timer2.setEnabled(False)

# Function to start the third timer
def start_third_timer():
    global timer3
    timer3.setEnabled(True)

# Function to check the third intersection
def third_intersection_check():
    sphere1.color(1, 0, 0)

    info = viz.intersect([10, 8.9, 0], [10, 8.8, 0])

    if info.valid:
        global collide3
        collide3 = True
        print()
        print('Third intersection success!!')
        sphere1.color(1, 1, 1)  # Set the color to white
        stop_timer3()
        global elapsed_time3
        elapsed_time3 = viz.tick() - elapsed_time2 - elapsed_time
        print(f'Time taken for third collision: {elapsed_time3} seconds')
        distance3 = 3.83
        print(f'Distance traveled: ' ,distance3)
        print('IP = ', round(math.log2(2 * distance3 / elapsed_time3), 2))
        start_fourth_timer()
        print()
        print('move from 1 to 7')

# Create a timer for the third intersection check, initially disabled
timer3 = vizact.ontimer(0.01, third_intersection_check)
timer3.setEnabled(False)

# Function to stop the third timer
def stop_timer3():
    global timer3
    timer3.setEnabled(False)

def stop_timer4():
    global timer4
    timer4.setEnabled(False)

def stop_timer5():
    global timer5
    timer5.setEnabled(False)

def stop_timer6():
    global timer6
    timer6.setEnabled(False)

def stop_timer7():
    global timer7
    timer7.setEnabled(False)

def stop_timer8():
    global timer8
    timer8.setEnabled(False)



def start_fourth_timer():
    global timer4
    timer4.setEnabled(True)

def start_fifth_timer():
    global timer5
    timer5.setEnabled(True)

def start_sixth_timer():
    global timer6
    timer6.setEnabled(True)

def start_seventh_timer():
    global timer7
    timer7.setEnabled(True)

def start_eighth_timer():
    global timer8
    timer8.setEnabled(True)


# Function to check the fourth intersection
def fourth_intersection_check():
    sphere6.color(1, 0, 0)

    info = viz.intersect([3.54+5-1,8.54+5-1,0], [3.54+5-1,8.54+5-1.1,0])
    if info.valid:
        global collide4
        collide4 = True
        print()
        print('Fourth intersection success!!')
        global elapsed_time4
        elapsed_time4 = viz.tick() - elapsed_time3 - elapsed_time2 - elapsed_time
        print(f'Time taken for fourth collision: {elapsed_time4} seconds')
        distance4 = 3.83
        print(f'Distance traveled: ' ,distance4)
        print('IP = ', round(math.log2(2 * distance4 / elapsed_time4), 2))
        sphere6.color(1, 1, 1)  # Set the color to white
        stop_timer4()
        start_fifth_timer()
        print()
        print('move from 7 to 5')

# Create a timer for the fourth intersection check, initially disabled
timer4 = vizact.ontimer(0.01, fourth_intersection_check)
timer4.setEnabled(False)

# Function to check the fifth intersection
def fifth_intersection_check():
    sphere3.color(1, 0, 0)

    #-5+5,5+5,0
    info = viz.intersect([1.1, 10, 0], [1, 10 , 0])
    if info.valid:
        global collide5
        collide5 = True
        print()
        print('Fifth intersection success!!')
        global elapsed_time5
        elapsed_time5 = viz.tick() - elapsed_time4 - elapsed_time3 - elapsed_time2 - elapsed_time
        print(f'Time taken for fifth collision: {elapsed_time5} seconds')
        distance5 = 9.24
        print(f'Distance traveled: ' ,distance5)
        print('IP = ', round(math.log2(2 * distance5 / elapsed_time5), 2))
        sphere3.color(1, 1, 1)  # Set the color to white
        stop_timer5()
        start_sixth_timer()
        print()
        print('move from 5 to 3')

# Create a timer for the fifth intersection check, initially disabled
timer5 = vizact.ontimer(0.01, fifth_intersection_check)
timer5.setEnabled(False)


# Function to check the sixth intersection
def sixth_intersection_check():
    sphere4.color(1, 0, 0)
    #5 5 0
    info = viz.intersect([5, 6.1, 0], [5, 6.2, 0])
    if info.valid:
        global collide6
        collide6 = True
        print()
        print('Sixth intersection success!!')
        global elapsed_time6
        elapsed_time6 = viz.tick() - elapsed_time5 - elapsed_time4 - elapsed_time3 - elapsed_time2 - elapsed_time
        print(f'Time taken for sixth collision: {elapsed_time6} seconds')
        distance6 = 7.07
        print(f'Distance traveled: ' ,distance6)
        print('IP = ', round(math.log2(2 * distance6 / elapsed_time6), 2))
        sphere4.color(1, 1, 1)  # Set the color to white
        stop_timer6()
        start_seventh_timer()
        print()
        print('move from 3 to 6')

# Create a timer for the sixth intersection check, initially disabled
timer6 = vizact.ontimer(0.01, sixth_intersection_check)
timer6.setEnabled(False)

# Function to check the seventh intersection
def seventh_intersection_check():
    sphere8.color(1, 0, 0)
    
    #-3.54+5,8.54+5,0
    info = viz.intersect([1.46+0.7, 8.54+5-1, 0], [-3.54+5+1, 13.54 -0.7, 0])
    if info.valid:
        global collide7
        collide7 = True
        print()
        print('Seventh intersection success!!')
        global elapsed_time7
        elapsed_time7 = viz.tick() - elapsed_time6  - elapsed_time5 - elapsed_time4 - elapsed_time3 - elapsed_time2 - elapsed_time
        print(f'Time taken for seventh collision: {elapsed_time7} seconds')
        distance7 = 9.24
        print(f'Distance traveled: ' ,distance7)
        print('IP = ', round(math.log2(2 * distance7 / elapsed_time7), 2))
        sphere8.color(1, 1, 1)  # Set the color to white
        stop_timer7()
        start_eighth_timer()
        print()
        print('move from 6 to 4')

# Create a timer for the seventh intersection check, initially disabled
timer7 = vizact.ontimer(0.01, seventh_intersection_check)
timer7.setEnabled(False)


# Function to check the eighth intersection
def eighth_intersection_check():
    sphere7.color(1, 0, 0)
    #-3.54+5,1.46+5,0
    info = viz.intersect([-3.54+5+0.7, 1.46+5+1, 0], [-3.54+5+1, 1.46+5 + 0.7, 0])
    if info.valid:
        global collide8
        collide8 = True
        print()
        print('Eighth intersection success!!')
        global elapsed_time8
        elapsed_time8 = viz.tick() - elapsed_time7- elapsed_time6  - elapsed_time5 - elapsed_time4 - elapsed_time3 - elapsed_time2 - elapsed_time
        print(f'Time taken for eighth collision: {elapsed_time8} seconds')
        distance8 = 7.08
        print(f'Distance traveled: ' ,distance8)
        print('IP = ', round(math.log2(2 * distance8 / elapsed_time8), 2))
        sphere7.color(1, 1, 1)  # Set the color to white
        stop_timer8()
        

# Create a timer for the eighth intersection check, initially disabled
timer8 = vizact.ontimer(0.01, eighth_intersection_check)
timer8.setEnabled(False)



viz.go()