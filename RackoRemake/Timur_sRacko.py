from pygame import  * 
import os 
from random import  * 
init()

#variable initialization pt 1

 # display
SIZE = (1000, 700)
screen = display.set_mode(SIZE)

 # fonts and images
fontCal = font.SysFont("Calibri",  15) 
fontCalB = font.SysFont("Calibri",  15,  True)
fontCalBig = font.SysFont("Calibri",  45, True)
fontCalMid = font.SysFont("Calibri", 25)
bg = image.load("rackoBackground.png")
bgDim = image.load("rackoBackgroundDim.png")

 # colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
D_RED = (222, 33, 46)
RED = (255,0,0)
DD_RED = (150, 0, 0)
GREY = (128,128,128)
GREEN = (0,255,0)
D_GREEN = (37, 87, 0)
L_BLUE = (0,128,255)
YELLOW = (255,255,0)

# mouse variables
button = 0
mx, my = 0, 0
    
# end of variable init. pt 1
    
#start of rect hitbox init. and def commands for drawing all menus

#main menu rects (made with loop)
mainMenu = []
for y in range(200, 500, 100):
    mainMenu.append((400, y, 200, 75))
    
#function for drawing the main menu
def drawMain(): 
    texts = ["Play game", "Highscores/Options", "Exit game"]
    for i in range(3): #sequentially draws buttons for menu, using text from list above if necessary
        draw.rect(screen, WHITE, mainMenu[i])
        text = fontCal.render(texts[i],  1,  (0,  0,  0))	
        screen.blit(text, mainMenu[i]) 

#player number rects (made with loop)
playerNumbers = []
for x in range(400, 600, 50):
    playerNumbers.append((x, 350, 25, 25))
    
#function for drawing player picking menu
def drawPlayers(): 
    texts = ["1", "2", "3", "4"] 
    text = fontCal.render("How many players are playing?",  1,  WHITE)	
    screen.blit(text, Rect(0, 0, 200, 15))    
    for i in range(4): #sequentially draws buttons for menu, using text from list above if necessary
        draw.rect(screen, WHITE, playerNumbers[i])
        text = fontCal.render(texts[i],  1,  (0,  0,  0))	
        screen.blit(text, playerNumbers[i])

#init. for all hitboxes and constants needed for login menu (made with nested loop)
loginButtons = []  
logStat = []
logInfo = []
logBoxes = []
nextButton = [(410, 330, 110, 50),(300, 330, 400, 50)]
for y in range(50, 650, 350):
    for x in range(150, 675, 450):
        logBoxes.append((x,y,240,250))
        loginButtons.append([(x+25, y+100, 150, 25), (x+25, y+200, 150, 25)])
        logStat.append([False,False])
        logInfo.append(["",""])

#function for drawing login menu
def drawLogin(noOfPlayers,loginInfo,inputStatus):
    for pl in range(noOfPlayers): #for each player (1 to 4)
        #draws basic guidelines for input 
        draw.rect(screen,WHITE,logBoxes[pl])
        draw.rect(screen,GREY,logBoxes[pl],5)
        text = fontCalBig.render("Player %i" %(pl+1), 1, BLACK)	
        screen.blit(text, Rect(logBoxes[pl][0]+5, logBoxes[pl][1]+3,logBoxes[pl][2]-10, logBoxes[pl][3]-10))
        text = fontCalMid.render("Username", 1, BLACK)	
        screen.blit(text, Rect(logBoxes[pl][0]+5, logBoxes[pl][1]+58, logBoxes[pl][2]-10, logBoxes[pl][3]-10))
        text = fontCalMid.render("(max 13 chars):", 1, BLACK)	
        screen.blit(text, Rect(logBoxes[pl][0]+5, logBoxes[pl][1]+75, logBoxes[pl][2]-10, logBoxes[pl][3]-10))        
        text = fontCalMid.render("Password", 1, BLACK)	
        screen.blit(text, Rect(logBoxes[pl][0]+5, logBoxes[pl][1]+158,logBoxes[pl][2]-10, logBoxes[pl][3]-10))    
        text = fontCalMid.render("(max 13 chars or numbers):", 1, BLACK)	
        screen.blit(text, Rect(logBoxes[pl][0]+5, logBoxes[pl][1]+175,logBoxes[pl][2]-10, logBoxes[pl][3]-10))            
        for i in loginButtons[pl]: #for each button
            if inputStatus[pl][loginButtons[pl].index(i)]: #outlines button in blue if login status is true 
                draw.rect(screen,WHITE,i)
                draw.rect(screen,L_BLUE,i,5)
            else: 
                draw.rect(screen,WHITE,i) #if it is not, box has grey outline
                draw.rect(screen,GREY,i,5)
            #actual drawing of inputed information (username, password)
            text = fontCal.render(loginInfo[pl][loginButtons[pl].index(i)], 1, BLACK)	
            screen.blit(text, Rect(i[0]+5, i[1]+2,i[2]-10, i[3]-4))
        #draws next button in the middle of the screen
        draw.rect(screen,WHITE,nextButton[0])
        draw.rect(screen,GREY,nextButton[0], 5)
        text = fontCalBig.render("Next", 1, BLACK)	
        screen.blit(text, Rect(nextButton[0][0]+5, nextButton[0][1]+3, nextButton[0][2]-10, nextButton[0][3]))        

#hit box init. for option menu (made using nested loop)
optionRect = []
for x in range(150, 850, 350):
    for y in range(100,500,100):
        optionRect.append((x, y, 250, 50))
backRect = (0, 0, 100, 50)

#hitbox init. for delete account menu (similar to login menu hitbox init, but without loops)
delBox = logBoxes[0]
delButtons = [loginButtons[0][0],loginButtons[0][1]]
delStat = [False, False]
delInfo = ['','']
deleteButton = (150, 330, 250, 50)

#function for drawing the delete account menu
def drawDeleteAcc(delBox, delStat, delInfo, delButtons):
    #draws basic guidelines for input
    draw.rect(screen,WHITE,delBox)
    draw.rect(screen,GREY,delBox,5)
    text = fontCalMid.render("Username", 1, BLACK)	
    screen.blit(text, Rect(delBox[0]+5, delBox[1]+58, delBox[2]-10, delBox[3]-10))
    text = fontCalMid.render("(max 13 chars):", 1, BLACK)	
    screen.blit(text, Rect(delBox[0]+5, delBox[1]+75, delBox[2]-10, delBox[3]-10))        
    text = fontCalMid.render("Password", 1, BLACK)	
    screen.blit(text, Rect(delBox[0]+5, delBox[1]+158,delBox[2]-10, delBox[3]-10))    
    text = fontCalMid.render("(max 13 chars or numbers):", 1, BLACK)	
    screen.blit(text, Rect(delBox[0]+5, delBox[1]+175, delBox[2]-10, delBox[3]-10))  
    for i in delButtons:
        if delStat[delButtons.index(i)]: #outlines button in blue if login status is true
            draw.rect(screen,WHITE,i)
            draw.rect(screen,L_BLUE,i,5)
        else: 
            draw.rect(screen,WHITE,i) #if it is not, box has grey outline
            draw.rect(screen,GREY,i,5)
        #actual drawing of inputed information (username, password)
        text = fontCal.render(delInfo[delButtons.index(i)], 1, BLACK)	
        screen.blit(text, Rect(i[0]+5, i[1]+2,i[2]-10, i[3]-4))   
    #draws delete account and back buttons, for functionality and navigation
    draw.rect(screen, WHITE, backRect)
    text = fontCal.render("Back", 1, BLACK)
    screen.blit(text, Rect(backRect)) 
    draw.rect(screen, WHITE, deleteButton)
    text = fontCal.render("Delete account", 1, BLACK)
    screen.blit(text, Rect(deleteButton))     
    
#function for drawing the options menu
def drawOptions():
    texts = ["Delete account", "best average points 2 player", "best average points 3 player", "best average points 4 player", "Quickest Win solo", "Quickest Win 2 player", "Quickest Win 3 player" , "Quickest Win 4 Player"]
    #draws back button
    draw.rect(screen, WHITE, backRect)
    text = fontCal.render("Back", 1, BLACK)
    screen.blit(text, Rect(backRect))    
    for button in optionRect: #sequentially draws buttons for menu, using text from list above if necessary
        draw.rect(screen,WHITE,button)
        text = fontCalMid.render(texts[optionRect.index(button)], 1, BLACK)
        screen.blit(text, Rect(button))

#function for drawing the highest point average menu
def drawPoints(users, playerNo):
    #takes all users from userInfo and sorts them by average point score using an anonymous function (lambda)
    pointsList = sorted(users, key = lambda x: int(x[5 + playerNo * 3]))
    draw.rect(screen, DD_RED, (250, 200, 400, 300))
    #draws labels for to-be table of records
    text = fontCal.render("%s %20s" %("Name" ,"Average Score"), 1,BLACK)
    screen.blit(text, Rect(255, 205, 400, 25))
    #draws back button
    draw.rect(screen, WHITE, backRect)
    text = fontCal.render("Back", 1, BLACK)
    screen.blit(text, Rect(backRect))    
    if len(users)>=10: #displays top 10 entries for this record (if 10 are present. if not, displays the amount present)
        for i in range(10):
            draw.rect(screen, YELLOW, (255, 225+i*25, 395, 15))
            text = fontCal.render("%s %20i" %(pointsList[i][0], pointsList[i][5+playerNo*3]), 1, BLACK)
            screen.blit(text, Rect(255, 225+i*25, 400, 15))
    else:
        for i in range(len(users)):
            draw.rect(screen, YELLOW, (255, 225+i*25, 395, 15))
            text = fontCal.render("%s %20s" %(pointsList[i][0], pointsList[i][5+playerNo*3]), 1, BLACK)
            screen.blit(text, Rect(255, 225+i*25, 400, 15)) 

#function for drawing the quickest win menu
def drawTurns(users, playerNo):
    #takes all users from userInfo and sorts them by quickest win score using an anonymous function (lambda)
    turnsList = sorted(users, key = lambda x: int(x[playerNo + 2]))
    draw.rect(screen, DD_RED, (250, 200, 400, 300))
    #labels to-be table
    text = fontCal.render("%s %20s" %("Name" ,"Turn number"), 1, BLACK)
    screen.blit(text, Rect(255, 205, 400, 25))
    #back button (you already know)
    draw.rect(screen, WHITE, backRect)
    text = fontCal.render("Back", 1, BLACK)
    screen.blit(text, Rect(backRect))    
    if len(users)>=10: #displays top 10 entries for this record (if 10 are present. if not, displays the amount present) 
        for i in range(10):
            draw.rect(screen, YELLOW, (255, 225+i*25, 395, 15))
            text = fontCal.render("%s %20i" %(turnsList[i][0], turnsList[i][playerNo+2]), 1, BLACK)
            screen.blit(text, Rect(255, 225+i*25, 400, 15))
    else:
        for i in range(len(users)):
            draw.rect(screen, YELLOW, (255, 225+i*25, 395, 15))
            text = fontCal.render("%s %20s" %(turnsList[i][0], turnsList[i][playerNo+2]), 1, BLACK)
            screen.blit(text, Rect(255, 225+i*25, 400, 15))    
    

#hitbox init. for deck choosing (draw pile and discard pile)
deckRect = []
for x in range(500, 700, 100):
    deckRect.append((x, 250, 80, 80))
    
#function for drawing deck menu
def drawDeck(tempCard, discard, turn, points, rackRound): 
    texts = ["Draw Pile", "Discard Pile"]   
    text = fontCal.render("Choose which deck to draw from",  1,  WHITE)	
    screen.blit(text, Rect(0, 0, 200, 15))    
    for i in range(len(deckRect)): #draws piles
        draw.rect(screen, WHITE, deckRect[i])
        text = fontCal.render(texts[i],  1,  (0,  0,  0))	
        screen.blit(text, deckRect[i])
    if tempCard != 0: # draws ongoing card (if present)
        draw.rect(screen, WHITE, (500, 400, 100, 100))
        text = fontCalBig.render(str(tempCard),  1,  (0,  0,  0))	
        screen.blit(text, Rect(550, 450, 50, 50))  
    if discard!=[]: #draws top of discard pile (if present)
        text = fontCalBig.render(str(discard[-1]),  1,  (0,  0,  0))	
        screen.blit(text, deckRect[1][0]+15,deckRect[1][1]+15,deckRect[1][2],deckRect[1][3])   
    #draws game info (round, current player points)
    draw.rect(screen, WHITE, (800,0,200,50))
    text = fontCal.render("Round: %i" %rackRound,  1,  BLACK)
    screen.blit(text, Rect(800, 15, 100, 15)) 
    text = fontCal.render("Points: %i" %(sum(points[turn])),  1,  BLACK)
    screen.blit(text, Rect(900, 15, 100, 15))     
    
#hitbox  init. for tray slots during game (I named racks tray in this code, I know it's a bit confusing but hey)
traySlot = []
for y in range(100, 601, 50):
    traySlot.append((200,  y,  200,  45))
    
#function for drawing players tray of cards in-game
def drawTray(hand, turn, name):
    draw.rect(screen, DD_RED, (80,  60,  360,  555))
    text = fontCalBig.render("%s's rack" %name[turn],  1, WHITE)	
    screen.blit(text, Rect(80 + 5, 60 + 5, 50, 45))    
    for i in range(10):
        draw.rect(screen, WHITE, traySlot[i])
        text = fontCalBig.render(str(hand[i]), 1, BLACK)	
        screen.blit(text, Rect(traySlot[i][0]  +  75, traySlot[i][1]  + 10, 50, 45))
        
        draw.rect(screen, D_RED, (traySlot[i][0]  - 100, traySlot[i][1], 50, 45))
        text = fontCalB.render(str(50  - i * 5),  1, WHITE)	
        screen.blit(text, Rect(traySlot[i][0]  - 83, traySlot[i][1] + 13, 50, 45))

#hitbox init. for round winning menu (made using loop)
winRect = []
for y in range(600,700, 50):
    winRect.append((500,y,125,50))

#function for drawing round win menu 
def drawWinscreen(winningPlayer, hand, turn, names, playerPoints, turnNumber, soloWinProfile):
    x = 80
    y = 0
    #labels
    draw.rect(screen, DD_RED, (x, y, 360, 100))
    text = fontCalBig.render("Player %s  Wins" % names[winningPlayer], 1, WHITE)	
    screen.blit(text, Rect(x+5, y, 100, 45))
    
    text = fontCalBig.render("With these cards:", 1, WHITE)	
    screen.blit(text, Rect(x+5, y + 45, 100, 45))     
    
    if len(names)>1: #displays turn number if players is 1
        draw.rect(screen, DD_RED, (600, 45, 330, 500))
        text = fontCalBig.render("Current points", 1, WHITE)	
        screen.blit(text, Rect(600, 50, 100, 45))
        text = fontCalBig.render("vs Total points", 1, WHITE)	
        screen.blit(text, Rect(600, 80, 100, 45))        
        text = fontCalBig.render("For each player:", 1, WHITE)	
        screen.blit(text, Rect(600, 110, 100, 45))        
        for i in range(len(names)):
            if i == winningPlayer:
                draw.rect(screen, YELLOW, (600, 150 + (30*i), 330, 25))
            text = fontCalBig.render("%i %-13s %i/%i" %(i+1, names[i], points[i][rackRound], sum(points[i])), 1, BLACK)	
            screen.blit(text, Rect(600, 150 + (30*i), 100, 25))
    
    else: #displays points otherwise
        draw.rect(screen, DD_RED, (600, 45, 300, 300))
        text = fontCalBig.render("Number of turns used:", 1, WHITE)	
        screen.blit(text, Rect(600, 45, 100, 45))
        text = fontCalBig.render(str(turnNumber), 1, WHITE)	
        screen.blit(text, Rect(750, 85, 100, 45))
        text = fontCalBig.render("Personal record:", 1, WHITE)	
        screen.blit(text, Rect(600, 125, 100, 45))
        text = fontCalBig.render(soloWinProfile[2], 1, WHITE)	
        screen.blit(text, Rect(750, 165, 100, 45))  
        #round displays only is more than 1
        draw.rect(screen,WHITE,winRect[0])
        draw.rect(screen,BLACK,winRect[0],4)
        text = fontCalMid.render("Next round", 1, BLACK)	
        screen.blit(text, Rect(winRect[0][0]+5,winRect[0][1]+15,winRect[0][2],winRect[0][3]))        
    
    #end buttons, to  quit
    draw.rect(screen,WHITE,winRect[1])
    draw.rect(screen,BLACK,winRect[1],4)
    text = fontCalMid.render("To main menu", 1, BLACK)	
    screen.blit(text, Rect(winRect[1][0]+5,winRect[1][1]+15,winRect[1][2],winRect[1][3]))
    
#function for drawing game winning menu (no hitbox init. for this one b/c it does not require it's own unique buttons, and therefore does not need it's own hitbox list)
def drawWinGame(winner, turns, names):
    x = 80
    y = 0
    #labels for winning player, text within explains info displayed
    draw.rect(screen, DD_RED, (x, y, 450, 100))
    text = fontCalBig.render("Player %s  Wins the game!" % names[winner], 1, WHITE)	
    screen.blit(text, Rect(x+5, y, 100, 45))
    
    text = fontCalBig.render("With these cards:", 1, WHITE)	
    screen.blit(text, Rect(x+5, y + 45, 100, 45))    

    draw.rect(screen, DD_RED, (600, 45, 500, 300))
    text = fontCalBig.render("Number of turns used:", 1, WHITE)	
    screen.blit(text, Rect(600, 45, 100, 45))
    text = fontCalBig.render(str(turns), 1, WHITE)	
    screen.blit(text, Rect(750, 85, 100, 45))    

    draw.rect(screen,WHITE,winRect[1])
    draw.rect(screen,BLACK,winRect[1],4)
    text = fontCalMid.render("To main menu", 1, BLACK)	
    screen.blit(text, Rect(winRect[1][0]+5,winRect[1][1]+15,winRect[1][2],winRect[1][3])) 
    
#end of rect hitbox init. and def commands for drawing all menus

#start of variable init. pt 2

#  all menu states needed for game
MAIN = 0
PLAYERNO = 1
HIGHoPTION = 2
EXIT = 3
TRAYSLOT = 4
DECK = 5
WAIT = 6
LOGIN = 7
WIN = 8
DELETE = 9
WINGAME = 99
POINTS = 10
TURNS = 20

#init for menu itself, run condition, and amount of players
menu = 0
running = True
players = 0

#init for all deck lists, where cards are to go
deck = []
discard = []
piles = [deck,discard]

#init for list of hands, cards held by each player
hands = []

#more variables for actual game, including rounds, turns, ongoing card visuals, points and winner info
rackRound = 0
turn = 0
noOfTurns = 0 
cardDealt = 0
points = [[0],[0],[0],[0]]
winner = []
gameWinner = 0
pointRecord = 0
turnRecord = 0

#string init for proper keyboard input for login menus
alpha = "abcdefghijklmnopqrstuvwxyz"
alphaNum = "abcdefghijklmnopqrstuvwxyz123456789"

#opens each line of players.txt (our player database) to a new list in userInfo. Each list in  list userinfo contains info for said user segmented into individual elements (name, password, recordTurn, etc.) 
playerFile = open('players.txt', 'r')
userInfo = playerFile.read().splitlines()
for i in range(len(userInfo)):
    userInfo[i] = userInfo[i].split()
playerFile.close()
#more variable init for names and codes for current users playing for easy access to information needed
playerNames = []
playerCodes = []

#game Loop
while running:
    for evnt in event.get():
        # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            # checks if any mouse button is down,  if so sets clicking to true
            button = evnt.button
        if evnt.type == MOUSEMOTION:
            # sets mx and my to mouse x and y if mouse is moving
            mx, my  = evnt.pos
        if button==1: #if button is pressed, activates all these other conditions
            #conditions for specific , menu states, mostly button statuses. 
            if menu == MAIN:
                #allows the player to choose what to do
                for buttons in range(len(mainMenu)):
                    if Rect(mainMenu[buttons]).collidepoint(mx, my):
                        menu = buttons + 1
            elif menu == PLAYERNO:
                #allows player to choose how many players are going to play, deals and shuffles cards to players accordingly
                for buttons in range(len(playerNumbers)):
                    if Rect(playerNumbers[buttons]).collidepoint(mx, my):
                        if buttons + 1==1:
                            for card in range(1, 25 + 1):
                                deck.append(card)
                        else:
                            for card in range(1, 40 + (buttons  - 1) * 10 + 1):
                                deck.append(card)
                        players = buttons + 1
                        shuffle(deck)
                        for hand in range(buttons + 1):
                            hands.append([])
                            for card in range(10):
                                hands[hand].append(deck.pop())
                        #brings players over to login screen, sets turn to random
                        menu = LOGIN
                        turn = randrange(players)
            elif menu==LOGIN:
                #takes care of input states for each input area on screen. basically, if one is on, all others have to be off. this is done using lists of lists initialized in the above section for list and input constants
                for pl in range(players):
                    for buttons in range(len(loginButtons[pl])):
                        if Rect(loginButtons[pl][buttons]).collidepoint(mx, my):
                            #toggles input stat
                            if logStat[pl][buttons]:
                                logStat[pl][buttons] = False
                            else:
                                logStat[pl][buttons] = True  
                            # turns all other input stats off
                            for j in range(players):
                                if j!=pl:
                                    logStat[j] = [False,False]
                                else:
                                    for i in range(2):
                                        if i != buttons:
                                            logStat[pl][i] = False
                #if user clicks "next" button, checks validity of input. If some field is empty, stops. if username is correct but password does not match, stops. If nothing matches, makes new user. A lot of this code is visual (draw. rect, text, etc) so i'm not going to comment on it because it is explained here.
                if Rect(nextButton[0]).collidepoint(mx, my):
                    for pl in range(players): #for each player playing 
                        if not logInfo[pl][0] and not logInfo[pl][1]: #checks that field is not empty
                            draw.rect(screen,WHITE,nextButton[1])
                            draw.rect(screen,RED,nextButton[1],5)                                
                            text = fontCalBig.render("Not all fields filled", 1, BLACK)	
                            screen.blit(text, Rect(nextButton[1][0]+5,nextButton[1][1]+3,nextButton[1][2],nextButton[1][3]))
                            display.flip()
                            time.wait(1000)
                            break
                        else:
                            print("logging")
                            if len(userInfo) != 0: #checks length of file, if empty, adds users into file. if not, trys to log them in.
                                print("file is not empty")
                                found = False
                                wrongPass = False
                                for user in userInfo: #for each player, matches input to all usernames and passwords in database at the moment
                                    name = user[0]
                                    password = user[1]
                                    if logInfo[pl] == [name,password]: #if name and pass match, logs player in, adding his name to game vars and his unique user code
                                        found =  True
                                        playerNames.append(logInfo[pl][0])   
                                        playerCodes.append(userInfo.index(user))                                        
                                        draw.rect(screen,WHITE,nextButton[1])
                                        draw.rect(screen,GREEN,nextButton[1],5)                                
                                        text = fontCalBig.render("logged player %i" %(pl+1), 1, BLACK)	
                                        screen.blit(text, Rect(nextButton[1][0]+5,nextButton[1][1]+3,nextButton[1][2],nextButton[1][3]))
                                        display.flip()
                                        time.wait(1000)       
                                        
                                    elif logInfo[pl][0] == name: #if only name matches, breaks both loops and requires user to input again
                                        draw.rect(screen,WHITE,(nextButton[1][0]-275,nextButton[1][1],nextButton[1][2]+550,nextButton[1][3]))
                                        draw.rect(screen,RED,(nextButton[1][0]-275,nextButton[1][1],nextButton[1][2]+550,nextButton[1][3]),5)            
                                        text = fontCalBig.render("Player %i: name already exists, or wrong password" %(pl+1), 1, BLACK)	
                                        screen.blit(text, Rect(nextButton[1][0]-270,nextButton[1][1]+3,nextButton[1][2],nextButton[1][3]))
                                        display.flip()
                                        time.wait(3000)                                         
                                        found = True
                                        wrongPass = True
                                        break
                                else:
                                    if not found: #registers new user if input info is new to file, adding his name to game vars and his unique user code
                                            userInfo.append([str(logInfo[pl][0]), str(logInfo[pl][1]), "99", "99", "99", "99", "0", "0", "0", "0", "0", "0", "0", "0", "0"])
                                            playerNames.append(logInfo[pl][0])
                                            playerCodes.append(len(userInfo)-1)                                            
                                            draw.rect(screen,WHITE,nextButton[1])
                                            draw.rect(screen,GREEN,nextButton[1],5)                                
                                            text = fontCalBig.render("registered player %i" %(pl+1), 1, BLACK)	
                                            screen.blit(text, Rect(nextButton[1][0]+5,nextButton[1][1]+3,nextButton[1][2],nextButton[1][3]))
                                            display.flip()
                                            time.wait(1000) 
                                if wrongPass: #used in situations where pass is wrong to break loop
                                    break
                            else: #used if file is empty (registers user)
                                print("file is empty")
                                userInfo.append([str(logInfo[pl][0]), str(logInfo[pl][1]), "99", "99", "99", "99", "0", "0", "0", "0", "0", "0", "0", "0", "0"])
                                playerNames.append(logInfo[pl][0])
                                playerCodes.append(pl)
                                draw.rect(screen,WHITE,nextButton[1])
                                draw.rect(screen,GREEN,nextButton[1],5)                                
                                text = fontCalBig.render("registered player %i" %(pl+1), 1, BLACK)	
                                screen.blit(text, Rect(nextButton[1][0]+5,nextButton[1][1]+3,nextButton[1][2],nextButton[1][3]))                                
                                display.flip()
                                time.wait(1000)                                
                                
                            print("Done logging",pl)
                            time.wait(25)
                    else:
                        #if nothing broke, moves player into actual game.
                        menu = DECK
                    break
            elif menu == DECK:
                for buttons in range(len(deckRect)):
                    if Rect(deckRect[buttons]).collidepoint(mx, my): #checks if draw or discard piles were pressed
                        if cardDealt!=0: #if there is no ongoing card, tries to pull one from desired deck
                            if buttons==1:
                                try :
                                    piles[buttons].append(cardDealt)
                                    cardDealt=0
                                    if turn == players-1:
                                        turn = 0
                                    else:
                                        turn += 1 
                                    if players == 1:
                                        noOfTurns+=1                                    
                                except:
                                    pass
                        else:
                            try:
                                cardDealt = piles[buttons].pop()
                            except:
                                print("Empty") #if draw deck is empty, loses the game for solo players, but flips discard pile into a new draw deck if there is more than 1 player
                                if players != 1:
                                    piles[0] = piles[1][::-1]
                                    piles[1].clear()
                                else:
                                    #displays lose screen and returns to main menu automatically
                                    screen.blit(bgDim, Rect(0, 0, 1000, 700))
                                    draw.rect(screen, DD_RED, (250, 200, 500, 50))
                                    text = fontCalBig.render("Draw pile depleted.", 1, WHITE)
                                    screen.blit(text, Rect(250,200,500,50))
                                    draw.rect(screen, DD_RED, (250, 250, 500, 50))
                                    text = fontCalBig.render("You lose!", 1, WHITE)
                                    screen.blit(text, Rect(250,250,500,50))                                    
                                    display.flip()
                                    time.wait(3000)
                                    hands = []
                                    deck = []
                                    playerNames = []
                                    playerCodes = []
                                    piles = [[],[]]
                                    turn = 0
                                    noOfTurns = 0 
                                    cardDealt = 0   
                                    players = 0
                                    winner = []
                                    menu = MAIN                                     
                        
                for buttons in range(len(traySlot)):
                    if Rect(traySlot[buttons]).collidepoint(mx, my): #checks if any slots in player's own hand were pressed
                        if cardDealt != 0: #if ongoing card is present, switches ongoing card with card pressed. if player = 1, old card gets thrown away. Otherwise, card goes to discard pile.
                            if players!=1:
                                piles[1].append(hands[turn][buttons])
                            else:
                                noOfTurns+=1                                
                            hands[turn][buttons]=cardDealt
                            cardDealt = 0
                            display.flip()
                            time.wait(250)  
                            #changes turn
                            if turn == players-1:
                                turn = 0
                            else:
                                turn += 1

            elif menu == WIN:#checks button presses for round win screen
                if players != 1:
                    if Rect(winRect[0]).collidepoint(mx,my): #if "next round is pressed, sets up vars for next round, then goes to next round.
                        rackRound += 1
                        turn = randrange(players)
                        for pl in range(players):
                            points[pl].append(0)
                        deck = []
                        discard = []
                        piles = [deck,discard] 
                        for card in range(1, 41 + (players - 1) * 10):
                            deck.append(card)  
                        shuffle(deck)
                        for hand in range(players):
                            hands[hand] = []
                            for card in range(10):
                                hands[hand].append(deck.pop())
                        menu = DECK
                if Rect(winRect[1]).collidepoint(mx,my): # if exit game is pressed, exits out of game to main menu, resetting everything
                    hands = []
                    deck = []
                    playerNames = []
                    playerCodes = []
                    piles = [[],[]]
                    turn = 0
                    noOfTurns = 0 
                    cardDealt = 0   
                    players = 0
                    winner = []
                    menu = MAIN                    
            
            elif menu == HIGHoPTION: #checks button presses for options screen
                if Rect(backRect).collidepoint(mx,my): #back button is self-explanatory
                    menu = MAIN
                #checks all main buttons for presses
                for button in range(len(optionRect)): 
                    if Rect(optionRect[button]).collidepoint(mx,my):
                        if button < 1:
                            menu = DELETE # if delete account is pressed, sets menu to account deletion screen
                        elif button < 4: # if button pressed is within range for average point records, sets menu to appropriate point records (using player numbers)
                            menu = POINTS
                            pointRecord = button
                        else: #otherwise, sets menu to appropriate number of turns record (using player numbers)
                            menu = TURNS
                            turnRecord = button-3
            
            elif menu == DELETE: #checks button presses for account deletion screen. this is similar to login screen, minus the player counting. basically, if account is found, it is deleted, if something doesnt match, or field is empty, stops process and makes user redo their input, along with an appropriate warning
                for buttons in range(len(delButtons)):
                    if Rect(delButtons[buttons]).collidepoint(mx, my): 
                        if delStat[buttons]:
                            delStat[buttons] = False
                        else:
                            delStat[buttons] = True  
                            for i in range(2):
                                if i != buttons:
                                    delStat[i] = False 
                if Rect(deleteButton).collidepoint(mx, my): # field emptyness sensor
                        if not delInfo[0] or not delInfo[1]:
                            draw.rect(screen,WHITE,deleteButton)
                            draw.rect(screen,RED,deleteButton,5)                                
                            text = fontCalBig.render("Not all fields filled", 1, BLACK)	
                            screen.blit(text, Rect(deleteButton[0]+5,deleteButton[1]+3,deleteButton[2],deleteButton[3]))
                            display.flip()
                            time.wait(1000)
                            break
                        else:
                            print("logging") # checks validity of input, same way login screen handles it.
                            if len(userInfo) != 0:
                                print("file is not empty")
                                found = False
                                wrongPass = False
                                for user in userInfo:
                                    name = user[0]
                                    password = user[1]
                                    if delInfo == [name,password]:
                                        found =  True
                                        userInfo.remove(user)
                                        draw.rect(screen,WHITE,(deleteButton[0],deleteButton[1],deleteButton[2]+300,deleteButton[3]))
                                        draw.rect(screen,GREEN,(deleteButton[0],deleteButton[1],deleteButton[2]+300,deleteButton[3]),5)                      
                                        text = fontCalBig.render("succesfully deleted account", 1, BLACK)	
                                        screen.blit(text, Rect(deleteButton[0]+5,deleteButton[1]+3,deleteButton[2],deleteButton[3]))
                                        display.flip()
                                        time.wait(1000)       
                                        
                                    elif delInfo[0] == name:
                                        draw.rect(screen,WHITE,(deleteButton[0]-275,deleteButton[1],deleteButton[2]+550,deleteButton[3]))
                                        draw.rect(screen,RED,(deleteButton[0]-275,deleteButton[1],deleteButton[2]+550,deleteButton[3]),5)            
                                        text = fontCalBig.render("Wrong password" %(pl+1), 1, BLACK)	
                                        screen.blit(text, Rect(deleteButton[0]-270,deleteButton[1]+3,deleteButton[2],deleteButton[3]))
                                        display.flip()
                                        time.wait(1000)                                         
                                        found = True
                                        wrongPass = True
                                        break
                                else:
                                    if not found:
                                            draw.rect(screen,WHITE,deleteButton)
                                            draw.rect(screen,GREEN,deleteButton,5)                                
                                            text = fontCalBig.render("No such player exists" %(pl+1), 1, BLACK)	
                                            screen.blit(text, Rect(deleteButton[0]+5,deleteButton[1]+3,deleteButton[2],deleteButton[3]))
                                            display.flip()
                                            time.wait(1000) 
                                            break
                                if wrongPass:
                                    break 
                elif Rect(backRect).collidepoint(mx,my): #if back button is pressed, goes to option screen
                    menu = HIGHoPTION
            
            elif menu == TURNS or menu == POINTS: #if back button is pressed, goes to option screen (during any record screens)
                if Rect(backRect).collidepoint(mx,my):
                    menu = HIGHoPTION
                    
            elif menu == WINGAME: #checks buttons during game win screen
                if Rect(winRect[1]).collidepoint(mx,my): #if exit button is pressed, resets all vars and goes to main menu
                    hands = []
                    deck = []
                    playerNames = []
                    playerCodes = []
                    piles = [[],[]]
                    rackRound = 0
                    turn = 0
                    noOfTurns = 0 
                    cardDealt = 0
                    points = [[0],[0],[0],[0]]
                    winner = []
                    gameWinner = 0
                    pointRecord = 0
                    turnRecord = 0
                    menu = MAIN                      
    
                
            button=0 # resets button to 0 
            
            
        if button==3: # cheat button, sorts current hand. I am keeping this in because it's easier for you to test it this way, if you are short on time.
            hands[turn].sort()
            hands[turn].reverse()
            button = 0
        if menu == LOGIN: #handles keyboard input for login screen
            for pl in range(players):
                for buttons in range(len(loginButtons[pl])):
                    if logStat[pl][buttons]:
                        if evnt.type == KEYDOWN:
                            if key.name(evnt.key) in alpha: 
                                if buttons==0 and len(logInfo[pl][0])<13:
                                    logInfo[pl][buttons]+=key.name(evnt.key) #adds letters to username if letter pressed
                            if key.name(evnt.key) in alphaNum:
                                if buttons==1 and len(logInfo[pl][1])<13:
                                    logInfo[pl][buttons]+=key.name(evnt.key) #adds letters or numbers to password if they are pressed                               
                            elif key.name(evnt.key)=="backspace": # deletes letter or numbers from current field if backspace is pressed
                                logInfo[pl][buttons] = logInfo[pl][buttons][:-1] 
        elif menu == DELETE: #handles keyboard input for delete account screen. this works as above but this time there are only 2 fields instead of a max of 8. Because of this, one loop is removed.
            for buttons in range(len(delButtons)):
                if delStat[buttons]:
                    if evnt.type == KEYDOWN:
                        if key.name(evnt.key) in alpha: 
                            if buttons==0 and len(delInfo[0])<13:
                                delInfo[buttons]+=key.name(evnt.key)
                        if key.name(evnt.key) in alphaNum:
                            if buttons==1 and len(delInfo[1])<13:
                                delInfo[buttons]+=key.name(evnt.key)                                
                        elif key.name(evnt.key)=="backspace":
                            delInfo[buttons] = delInfo[buttons][:-1]            
    if menu != WIN and menu != WINGAME: #checks if anyone is winning the round or the whole game
        for hand in hands: 
            if sum(points[hands.index(hand)]) >= 500: # checks if current player has 500 or points. if so, stops game and shows game win screen, as well as updates userInfo for total games, total points and average points per game for all players.
                gameWinner = hands.index(hand)
                noOfTurns //= players
                for pl in range(players):
                    userInfo[playerCodes[pl]][3+players*3] = int(userInfo[playerCodes[pl]][3 + players * 3]) + 1  #add to games of everyone involved
                    userInfo[playerCodes[pl]][4+players*3] = int(userInfo[playerCodes[pl]][4 + players * 3]) + sum(points[pl]) #add to total points of everyone involved
                    userInfo[playerCodes[pl]][5+players*3] = int(userInfo[playerCodes[pl]][4 + players * 3]) / int(userInfo[playerCodes[pl]][3 + players * 3]) #add to average score of everyone involved  
                menu = WINGAME #sets screen to game win display
            
            #handles points for each player for each round. basically, adds points as long as card is larger than the last. if loop goes to the end, triggers round win screen, win bonus.
            revHand = hand[::-1]             
            points[hands.index(hand)][rackRound] = 5 
            for card in revHand[1:]:
                if not card > revHand[revHand.index(card)-1]:
                    break
                points[hands.index(hand)][rackRound] += 5
            else:
                #bonus points and winner identification
                points[hands.index(hand)][rackRound] += 25
                winner.append(hands.index(hand))
                #alternatively, if player is alone
                if players == 1:
                    if noOfTurns<int(userInfo[playerCodes[winner[rackRound] ]][2]): 
                        userInfo[playerCodes[winner[rackRound]]][2] = str(noOfTurns)                        
                menu = WIN
    
    #handles all visuals. why call all these conditions again? it separates button presses and visual elements in an efficent way. code is pretty self-explanatory, corresponds with button press code.
    screen.blit(bgDim, Rect(0, 0, 1000, 700))
    if menu == MAIN:
        drawMain()
    elif menu == HIGHoPTION:
        drawOptions()
    elif menu == PLAYERNO:
        drawPlayers()
    elif menu==LOGIN:
        drawLogin(players,logInfo,logStat)
    elif menu== DECK:
        #drawing current turn hand
        drawDeck(cardDealt, piles[1], turn, points, rackRound)
        drawTray(hands[turn], turn, playerNames)
    elif menu==WIN:
        #drawing real winner hand
        drawTray(hand,turn,playerNames)
        drawWinscreen(winner[rackRound], hands[winner[rackRound]],turn, playerNames, points, noOfTurns, userInfo[playerCodes[winner[rackRound]]])
    elif menu == WINGAME:
        #drawing winner hand
        drawTray(hands[gameWinner], 0, playerNames)
        drawWinGame(gameWinner, noOfTurns, playerNames)
    elif menu == DELETE:
        drawDeleteAcc(delBox, delStat, delInfo, delButtons)
    elif menu == POINTS:
        drawPoints(userInfo, pointRecord) 
    elif menu == TURNS:
        drawTurns(userInfo, turnRecord)
    elif menu==EXIT:
        break
    display.flip()
#takes all lists in userInfo, turns it into one big string and writes it to file players.txt
playerFile = open("players.txt","w")
for user in userInfo:
    stringUser = [str(i) for i in user]
    playerFile.write(' '.join(stringUser)+'\n')
playerFile.close()
quit()