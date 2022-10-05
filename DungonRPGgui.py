from os import mkdir, system, path
from time import sleep
from random import randint, seed, random
import sys,pygame,Simplebutton

syspath = sys.path  # <-file_location
del sys
from sys import platform, exit

pygame.init()


def clear():
    #poriable clear function
    for i in range(2):
        if platform == ("linux", "win32")[i]:
            system(("clear", "cls")[i])

class game:
    player = () #Player will have the most objects so far I appending the information to make it less complicated
    def __init__(self, screen):
        
        screen = pygame.display.set_mode(
            screen
        )  # (width, height) -> Most important agument to display the window
        screen.fill("White")
        clock = pygame.time.Clock()  # frame
        b = Simplebutton.SimpleButton(screen, (50,50), 'assets/buttonup.png', 'assets/buttondown.png')
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()  # This is sys.exit and please check the imports
            if b.handleEvent(event):
                print('test')
            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    game((800, 400))
