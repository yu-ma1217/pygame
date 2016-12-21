#着想ピンポンを参考にする
#http://gamepro.blog.jp/python/pygame/pong
#http://aidiary.hatenablog.com/entry/20080509/1275698879

import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (400,400)
    #//で割ると切り捨てる /で小数点まで
    (x,y) = (w//2, h//2)
    pygame.init()
    pygame.display.set_mode((w,h),0,32)
    screen = pygame.display.get_surface()
    #画像をオブジェクトに変換
    img = pygame.image.load("snowman.png").convert_alpha()
    rect = img.get_rect()
    rect.center = (w//2, h//2)

    while(1):
        #中心線
        pygame.draw.line(screen, (0,95,0),(0,200),(400,200),5)

        #for文で無限のように感じるメモリを作成
        #for i in オブジェクト
        for i in range(-4000, 4000, 15):
            #メモリの描写
            pygame.draw.line(screen, (0, 200, 0), (x+i, y+30),(x+i,y-30), 1)

        #長押し処理
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            x += 2
        if pressed_key[K_RIGHT]:
            x -= 2
        #跳ね返り処理
        if rect.right < 0:
            rect.left = 400
        if rect.left > 400:
            rect.right = 0

        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,20,0,0))
        screen.blit(img, rect) #画像の描画

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #キーを押したとき
            if event.type == KEYDOWN:
                #ESCキーで終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
