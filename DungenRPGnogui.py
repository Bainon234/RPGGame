from os import mkdir, system, path
from time import sleep
from random import randint
import sys
syspath = sys.path #<-file_location
del sys
from sys import platform

class file_manager:
    folder_name = None
    def check_folder(name):
        if path.isdir(name): return 1
        file_manager.folder_name = name
        return 0
    def __new__(cls,number):
        if file_manager.check_folder('saves') == 0 and number >= 3: mkdir(syspath[0] + '/' + file_manager.folder_name)
class intro:
    print('|‾‾‾‾‾‾‾‾‾‾‾|\n| Welcome   |\n|   to      |\n| DungenRPG |\n|  Alptha   |\n|___________|\n')
    for i in range(12):
        print('[' + '-'*i + ']', end='\r')
        file_manager(i)
        sleep(0.045)
    print('       Type (start,load or quit)', end='\r')
class stats:
    playerlocation = player_max_health = player_experiance = player_level = player_gold = player_dmg = None
    def __new__(cls,pl = None, pmh = None, pxp =None, plevel = None, pg = None,pdmg=None):
        playerlocation = plevel
        player_max_health = pmh
        player_experiance = pxp
        player_level = pl
        player_gold = pg
        player_dmg = pdmg
class game:
    def generate(layout = [],vec2=(randint(4,10),randint(4,10))):
        for i in range(vec2[0]+1):
            layout.append([])
            for j in range(vec2[1]):
                layout[i] += '.'
        while 1:
            try:
                stats.playerlocation =[randint(1,vec2[1]-1),randint(1,vec2[0]-1)]
                layout[stats.playerlocation[0]][stats.playerlocation[1]] = 'p'
                break
            except IndexError:pass
        return layout
    def player_controls(usr):
        stats.playerlocation[0] -= int(usr.lower() == 'w')
        stats.playerlocation[0] += int(usr.lower() == 's')
        stats.playerlocation[1] -= int(usr.lower() == 'a')
        stats.playerlocation[1] += int(usr.lower() == 'd')
        return usr
    def update(target,changes):
        if changes == 'w':  target[stats.playerlocation[0] + 1][stats.playerlocation[1]] = '_'
        elif changes == 's':target[stats.playerlocation[0] - 1][stats.playerlocation[1]] = '_'
        elif changes == 'a':target[stats.playerlocation[0]][stats.playerlocation[1]+1] = '_'
        elif changes == 'd':target[stats.playerlocation[0]][stats.playerlocation[1]-1] = '_'
        if changes in ['w','a','s','d']:target[stats.playerlocation[0]][stats.playerlocation[1]] = 'P'
        
    def dungon(map = generate()):
        while 1:
            for i in range(len(map)):print(''.join(map[i][:]).replace('.',' . ').replace('P', ' P ').replace('_', ' _ '))
            print(stats.playerlocation)
            game.update(map,game.player_controls(input('<move>')))
    def shop():pass
    def streets():
        print('level:',stats.player_level,'health:',stats.player_max_health,'damage:',stats.player_dmg)
        usr = input('<streets>')
        for i in range(2):
            if platform == 'linux': system('clear')
            if platform == 'win32': system('cls')
            if usr.lower() == ['dungon','shop'][i]:[game.dungon,game.shop][i]()
class menu:
    def load(): pass
    def clear():
        if platform == 'linux': system('clear')
        elif platform == 'win32': system('cls')
    def quit():del game
    def switch_logic(usr):
        for i in range(4):
            if usr.lower() == ['load','clear','quit','start'][i]:[menu.load,menu.clear,menu.quit,game.streets][i]()
        if not usr.lower() in ['load','clear','quit','start']:   print(f'Error: {usr} is not in commands')
    def __new__(cls):
        while 1:
            menu.switch_logic(input('<menu> '))
if __name__ == '__main__':
    del intro
    menu()