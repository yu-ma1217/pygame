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
        #長押し処理
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            rect.move_ip(-10,0)
        if pressed_key[K_RIGHT]:
            rect.move_ip(10,0)

        #跳ね返り処理
        if rect.right < 0:
            rect.left = 400
        if rect.left > 400:
            rect.right =0

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
