import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1200, 600


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))  # 練習1　
    bb_img.set_colorkey((0, 0, 0))  #練習2
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_rct = bb_img.get_rect()  # 練習2
    bb_rct.centerx = random.randint(0, WIDTH)  # 練習2
    bb_rct.centery = random.randint(0, HEIGHT)  # 練習2
    
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bb_img, bb_rct)  # 練習2
        pg.display.update()
        tmr += 1
        clock.tick(10)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()