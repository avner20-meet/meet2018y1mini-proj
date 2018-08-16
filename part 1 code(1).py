
import turtle
import random
import time

turtle.tracer(1,0)

window_size_x=1920
window_size_y=1080

turtle.setup(window_size_x,window_size_y)
global score
score = 0

from pygame import mixer 

mixer.init()
mixer.music.load('whackamole.mp3')
mixer.music.play()

turtle.addshape("hammer.gif")
hammer=turtle.clone()
hammer.shape("hammer.gif")
hammer.penup()

trash=turtle.clone()
teachers=turtle.clone()
screen=turtle.clone()
writer=turtle.clone()

turtle.register_shape("heart.gif")
turtle.register_shape("trash.gif")
turtle.register_shape("Calebb.gif")
turtle.register_shape("backpack.gif")

teachers.shape("Calebb.gif")
turtle.addshape("heart.gif")
turtle.bgpic("backpack.gif")
trash = turtle.clone()
turtle.addshape("trash3.gif")
trash.shape("trash3.gif")
trash.penup()
#first heart 
heart = turtle.clone()
heart.shape("heart.gif")
heart.penup()
heart.goto(-700,400)
#second heart
heart2 = turtle.clone()
heart2.shape("heart.gif")
heart2.penup()
heart2.goto(-770,400)
#third heart
heart3= turtle.clone()
heart3.shape("heart.gif")
heart3.penup()
heart3.goto(-840,400)
turtle.undo()
heart.penup()
writer.penup()
teachers.penup()

Death=0
hole_loc = [(483,293),(-14,289),(-512,292),(595,91),(185,87),(-217,90),(-633,88),(496,-220),(-20,-224),(-537,-222)]
trash_list = [trash, trash.clone()]
caleb_list = [teachers, teachers.clone()]
trash_hole = []
caleb_hole = []
def show_trash():
    global trash_hole
    trash_hole = []
    for t in trash_list:
        hole = random.randint(0,9)
        while hole in trash_hole or hole in caleb_hole:
            hole = random.randint(0,9)
        trash_hole.append(hole)
        t.goto(hole_loc[hole])
        

def show_caleb():
    global caleb_hole
    caleb_hole = []
    for c in caleb_list:
        hole = random.randint(0,9)
        while hole in trash_hole or hole in caleb_hole:
            hole = random.randint(0,9)
        caleb_hole.append(hole)
        c.goto(hole_loc[hole])

def end_timer():
    show_trash()
    show_caleb()
    print(caleb_hole+trash_hole)
    turtle.ontimer(end_timer, 3000)
    

def click(x,y):
    global Death, score, play
    play = False
    hammer.goto(x,y)
    x=hammer.pos()[0]
    y=hammer.pos()[1]
    z=30
    click_trash = False
    for t in trash_list:
        if x in range (t.pos()[0]-z,t.pos()[0]+z) and y in range (t.pos()[1]-z,t.pos()[1]+z):
            show_trash()
            turtle.undo()
            turtle.hideturtle()
            turtle.penup()
            turtle.color('red')
            score+=1
            turtle.goto(900,450)
            turtle.write(score, move=False, align='left', font= ('Arial', 30,'normal'))
            click_trash = True
    if not click_trash:
        Death+=1
        for c in caleb_list:
            if x in range (c.pos()[0]-z,c.pos()[0]+z) and y in range (c.pos()[1]-z,c.pos()[1]+z):
                show_caleb()
        if Death == 1 :
            heart.ht()
        elif Death == 2 :
            heart2.ht()
        elif Death == 3 :
            heart3.ht()
            writer.ht()
            FONT = ('Arial',60,'normal')
            writer.color("white") 
            writer.goto(-200,0)
            writer.write("Game Over",font=FONT)
            return quit()
#for i in rang (0,  
turtle.onscreenclick(click)
end_timer()


show_trash()
show_caleb()


turtle.mainloop()
                      
