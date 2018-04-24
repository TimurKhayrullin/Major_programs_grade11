from pygame import * # imports needed for pygame and rng and quitting mech.
from os import *
from random import *
init()
SIZE = (1000,700) #sets screen size
screen = display.set_mode(SIZE)

BLACK = (0,0,0) #declares all colours needed
ORANGE = (255,128,0)
DARKORANGE = (153,76,0)
DARKISHORANGE = (204,102,0)
LEAFGREEN = (51,102,0)
GREEN = (0,255,0)
DARKTEAL = (0,153,153)
WHITE = (255,255,255)
RED = (255,0,0)
DARKGREEN = (0,128,0)
DARKBLUE = (0,0,128)
BROWN = (102,51,0)
GREY = (128,128,128)
LIGHTGREY = (201,201,201)
DARKBROWN = (51,25,0)
YELLOW = (255,255,0)
PINK = (204,0,204)
TREES = [RED,YELLOW,GREEN] #different tree colour possibilities
BLUES = [DARKBLUE,(0,102,204),(0,76,153),(0,51,102),(0,25,52),(0,0,204),(0,0,153),(0,0,102),(0,0,51)] #sky colour possibilities

def drawMoonCraters(x,y): #draws craters in grey on the moon
    draw.ellipse(screen,GREY,(x+20,y+15,25,20))
    draw.ellipse(screen,GREY,(x+50,y+25,15,15))
    draw.ellipse(screen,GREY,(x+20,y+45,20,25))
    draw.ellipse(screen,GREY,(x+55,y+55,15,20))
    draw.ellipse(screen,GREY,(x+25,y+80,20,15))
    draw.ellipse(screen,GREY,(x+70,y+25,20,20))
    
def drawSky(colour,x,y,phase): #draw sky colour,stars and the actual moon (moon position is random)
    draw.rect(screen,BLUES[colour],(0,0,1000,700))#draw sky
    
    stars = 0
    while stars<=25: #draws 25 stars in random positions
        x= randint(0,1000) #picks random x posisiton
        y= randint(0,400) #picks random y position
        draw.ellipse(screen,YELLOW,(x,y,10,5)) #draws horizontal part of star
        draw.ellipse(screen,YELLOW,(x+3,y-3,5,10)) #draws veritical part of star
        stars+=1
        
    
    if phase == 1: #draws moon in 3 different possible phases (full, crescent, gibous)
        draw.ellipse(screen,LIGHTGREY,(x,y,100,100)) #draws moon
        drawMoonCraters(x,y)        
    elif phase == 2:
        draw.ellipse(screen,LIGHTGREY,(x,y,100,100)) # draws moon
        drawMoonCraters(x,y)        
        draw.ellipse(screen,BLUES[colour],(x+30,y,70,100)) #draws shadow of earth that secludes the moon
    else: 
        draw.ellipse(screen,LIGHTGREY,(x,y,70,100)) #draws gibous moon with 1 crater secluded by shadow of earth
        draw.ellipse(screen,GREY,(x+20,y+15,25,20))
        draw.ellipse(screen,GREY,(x+50,y+25,15,15))
        draw.ellipse(screen,GREY,(x+20,y+45,20,25))
        draw.ellipse(screen,GREY,(x+55,y+55,15,20))
        draw.ellipse(screen,GREY,(x+25,y+80,20,15))     
    draw.rect(screen,DARKGREEN,(0,450,1000,1000)) #draw grass
def drawTrees(): # draws trees in 3 different possible y positions, 149 different possible heights, and 3 different colours
    for i in range(0,1000,75):
        leaf = randint(0,2) # chooses colour of leaves
        treeY = randint(0,4) # chooses y poisition
        treeH = randint(250,400) # chooses tree height
        draw.polygon(screen,DARKBROWN,((i,treeY*10+450),(i+50,treeY*10+450),(i+25,treeY*10+425))) #draw trunk base
        draw.polygon(screen,DARKBROWN,((i+13,treeY*10+450),(i+38,treeY*10+450),(i+38,treeY*10+treeH),(i+13,treeY*10+treeH))) #draw trunk
        draw.ellipse(screen,TREES[leaf],(i,treeY*10+treeH-25,50,35)) #draw a head of leaves on top of the tree
        draw.ellipse(screen,TREES[leaf],(i+25,treeY*10+treeH-15,40,35))
        draw.ellipse(screen,TREES[leaf],(i-25,treeY*10+treeH-15,40,35)) 
        draw.ellipse(screen,TREES[leaf],(i-27,treeY*10+treeH,100,35))
        
def drawVines(thicc) :
    draw.line(screen,LEAFGREEN,(250,400),(375,375),thicc) # drawvines on the top left and top middle of house
    draw.line(screen,LEAFGREEN,(375,375),(400,350),thicc)
    draw.line(screen,LEAFGREEN,(400,350),(428,325),thicc)
    draw.line(screen,LEAFGREEN,(428,325),(390,315),thicc)
    draw.line(screen,LEAFGREEN,(390,315),(370,325),thicc)
    draw.line(screen,LEAFGREEN,(370,325),(350,345),thicc)
    draw.line(screen,LEAFGREEN,(350,345),(330,320),thicc)
    draw.line(screen,LEAFGREEN,(370,325),(350,315),thicc)
    draw.line(screen,LEAFGREEN,(390,315),(455,290),thicc)
    draw.line(screen,LEAFGREEN,(455,290),(450,337),thicc)
    
    draw.line(screen,LEAFGREEN,(450,337),(490,390),thicc) # draws vines to the middle right
    draw.line(screen,LEAFGREEN,(490,390),(460,420),thicc)
    draw.line(screen,LEAFGREEN,(460,420),(460,435),thicc)
    draw.line(screen,LEAFGREEN,(490,390),(520,420),thicc)
    draw.line(screen,LEAFGREEN,(520,420),(520,435),thicc)
    
    draw.line(screen,LEAFGREEN,(375,375),(400,400),thicc) #draws vine in the middle middle (the most realitic looking one)
    draw.line(screen,LEAFGREEN,(400,400),(375,425),thicc)
    draw.line(screen,LEAFGREEN,(375,425),(380,475),thicc)
    draw.line(screen,LEAFGREEN,(380,475),(380,500),thicc)
    
    draw.line(screen,LEAFGREEN,(250,550),(265,525),thicc) # draws vines climbing the side of the house
    draw.line(screen,LEAFGREEN,(250,550),(265,525),thicc)
    draw.line(screen,LEAFGREEN,(265,525),(250,490),thicc)
    draw.line(screen,LEAFGREEN,(250,490),(270,460),thicc)
    draw.line(screen,LEAFGREEN,(270,460),(250,430),thicc)
    draw.line(screen,LEAFGREEN,(250,550),(260,600),thicc)
    
def drawWindows():
    draw.rect(screen,ORANGE,(475,425,50,50)) # drawwindow 1
    draw.rect(screen,DARKORANGE,(480,430,40,40))
    draw.rect(screen,ORANGE,(475,448,50,5)) # draw crossbars 
    draw.rect(screen,ORANGE,(498,425,5,50))
    
    draw.rect(screen,ORANGE,(300,425,50,50)) # draw window 2
    draw.rect(screen,DARKORANGE,(305,430,40,40))
    draw.rect(screen,ORANGE,(300,448,50,5)) # draw crossbars 
    draw.rect(screen,ORANGE,(323,425,5,50))
    
def drawHouse():
    draw.rect(screen,BROWN,(250,400,350,200)) #draw wall
    for i in range(260,600,30): #draw tiles (vertical dividers)
        draw.line(screen,BLACK,(i,400),(i,600),3)
    for j in range(410,600,30): #draw tiles (horizontal dividers)
        draw.line(screen,BLACK,(250,j),(600,j),3)
    draw.polygon(screen,BROWN,((600,400),(600,600),(675,525),(675,325))) #draw side wall
    draw.line(screen,BLACK,(615,585),(615,385),3) #draw side tiles (vertical)
    draw.line(screen,BLACK,(630,570),(630,370),3)
    draw.line(screen,BLACK,(645,555),(645,355),3)
    draw.line(screen,BLACK,(660,540),(660,340),3)
    for j in range(410,600,30): #draw side tiles (horizontal)
        draw.line(screen,BLACK,(600,j),(675,j-75),3)    
    draw.polygon(screen,ORANGE,((675,325),(600,400),(425,325),(500,250))) #draw side of roof
    draw.polygon(screen,DARKISHORANGE,((250,400),(425,325),(500,250),(325,325))) #draw other side of roof
    
    draw.polygon(screen,DARKISHORANGE,((542,374),(550,365),(550,336),(542,350))) # draw side of chimney 
    draw.polygon(screen,DARKISHORANGE,((550,350),(558,341),(558,341-24),(550,326)))
    draw.polygon(screen,BLACK,((500,325),(550,325),(558,341-24),(508,341-24))) # draw chimney hole
    draw.rect(screen,DARKORANGE,(500,325,50,25)) #draw front of chimney
    draw.rect(screen,DARKORANGE,(507,325,35,70))

    draw.polygon(screen,ORANGE,((250,400),(600,400),(425,325))) #draw front of roof
    draw.rect(screen,ORANGE,(300,550,40,50)) #draw door
    draw.circle(screen,BLACK,(335,575),5) #draw doorknob
    
    drawWindows() #calls for windows and vines
    drawVines(8)
    
def drawTombstone1(x,y): #draws a tombstone within an x and y range (random), with a semi-circle on top
    draw.rect(screen,GREY,(x,y,16,25)) #draws stone
    draw.circle(screen,GREY,(x+8,y),8)
    draw.circle(screen,LEAFGREEN,(x-3,y+25),4) #draws grass below
    draw.circle(screen,LEAFGREEN,(x+1,y+25),3)
    draw.circle(screen,LEAFGREEN,(x+6,y+25),4)
    draw.circle(screen,LEAFGREEN,(x+11,y+25),3)
    draw.circle(screen,LEAFGREEN,(x+16,y+25),4)
    
def drawTombstone2(x,y): #draws a tombstone within an x and y range (random), in the shape of a cross
    draw.rect(screen,GREY,(x,y,5,50)) #draws stone cross
    draw.rect(screen,GREY,(x-15,y+15,34,5)) 
    draw.circle(screen,BROWN,(x-7,y+50),4) #draws dirt below
    draw.circle(screen,BROWN,(x-3,y+50),3)
    draw.circle(screen,BROWN,(x+1,y+50),4)
    draw.circle(screen,BROWN,(x+7,y+50),3)
    draw.circle(screen,BROWN,(x+12,y+50),4)  
    
def drawTombstone3(x,y): #draws a tombstone within an x and y range (random), in the shape of a rectangle
    draw.rect(screen,GREY,(x,y-15,16,40)) # draws stone
    draw.circle(screen,LEAFGREEN,(x-3,y+25),4) #draws grass below
    draw.circle(screen,LEAFGREEN,(x+1,y+25),3)
    draw.circle(screen,LEAFGREEN,(x+6,y+25),4)
    draw.circle(screen,LEAFGREEN,(x+11,y+25),3)
    draw.circle(screen,LEAFGREEN,(x+16,y+25),4)

def drawCandycorn(x,y): #draws a huge piece of cadycorn within an x and y range (random)
    draw.polygon(screen,YELLOW,((x,y),(x+10,y-10),(x+60,y-10),(x+70,y))) #bottom
    draw.polygon(screen,WHITE,((x+10,y-10),(x+60,y-10),(x+50,y-20),(x+20,y-20))) #middle
    draw.polygon(screen,ORANGE,((x+50,y-20),(x+20,y-20),(x+30,y-30),(x+40,y-30))) #top

def drawLollipop(x,y): #draws a huge pink lollipop within an x and y range
    draw.line(screen,WHITE,(x+25,y+25),(x+75,y+75),3) #stick
    draw.ellipse(screen,PINK,(x,y,40,40)) #candy part
    

drawSky(randint(0,8),randint(0,950),randint(0,150),randint(1,3)) #calls all functions and puts random x's, y's, and other parameters (if needed)
drawTrees() #draws all trees
drawHouse() #draws all of house
drawTombstone2(randint(0,225,),randint(600,675)) #draw tombstone
drawTombstone1(randint(0,225,),randint(500,590)) # draw tombstone 2
drawTombstone3(randint(690,1000),randint(500,590)) # draw tombstone 3
drawCandycorn(randint(610,930),randint(610,700)) # draw huge candycorn
drawLollipop(randint(250,600),randint(600,625)) # draw big lollipop
time.wait(10000) #waits so you can observe my masterpiece
_exit(0) # exits pygame