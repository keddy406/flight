import pygame, sys
from pygame.locals import *
import  random, time
def main():
    list_explosion = []
    imageexplosion = []
    list_enemies = []
    list_enemy_bullet = []
    list_bullet = []
    list_score = []
    list_ufo =[]
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
    image_bullet_enemy = pygame.image.load('images/enemybullet.png')

    image_start = pygame.image.load('images/Start.png')
    pygame.mixer_music.load('sound/bg.wav')
    pygame.mixer.music.play(-1)
    music_bullet = pygame.mixer.Sound('sound/bulleteffect.wav')
    music_effect1 = pygame.mixer.Sound('sound/effect1.wav')
    music_effect2 = pygame.mixer.Sound('sound/effect2.wav')
    music_effect_explosion = pygame.mixer.Sound('sound/explosion.wav')
    music_effect_gameocver = pygame.mixer.Sound('sound/icebird.wav')
    image_gameover = pygame.image.load('images/gameover.png')
    for i in range(1,6):
        imageexplosion.append(pygame.image.load('images/explosion0' + str(i) + '.png'))

    for i in range(10):
        list_score.append(pygame.transform.scale(pygame.image.load('images/' + str(i) + '.png'),(35 // 2 , 44 // 2)))
    image_scoretitle = pygame.image.load('images/scoretitle.png')

    image_hp_hero_1 = pygame.transform.scale(pygame.image.load('images/heroHP1.png'), (204 // 2, 11 // 2))
    image_hp_hero_2 = pygame.transform.scale(pygame.image.load('images/heroHP2.png'), (289 // 2, 52 //2))
    image_heart_hero =pygame.transform.scale(pygame.image.load('images/life.png'), (20, 20))

    image_hp_plus_1 = pygame.image.load('images/hp_plus1.png')
    image_hp_plus_2 = pygame.image.load('images/hp_plus2.png')
    image_ulitimate_1 = pygame.image.load('images/ulitimate1.png')
    image_ulitimate_2 = pygame.image.load('images/ulitimate2.png')

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
            self.candelete = False
        def draw(self):
            screen.blit(self.image, (self.x , self.y))
        def step(self):
            self.y += 0.8
        def shoot(self):
            list_enemy_bullet.append(Enemybullet(self.x, self.y, self.width, self.height))

    class Hero:
        def __init__(self):
            self.x = 200
            self.y = 700
            self.width = 81
            self.height = 86
            self.image = image_hero
        def draw(self):
            screen.blit(self.image,(self.x, self.y))
    hero = Hero()

    class Bullet:
        def __init__(self, type = 0):
            self.height = 55
            self.width = 31
            self.x = hero.x + hero.width/2 - self.width/2
            self.y = hero.y - self.height/2
            self.image = image_bullet_hero
            self.type = type
            self.candelete = False
        def draw(self):
            screen.blit(self.image, (self.x, self.y))
        def step(self):
            self.y -= 5
            if self.type == 0:
                pass
            elif self.type == 1:
                self.x -= 2
            elif self.type == 2:
                self.x -= 4
            elif self.type == 3:
                self.x += 4
            elif self.type == 4:
                self.x += 2

    class Enemybullet:
        def __init__(self, enemyX, enemyY, enemyWidth, enemyHeight):
            self.x = enemyX + enemyWidth / 2
            self.y = enemyY + enemyHeight / 2
            self.image = image_bullet_enemy
            self.width = 10
            self.height = 10
        def draw(self):
            screen.blit(self.image, (self.x, self.y))

        def step(self):
            self.y += 2


    class Explosion:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.images = imageexplosion
            self.delete = False
            self.n = 0
            self.lastExplosion = 0
        def draw(self):
            now = time.time()
            if self.n < len(self.images):
                screen.blit(self.images[self.n], (self.x, self.y))
                if now - self.lastExplosion > 0.2:
                    self.n += 1
                    self.lastExplosion = now
            else:
                self.delete = True

    class Ufo:
        #產生功能
        def __init__(self, type, image1, image2, width, height):
            self.type = type
            self.image1 = image1
            self.image2 = image2
            self.width = width
            self.height = height
            self.x = (480 - self.width) *random.random()
            self.y = -self.height
            self.ishit = False
            self.deleted = False
            self.time = 0
        def draw(self):
            if not self.ishit:
                screen.blit(self.image1, (self.x, self.y))
                self.time = time.time()
            else :
                if time.time() - self.time > 0.5:
                    self.deleted = True
                screen.blit(self.image2, (self.x, self.y))
        def step(self):
            self.y += 2


    def heroBullet():
        global lastTimeMakeBullet,makeSdBullet,makeSdBulletTime
        now = time.time()
        if makeSdBullet:
            # 英雄發射散弹
            now = time.time()
            if now-makeSdBulletTime>=5:
                makeSdBullet=False
            if now - lastTimeMakeBullet >= 0.2:
                music_bullet.play(0)
                for type in range(5):
                    list_bullet.append(Bullet(type))
                lastTimeMakeBullet = now
        else:
            # 英雄机普通子弹
            now = time.time()
            makeSdBulletTime=now
            if now - lastTimeMakeBullet >= 0.3:
                music_bullet.play(0)
                list_bullet.append(Bullet(0))
                lastTimeMakeBullet = now




    # 產生一堆enemy
    def makeEnemies():
        global lastTime
        now = time.time()
        if now - lastTime >= 0.5:
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

    def makeUfo():
        global lastTimeMakeUFO
        now = time.time()
        if now-lastTimeMakeUFO > 10:
        #隨機添加1 or 2
            if random.random() < 0.5:
                list_ufo.append(Ufo(1, image_hp_plus_1, image_hp_plus_2, 54, 54))
            else :
                list_ufo.append(Ufo(2, image_ulitimate_1, image_ulitimate_2, 138, 162))
            lastTimeMakeUFO = now

    def makeEnemyBullet():
        global LastTimeMakeEnemyBullet
        if time.time() - LastTimeMakeEnemyBullet >= 0.2 :
            if len(list_enemies) >= 1:
                for n in range (random.randint(0, len(list_enemies)-1)):
                    list_enemies[n].shoot()
                LastTimeMakeEnemyBullet = time.time()

    def draw_Component():
        for enemy in list_enemies:
            enemy.draw()
        for bullet in list_bullet:
            bullet.draw()
        for exolosion in list_explosion:
            exolosion.draw()
        for enemybullet in list_enemy_bullet:
            enemybullet.draw()
        for u in list_ufo:
            u.draw()

    def step_Component():
        for enemy in list_enemies:
            enemy.step()
        for bullet in list_bullet:
            bullet.step()
        for enemybullet in list_enemy_bullet:
            enemybullet.step()
        for u in list_ufo:
            u.step()

    def deleteComponent():
        for enemy in list_enemies:
            if enemy.y >= 800 or enemy.candelete:
                list_enemies.remove(enemy)
        for bullet in list_bullet:
            if bullet.y < -bullet.height or bullet.candelete:
                list_bullet.remove(bullet)
        for explosion in list_explosion:
            if explosion.delete:
                list_explosion.remove(explosion)
        for u in list_ufo:
            if u.y >= 800:
                list_ufo.remove(u)
            if u.deleted:
                list_ufo.remove(u)

    def checkHit():
        global killNumber, heroHP,makeSdBullet ,gameStatus
        for enemy in list_enemies:
            for bullet in list_bullet:
                if bullet.x > enemy.x - bullet.width:
                    if bullet.x < enemy.x + enemy.width:
                        if bullet.y > enemy.y - bullet.height:
                            if bullet.y < enemy.y + enemy.height:
                                bullet.candelete = True
                                enemy.candelete = True
                                list_explosion.append(Explosion(enemy.x, enemy.y))
                                music_effect_explosion.play(0)
                                killNumber += 1
        #hero hit bullet
        for bullet in list_enemy_bullet:
            if bullet.x > hero.x - bullet.width :
                if bullet.x < hero.x + hero.width:
                    if bullet.y > hero.y - bullet.height:
                        if bullet.y < hero.y + hero.height:
                            list_enemy_bullet.remove(bullet)
                            heroHP -= 15
                            if heroHP < 20:
                                list_explosion.append(Explosion(hero.x, hero.y))
                                gameStatus = 'gameover'
                                pygame.mixer.music.stop()
                                music_effect_gameocver.play(0)

        #hero hit ufo
        for u in list_ufo:
            if u.x > hero.x - u.width:
                if u.x < hero.x + hero.width:
                    if u.y > hero.y - u.width:
                        if u.y < hero.y + hero.height:
                            if not u.ishit :
                                u.ishit = True
                                if u.type == 1 :
                                    music_effect1.play(0)
                                    if heroHP < 127:
                                        heroHP += 15
                                if u.type == 2 :
                                    music_effect2.play(0)
                                    makeSdBullet = True


    def score():
        global killNumber
        screen.blit(image_scoretitle,[0,0])
        x = 80
        for n in str(killNumber):
            screen.blit(list_score[int(n)], (x, 5))
            x += 20

    def heroLife():
        global heroHP
        #紅色HP右邊開始減少製造HP減少
        screen.blit(image_hp_hero_1,[480 - heroHP, 14])
        screen.blit(image_hp_hero_2,[480 - 289 //2, 0])
        screen.blit(image_heart_hero,[480 - 44 // 2 ,3])

    def gamestatus():
        global gameStatus
        if gameStatus =='start':
            start()
        if gameStatus =='pause':
            pause()
        if gameStatus =='gameover':
            gameover()
        if gameStatus =='running':
            running()
#遊戲狀態
    #1點圖片開始   start
    #2滑鼠離開螢幕暫停 pause
    #3gameover
    #4滑鼠在螢幕裡 running

    def start():
        bg.draw()
        screen.blit(image_start,(100, 200))
        hero.draw()
    def pause():
        bg.draw()
        draw_Component()
        score()
        heroLife()
        hero.draw()
    def gameover():
        bg.draw()
        bg.step()
        makeEnemies()
        draw_Component()
        step_Component()
        deleteComponent()
        score()
        heroLife()
        screen.blit(image_gameover, [150, 400])
    def running():
        bg.draw()
        bg.step()
        makeEnemies()
        heroBullet()
        step_Component()
        draw_Component()
        deleteComponent()
        makeEnemyBullet()
        checkHit()
        score()
        heroLife()

        hero.draw()
        makeUfo()
        # print(len(list_bullet))


    bg = Bg()
    hero = Hero()
    while True:
        global gameStatus
        gamestatus()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                if gameStatus =='running':
                    hero.x = event.pos[0] - hero.width /2
                    hero.y = event.pos[1] - hero.height /2
                if event.pos[0] >= 479 or event.pos[0] <= 1 or event.pos[1] >= 799 or event.pos[1] <= 1 :
                    if gameStatus == 'running':
                        gameStatus = 'pause'
                        pygame.mixer.music.pause()
                else:
                    if gameStatus == 'pause':
                        gameStatus = 'running'
                        pygame.mixer.music.unpause()
            if event.type == MOUSEBUTTONDOWN:
                if gameStatus =='start':
                    gameStatus = 'running'


        pygame.display.update()


if __name__ == '__main__':
    gameStatus = 'start'
    killNumber = 0
    lastTime = 0
    lastTimeMakeUFO = time.time()
    LastTimeMakeEnemyBullet= 0
    heroHP = 127
    lastTimeMakeBullet = 0
    makeSdBullet = False
    makeSdBulletTime = 0
    main()
