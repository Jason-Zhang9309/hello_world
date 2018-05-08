import pygame #导入所需的包
import time
from pygame.locals import *
import random

#创建基类
class Base(object):
	def __init__(self, screen_temp,x,y,image_name):
		self.x = x
		self.y = y
		self.screen = screen_temp
		self.image = pygame.image.load(image_name)

class BasePlane(Base):
	
	def __init__(self, screen_temp,x,y,image_name):
		Base.__init__(self,screen_temp,x,y,image_name)
		self.bullet_list = []
	
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
			if bullet.judge():
				self.bullet_list.remove(bullet)
		
		

class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,500,"./feiji/hero1.png")
        self.hit = False #表示是否要爆炸
        self.bomb_list = [] #用来存储爆炸时需要的图片
        self.__crate_images() #调用这个方法向bomb_list中添加图片
        self.image_num = 0#用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0#用来记录当前要显示的爆炸效果的图片的序号

    def __crate_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

    def display(self):
        """显示玩家的飞机"""
        #如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num+=1
            if self.image_num == 7:
                self.image_num=0
                self.image_index+=1
            if self.image_index>3:
                time.sleep(1)
                exit()#调用exit让游戏退出
                #self.image_index = 0
        else:
            self.screen.blit(self.image,(self.x, self.y))

        for bullet in self.bullet_list:
        	bullet.display()
        	bullet.move()
        	if bullet.judge():
        		self.bullet_list.remove(bullet)


    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
    	self.bullet_list.append(Bullet(self.screen,self.x,self.y))

    def bomb(self):
        self.hit = True

class Enemyplane(BasePlane):
	def __init__(self, screen_temp):
		BasePlane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
		self.direction = "right"

	def move(self):
		if self.direction=="right":
			self.x += 5
		elif self.direction=="left":
			self.x -= 5

		if self.x>480-50:
			self.direction = "left"
		elif self.x<0:
			self.direction = "right"

	def fire(self):
		random_num = random.randint(1,100)
		print(random_num)
		if random_num == 8 or random_num == 20:
				self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


class BaseBullet(Base):
	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		

class Bullet(BaseBullet):
	def __init__(self, screen_temp,x,y):
		BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")

	def move(self):
		self.y -= 20

	def judge(self):
		if self.y<0:
			return True
		else:
			return False

class EnemyBullet(BaseBullet):
	def __init__(self,screen_temp,x,y):	
		BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")
	
	def move(self):
		self.y+=5

	def judge(self):
		if self.y>852:
			return True
		else:
			return False

def key_control(hero_temp):
	 for event in pygame.event.get():

            if event.type == QUIT:
                print("exit")
                exit()
            
            elif event.type == KEYDOWN:
                
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    hero_temp.move_left()
                
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero_temp.move_right()
               
                elif event.key == K_SPACE:
                    print('space')
                    hero_temp.fire()
                elif event.key == K_b:
                	print('b')
                	hero_temp.bomb()
def main():
   
    screen = pygame.display.set_mode((480,652),0,32)
   
    background = pygame.image.load("./feiji/background.png")
    
    hero = HeroPlane(screen)
   	
    enemy = Enemyplane(screen)

    while True :
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
       
        pygame.display.update()
        key_control(hero)
        time.sleep(0.05) 
if __name__ == "__main__":
	
	main()
