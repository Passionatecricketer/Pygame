import sys, pygame
pygame.init()

size = width, height = 900, 600
speed = [0, 1]
black = 0, 0, 0
white = 255,255,255
car_width=90

screen = pygame.display.set_mode(size)

car = pygame.image.load("C:\Users\Rishabh\Downloads\download.png")
carrect = car.get_rect()

def racecar(x,y):
    screen.blit(car,(x,y))

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((width/2),(height/2))
    screen.blit(textsurf,textrect)
    pygame.display.update()
    game()

def crash():
    message_display('Game Over')



def game():
    x = (width*0.5)
    y = (height*0.5)
    x_change=0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

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
        racecar(x,y)

        if x>width-car_width or x<0:
            crash()
    #screen.blit(car, carrect)
        pygame.display.flip()

game()
pygame.quit()
quit()
