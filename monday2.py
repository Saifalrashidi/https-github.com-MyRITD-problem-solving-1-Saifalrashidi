import turtle 


def rectangle_activity(): #1st house with a roof.
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.end_fill()
    




def triangle_activity():
    turtle.pencolor("seagreen")
    turtle.fillcolor("seagreen")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(140)
    turtle.end_fill()
    



def house():
    rectangle_activity()
    triangle_activity()
    



def lollipop():
    turtle.pencolor("darkred")
    turtle.fillcolor("darkred")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(250)
    turtle.end_fill()
    turtle.right(180)
    turtle.forward(240)
    turtle.pencolor("seagreen")
    turtle.fillcolor("seagreen")
    turtle.right(90)
    turtle.forward(25)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
   


def house2():
    turtle.down()
    turtle.pencolor("aqua")
    turtle.fillcolor("aqua")
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(120)
    turtle.pencolor("gold")
    turtle.fillcolor("gold")
    turtle.begin_fill()
    turtle.left(45)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.end_fill()


def window1():
    turtle.speed(10)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.down()
    turtle.pencolor("beige")
    turtle.fillcolor("beige")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()


    turtle.up()
    turtle.right(90)
    turtle.forward(100)
    turtle.down()
    turtle.pencolor("beige")
    turtle.fillcolor("beige")
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.up()
    
def door_house1():
    turtle.up()
    turtle.right(90)
    turtle.forward(-50)
    turtle.right(90)
    turtle.forward(30)
    turtle.down()
    turtle.pencolor("aqua")
    turtle.fillcolor("aqua")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()
    turtle.up()
    turtle.home()
    turtle.forward(-150)
    turtle.right(90)
    turtle.forward(35)
    turtle.down()
    turtle.right(90)
    turtle.forward(30)
   

def door_window2(): #from here its not working, the pen is not going down for some reason 
    turtle.color('grey')
    turtle.begin_fill()
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(40)
    turtle.down()
    turtle.color('grey')
    turtle.begin_fill()
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    turtle.color('grey')
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.right(90)
    turtle.forward(-60)
    turtle.down()
    turtle.color('grey')
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(-40)  #change the place of the door
    turtle.down
    turtle.pencolor("peru")
    turtle.fillcolor("peru")
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(20)
    turtle.up()
    turtle.down()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(20)
    turtle.up()
    turtle.end_fill()

    
    
    
    

   
    
    
    
   


    

    
   


















def main():
    house()
    turtle.up()
    turtle.left(45)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    lollipop()
    turtle.up()
    turtle.home()
    turtle.right(180)
    turtle.forward(120)
    turtle.down()
    house2()
    turtle.up()
    turtle.home()
    window1()
    
    door_house1()
    
    door_window2()
    turtle.done()


    
   
    


    
main()
