
import turtle
import random 
turtle.tracer(1,0) #This helps the turtle move more smoothly        
SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
count=0
turtle.penup()
SQUARE_SIZE = 60
global START_LENGTH 
START_LENGTH = 1
writer=turtle.clone()
LENGTH = [START_LENGTH]
textturtle=turtle.clone()
textturtle.hideturtle()
textturtle.penup()
textturtle.goto(0,-350)
turtle.addshape("Calebb.gif")
border = turtle.clone()
border.shape("Calebb.gif")
border.penup()
border.goto(300,300)
border.pendown()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
textturtle.write(int(len(stamp_list)),align="center",font=("times",33,"bold"))

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
turtle.addshape("Calebb.gif")
snake.shape("Calebb.gif")
snake.color("black")
turtle.register_shape("599e10b2a05d6.image.gif")
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script
turtle.bgpic("599e10b2a05d6.image.gif")
food = turtle.clone()
food.shape("Calebb.gif") 
food.ht()

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]         #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
    
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(my_pos[0],my_pos[1]) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    SNAKE= snake.stamp()
    stamp_list.append(SNAKE)
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!
UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
Left=1
Down=2
Right=3
direction= UP
def check_eat():
    if len(pos_list)!=len(set(pos_list)):
        writer.ht()
        FONT = ('Arial',60,'normal')
        writer.color("white") 
        writer.goto(-200,0)
        writer.write("Game Over",font=FONT)
        quit()
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP
    
    #Change direction to up
 #Update the snake drawing <- remember me later
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW) # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()
def down():
    global direction #snake direction is global (same everywhere)
    direction=Down #Change direction to up #Update the snake drawing <- remember me later
    print("You pressed the down key!")
turtle.onkeypress(down, DOWN_ARROW)
turtle.listen()
def left():
    global direction #snake direction is global (same everywhere)
    direction=Left #Change direction to up
#Update the snake drawing <- remember me later
    print("You pressed the left key!")
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()
def right():
    global direction #snake direction is global (same everywhere)
    direction=Right #Change direction to up
 #Update the snake drawing <- remember me later
    print("You pressed the right key!")
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
    
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=(LEFT_EDGE/SQUARE_SIZE)+1
    max_x=(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=(DOWN_EDGE/SQUARE_SIZE)+1
    max_y=(UP_EDGE/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y =  random.randint(min_x,max_x)*SQUARE_SIZE
    food.goto(food_x,food_y)
    global food_stamps
    Fod=food.stamp()
    foodpos=food.pos()
    food_pos.append(foodpos)
    food_stamps.append(Fod)
    
    
    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
                  
def move_snake():
    global direction
    global count
    color = ["red","orange","pink","purple","black","blue","yellow"]
    snake.color(color[(count)%7])
    count+=1
    eatan = False
    global UP_EDGE
    UP_EDGE = 300
    global DOWN_EDGE
    DOWN_EDGE = -300
    global RIGHT_EDGE
    RIGHT_EDGE = 300
    global LEFT_EDGE
    LEFT_EDGE = -300
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==Right:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("you moved right!")
    elif direction==Left:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("you moved left!")
    if direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("you moved up!")
    elif direction==Down:
         snake.goto(x_pos, y_pos - SQUARE_SIZE)
         print("you moved down")
    



    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                                     #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("you have eaten the food!")
        textturtle.clear()          
        textturtle.write(int(len(stamp_list)),align="center",font=("times",33,"bold"))          
        global START_LENGTH 
        START_LENGTH = START_LENGTH + 1
        eatan = True
        make_food()
        
    
    #HINT: This if statement may be useful for Part 8
    if eatan != True:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
    


    
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the right edge! GAME OVER!")
        writer.ht()
        FONT = ('Arial',60,'normal')
        writer.color("white") 
        writer.goto(-200,0)
        writer.write("Game Over",font=FONT)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! GAME OVER!")
        writer.ht()
        FONT = ('Arial',60,'normal')
        writer.color("white") 
        writer.goto(-200,0)
        writer.write("Game Over",font=FONT)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("you hit the up edge! GAME OVER!")
        writer.ht()
        FONT = ('Arial',60,'normal')
        writer.color("white") 
        writer.goto(-200,0)
        writer.write("Game Over",font=FONT)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit the down edge! GAME OVER!")
        writer.ht()
        FONT = ('Arial',60,'normal')
        writer.color("white") 
        writer.goto(-200,0)
        writer.write("Game Over",font=FONT)
        quit()
        

     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE     
    check_eat()

    #while len(food_pos) < :
     #   make_food()
        

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()


#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]        
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    id_stamp=food.stamp()
    food_stamps.append(id_stamp)
    ####WRITE YOUR CODE HERE!!


turtle.mainloop()
