from os import mkdir, system, path
from time import sleep
from random import randint,seed,random
import sys
syspath = sys.path #<-file_location
del sys
from sys import platform
class stats:playerlocation = player_kills = inflation = player_health = player_max_health = player_experiance = player_level = player_gold = player_dmg = 0
def clear():
        if platform == 'linux':   system('clear')
        elif platform == 'win32': system('cls')
class file_manager:
    files = []
    if not path.isdir('save'): mkdir('save')
    if not path.isfile('save/fl.lc'): 
        with open('save/fl.lc', 'w') as f:f.close()
        
    with open('save/fl.lc','r') as fl:
        for line in fl:files += line
        fl.close()
    def load():pass
    def save():
        filename = input('What name would you like to save? ')
        if not filename in ['',' ']:
            with open(f'save/{filename}.sav', 'w') as save:
                stuff_into_save = str(stats.player_health) + str(stats.player_max_health) + str(stats.player_experiance) + str(stats.player_level) + str(stats.player_gold) + str(stats.player_dmg)
                save.write(' '.join(format(x,'b') for x in bytearray(stuff_into_save, 'utf-8'))[::-1])
                file_manager.files.append(f'{filename}.sav') 
                print(file_manager.files)
            with open('save/fl.lc', 'w') as fl:
                for i in range(len(filename)):
                    for j in range(len(filename[i])):
                        fl.write(' '.join(format(x,'b') for x in bytearray(f'{filename[i][j]}.sav','utf-8')) + ' ')
                fl.write('\n')
                fl.close()
                
class intro:
    print('|‾‾‾‾‾‾‾‾‾‾‾|\n| Welcome   |\n|   to      |\n| DungenRPG |\n|  devbui   |\n|___________|\n')
    for i in range(12):
        print('[' + '-'*i + ']', end='\r')
        sleep(0.045)
    print('       Type (start,load or quit)', end='\r')
class game:
    def generate(layout = [],vec2=(randint(4,10),randint(4,10))):
        for i in range(vec2[0]+1):
            layout.append([])
            for j in range(vec2[1]):layout[i] += '.'
        while 1:
            try:
                stats.playerlocation =[randint(1,vec2[1]-1),randint(1,vec2[0]-1)]
                layout[stats.playerlocation[0]][stats.playerlocation[1]] = 'p'
                break
            except IndexError:pass
        return layout
    def player_controls(usr):
        if not usr.lower() in ['w','a','s','d']:print(f'Error: {usr} is not a invalid move command')
        if (usr := usr.lower()) in ['w','a','s','d']:
            stats.playerlocation[0] += int(usr == 's') - int(usr == 'w')
            stats.playerlocation[1] += int(usr == 'd') - int(usr == 'a')
            return usr
        return None
    def check_level():
        for i in range(int(stats.player_experiance/5)):
            if stats.player_experiance >= 5 + 5 * stats.player_level:
                stats.player_level += 1
                stats.player_experiance -= 5 + 5 * stats.player_level
                stats.player_health += randint(1,5)
                stats.player_dmg += randint(1,5)
        
    def battle(enemy_health, enemy_attack):
        stats.player_health = stats.player_max_health
        while 1:
            seed(random())
            if enemy_health <= 0: 
                stats.player_gold += 10 + 10 * stats.player_level
                stats.player_experiance += 5
                return 1
            if stats.player_health < 0:return 0
            print(f'player health: {stats.player_health} enemy health: {enemy_health}')
            usr = input('<in-combat> ').lower()
            if usr == 'ack' and randint(1,4) == 4: enemy_health -= stats.player_dmg
            if usr in ['ack'] and randint(1,4): stats.player_health -= enemy_attack
            if usr == 'run' and randint(1, 4) == 4: return 1
    def update(target,changes):
        if len(target) == 1: 
            del target[0]
            return True
        if changes in ['w','a','s','d'] and randint(0, 8) == 8:game.battle(5 + 2 * stats.player_level, randint(1, 2) + randint(1,3) * stats.player_level)
        if not changes == None:
            try:
                if changes in ['w','a','s','d']:target[stats.playerlocation[0]+int(changes == 'w')-int(changes=='s')][stats.playerlocation[1]+int(changes=='a')-int(changes=='d')] = '_'
                if changes in ['w','a','s','d']:target[stats.playerlocation[0]][stats.playerlocation[1]] = 'P'
            except IndexError:
                try:
                    if changes in ['w','a','s','d']:
                        if changes in ['a','d']: stats.playerlocation[1] = 0
                        if changes in ['w','s']: stats.playerlocation[0] = 0
                        if changes in ['w','a','s','d']:target[stats.playerlocation[0]][stats.playerlocation[1]] = 'P'
                except IndexError: pass
        try:
            for i in range(len(target)):
                if target[i] == list('_'*len(target[i])): del target[i]
        except IndexError: pass
    def dungon():
        map = game.generate()
        while 1:
            for i in range(len(map)):print(''.join(map[i][:]).replace('.',' . ').replace('P', ' P ').replace('_', ' _ '))
            print(stats.playerlocation)
            if game.update(map,game.player_controls(input('<move>'))):
                stats.inflation = randint(-1, 3) + randint(-1, 3) + randint(-1, 3) + randint(-1, 3)
                clear()
                print('Dungon cleared!')
                return 1
            clear()
    def shop():
        hp,dmg = int(1.5 * stats.player_max_health),5 * stats.player_dmg
        if stats.inflation > 0: hp,dmg = stats.player_max_health * stats.inflation,stats.player_dmg * stats.inflation
        while 1:
            clear()
            print(f"gold:{stats.player_gold}\nupgrades: \n1: more hp: {hp}g\n2: more dmg:{dmg}g")
            usr = input('<shop>')
            if usr == '1' and stats.player_gold >= hp : 
                stats.player_max_health += int(hp/2)
                stats.player_gold -= hp
            if usr == '2' and stats.player_gold >= dmg:
                stats.player_dmg += int(dmg/2)
                stats.player_gold -= dmg
            if usr.lower() == 'quit': break
    def streets():
        while 1:
            print('level:',stats.player_level,'health:',stats.player_max_health,'damage:',stats.player_dmg)
            usr = input('<streets>')
            clear()
            for i in range(3):
                if usr.lower() == ['dungon','shop','save'][i]:
                    if [game.dungon,game.shop,file_manager.save][i]():
                        stats.inflation = randint(-1, 3) + randint(-1, 3) + randint(-1, 3) + randint(-1, 3)
                        game.check_level()
                        
class menu:
    def default_start():
        stats.player_max_health = 10
        stats.player_dmg = 5
        game.streets()
    def load(): pass
    def quit():return 1
    def switch_logic(usr):
        for i in range(4):
            if usr.lower() == ['load','clear','quit','start'][i]:[menu.load,clear,menu.quit,menu.default_start][i]()
        if not usr.lower() in ['load','clear','quit','start']   :print(f'Error: {usr} is not in commands')
    def __new__(cls):
        while 1:menu.switch_logic(input('<menu> '))
if __name__ == '__main__':
    del intro
    if menu():
        del file_manager, stats, game, clear
        quit()