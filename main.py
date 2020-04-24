import pygame, sys
from pygame.locals import *
import  random, time
def main():
    pygame.init()
    #設置背景
    screen = pygame.display.set_mode((480, 800))
    #設置背景圖片
    image_bg1 = pygame.image.load('images/bg4.png')
    image_bg2 = pygame.image.load('images/bg3.png')
    #enemy
    image_enemy1 = pygame.image.load('images/enemy1.png')
    image_enemy2 = pygame.image.load('images/enemy2.png')
    #縮小
    image_enemy2 = pygame.transform.scale(image_enemy2, (195//2 , 142//2))
    image_enemy3 = pygame.image.load('images/enemy3.png')
    image_enemy3 = pygame.transform.scale(image_enemy3, (180 // 2, 169 // 2))
    image_enemy4 = pygame.image.load('images/enemy4.png')
    image_enemy4 = pygame.transform.scale(image_enemy4, (156 // 2, 124 // 2))
    #hero
    image_hero = pygame.image.load('images/hero.png')
    image_bullet_hero =  pygame.image.load('images/Mybullet.png')

    screen.blit(image_bg1,(0,0))

    class Bg:
        #產生背景 兩張圖 Y軸遞減營造向上感覺
        def __init__(self):
            self.x1 = 0
            self.x2 = 0
            self.y1 = 0
            self.y2 = -800
            self.image1 = image_bg1
            self.image2 = image_bg2
        def draw(self):
            #畫背景
            screen.blit(self.image1, (self.x1, self.y1))
            screen.blit(self.image2, (self.x2, self.y2))
        def step(self):
            #畫面更新速度
            self.y1 += 0.5
            self.y2 += 0.5
            if self.y1 >= 800:
                self.y1 = -800
            if self.y2 >= 800:
                self.y2 = -800

    class Enemy:
        def __init__(self, image , width , height):
            self.image = image
            self.width = width
            self.height = height
            self.x = int((480-self.width)*random.random())
            #畫布最上方出現
            self.y = -self.height
        def draw(self):
            screen.blit(self.image, (self.x , self.y))
        def step(self):
            self.y += 0.8

    # 產生一堆enemy
    list_enemies = []
    def makeEnemies():
        global lastTime
        now = time.time()
        if now - lastTime >= 1:
            n = random.randint(1, 5)
            if n == 1:
                list_enemies.append(Enemy(image_enemy1, 101, 78))
            if n == 2:
                list_enemies.append(Enemy(image_enemy2, 195//2, 142//2))
            if n == 3:
                list_enemies.append(Enemy(image_enemy3, 180//2, 169//2))
            if n == 4:
                list_enemies.append(Enemy(image_enemy4, 156//2, 124//2))
            lastTime = now

    list_bullet = []
    def draw_Component():
        for enemy in list_enemies:
            enemy.draw()
            enemy.step()
        for bullet in list_bullet:
            bullet.draw()
            bullet.step()

    def deleteCanvaousComponent():
        for enemy in list_enemies:
            if enemy.y >= 800:
                list_enemies.remove(enemy)
        for bullet in list_bullet:
            if bullet.y < -bullet.height:
                list_bullet.remove(bullet)
    class Hero:
        def __init__(self):
            self.x = 200
            self.y = 700
            self.width = 81
            self.height = 86
            self.image = image_hero
        def draw(self):
            screen.blit(self.image,(self.x, self.y))

    class Bullet:
        def __init__(self):
            self.height = 55
            self.width = 31
            self.x = hero.x + hero.width/2 - self.width/2
            self.y = hero.y - self.height/2

            self.image = image_bullet_hero
        def draw(self):
            screen.blit(self.image, (self.x, self.y))
        def step(self):
            self.y -= 3

    def heroBullet():
        global herobulletTime
        now = time.time()
        if now - herobulletTime > 0.3:
            list_bullet.append(Bullet())
            herobulletTime = now
    def running():
        bg.draw()
        bg.step()
        makeEnemies()
        heroBullet()
        draw_Component()
        deleteCanvaousComponent()
        hero.draw()
        print(len(list_bullet))
    bg = Bg()
    hero = Hero()
    while True:
        running()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                hero.x = event.pos[0] - hero.width /2
                hero.y = event.pos[1] - hero.height /2
        pygame.display.update()


if __name__ == '__main__':
    lastTime = 0
    herobulletTime = 0
    main()
