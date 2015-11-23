import pygame
import random
import constant
import game_items

class Enemy(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.screen = self.game.screen
		# hinh, toa do xuat hien, mau
		self.image = pygame.image.load(constant.ENEMY_IMAGE)
		self.rect = self.image.get_rect()
		
		self.hp = constant.ENEMY_HP # co 5 giot mau 

		# move cua moi~ enemy la ngau nhien
		self.x = random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX)
		self.y = random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX)

		# thoi gian ban' ra cung ngau nhien
		self.shootcounter = random.randint(constant.ENEMY_MIN_BULLET_SPEED, constant.ENEMY_MAX_BULLET_SPEED)

		# sprite group dan. cua? dich
		self.bullets_sprite_list = pygame.sprite.Group()

		self.directions = ('n', 'e', 's', 'w')

		self.facing = self.directions[random.randint(0, 3)]
		self.random_position()

	def random_position(self):
		self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
		self.rect.y = random.randint(0, self.screen.get_height() - self.rect.height)

	def set_state(self, x_pos, y_pos, x, y, time, die):
		self.rect.x = x_pos
		self.rect.y = y_pos
		self.x = x
		self.y = y
		self.shootcounter = time
		self.facing = die
	# check enemy ko duoc vuot qua man hinh 
	# tu dong di chuyen enemy, doi huong' khi va cham 
	# tu. dong ban' dan.
	def update(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.move()
		self.shootcounter -= 1
		if self.shootcounter == 0:
			# neu het thoi gian thi enemy duoc phep ban' , ban ngau nhien 1 trong 8 huong 
			self.shoot(self.facing)
			self.shootcounter = random.randint(constant.ENEMY_MIN_BULLET_SPEED, constant.ENEMY_MAX_BULLET_SPEED)

	def boundaries(self):
		"""
		Ensures that when this sprite hits the edge of the screen, it bounces off again and stays in the game.
		"""
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= (self.screen.get_width() - self.rect.width):
			self.rect.x = self.screen.get_width() - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (self.screen.get_height() - self.rect.height):
			self.rect.y = self.screen.get_height() - self.rect.height

	def move(self):
		"""
		Moves the sprite on its generated path & direction.
		"""
		# tu dong di chuyen
		#self.rect.y += self.y
		#self.rect.x += self.x
		self.rect.y += self.y
		self.rect.x += self.x

		if self.rect.x <= 0:
			self.rect.x = 0
			self.x = -self.x
		elif self.rect.x >= (self.screen.get_width() - self.rect.width):
			self.rect.x = self.screen.get_width() - self.rect.width
			self.x = -self.x
		elif self.rect.y <= 0:
			self.rect.y = 0
			self.y = -self.y
		elif self.rect.y >= (self.screen.get_height() - self.rect.height):
			self.rect.y = self.screen.get_height() - self.rect.height
			self.y = -self.y

	def shoot(self, direction):
		"""
		Shoots a bullet in a random direction.
		"""
		self.facing = direction
		bullet = game_items.Bullet(self)
		self.bullets_sprite_list.add(bullet)
		self.game.all_sprite_list.add(bullet)

	def get_name(self):
		return "enemy"

class Snake(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.screen = self.game.screen

		# load hinh
		self.image_snake = []
		for i in range(5):
			self.image_snake.append(pygame.image.load("./image/enemy/snakes/appear-disappear/app" + str(i) + ".png"))

		for i in range(4):
			self.image_snake.append(pygame.image.load("./image/enemy/snakes/attack/hit" + str(i) + ".png"))

		for i in range(6):
			self.image_snake.append(pygame.image.load("./image/enemy/snakes/idle/idle" + str(i) + ".png"))

		self.image = self.image_snake[0]
		self.rect = self.image.get_rect()
		
		self.rect.x = random.randint(0, constant.SCREEN_WIDTH - self.rect.width)	
		self.rect.y = random.randint(0, constant.SCREEN_HEIGHT - self.rect.height)	

		# thoi gian giua 2 frame
		self.count = 0
		self.choose_state = 0 # chon. trang thai cua con ran

	def update(self):
		if self.count == 5:
			self.choose_state += 1
			self.count = 0
		if self.choose_state >= 15:
			self.kill()
		else:
			self.image = self.image_snake[self.choose_state]
		self.count += 1

	def set_state(self, x, y):
		self.rect.x = x 
		self.rect.y = y

class Boss(pygame.sprite.Sprite):
	def __init__(self, one_player):
		pygame.sprite.Sprite.__init__(self)
		self.one_player = one_player
		self.screen = self.one_player.game.screen_boss

		# load hinh boss
		self.image_boss = []
		for i in range(15): # xuat hien
			self.image_boss.append(pygame.image.load("./image/BOSS/appear/appear" + str(i) + ".png"))
		for i in range(6): # di
			self.image_boss.append(pygame.image.load("./image/BOSS/walk/walk" + str(i) + ".png"))
		for i in range(6): # tan cong
			self.image_boss.append(pygame.image.load("./image/BOSS/attack/hit" + str(i) + ".png"))
		for i in range(6):
			self.image_boss.append(pygame.image.load("./image/BOSS/attack/hit" + str(i) + ".png"))
		for i in range(6): # di
			self.image_boss.append(pygame.image.load("./image/BOSS/walk/walk" + str(i) + ".png"))
		for i in range(6): # tan cong
			self.image_boss.append(pygame.image.load("./image/BOSS/attack/hit" + str(i) + ".png"))
		for i in range(6):
			self.image_boss.append(pygame.image.load("./image/BOSS/attack/hit" + str(i) + ".png"))
		for i in range(15): # thay doi vi tri
			self.image_boss.append(pygame.image.load("./image/BOSS/appear/appear" + str(14 - i) + ".png"))

		#self.image_boss.append(self.image_appear)
		#self.image_boss.append(self.image_walk)
		#self.image_boss.append(self.image_attack)
		#self.image_boss.append(self.image_dis)

		self.image = self.image_boss[0]
		self.rect = self.image.get_rect()

		# vi. tri' luc' dau cua? boss la co' dinh tai. diem? giua~ man` hinh` 
		self.rect.x = int(constant.SCREEN_WIDTH_BOSS / 2)
		self.rect.y = int(constant.SCREEN_HEIGHT_BOSS / 2)

		# thoi gian giua 2 frame
		self.count = 0
		self.choose_state = 0 # chon. trang thai cua boss

		# 2 thong so xac dinh huong' di cua boss, huong cung~ co' dinh. luc dau` 
		self.x = 1
		self.y = 1

		# cac huong bay cua dan
		self.direction_bullet = []
		self.direction_bullet.append((-1, -1))
		self.direction_bullet.append((0, -1))
		self.direction_bullet.append((1, -1))
		self.direction_bullet.append((1, 0))

		self.direction_bullet.append((1, 1))
		self.direction_bullet.append((0, 1))
		self.direction_bullet.append((-1, 1))
		self.direction_bullet.append((-1, 0))

		# chi ban 1 lan khi attack 
		self.can_shoot = True

		# 4 bien' tam.
		self.x_pos = 0
		self.y_pos = 0
		self.die_x = 0
		self.die_y = 0

		self.first = True

		self.hp = 20 #mau cua boss la` 20 

	# set lai HP cho boss dua. vao server
	def set_HP(self, hp):
		self.hp = hp

	def update_boss(self):
		if self.count == 5:
			self.choose_state += 1
			self.count = 0
		# attack
		if self.choose_state >= 15 and self.choose_state <= 20 :
			self.rect.x += 10 * self.x
			self.rect.y += 10 * self.y
			self.boundaries() # check vi tri cua boss co vuot ngoai man hinh ko
			if self.can_shoot:
				self.can_shoot = False
				self.shoot() # ban 8 vien dan 
		elif self.choose_state >= 21 and self.choose_state <= 32:
			self.can_shoot = True
		elif self.choose_state >= 33 and self.choose_state <= 38:
			self.rect.x += 10 * self.x
			self.rect.y += 10 * self.y
			self.boundaries() # check vi tri cua boss co vuot ngoai man hinh ko
			if self.can_shoot:
				self.can_shoot = False
				self.shoot() # ban 8 vien dan 
		elif self.choose_state >= 39 and self.choose_state <= 65:
			self.can_shoot = True
		elif self.choose_state >= 66:
			self.rect.x = random.randint(0, constant.SCREEN_WIDTH_BOSS - self.rect.width)
			self.rect.y = random.randint(0, constant.SCREEN_HEIGHT_BOSS - self.rect.height)
			self.choose_state = 0
			self.image = self.image_boss[self.choose_state]
			self.x = random.choice([1, -1])
			self.y = random.choice([1, -1])

		self.image = self.image_boss[self.choose_state]
		self.count += 1

	# update boss khi choi 2 nguoi 
	def update_boss_2(self):
		if self.choose_state == 0 and self.first:
			# luc nay` send cho server biet' de? no' xac dinh. lai. vi. tri' xuat' hien va` huong' cua nhan vat
			self.one_player.game.Send({"action" : "Boss", "id" : self.one_player.game.index_player})
			self.first = False 
		if self.count == 5:
			self.choose_state += 1
			self.count = 0
		# attack
		if self.choose_state >= 15 and self.choose_state <= 20 :
			self.first = True
			self.rect.x += 10 * self.x
			self.rect.y += 10 * self.y
			self.boundaries() # check vi tri cua boss co vuot ngoai man hinh ko
			if self.can_shoot:
				self.can_shoot = False
				self.shoot() # ban 8 vien dan 
		elif self.choose_state >= 21 and self.choose_state <= 32:
			self.can_shoot = True
		elif self.choose_state >= 33 and self.choose_state <= 38:
			self.rect.x += 10 * self.x
			self.rect.y += 10 * self.y
			self.boundaries() # check vi tri cua boss co vuot ngoai man hinh ko
			if self.can_shoot:
				self.can_shoot = False
				self.shoot() # ban 8 vien dan 
		elif self.choose_state >= 39 and self.choose_state <= 65:
			self.can_shoot = True
		elif self.choose_state >= 66:
			self.rect.x = self.x_pos 
			self.rect.y = self.y_pos
			self.x = self.die_x
			self.y = self.die_y

			self.choose_state = 0
			self.image = self.image_boss[self.choose_state]

		self.image = self.image_boss[self.choose_state]
		self.count += 1

	def set_state(self, x, y, die_x, die_y):
		self.x_pos = x 
		self.y_pos = y 
		self.die_x = die_x
		self.die_y = die_y

	def boundaries(self):
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= (constant.SCREEN_WIDTH_BOSS - self.rect.width):
			self.rect.x = constant.SCREEN_WIDTH_BOSS - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (constant.SCREEN_HEIGHT_BOSS - self.rect.height):
			self.rect.y = constant.SCREEN_HEIGHT_BOSS - self.rect.height

	def shoot(self):
		# make 8 bullet 
		for i in range(8):
			bullet = game_items.BulletBoss(self, self.direction_bullet[i])
			self.one_player.all_sprite_list_boss.add(bullet)
			self.one_player.bullet_sprite_list_boss.add(bullet)

	







