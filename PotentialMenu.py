from pygame import *
import os
init()

SIZE = (1000,700)
screen = display.set_mode(SIZE)

BLACK = (0,0,0)
WHITE = (255,255,255)
fontHel = font.SysFont("Helvetica", 30) 
button = 0
clicking = False

def getVal(tup):
    """ getVal returns the (position+1) of the first 1 within a tuple.
        This is used because MOUSEBUTTONDOWN and MOUSEMOTION deal with
        mouse events differently
    """
    for i in range(3):
        if tup[i]==1:
            return i+1
    return 0

x = 300
l,w = 300,100
h = 100
rects=[(x,h,l,w),(x,h+200,l,w),(x,h+400,l,w)]


def drawMain(levels): 
    draw.rect(screen,BLACK,(0,0,1000,700))
    texts = ["Play game","Change level","Exit game"]
    text = fontHel.render("Your current level is: "+str(levels) , 1, WHITE)	
    screen.blit(text,Rect(0,0,300,200))    
    for i in range(3):
        draw.rect(screen,WHITE,rects[i])
        text = fontHel.render(texts[i], 1, (0, 0, 0))	
        screen.blit(text,rects[i]) 

def drawLevels(): 
    draw.rect(screen,BLACK,(0,0,1000,700))
    texts = ["level 1","level 2","level 3"]   
    for i in range(3):
        draw.rect(screen,WHITE,rects[i])
        text = fontHel.render(texts[i], 1, (0, 0, 0))	
        screen.blit(text,rects[i])
        
level = 1
menu = 0
running = True
while running:
    for evnt in event.get():
        # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN: #checks if any mouse button is down, if so sets clicking to true
            button = evnt.button
        if evnt.type == MOUSEMOTION: #sets mx and my to mouse x and y if mouse is moving
            mx,my  = evnt.pos
            button = getVal(evnt.buttons)
        if button==1:
            if menu==0:
                for press in range(len(rects)):
                    if Rect(rects[press]).collidepoint(mx,my):
                        menu = press + 1
                        print("Clicked", press+1)
            elif menu== 2:
                for press in range(len(rects)):
                    if Rect(rects[press]).collidepoint(mx,my):
                        level = press +1                         
        if button ==3:
            if menu == 1:
                menu = 0
            if menu == 2:
                menu = 0            
                
            
    if menu==0:
        drawMain(level)
    elif menu == 1:
        draw.rect(screen,(255,0,0),(0,0,1000,700))
    elif menu== 2:
        drawLevels()
    elif menu==3:
        break
    display.flip()
os._exit(0)