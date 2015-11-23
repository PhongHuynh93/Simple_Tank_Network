import pygame
import random
import constant

class Bullet(pygame.sprite.Sprite):
	def __init__(self, tank):
		pygame.sprite.Sprite.__init__(self)
		self.tank = tank
		self.screen = tank.screen
		if self.tank.get_name() == "tank_player":
			if self.tank.one_player.game.index_player == 0:
				self.image = pygame.image.load(constant.BULLET_PLAYER)
			else:
				self.image = pygame.image.load(constant.BULLET_PLAYER_2)
		if self.tank.get_name() == "enemy":
			self.image = pygame.image.load(constant.ENEMY_BULLET)

		self.facing = "n"
		# vi tri vien dan
		self.rect = self.image.get_rect()
		self.rect.centerx = tank.rect.centerx
		self.rect.centery = tank.rect.centery

		self.x = 0 # bien' chi? toc do cung nhu huong di chuyen cua vien dan 
		self.y = 0
		self.die = tank.facing
		self.flight_path()
		self.set_position()
 
	def set_state(self, x, y, face, id):
		if self.tank.get_name() == "tank_player":
			if id == 0:
				self.image = pygame.image.load(constant.BULLET_PLAYER)
			else:
				self.image = pygame.image.load(constant.BULLET_PLAYER_2)
		if self.tank.get_name() == "enemy":
			self.image = pygame.image.load(constant.ENEMY_BULLET)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.die = face

		self.flight_path()
		self.set_position()



	def flight_path(self):
		if self.die == "n":
			self.x = 0
			self.y = -constant.BULLET_SPEED
		if self.die == "s":
			self.x = 0
			self.y = constant.BULLET_SPEED
		if self.die == "w":
			self.x = -constant.BULLET_SPEED
			self.y = 0
		if self.die == "e":
			self.x = constant.BULLET_SPEED
			self.y = 0

	def set_position(self):
		"""
		Sets the position of the bullet relative to the tank sprite which fired it.
		"""
		if self.die == "n":
			self.rect.centery += - int(self.tank.rect.height / 2 + 10)

		elif self.die == "e":
			self.rect.centerx += int(self.tank.rect.height / 2 + 10)
			self.rect.centery += 7
			self.image = pygame.transform.rotate(self.image, 270)

		elif self.die == "s":
			self.rect.centery += int(self.tank.rect.height / 2 + 10)
			self.image = pygame.transform.rotate(self.image, 180)

		elif self.die == "w":
			self.rect.centerx += -int(self.tank.rect.height / 2 + 20)
			self.rect.centery += 7
			self.image = pygame.transform.rotate(self.image, 90)


	def boundaries(self):
		"""
		Ensures that when this bullet hits a screen boundary, it is immediately destroyed.
		"""
		if(self.rect.x <= 0 or self.rect.x >= (self.screen.get_width()-self.rect.width) or self.rect.y <= 0 or self.rect.y >= (self.screen.get_height()-self.rect.height)):
			self.kill()

	def update(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y
		self.rect.centerx += self.x

	def update_boss(self):
		self.boundaries_boss()
		self.rect.centery += self.y
		self.rect.centerx += self.x

	def boundaries_boss(self):
		"""
		Ensures that when this bullet hits a screen boundary, it is immediately destroyed.
		"""
		if(self.rect.x <= 0 or self.rect.x >= (constant.SCREEN_WIDTH_BOSS-self.rect.width) or self.rect.y <= 0 or self.rect.y >= (constant.SCREEN_HEIGHT_BOSS-self.rect.height)):
			self.kill()

class BulletBoss(pygame.sprite.Sprite):
	def __init__(self, boss, direction):
		pygame.sprite.Sprite.__init__(self)
		self.boss = boss
		self.direction = direction
		self.screen = boss.one_player.game.screen_boss

		self.image = pygame.image.load(constant.BULLET_BOSS)

		# vi tri vien dan
		self.rect = self.image.get_rect()

		# tren trai
		if self.direction[0] == -1 and self.direction[1] == -1:
			self.rect.centerx = self.boss.rect.x
			self.rect.centery = self.boss.rect.y

		#tren giua
		if self.direction[0] == 0 and self.direction[1] == -1:
			self.rect.centerx = self.boss.rect.centerx
			self.rect.centery = self.boss.rect.y
		
		# tren phai
		if self.direction[0] == 1 and self.direction[1] == -1:
			self.rect.centerx = self.boss.rect.x + self.boss.rect.width
			self.rect.centery = self.boss.rect.y
		
		# trai giua
		if self.direction[0] == 1 and self.direction[1] == 0:
			self.rect.centerx = self.boss.rect.x + self.boss.rect.width
			self.rect.centery = self.boss.rect.centery
		
		# trai duoi
		if self.direction[0] == 1 and self.direction[1] == 1:
			self.rect.centerx = self.boss.rect.x + self.boss.rect.width
			self.rect.centery = self.boss.rect.y + self.boss.rect.height
		
		# duoi giua
		if self.direction[0] == 0 and self.direction[1] == 1:
			self.rect.centerx = self.boss.rect.centerx
			self.rect.centery = self.boss.rect.y + self.boss.rect.height
		
		# duoi trai
		if self.direction[0] == -1 and self.direction[1] == 1:
			self.rect.centerx = self.boss.rect.x
			self.rect.centery = self.boss.rect.y + self.boss.rect.height
		
		# giua phai
		if self.direction[0] == -1 and self.direction[1] == 0:
			self.rect.centerx = self.boss.rect.x
			self.rect.centery = self.boss.rect.centery
		
		self.x = self.direction[0] * 10 # bien' chi? toc do cung nhu huong di chuyen cua vien dan 
		self.y = self.direction[1] * 10

		self.x_limit = 0
		self.y_limit = 0


	def boundaries(self):
		"""
		Ensures that when this bullet hits a screen boundary, it is immediately destroyed.
		"""
		if(self.rect.x <= 0 or self.rect.x >= (self.screen.get_width()-self.rect.width) or self.rect.y <= 0 or self.rect.y >= (self.screen.get_height()-self.rect.height)):
			self.kill()

	def update_boss(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y
		self.rect.centerx += self.x

		self.y_limit += self.y
		self.x_limit += self.x

		# khi x, y di duoc 1 doan nao do thi xoa' va goi. tao 3 vien dan 
		if self.x_limit >= 200 or self.y_limit >= 200 or self.x_limit <= -200 or self.y_limit <= -200:
			# tren trai
			if self.direction[0] == -1 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)


			#tren giua
			if self.direction[0] == 0 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			# tren phai
			if self.direction[0] == 1 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# trai giua
			if self.direction[0] == 1 and self.direction[1] == 0:
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# trai duoi
			if self.direction[0] == 1 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# duoi giua
			if self.direction[0] == 0 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# duoi trai
			if self.direction[0] == -1 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# giua phai
			if self.direction[0] == -1 and self.direction[1] == 0:
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			self.kill()


	def update_boss_2(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y
		self.rect.centerx += self.x

		self.y_limit += self.y
		self.x_limit += self.x

		# khi x, y di duoc 1 doan nao do thi xoa' va goi. tao 3 vien dan 
		if self.x_limit >= 200 or self.y_limit >= 200 or self.x_limit <= -200 or self.y_limit <= -200:
			# tren trai
			if self.direction[0] == -1 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)


			#tren giua
			if self.direction[0] == 0 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			# tren phai
			if self.direction[0] == 1 and self.direction[1] == -1:
				smallbullet = SmallBulletBoss(self, (0, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# trai giua
			if self.direction[0] == 1 and self.direction[1] == 0:
				smallbullet = SmallBulletBoss(self, (1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# trai duoi
			if self.direction[0] == 1 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# duoi giua
			if self.direction[0] == 0 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# duoi trai
			if self.direction[0] == -1 and self.direction[1] == 1:
				smallbullet = SmallBulletBoss(self, (0, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			
			# giua phai
			if self.direction[0] == -1 and self.direction[1] == 0:
				smallbullet = SmallBulletBoss(self, (-1, -1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 0))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
				smallbullet = SmallBulletBoss(self, (-1, 1))
				self.boss.one_player.bullet_sprite_list_boss.add(smallbullet)
				self.boss.one_player.all_sprite_list_boss.add(smallbullet)
			self.kill()


class SmallBulletBoss(pygame.sprite.Sprite):
	def __init__(self, bulletBoss, direction):
		pygame.sprite.Sprite.__init__(self)
		self.boss = bulletBoss.boss
		self.direction = direction
		self.screen = self.boss.one_player.game.screen_boss

		self.image = pygame.image.load(constant.BULLET_BOSS_SMALL)

		# vi tri vien dan
		self.rect = self.image.get_rect()
		self.rect.centerx = bulletBoss.rect.centerx
		self.rect.centery = bulletBoss.rect.centery
		
		self.x = self.direction[0] * 15 # bien' chi? toc do cung nhu huong di chuyen cua vien dan 
		self.y = self.direction[1] * 15


	def boundaries(self):
		"""
		Ensures that when this bullet hits a screen boundary, it is immediately destroyed.
		"""
		if(self.rect.x <= 0 or self.rect.x >= (self.screen.get_width()-self.rect.width) or self.rect.y <= 0 or self.rect.y >= (self.screen.get_height()-self.rect.height)):
			self.kill()

	def update_boss(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y
		self.rect.centerx += self.x

	def update_boss_2(self):
		"""
		Allows a game to update this sprite.
		"""
		self.boundaries()
		self.rect.centery += self.y 
		self.rect.centerx += self.x


class Track(pygame.sprite.Sprite):
	def __init__(self, tank):
		pygame.sprite.Sprite.__init__(self)
		self.screen = tank.screen
		self.tank = tank
		self.image_0 = pygame.image.load(constant.TANK_IMAGE_1)
		self.image_1 = pygame.transform.rotate(self.image_0, 90)
		self.image = self.image_0
		self.rect = self.image.get_rect()
		self.rect.x = tank.rect.x
		self.rect.y = tank.rect.y - 10 - self.rect.height

	def update(self):
		if self.tank.facing == "s":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y - 10 - self.rect.height
		if self.tank.facing == "n":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y + 10 + self.tank.rect.height
		if self.tank.facing == "e":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x - 10 - self.rect.width
			self.rect.y = self.tank.rect.y
		if self.tank.facing == "w":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 10 + self.tank.rect.height
			self.rect.y = self.tank.rect.y

	def update_boss(self):
		if self.tank.facing == "s":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y - 10 - self.rect.height
		if self.tank.facing == "n":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y + 10 + self.tank.rect.height
		if self.tank.facing == "e":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x - 10 - self.rect.width
			self.rect.y = self.tank.rect.y
		if self.tank.facing == "w":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 10 + self.tank.rect.height
			self.rect.y = self.tank.rect.y

	def update_boss_2(self):
		if self.tank.facing == "s":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y - 10 - self.rect.height
		if self.tank.facing == "n":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 5
			self.rect.y = self.tank.rect.y + 10 + self.tank.rect.height
		if self.tank.facing == "e":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x - 10 - self.rect.width
			self.rect.y = self.tank.rect.y
		if self.tank.facing == "w":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.x = self.tank.rect.x + 10 + self.tank.rect.height
			self.rect.y = self.tank.rect.y

# cai nong sung 
class Barrel(pygame.sprite.Sprite):
	def __init__(self, tank, otherColor = False):
		pygame.sprite.Sprite.__init__(self)
		self.screen = tank.screen
		self.tank = tank
		self.image_0 = pygame.image.load(constant.TANK_IMAGE_2)
		if not otherColor: 
			if self.tank.one_player.game.index_player == 0: 
				self.image_0 = pygame.image.load(constant.TANK_IMAGE_2)
			elif self.tank.one_player.game.index_player == 1:
				self.image_0 = pygame.image.load(constant.TANK_IMAGE_2_PLAYER_2)
		else:
			if self.tank.one_player.game.index_player == 1: 
				self.image_0 = pygame.image.load(constant.TANK_IMAGE_2)
			elif self.tank.one_player.game.index_player == 0:
				self.image_0 = pygame.image.load(constant.TANK_IMAGE_2_PLAYER_2)
		self.image_1 = pygame.transform.rotate(self.image_0, 90)
		self.image = self.image_0
		self.rect = self.image.get_rect()	
		self.rect.centerx = tank.rect.centerx
		self.rect.centery = tank.rect.centery

	def update(self):
		if self.tank.facing == "s":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.centerx = self.tank.rect.centerx
			self.rect.centery = int(self.tank.rect.centery + self.tank.rect.height / 3)
		if self.tank.facing == "n":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.centerx = self.tank.rect.centerx 
			self.rect.centery = int(self.tank.rect.centery  - self.tank.rect.height / 3)
		if self.tank.facing == "e":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.centerx = int(self.tank.rect.centerx + self.tank.rect.height / 3)
			self.rect.centery = self.tank.rect.centery
		if self.tank.facing == "w":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.centerx = int(self.tank.rect.centerx - self.tank.rect.height / 3)
			self.rect.centery = self.tank.rect.centery

	def update_boss(self):
		if self.tank.facing == "s":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.centerx = self.tank.rect.centerx
			self.rect.centery = int(self.tank.rect.centery + self.tank.rect.height / 3)
		if self.tank.facing == "n":
			self.image = self.image_0
			self.rect = self.image.get_rect()
			self.rect.centerx = self.tank.rect.centerx 
			self.rect.centery = int(self.tank.rect.centery  - self.tank.rect.height / 3)
		if self.tank.facing == "e":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.centerx = int(self.tank.rect.centerx + self.tank.rect.height / 3)
			self.rect.centery = self.tank.rect.centery
		if self.tank.facing == "w":
			self.image = self.image_1
			self.rect = self.image.get_rect()
			self.rect.centerx = int(self.tank.rect.centerx - self.tank.rect.height / 3)
			self.rect.centery = self.tank.rect.centery

# explosion
class Explosion(pygame.sprite.Sprite):
	def __init__(self, object):
		pygame.sprite.Sprite.__init__(self)
		self.screen = object.screen
		if object.get_name() == "tank_player":
			self.image_0 = pygame.image.load(constant.EXPLOSION_IMAGE_PLAYER1_0)
			self.image_1 = pygame.image.load(constant.EXPLOSION_IMAGE_PLAYER1_1)
		if object.get_name() == "enemy":
			self.image_0 = pygame.image.load(constant.EXPLOSION_IMAGE_ENEMY_0)
			self.image_1 = pygame.image.load(constant.EXPLOSION_IMAGE_ENEMY_1)
		
		self.image = self.image_0

		# vi tri
		self.rect = self.image.get_rect()
		self.rect.centerx = object.rect.centerx
		self.rect.centery = object.rect.centery

		# thoi gian tao. hieu ung no
		self.lifemax = 10
		self.lifecounter = 0
		self.first = True

	def update(self):
		"""
		Allows the game to update this sprite.
		"""
		self.lifecounter += 1
		if self.lifecounter == self.lifemax and self.first:
			self.lifecounter = 0
			self.image = self.image_1
			self.first = False

		if self.lifecounter == self.lifemax and not self.first:
			self.kill()

# la vat dung de tang mau
class PowerBox(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		# hinh`, toa. do xuat hien., tang mau', thoi` gian x
		self.image = pygame.image.load(constant.TANK_IMAGE_POWER)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0, constant.SCREEN_WIDTH - self.rect.width)
		self.rect.y = random.randint(0, constant.SCREEN_HEIGHT - self.rect.height)
		self.tolive = 400

	def set_position(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def update(self):
		"""
		Allows the game to update this sprite.
		"""
		self.tolive -= 1
		# het thoi gian thi no' mat 
		if self.tolive == 0:
			self.kill()

	def get_name(self):
		return "power"

