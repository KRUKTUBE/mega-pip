import pygame as pg
import sys

def main():
    sc = pg.display.set_mode((300, 200))

    y=70
    x=100
    naprx=1
    napry=1
    while 1:
        pg.draw.rect(sc, (0, 0, 0), 
                     (0, 0, 300, 200))
        y = y + 10*napry
        if y >= 200-30:
            napry=-1
        if y <= 0:
            napry=1
        x = x + 10*naprx
        if x >= 300-60:
            naprx=-1
        if x <= 0:
            naprx=1
        pg.draw.rect(sc, (100, 200, 30), 
                     (x, y, 60, 30))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
        
        pg.display.update()
        
        pg.time.delay(100)