from os import mkdir, system, path
from time import sleep
from random import randint,seed,random
import sys, pygame
syspath = sys.path #<-file_location
del sys
from sys import platform
class stats:playerlocation = player_kills = inflation = player_health = player_max_health = player_experiance = player_level = player_gold = player_dmg = 0
def clear():
    for i in range(3):
        if platform == ['linux','win32'][i]:   system(['clear','cls'][i])
class file_manager:
    files,info  = [], None
    if not path.isdir('save'): mkdir('save')
    if not path.isfile('save/fl.lc'):
        with open('save/fl.lc', 'w') as f:f.close()
    def load():
        with open('save/fl.lc', 'r') as fl:file_manager.files += fl.read().replace('\n',' ').split()
        if len(file_manager.files) >= 1:
            print(str(file_manager.files).replace('.sav', ''))
            usr = input('<choose>')
            if usr in str(file_manager.files).replace('.sav', ''):
                for i in range(len(file_manager.files)):
                    if (usr := usr.lower()) == file_manager.files[i].replace('.sav',''):
                        with open(f'save/{file_manager.files[i]}', 'r') as sv:
                            info = sv.read()[::-1].split()
        if not info == None:
            for i in range(len(info)):info[i] = chr(int(info[i],2))
            info = ''.join(info)
            for i in range(4):info = info.replace(['mh','ep','pl','pg'][i], ' ')
            info = info.split()
            for i in range(len(info)):info[i] = int(info[i])
            stats.player_max_health= info[0]
            stats.player_experiance = info[1]
            stats.player_level = info[2]
            stats.player_gold = info[3]
            stats.player_dmg = info[4]
class game:
    pygame.init()
    pygame.mouse.set_cursor(pygame.cursors.arrow)
    display = display_info = clock = None
    buttonzero = buttonone = buttontwo = pygame.image.load('assets/button.png')
    def display_size(x,y):
        game.display_info,game.display,game.clock = (x,y),pygame.display.set_mode((x,y)), pygame.time.Clock()
    def phasezero():
        game.display.fill(pygame.color.Color(255, 255,255))
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:return 0
            for i in range(3):game.display.blit((game.buttonzero, game.buttonone, game.buttontwo)[i],(int(game.display_info[0] * 1/2.5),game.display_info[1]* (1/1.3, 1/2.25,1/6)[i]))
            pygame.display.update()
            game.clock.tick(60)
    def __new__(cls, x_size,y_size, title, list_of_phrases = None):
        game.display_size(x_size,y_size),pygame.display.set_caption(title)
        if (list_of_phrases := game.phasezero()) == 1:pass
        return 1
        
if __name__ == '__main__':
    if game(800, 400, 'test') == 1:
        del clear, file_manager, game