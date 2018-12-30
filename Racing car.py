import pygame
import time
import random
pygame.init()

width = 700
height = 700
#speed = [0, 1]
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
green = 0,255,0
red = 255,0,0
car_width=90

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Racing car hurdle cross')
clock = pygame.time.Clock()

car = pygame.image.load("C:\Users\Rishabh\Downloads\download1.png")
#carrect = car.get_rect()

def obstacle(obx,oby,obw,obh,color):
    pygame.draw.rect(screen,color,[obx,oby,obw,obh])

def racecar(x,y):
    screen.blit(car,(x,y))

def text_objects(text,font):
    textsurface=font.render(text,True,blue)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((width/2),(height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game()

def crash():
    message_display('Game Over')

def block_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(count),True,red)
    screen.blit(text,(0,0))


def game():
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
            if event.type == pygame.QUIT: #sys.exit()
                pygame.quit()
                quit()

            '''pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                x_change = -5
            elif pressed[pygame.K_RIGHT]:
                x_change = 5'''
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x+=x_change

        '''carrect = carrect.move(speed)
        if carrect.left < 0 or carrect.right > width:
            speed[0] = -speed[0]
        if carrect.top < 0 or carrect.bottom > height:
            speed[1] = -speed[1]'''

        screen.fill(white)

        obstacle(ob_startx,ob_starty,ob_width,ob_height,black)
        ob_starty+=ob_speed
        
        racecar(x,y)

        block_dodged(dodged)

        if x > width - car_width or x < 0:
            crash()
    #screen.blit(car, carrect)

        if ob_starty > height:
            ob_starty = 0 - ob_height
            ob_startx = random.randrange(0,width)
            dodged+=1
            ob_speed+=1
            ob_width+=(dodged*1.1)

        if y < ob_starty+ob_height:
            print "y crossover"

            if x > ob_startx and x < ob_startx + ob_width or x+car_width > ob_startx and x + car_width < ob_startx+ob_width:
                print "x crossover"
                crash()

        #pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()
quit()
