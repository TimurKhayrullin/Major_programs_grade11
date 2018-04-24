from pygame import * # imports modules needed 
import random
from os import * ##mac required for quitting the game discreetly
init()
size = width, height = 1000, 700 # initializes size variables for 
screen = display.set_mode(size) #sets screen
button = 0
clicking = False #initializes mousebutton state
customCol= [(1,0,0),(2,0,0),(3,0,0),(4,0,0)] # initializes custom color list
pntAtt = (255,0,0,10,"circ",False,customCol) #initializes all paint Attributes
fontHel = font.SysFont("Helvetica", 20) #initializes all fonts
fontTiny = font.SysFont("Helvetica", 15)
fontTinier = font.SysFont("Helvetica", 1)
fontTim = font.SysFont("Times New Roman", 20)

BLACK = (0, 0, 0) #initializes all specific colors needed for interface and color library
GREY = (128,128,128)
ORANGES = [(225,229,204),(225,204,153),(225,178,102),(255,153,51),(255,128,0),(204,102,0),(153,76,0),(102,51,0),(51,25,0)]
YELLOWS = [(255,255,204),(255,255,153),(255,255,102),(255,255,51),(255,255,0),(204,204,0),(153,153,0),(102,102,0),(51,51,0)]
LGREENS = [(204,255,229),(153,255,204),(102,255,178),(51,255,153),(0,255,128),(0,204,102),(0,153,76),(0,102,51),(0,51,25)]
TOURQUOISES = [(204,255,255),(153,255,255),(102,255,255),(51,255,255),(0,255,255),(0,204,204),(0,153,153),(0,102,102),(0,51,51)]
PURPLES = [(229,204,255),(204,153,255),(178,102,255),(153,51,255),(127,0,255),(102,0,204),(76,0,153),(51,0,102),(25,0,51)]
PINKS = [(255,204,255),(255,153,255),(255,102,255),(255,51,255),(255,0,255),(204,0,204),(153,0,153),(102,0,102),(51,0,51)]
HOTPINKS = [(255,204,229),(255,153,204),(255,102,178),(255,51,153),(255,0,127),(204,0,102),(153,0,76),(102,0,51),(51,0,25)]
ROWS = [ORANGES,YELLOWS,LGREENS,TOURQUOISES,PURPLES,PINKS,HOTPINKS]


def buttons(click,moux,mouy,r,g,b,radi,shape,piCol,custom): #Function for mouse collision for buttons
    if click: #checks if mouse button is down
        if moux<300: #checks if mouse is inside the boundaries of the left interface block, addresses buttons within
            if 0<=moux<=255 and 50<=mouy<=200: ##checks if mouse is within the boundries of the rgb blocks
                if 50<mouy<100: ##checks if mouse is within red gradient block
                    r=moux ##sets r value of brush to x value of mouse
                elif 100<mouy<150: ##checks if mouse is within green gradient block
                    g=moux ##sets g value of brush to x value of mouse
                elif 150<mouy<200: ##checks if mouse is within blue gradient block
                    b=moux ##sets b value of brush to x value of mouse
            elif 225<mouy<275 and 0<=moux<=100: ##checks if mouse is within size slider block
                radi=moux//2 ##sets size (radius) value of brush to x value of mouse
            elif 325<mouy<550 and moux<225: ##checks if mouse is within special colors library block
                r = screen.get_at((moux,mouy))[0] ##sets brush color to color at current mouse x and y
                g = screen.get_at((moux,mouy))[1]
                b = screen.get_at((moux,mouy))[2]
            elif 595<mouy<641: # checks if mouse is within the y of custom color blocks
                if 4<moux<46 or 54<moux<100 or 104<moux<150 or 154<moux<200: ##checks if mouse x is within the 4 different custom color slots
                    r = screen.get_at((moux,mouy))[0] ##sets brush color to color at current mouse x and y
                    g = screen.get_at((moux,mouy))[1]
                    b = screen.get_at((moux,mouy))[2]  
            elif 580<mouy<590: # checks if mouse is within the boundries for the "Add custom color" buttons
                if 4<moux<46: ##checks if mouse x is within the 4 different "add color" buttons
                    custom[0] = (r,g,b)
                elif 54<moux<100:
                    custom[1] = (r,g,b)
                elif 104<moux<150:
                    custom[2] = (r,g,b) 
                elif 154<moux<200:
                    custom[3] = (r,g,b)                 
        else: # checks if mouse is within the top interface block, adresses appropriate buttons
            if mouy<50: ##checks if mouse is within top 50 pixels
                if 350<=moux<=480: ##checks if mouse x is within random color button
                    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255) #sets r,g and b values to random integers from 0 to 255
                elif 500<moux<610: ##checks if mouse x is within clear colors button
                    r=g=b=0 ## sets r,g and b to 0 
                elif 630<moux<746: ##checks if mouse x is within clear canvas button
                    draw.rect(screen,BLACK,(300,100,700,600)) #draws a black rectangle over the whole canvas 
                elif 767<moux<885: ##checks if mouse x is within pick color button
                    piCol = True
            else: ##if mouse y is not less than 50 
                if 500<moux<535: #checks if mouse is within the boundries for the shape buttons, and which specific button is being pressed. sets the shape to the shape on said button
                    shape = "tri"
                elif 547<moux<547+35:
                    shape = "squ"
                elif 594<moux<594+35:
                    shape = "circ"            
            if 946<moux: #checks if mouse x is within save and load buttons
                ##saves to same directory as this .py file
                if mouy<25: #if mouse x and y is within save buttons 1 and 2
                    if 946<moux<946+25:
                        image.save(screen.subsurface(300,100,700,600),"saved_image1.jpg") ##Saves current canvas to saved_image1.jpg
                        print("Saved Image 1")
                    else:
                        image.save(screen.subsurface(300,100,700,600),"saved_image2.jpg")##Saves current canvas to saved_image2.jpg
                        print("Saved Image 2")
                elif 25<mouy<50: #if mouse x and y is within save buttons 3 and 4
                    if 946<moux<946+25:
                        image.save(screen.subsurface(300,100,700,600),"saved_image3.jpg")##Saves current canvas to saved_image3.jpg
                        print("Saved Image 3")
                    else:
                        image.save(screen.subsurface(300,100,700,600),"saved_image4.jpg")##Saves current canvas to saved_image4.jpg
                        print("Saved Image 4") 
                elif 50<mouy<75: #if mouse x and y is within load buttons 1 and 2
                    if 946<moux<946+25:
                        try:
                            loadedPic = image.load("saved_image1.jpg") ##loads saved_image1.jpg to current canvas
                            screen.blit(loadedPic, Rect(300,100,700,600))
                            print("Loaded Image 1")
                        except :
                            print("Could not load image 1. Yes I predicted you attempting to crash my program. Save a drawing first!") ##if error occurs, avoids program crash
                    else:
                        try:
                            loadedPic = image.load("saved_image2.jpg") ##loads saved_image2.jpg to current canvas
                            screen.blit(loadedPic, Rect(300,100,700,600))
                            print("Loaded Image 2")
                        except :
                            print("Could not load image 2. Keep calm, try not to cry, and make sure you saved one first!") ##if error occurs, avoids program crash
                elif 75<mouy<100: #if mouse x and y is within load buttons 3 and 4
                    if 946<moux<946+25:
                        try:
                            loadedPic = image.load("saved_image3.jpg") ##loads saved_image3.jpg to current canvas
                            screen.blit(loadedPic, Rect(300,100,700,600))
                            print("Loaded Image 3")
                        except : 
                            print("Could not load image 3. Maybe you should consider trying to save one first, smartypants.") ##if error occurs, avoids program crash
                    else:
                        try:
                            loadedPic = image.load("saved_image4.jpg") ##loads saved_image4.jpg to current canvas
                            screen.blit(loadedPic, Rect(300,100,700,600))
                            print("Loaded Image 4")    
                        except:
                            print("Could not load image 4. I see what you're trying to do, save a drawing first!") ##if error occurs, avoids program crash
    return [r,g,b,radi,shape,piCol,custom]  
    
def drawGradient(r,g,b): #Color gradient buttons
    text = fontHel.render("Manual RGB color select:" , 1, (0, 0, 0)) 
    screen.blit(text, Rect(0,20,200,50))    ##blits above text at the top of the screen
    draw.rect(screen,(0,0,0),(0,46,260,158))  ##draws border around gradient boxes
    for i in range(0,256): # draws the Red, green and blue gradients sequentially, going from 0 to 255
        draw.rect(screen,(i,0,0),(i,50,1,50)) 
        draw.rect(screen,(0,i,0),(i,100,1,50))
        draw.rect(screen,(0,0,i),(i,150,1,50))
    draw.rect(screen,(0,255,255),(r,50,-2,50)) #draws sliders for graident block at appropriate x value, reflecting the RGB value of current color
    draw.rect(screen,(255,0,255),(g,100,-2,50))
    draw.rect(screen,(255,255,0),(b,150,-2,50))  
    text = fontHel.render(str(r) , 1, (0, 0, 0)) #blits current r,g and b as numbers, next to corresponding gradient block	
    screen.blit(text, Rect(265,65,300-255,50))	
    text = fontHel.render(str(g) , 1, (0, 0, 0))	
    screen.blit(text, Rect(265,115,300-255,50))    
    text = fontHel.render(str(b) , 1, (0, 0, 0))	
    screen.blit(text, Rect(265,165,300-255,50))           

def drawBrushSize(radius,y): #Brush size button
    draw.rect(screen,(0,0,0),(0,y-4,100+4,50+8)) #draws black border under actual brush size button
    draw.rect(screen,(255,0,255),(0,y,100,50)) #draws actual pink block for brush size slider
    text = fontHel.render("Brush size", 1, (0, 0, 0)) # blits "Brush size" inside the button	
    screen.blit(text, Rect(0,y,100,50)) 
    text = fontHel.render(str(radius*2)+"px" , 1, (0, 0, 0))	# blits brush size in pixels inside the button
    screen.blit(text, Rect(0,y+25,100,50))
    draw.rect(screen,(0,255,0),(int(radius*2),y,-2,50))  #draws green slider at appropriate x value, reflecting the current brush size
    
def drawColorLib(y): #Color Library
    text = fontHel.render("Special Color Library:" , 1, (0, 0, 0)) #blits "Special Color Library:" above actual color grid	
    screen.blit(text, Rect(0,y-25,200,25))    
    draw.rect(screen,(0,0,0),(0,y,229,183)) #draws actual color grid sequentially, using color values from a list of lists called ROWS (see start)
    for col in ROWS: #loops 7 times for 7 rows of colors
        for tint in col: #loops 9 times for each tint of current row
            draw.rect(screen,tint,(col.index(tint)*25,y+4+ROWS.index(col)*25,25,25)) #actual rect command, x and y are incremented as row and tint changes    
    
def drawCustomLib():
    #Custom colors info
    text = fontHel.render("Custom colors:" , 1, (0, 0, 0)) #blits instructions above actual custom colors buttons	
    screen.blit(text, Rect(0,510,200,25))    
    text = fontTiny.render("Click on them to set as current color, " , 1, (0, 0, 0))	
    screen.blit(text, Rect(0,534,200,25))
    text = fontTiny.render("Click on + to save current color as that spot." , 1, (0, 0, 0))	
    screen.blit(text, Rect(0,550,200,25))    
    #actual buttons
    draw.rect(screen,(0,0,0),(0,575,206,72)) ##draws black Border under buttons
    #Color slots and + signs
    for x in range(len(customCol)): #draws add buttons and custom color slots sequentially, getting color values from a list called customCol (see start)
        draw.rect(screen,(255,255,255),(x*50+4,580,46,10)) ##draws add color button
        text = fontHel.render("+" , 1, (0, 0, 0))	
        screen.blit(text, Rect(x*50+4+17,573,200,25))
        draw.rect(screen,(255,255,255),(x*50+4,595,46,46),3)
        draw.rect(screen,customCol[x],(x*50+4,595,46,46)) ##draws actual custom color slot

def drawRandom(x,y): #Random color button
    draw.rect(screen,(0,0,0),(x-4,y,130+8,50)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,y+4,130,42)) ##fills button area in with white
    text = fontHel.render("Random Color" , 1, (0, 0, 0)) #blits button name within the button	
    screen.blit(text, Rect(x,y+2,200,50))
    text = fontHel.render("button" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+35,y+25,200,50))  
    
def drawColorClear(x): #Clear colors button
    draw.rect(screen,(0,0,0),(x-4,0,110+8,50)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,4,110,42)) ##fills button area in with white
    text = fontHel.render("Clear colors", 1, (0, 0, 0))	#blits button name within the button	
    screen.blit(text, Rect(x,10,130,50))
    
def drawCanvasClear(x): #Clear canvas button
    draw.rect(screen,(0,0,0),(x-4,0,116+8,50)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,4,116,42)) ##fills button area in with white
    text = fontHel.render("Clear canvas", 1, (0, 0, 0))	#blits button name within the button
    screen.blit(text, Rect(x,10,130,50))   
    
def drawColorPick(x):
    #Color picker
    draw.rect(screen,(0,0,0),(x-4,0,116+8,50)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,4,116,42)) ##fills button area in with white
    text = fontHel.render("Pick color", 1, (0, 0, 0))	#blits button name within the button
    screen.blit(text, Rect(x+4,4,130,50))
    text = fontHel.render("from canvas", 1, (0, 0, 0))	
    screen.blit(text, Rect(x+4,22,130,50)) 

def drawShapes(x,y,w): #Shape buttons, uses given x ,y and w for x,y position of button, and width of button (w)
    text = fontHel.render("Brush Shapes:" , 1, (0, 0, 0)) #blits "brush size" beside actual shape buttons	
    screen.blit(text, Rect(350,65,200,50))    
    #Triangle
    draw.rect(screen,(0,0,0),(x-4,y-4,w+8,w+8)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,y,w,w)) ##fills button area in with white
    draw.polygon(screen,(0,0,0),((x+int(w/2),y+3),(x+3,y+w-4),(x+w-3,y+w-4))) #draws corresponding shape
    #Square
    x += 47 #increments x value to draw next button
    draw.rect(screen,(0,0,0),(x-4,y-4,w+8,w+8)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,y,w,w)) ##fills button area in with white
    draw.rect(screen,(0,0,0),(x+4,y+4,w-8,w-8)) #draws corresponding shape
    #Circle
    x += 47 #increments x value to draw next button
    draw.rect(screen,(0,0,0),(x-4,y-4,35+8,35+8)) ##draws black Border under buttons
    draw.rect(screen,(255,255,255),(x,y,35,35)) ##fills button area in with white
    draw.ellipse(screen,(0,0,0),(x+4,y+4,w-8,w-8)) #draws corresponding shape
    
def drawSaveLoad(x): #Save
    #blits in tiny text, button inscructions beside save buttons
    text = fontTiny.render("Save" , 1, (0, 0, 0)) 	
    screen.blit(text, Rect(946-55,5,200,50))    
    text = fontTiny.render("drawing:" , 1, (0, 0, 0))	
    screen.blit(text, Rect(946-55,20,200,50))    
    draw.rect(screen,(0,0,0),(x,0,50+4,50+4))
    
    #blits save slot number at appropriate x and y
    #save slot 1
    draw.rect(screen,(255,255,255),(x+4,0+4,25-4,25-4))  
    text = fontTiny.render("1" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+4,0+4,25-3,25-3)) 
    #save slot 2
    draw.rect(screen,(255,255,255),(x+25+4,0+4,25-4,25-4))
    text = fontTiny.render("2" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+25+4,0+4,25-3,25-3))
    #save slot 3
    draw.rect(screen,(255,255,255),(x+4,25+4,25-4,25-4))
    text = fontTiny .render("3" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+4,25+4,25-3,25-3))
    #save slot 4
    draw.rect(screen,(255,255,255),(x+25+4,25+4,25-4,25-4))
    text = fontTiny.render("4" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+25+4,25+4,25-3,25-3))    
    
    #Load
    #blits in tiny text, button inscructions beside load buttons	
    text = fontTiny.render("Load" , 1, (0, 0, 0)) 	
    screen.blit(text, Rect(946-55,55,200,50))    
    text = fontTiny.render("drawing:" , 1, (0, 0, 0))	
    screen.blit(text, Rect(946-55,70,200,50))    
    draw.rect(screen,(0,0,0),(x,50,50+4,50+4))
    
    #blits save slot number at appropriate x and y
    #load slot 1
    draw.rect(screen,(255,255,255),(x+4,50+4,25-4,25-4)) 
    text = fontTiny.render("1" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+4,50+4,25-3,25-3)) 
    #load slot 2
    draw.rect(screen,(255,255,255),(x+25+4,50+4,25-4,25-4))
    text = fontTiny.render("2" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+25+4,50+4,25-3,25-3))
    #load slot 3
    draw.rect(screen,(255,255,255),(x+4,75+4,25-4,25-4))
    text = fontTiny.render("3" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+4,75+4,25-3,25-3))
    #load slot 4
    draw.rect(screen,(255,255,255),(x+25+4,75+4,25-4,25-4))
    text = fontTiny.render("4" , 1, (0, 0, 0))	
    screen.blit(text, Rect(x+25+4,75+4,25-3,25-3)) 
    
def drawPaint(r,g,b,radius,shape,pickCol,click): #Paint
    if click and mx>300 and my>100: #checks if mouse is within canvas boundries and is clicked
        if pickCol: #checks if user clicked pick color button
            r = screen.get_at((mx,my))[0] ##sets current color to color at mouse x and y, stops pick color process, and waits 15% of a second
            g = screen.get_at((mx,my))[1]
            b = screen.get_at((mx,my))[2] 
            pickCol = False
            time.wait(150)
        elif shape == "circ": draw.circle(screen,(r,g,b),(mx,my), radius) #checks which shape is active, draws said shape at mouse x and y
        elif shape == "tri": draw.polygon(screen,(r,g,b),((mx-radius,int(my+radius)),(mx+radius,my+radius),(mx,my-radius)))
        else: draw.rect(screen,(r,g,b),(mx-radius,my-radius,int(radius*2),int(radius*2)))            
    #Brush display
    text = fontHel.render("Brush" , 1, (0, 0, 0)) #blits "Brush display" beside actual brush display	
    screen.blit(text, Rect(115,225,200,50))    
    text = fontHel.render("Display:" , 1, (0, 0, 0))	
    screen.blit(text, Rect(115,250,200,50))
    if shape == "circ":  #checks which shape is active, draws said shape in appropriate x and y, along with a black border
        draw.circle(screen,(0,0,0),(300-60,265),radius+3)
        draw.circle(screen,(r,g,b),(240,265),radius) 
    elif shape == "tri": 
        draw.polygon(screen,(0,0,0),((240-4-radius,int(265+2+radius)),(240+4+radius,265+2+radius),(240,265-4-radius)))        
        draw.polygon(screen,(r,g,b),((240-radius,int(265+radius)),(240+radius,265+radius),(240,265-radius)))
    elif shape == "squ": 
        draw.rect(screen,(0,0,0),(240-4-radius,265-4-radius,int(radius*2)+8,int(radius*2)+8))
        draw.rect(screen,(r,g,b),(240-radius,265-radius,int(radius*2),int(radius*2)))

def drawScene(screen,click,pntAtt): #all visual function calls and misc. visual elements are here
    #draws the grey gui blocks on the left and top of the screen
    draw.rect(screen,GREY,(0,0,300,700))
    draw.rect(screen,GREY,(300,0,700,100))
    
    #calls all functions that draw all the buttons and graphics needed for program, including paint, color option buttons, and save/load
    drawGradient(pntAtt[0],pntAtt[1],pntAtt[2])      
    drawBrushSize(pntAtt[3],225)
    drawColorLib(325)
    drawCustomLib()    
    drawRandom(350,0)     
    drawColorClear(500)
    drawCanvasClear(630)
    drawColorPick(767)
    drawShapes(500,60,35)
    drawSaveLoad(946)
    drawPaint(pntAtt[0],pntAtt[1],pntAtt[2],pntAtt[3],pntAtt[4],pntAtt[5],click)
    
    #Draws credits detailng what kind of godly entity conceived this amazing program, along with the name of the program itself
    text = fontTim.render("PainTim" , 1, (0, 255, 255))	
    screen.blit(text, Rect(0,659,200,50))
    text = fontTim.render("By Timur Khayrullin (2017)" , 1, (0, 255, 255))	
    screen.blit(text, Rect(0,679,200,50))    
    
    display.flip()  ##flips the display. (duh)
running = True
myClock = time.Clock()
# Game Loop
while running:
    for evnt in event.get():
        # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN: #checks if any mouse button is down, if so sets clicking to true
            clicking = True
            mx, my = evnt.pos            
        if evnt.type == MOUSEBUTTONUP: #checks if any mouse button is down, if so sets clicking to false
            clicking = False
        if evnt.type == MOUSEMOTION: #sets mx and my to mouse x and y if mouse is moving
            mx,my  = evnt.pos
        if (0<mx<300 and my<700) or (300<mx<1000 and my<100): # changes paint attributes if mouse is within gui (mouse is NOT on canvas), calling buttons with the appropriate parameters in order to have a paint brush that changes dependent on options and buttons provided by gui
            pntAtt = buttons(clicking,mx,my,pntAtt[0],pntAtt[1],pntAtt[2],pntAtt[3],pntAtt[4],pntAtt[5],pntAtt[6])    
    keys = key.get_pressed() #checks if escape key is pressed, if so, breaks game loop 
    if keys[K_ESCAPE]: break
    drawScene(screen,clicking,pntAtt) #calls drawscene, which handles all visuals 

_exit(0) #exits the program (uses function from os module because it works on OSX and PC, not just PC like pygame.quit() does
