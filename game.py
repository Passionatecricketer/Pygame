import pygame
import time
import random

pygame.init() #initialize pygame

width = 1350
height = 690 #size parameters for starting wondow

black = 0, 0, 0
white = 255,255,255
color = 0,200,100
blue = 0,0,255
green = 0,255,0
red = 255,0,0 #color coordinates (r,g,b)

car_width=90 #width of the car

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Racing car hurdle cross')
clock = pygame.time.Clock() #Mandatory commands to start the screen and enable gameplay

car = pygame.image.load("download1.png")#Image loading
pygame.display.set_icon(car)
pause = False

crash_sound = pygame.mixer.Sound("crash.wav")

def obstacle(obx,oby,obw,obh,color): #Function defintion for the structure of obstacle
    pygame.draw.rect(screen,color,[obx,oby,obw,obh])

def racecar(x,y): #Function to show car
    screen.blit(car,(x,y))

def text_objects(text,font): #Function used in message display
    textsurface=font.render(text,True,blue)
    return textsurface,textsurface.get_rect()

def crash(): #Function to check what happens acr touches obstacle aur boundary
    
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #screen.fill(white)
        largeText = pygame.font.SysFont('Arial',150)
        TextSurf,TextRect = text_objects("Game Over!!",largeText)
        TextRect.center = (675,100)
        screen.blit(TextSurf,TextRect)

        button("Play again!!",475,450,100,50,green,game)
        button("Quit",775,450,100,50,red,quitgame)
        pygame.display.update()
        clock.tick(30)

def block_dodged(count): #Function to check the count of blocks dodged
    font = pygame.font.SysFont('Arial',25)
    text = font.render("Score: "+str(count),True,red)
    screen.blit(text,(0,0))

def button(msg,x,y,w,h,c,action=None): #Generalized function to create any button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(screen,c,(x,y,w,h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(screen,c,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",15)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textSurf,textRect)

def paused(): #Function to see what happens when game is paused
    
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #screen.fill(white)
        largeText = pygame.font.SysFont('Calibri',150)
        TextSurf,TextRect = text_objects("Game Paused",largeText)
        TextRect.center = (675,100)
        screen.blit(TextSurf,TextRect)

        button("Continue",400,450,100,50,green,unpause)
        button("Restart",625,450,100,50,color,game)
        button("Quit",850,450,100,50,red,quitgame)
        pygame.display.update()
        clock.tick(30)

def unpause(): #to continue function from same step
    global pause
    pygame.mixer.music.unpause()
    pause = False


def game_intro(): #Start menu of the game

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        largeText = pygame.font.SysFont('Algerian',70)
        TextSurf,TextRect = text_objects("Racing car Hurdle cross",largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf,TextRect)

        button("Let's Play!!",475,450,100,50,green,game)
        button("Quit",775,450,100,50,red,quitgame)
        pygame.display.update()
        clock.tick(30)


def game(): #Main game function

    global pause

    pygame.mixer.music.load("Twirly_Tops.mp3")
    pygame.mixer.music.play(-1)
    
    x = (width*0.5)
    y = (height*0.5)
    x_change=0

    ob_startx = random.randrange(0,width)
    ob_starty = -600
    ob_speed = 5
    ob_width = 80
    ob_height = 80

    dodged = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x+=x_change

        screen.fill(black)

        obstacle(ob_startx,ob_starty,ob_width,ob_height,white)
        ob_starty+=ob_speed
        
        racecar(x,y)

        block_dodged(dodged)

        if x > width - car_width or x < 0:
            crash()

        if ob_starty > height:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0,width)
            dodged+=1
            ob_speed+=1

        if y < ob_starty+ob_height:
            print "y crossover"

            if x > ob_startx and x < ob_startx + ob_width or x+car_width > ob_startx and x + car_width < ob_startx+ob_width:
                print "x crossover"
                crash()
                
        pygame.display.update()
        clock.tick(60)

def quitgame(): #When game is aborted
    pygame.quit()
    quit()

game_intro()
game()
pygame.quit()
quit()
