import sys
import random
import pygame as pg

WIDTH, HEIGHT = 1250, 650

delta = {  # 練習3
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}

def check_bound(rct: pg.Rect) -> tuple[bool, bool]:  # 練習4
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを消す関数
    引数 rct:　こうかとんor爆弾SurfaceのRect
    戻り値:横方向、縦方向判定結果 (画面内：True/画面外：False)
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate 

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_over = pg.image.load("ex02/fig/4.png")
    kk_img_over = pg.transform.rotozoom(kk_img_over, 0, 2.0)
    kk_rct = kk_img.get_rect()  #練習3
    kk_rct.center = 900, 400  #練習3
    bb_img = pg.Surface((20, 20))  # 練習1　
    bb_img.set_colorkey((0, 0, 0))  #練習1
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_rct = bb_img.get_rect()  # 練習1
    bb_rct.centerx = random.randint(0, WIDTH)  # 練習1
    bb_rct.centery = random.randint(0, HEIGHT)  # 練習1
    vx, vy = +5, +5  # 練習2
    kk_img_1 = pg.transform.flip(kk_img, True, False)
    delta_1 = {
        (0,-5):pg.transform.rotozoom(kk_img_1, 90, 1.0),
        (+5,-5):pg.transform.rotozoom(kk_img_1, 45, 1.0),
        (+5,0):pg.transform.rotozoom(kk_img_1, 0, 1.0),
        (+5,+5):pg.transform.rotozoom(kk_img_1, -45, 1.0),
        (0,+5):pg.transform.rotozoom(kk_img_1, -90, 1.0),
        (-5,+5):pg.transform.rotozoom(kk_img, 45, 1.0),
        (-5,0):pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5,-5):pg.transform.rotozoom(kk_img, -45, 1.0)
    }
    accs = [a for a in range(1,11)]
    
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rct.colliderect(bb_rct):  # 追加3:着弾するとこうかとん画像が切り替わる
            screen.blit(bg_img, [0, 0])
            screen.blit(kk_img_over, kk_rct)
            pg.display.update()
            clock.tick(5)
            print("Game Over")
            return
             
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 練習3: 合計移動量
        for k, tpl in delta.items():
            if key_lst[k]:  # 練習3キーが押されたら
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        
        x, y = sum_mv[0], sum_mv[1]
        if event.type == pg.KEYDOWN:
            kk_img = delta_1[(x, y)]
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])  # 練習3
        if check_bound(kk_rct) != (True, True):  # 練習4
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])  
        screen.blit(kk_img, kk_rct)  #練習3
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        bb_rct.move_ip(avx, avy)  # 練習2
        yoko, tate = check_bound(bb_rct)
        if not yoko:  # 練習4
            vx *= -1
        if not tate:  # 練習4
            vy *= -1
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        bb_rct.move_ip(avx, avy)  # 練習4
        screen.blit(bb_img, bb_rct)  # 練習1
        pg.display.update()
        tmr += 1
        clock.tick(50)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()