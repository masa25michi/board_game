#Student Name: Masamichi tanaka
#Student ID: 14116974D
#File Name: MASAMICHI_TANAKA_14116974D.py

'''
The name of this game is called 'Flip It'

The reference of this game is based on this website:
http://www.4399.com/flash/8307_3.htm

Click the 'Start' button to start the game

------------------------------------------------------------------------------
-----
Rule
-----

The rule of this game is let the player to try to change all the color of the squares to white color.
If the player clicks one of the squares on the windows screen, its color would change from white to black or black to white,
and its around sqaures would be also changed in cross shape, and not in diagonal shape.
However, if the square the player clicked is located on the corner of the table, the squares next to that chosen square whould be changed.


------------------------------------------------------------------------------

The main modules that I usedare graphics and random

Step1: Create the window with size of 400 and 400.
Step2: Using for loop to update the level difficulties of the game.
Step3: Create a button for starting the game. After player clicked that button, the game would be started.
Step4: Create the window with size of 500 and 500, again.
Step5: Decides the list of colors to print out the squares.
Step6: Put the color into parameter of function, called background and create a table with calling several funtions, centerPoint(), rectangle(),Easy_drawRectangle(), and Hard_drawRectangle()
Step7: Get the center of Points of each rectangles for creating background table by using centerPoint() function
Step8: Create the rectangles by using points of center and width and height of each squares, which are 1, and return the list of rectangles.
Step9: Decide the difficulty of the table by choosing a function from Easy_drawRectangle() and Hard_drawRectangle()
Step10: Create main function to get the list of colors, list of rectangles with two points of each rectangles, and the list of rectangles, which is already using draw(win) from background()
Step11: Get the location of the point and knowing which square is choosen by clicking on the window by using the function called pointLocation()
Step12: Change the color of the square that player clicked and its around by using changecolor() function and changeAround() function.
Step13: If all the color of the squares are white, clear all the contents without that window, by using undraw() of graphics.py
Step14: Go to the next level of this game

------------------------------------------------------------------------------

Enjoy the Game!!

------------------------------------------------------------------------------
'''



import graphics
from graphics import *
import random
from random import*




def centerPoint(num_width,num_height):
    '''Return the list point of center of each rectangles'''
    point=[]
    width=2.5    #start the rectangle from point width= 2.5
    height=2.5   #start the rectangle from point height= 2.5
    for i in range(num_height):
        for j in range(num_width):
            point.append([width,height])
            width+=1
        height+=1
        width=2.5

    return point
            
def rectangle(point,width,height):
    '''Return the list of points which contain the list of two points to create the square'''
    
    rectangle=[]
    for j in point:
        x=j[0]  #width 
        y=j[1]  #height
        p1=Point(x-width/2, y-height/2)
        p2=Point(x+width/2, y+height/2)
        rectangle.append([p1,p2])


    return rectangle


def pointLocation (x,y,list_rectangle):
    '''Return the location of the square where player clicked, starting from number 0 to len(list_rectangle)-1'''
    count=0
    for i in list_rectangle:
        p1=i[0]
        p2=i[1]
        if p1.x< x < p2.x and p1.y< y < p2.y:
            return count

        else:
            count+=1

def Easy_drawRectangle(rectangle,color):
    '''Draw the easy rectangle table'''
    
    count=0
    after_color=[]
    rectangle_list=[]
    for i in rectangle:
        p1=i[0]
        p2=i[1]
        rec=Rectangle(p1,p2)
        rec.setFill(color[count])
        after_color.append(color[count]) #Remember the each squares' color into one list, named after_color
        rec.setOutline('sky blue')
        rec.draw(win)
        count+=1
        rectangle_list.append(rec)
    return after_color, rectangle_list

def Hard_drawRectangle(rectangle,color):
    '''Draw the harder rectangle table'''
    
    after_color=[]
    rectangle_list=[]
    for j in rectangle:
        p1=j[0]
        p2=j[1]
        shuffle(color)   #shuffle the color
        rec=Rectangle(p1,p2)
        rec.setFill(color[0])
        rec.setOutline('sky blue')
        after_color.append(color[0])
        rec.draw(win)
        rectangle_list.append(rec)   #append all the squares which are already draw(win) into the list, named rectangle_list

    return after_color,rectangle_list
    

def changecolor(num,Whole_Rectangle,after_color):
    '''Change the color of square that player clicked'''
    
    if after_color[num] == 'white':
        color='black'
    elif after_color[num] == 'black':
        color='white'
    rec=Whole_Rectangle[num]  #locate the square that player clicked
    rec.setFill(color)  
    
    after_color[num]=color  #memorize the color that just changed by the player
    

    return after_color


def changeAround(num,Whole_Rectangle,after_color):
    '''
       Change the color around the square that player clicked
       right: Change the color of right hand side of that square
       left:  Change the color of left hand side of that square
       up:    Change the color of up one of that square
       down:  Change the color of down one of that square

       return the list of colors that just changed by the player on the table
    '''
    
    
    rectangle=Whole_Rectangle  #list of all the rectangles
    if num%num_width==0 and num != len(rectangle)-(len(rectangle)/num_height) and num!=0:
        right=num+1   
        after_color=changecolor(right,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color

    elif (num+1)%num_width==0 and(num+1)!=num_width and num!=len(rectangle)-1:
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color
    elif 0<(num-1)<len(rectangle) and 0<(num+1)<len(rectangle) and 0<(num+num_width)<len(rectangle) and 0<(num-num_width)< len(rectangle):
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        right=num+1
        after_color=changecolor(right,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color

    
    elif num==0:
        right=num+1
        after_color=changecolor(right,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)

        return after_color


    elif 0 < num < (len(rectangle)/num_height)-1:
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        right=num+1
        after_color=changecolor(right,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)

        return after_color
    
    elif len(rectangle)-(len(rectangle)/num_height) < num < len(rectangle)-1:
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        right=num+1
        after_color=changecolor(right,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color



    elif num==len(rectangle)-1:
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color

    elif num==num_width-1:
        left=num-1
        after_color=changecolor(left,rectangle,after_color)
        up=num+num_width
        after_color=changecolor(up,rectangle,after_color)

        return after_color

    elif num==len(rectangle)-(len(rectangle)/num_height):
        right=num+1
        after_color=changecolor(right,rectangle,after_color)
        down=num-num_width
        after_color=changecolor(down,rectangle,after_color)

        return after_color
            
            
            



    
def congratulation(Whole_Rectangle):
    '''Draw the message on the windown after player finished the one level of game'''

    word=['Congratulation!','Good!','Excellent!','Great!','Wonderful!']
    shuffle(word)
    
    message1=Text(Point(4.5,5),word[1])
    message1.setTextColor('orchid')
    message1.setStyle('bold italic')
    message1.setSize(25)
    message1.draw(win)
    win.getMouse()
    
    for i in range(len(Whole_Rectangle)):   #Undraw all the squares that drawn on the window
        r=Whole_Rectangle[i]
        r.undraw()
    message1.undraw()
    


    
def background(color):
    '''Create the background of the table with number of squares'''
    
    square_width=1
    square_height=1
    center=centerPoint(num_width,num_height)  #Get the center points of each squares

    list_rectangle=rectangle(center,square_width, square_height)
    
    if len(color)==len(list_rectangle):
        
        after_color,Whole_Rectangle = Easy_drawRectangle(list_rectangle,color) # Draw the easy table of the game
        
    else:
        after_color,Whole_Rectangle = Hard_drawRectangle(list_rectangle,color) # Draw the hard table of the game
        

    return after_color,list_rectangle,Whole_Rectangle

def opening(word1,word2):
    '''Before start the game, create the window with size, 300 and 300 with the button, 'Start' '''
    
    win1=GraphWin('Flip It',300,300)
    win1.setCoords(0.0,0.0,10.0,10.0)
    win1.setBackground('green')
    message1=Text(Point(5,6),word1)
    message1.setTextColor('black')
    message1.setStyle('bold italic')
    message1.setSize(20)
    message1.draw(win1)
    rec=Rectangle(Point(4,1),Point(6,3))
    rec.setFill('white')
    rec.draw(win1)

    button=Text(Point(5,2),word2)
    button.draw(win1)

    valid = True
    while valid:   #If the player clicked start button, Then the game woud be started. 
        point=win1.getMouse()
        if 4< point.x <6 and 1 < point.y < 3:
            valid=False
            win1.close()
            return True
        else:
            None

def message(level):
    ''' Draw the level on the window so that player can know what level of dificulty it is.'''
    text=Text(Point(4,8.5),'level '+level)
    text.setTextColor('black')
    text.setStyle('bold italic')
    text.setSize(16)
    text.draw(win)

    return text
    



def end_The_Game():
    '''If the player finished all the levels of the game, then it will draw the texts and end and close the window'''
    
    text=Text(Point(5,6.5),'Thank you \nfor playing!')
    text.setTextColor('black')
    text.setStyle('bold italic')
    text.setSize(18)
    text.draw(win)

    text=Text(Point(5,3),'click everywhere to end the game')
    text.setTextColor('sky blue')
    text.setStyle('bold italic')
    text.setSize(10)
    text.draw(win)

    win.getMouse()
    win.close()

    return None

def num_click(count,height):
    '''count the number of clicks that player clicked on the window and draw it on the window'''
    
    text=Text(Point(9,9.5-height),'Click:'+str(count))
    text.setTextColor('black')
    text.setStyle('bold italic')
    text.setSize(8)
    text.draw(win)

    return text

def count_click(click,count):
    '''count the number of clicks that player clicked'''
    click.setText('Click:'+str(count))

    
def main(level,color):
    '''call the background function to create the table and run the game under main() function'''
    
    after_color,list_rectangle,Whole_Rectangle=background(color)

    text=message(level)
    
    valid=True
    count=0
    height=0+int(level)
    
    click=num_click(count,height)
    
    while valid:
        try:
            point=win.getMouse()
            count+=1
            count_click(click,count)

            
            location_rectangle=pointLocation(point.x,point.y,list_rectangle)



            after_color=changecolor(location_rectangle,Whole_Rectangle,after_color)
            
            after_color=changeAround(location_rectangle,Whole_Rectangle,after_color)


            

            if 'black' not in after_color:
                valid=False
            

        except:
            None

    congratulation(Whole_Rectangle)
    text.undraw()
    win.getMouse()
            
    
    


try:
    if opening('Flip It','Start') is True: #if player clicked 'Start' button, the game will start
        win=GraphWin('Flip It',400,400)
        win.setCoords(0.0,0.0,10.0,10.0)
        win.setBackground('green')
        num_width=4
        num_height=4
        color1=['white','black','white','white','black','black','black','white','white','black','white','black','white','white','black','black']
        color2=['black','black','black','black','black','white','white','black','black','white','white','black','black','black','black','black']
        color=[color1,color2]
        shuffle(color)
        main(str(1),color[0])
    else:
        raise Exception

except:
    print('sorry there is an error') #print out if there is an error
try:
    
    
    for i in range(3):
        if i==0:
            color=['white','black','black','white','black','black','black','black','black','black','black','black','white','black','black','white']
        elif i==1:
            color=['black','white','white','black','white','black','black','white','white','black','black','white','black','white','white','black']
        elif i==2:
            color=['white','white','white','black','white','white','black','white','white','black','white','white','black','white','white','white']

        main(str(i+2),color)

    
    
    for i in range(6):
        if i==0:
            num_width+=1
            color=['black','white','white','white','black','white','white','white','white','white','white','white','white','white','white','black','white','white','white','black']
            main(str(i+5),color)

        elif i==1:
            color=['white','black','black','black','white','black','black','white','black','black','black','black','white','black','black','white','black','black','black','white']
            main(str(i+5),color)

        elif i==2:
            color=['white','black','white','black','white','white','white','white','white','white','white','white','white','white','white','white','black','white','black','white']
            main(str(i+5),color)
            
        elif i==3:
            num_height+=1
            color=['white','black']
            main(str(i+5),color)
        elif i%2!=0 and i!=3:
            color=['white','black']
            main(str(i+5),color)
        elif i%2==0 and i!=2:
            color=['white','black']
            main(str(i+5),color)
    
    



    end_The_Game()  #End of the Game


except:
    print('sorry there is an error') #print out if there is an error
