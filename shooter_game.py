#Создай собственный Шутер!

from pygame import *
from random import*
font.init()
window =  display.set_mode((700,500))
display.set_caption("шутер")
background = transform.scale(image.load('galaxy.jpg'),(700,500))

sprite1 = transform.scale(image.load('l.png'),(100,100))

win_height = 500
win_width = 700

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,20)
        bullets.add(bullet)

        





font.init()
font1 = font.SysFont('Arial', 36)


lost = 0 #пропущено кораблей
class Enemy(GameSprite):
    def update(self):
        if self.rect.y <=500:
            self.direction = "down"
        if self.direction == "down":
            self.rect.y += self.speed


        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

#text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


    
    

    
    

    



bul1 = Bullet('bullet.png',100,100,8)
bullets = sprite.Group()

h = Player("rocket.png",299,435,5)
ufo1 = Enemy("5.png",randint(0,675), 0, 1)
ufo2 = Enemy("ufo.png",randint(0,675), 0, 1)
ufo3 = Enemy("ufo.png",randint(0,675), 0, 1)
ufo4 = Enemy("ufo.png",randint(0,675), 0, 1)
ufo5 = Enemy("ufo.png",randint(0,675), 0, 1)
ufo6 = Enemy("ufo.png",randint(0,675), 0, 1)
ufo7 = Enemy("ufo.png",randint(0,675), 0, 1)

monsters = sprite.Group()
monsters.add(ufo1)
monsters.add(ufo2)
monsters.add(ufo3)
monsters.add(ufo4)
monsters.add(ufo5)
monsters.add(ufo6)
monsters.add(ufo7)

monsters.draw(window)
#monsters.update()


score = 0

clock = time.Clock()
FPS = 1260

global number 
namber = 0

game = True
Finish = False
font = font.SysFont('Arial',50)
win = font.render('YOU WIN',True,(255,215,0))
los = font.render('YOU LOSE',True,(255,0,0))
'''text_lose = font1.render(
    "Пропущено: " + str(lost), 1, (255, 255, 255)
    )'''
#t_score = font.render("счед: " + str(score), 1, (255, 255, 255))

while game:
    window.blit(background,(0,0))


    mixer.init()
    mixer.music.load('space.ogg')
    mixer.music.play()


    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                h.fire()

    if Finish != True:
        
        sprite_list = sprite.groupcollide(monsters,bullets,True,True)

        for s in sprite_list:
            score = score + 1 
                
            ufo8 = Enemy("ufo.png",randint(0,675), 0, 1)
            monsters.add(ufo8)
        text_lose = font1.render(
            "Пропущено: " + str(lost), 1, (255, 255, 255)
            )
        t_score = font.render("с4еt: " + str(score), 1, (255, 255, 255))
        if lost >= 20 or sprite.spritecollide(h,monsters,False):
            window.blit(los,(250,250))
            Finish = True
        if score >= 30:
            window.blit(win,(250,250))
            Finish = True
        
        
        
        window.blit(text_lose,(0,0))
        window.blit(t_score,(0,40))


        bullets.update()
        bullets.draw(window)

        #bul1.reset()
        h.reset()
        #monsters.reset()
        '''ufo1.reset()
        ufo2.reset()
        ufo3.reset()
        ufo4.reset()
        ufo5.reset()
        ufo6.reset()
        ufo7.reset()'''

        monsters.draw(window)



        #bul1.update()
        h.update()
        monsters.update()
        '''ufo1.update()
        ufo2.update()
        ufo3.update()
        ufo4.update()
        ufo5.update()
        ufo6.update()
        ufo7.update()'''







        '''if sprite.collide_rect(hero,final):
                finish = True'''
    
        



        clock.tick(FPS)
        display.update()