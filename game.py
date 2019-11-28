import pygame, time, random

pygame.init()
pygame.mixer.init()

crash_sound = pygame.mixer.Sound("Audio/carcrash.wav")
pygame.mixer.music.load("Audio/noticed.wav")

#Resolution
display_width = 800
display_height = 600

#Färger
black = (0,0,0)
gray = (66,66,66)
white = (255,255,255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

car_height = 158
car_width = 60

#Spelfönsternamnochklocka
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('s90.png')

clock = pygame.time.Clock()

#Bilder
#carImg = pygame.image.load('Bilder/s90.png')
carImg = pygame.image.load('Bilder/cybertrucksmall.png')
startImg = pygame.image.load('Bilder/Teslacyber.png')
Gata1 = pygame.image.load("Bilder/Gata1.png")
carImg2 = pygame.image.load("Bilder/bubbla.png")
carImg3 = pygame.image.load("Bilder/audi.png")
carImg4 = pygame.image.load("Bilder/honda.png")
carImg5 = pygame.image.load("Bilder/konig.png")

#carImgList = [carImg3, carImg4, carImg5]

pygame.display.set_icon(carImg2)

#background = None

#pausemeny variabel
pause = False

#Funktioner

#Score counter
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, white)
    gameDisplay.blit(text,(10,10))
    
def dodge_cars(thingx,thingy,carImgList):
    gameDisplay.blit((carImg3), (thingx,thingy))

#bilens plats
def display_car(x,y):
    gameDisplay.blit(carImg,(x,y))

#Textobjects
def text_objectswhite(text, font):
    TextSurface = font.render(text, True, white)
    return TextSurface, TextSurface.get_rect()
def text_objectsblack(text, font):
    TextSurface = font.render(text, True, black)
    return TextSurface, TextSurface.get_rect()
def text_objectsgray(text, font):
    TextSurface = font.render(text, True, gray)
    return TextSurface, TextSurface.get_rect()

def crash():

    global dodged
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    crash = True
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objectswhite("You Crashed!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
    
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

#Knappar
def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
        else:
             pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        TextSurf, TextRect = text_objectswhite(msg, smallText)
        TextRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

#Pausemeny
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objectswhite("PAUSED", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        button("CONTINUE",150,450,100,50,green,bright_green,unpause)
        button("QUIT",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

#startmeny
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(startImg, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objectsgray("DODGE CARS", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("START",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

#Gamemechanics
def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.7) 

    x_change = 0

    thing_startx = random.randrange(0 + 165, display_width - 235)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    ypos = 0 

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        #Bakgrund
        
        # Rörelsen
        rel_ypos = ypos % Gata1.get_rect().height
        gameDisplay.blit(Gata1, (0,rel_ypos - Gata1.get_rect().height))
        if rel_ypos < display_height:
            gameDisplay.blit(Gata1, (0, rel_ypos))
        ypos += thing_speed + 1
        
        
        # Saker    
        dodge_cars(thing_startx, thing_starty, carImg3)
    
        thing_starty += thing_speed
        display_car(x,y)   
        things_dodged(dodged)
        

        # Banans gränser
        if x > 565 or x < 165:
            crash()
        

        if thing_starty > display_height:
            thing_starty = 0 - car_height
            thing_startx = random.randrange(165,565)
            dodged += 1
            thing_speed += 0.7

        if y < thing_starty+thing_height:

            if x > thing_startx and x < thing_startx + car_width or x + car_width > thing_startx and x + car_width < thing_startx + car_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
