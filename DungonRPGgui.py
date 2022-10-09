from os import mkdir, system, path
from time import sleep
from random import randint, seed, random
import sys,pgzrun
syspath = sys.path  # <-file_location
del sys
from sys import platform, exit
objects = ''
mode = 0
def buttonize(image_up, image_down, array_type = 'list'):
    return eval(f'{array_type}((Actor("{image_up}"), Actor("{image_down}"), 0))')
        
    
    
WIDTH = 800
HEIGHT = 400

but_one = buttonize('buttonup.png','buttondown.png')
but_two = buttonize('buttonup.png','buttondown.png')
but_three = buttonize('buttonup.png','buttondown.png')
objects += 'but_one[but_one[2]].draw(),but_two[but_two[2]].draw(),but_three[but_three[2]].draw()'

def update():
    if mode == 0:
        but_one[but_one[2]].y,but_one[but_one[2]].x = int(HEIGHT * 2.5/3), int(WIDTH * 0.5)
        but_two[but_two[2]].y,but_two[but_two[2]].x = int(HEIGHT * 1.75/3), int(WIDTH * 0.5)
        but_three[but_three[2]].y,but_three[but_three[2]].x = int(HEIGHT * 1/3), int(WIDTH * 0.5)
    if mode == 1:
        print("start")
    if mode == 3:
        quit()
    
def on_mouse_down(pos,button):
    global mode #localboundserror issues
    if mode == 0:
        if button == mouse.LEFT and but_three[but_three[2]].collidepoint(pos):
            but_three[2] = 1
            mode = 1
        if button == mouse.LEFT and but_two[but_two[2]].collidepoint(pos):
            but_two[2] = 1
            mode = 2 
        if button == mouse.LEFT and but_one[but_one[2]].collidepoint(pos):
            but_one[2] = 1
            mode = 3
        
def draw(): 
    screen.clear()
    if mode == 0:screen.fill((255,255,255)) #white
    eval(objects)
    if mode == 0:
        screen.draw.text('test3',(int(WIDTH * 0.5-20),int(HEIGHT * 1/3)), color= (255,255,255))
        screen.draw.text('test2',(int(WIDTH * 0.5-20),int(HEIGHT * 1.75/3)), color= (255,255,255))
        screen.draw.text('test1',(int(WIDTH * 0.5-20),int(HEIGHT * 2.5/3)), color= (255,255,255))
        screen.draw.text('DungonRPGgui',(int(WIDTH * 0.5-70),int(HEIGHT * 0.5/6)), color= (0,0,0))
pgzrun.go()