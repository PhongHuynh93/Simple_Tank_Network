import pygame
import constant
import game_items

class PlayerTank(object):
	def __init__(self):
		self.screen = self.one_player.screen
		self.facing = "s"
		self.can_shoot = False # bien cho phep ban dan
		self.bullet_counter = 0 # thoi gian cho phep duoc ban dan
		self.hp = constant.ENEMY_HP

		# list dan cua nguoi choi, vet xe cua nguoi choi 
		self.bullets_sprite_list = pygame.sprite.Group()

		# sau 2s khi dung quai' thi moi trung tiep dan
		self.count = 0
		self.count_max = 60
		self.can_hurt = True
		

	# thoi gian giua~ 2 lan ban' dan se quyet dinh. co duoc ban' ko, con ban' nhanh ko can rang buoc. thoi gian
	# check vi. tri' cua xe tang co' vuot. ngoai` man` hinh` chua
	def update(self):
		# sau 2s moi cho tru HP
		if not self.can_hurt:
			self.count += 1
			if self.count == self.count_max:
				self.can_hurt = True
				self.count = 0
		if self.is_power:
			if not self.can_shoot:
				self.bullet_counter += 1
			if self.bullet_counter == 3:
				self.can_shoot = True
				self.bullet_counter = 0
			self.boundaries()
		else:
			if not self.can_shoot:
				self.bullet_counter += 1
			if self.bullet_counter == constant.BULLET_COUNTER:
				self.can_shoot = True
				self.bullet_counter = 0
			self.boundaries()

	def boundaries(self):
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= ( constant.SCREEN_WIDTH - self.rect.width):
			self.rect.x = constant.SCREEN_WIDTH - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (constant.SCREEN_HEIGHT - self.rect.height):
			self.rect.y = constant.SCREEN_HEIGHT - self.rect.height


	def update_boss(self):
		# sau 2s moi cho tru HP
		if not self.can_hurt:
			self.count += 1
			if self.count == self.count_max:
				self.can_hurt = True
				self.count = 0
		if self.is_power:
			# phong to chiec xe ra
			if not self.can_shoot:
				self.bullet_counter += 1
			if self.bullet_counter == 3:
				self.can_shoot = True
				self.bullet_counter = 0
			self.boundaries_boss()
		else:
			if not self.can_shoot:
				self.bullet_counter += 1
			if self.bullet_counter == constant.BULLET_COUNTER:
				self.can_shoot = True
				self.bullet_counter = 0
			self.boundaries_boss()

	def boundaries_boss(self):
		if self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.x >= ( constant.SCREEN_WIDTH_BOSS - self.rect.width):
			self.rect.x = constant.SCREEN_WIDTH_BOSS - self.rect.width
		if self.rect.y <= 0:
			self.rect.y = 0
		if self.rect.y >= (constant.SCREEN_HEIGHT_BOSS - self.rect.height):
			self.rect.y = constant.SCREEN_HEIGHT_BOSS - self.rect.height

	def control_tank(self):
		raise Exception('Abstract method, please override in the subclass')

	# ban sung theo huong, tao sprite bullet va` add vao` sprite 
	def shoot(self):
		bullet = game_items.Bullet(self)
		self.bullets_sprite_list.add(bullet)
		self.one_player.all_sprite_list.add(bullet)
		# self.ammo -= 1

	def get_name(self):
		return "tank_player"

# che do 1 nguoi choi 
class Player1Tank(PlayerTank, pygame.sprite.Sprite):
	def __init__(self, one_player):
		self.one_player = one_player
		pygame.sprite.Sprite.__init__(self)
		PlayerTank.__init__(self)

		# load image tank of fist player
		self.image = pygame.image.load(constant.TANK_IMAGE_0)
		self.rect = self.image.get_rect()

		self.track = game_items.Track(self)
		self.barrel = game_items.Barrel(self)

		self.is_power = False

		# add vao man choi normal
		self.one_player.all_sprite_list.add(self.track)
		self.one_player.barrel_sprite_list.add(self.barrel)

		# add vao man choi boss
		self.one_player.all_sprite_list_boss.add(self.track)
		self.init_postition()


	def init_postition(self):
		# position
		self.rect.centerx = int(constant.REAL_SCREEN_WIDTH / 2)
		self.rect.centery = int(constant.REAL_SCREEN_HEIGHT / 2)

	# check boundaries
	# check event nhan' phim
	# xoay anh? tai. cho~ phu thuoc vao huong
	def update(self):
		PlayerTank.update(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank()

	def update_boss(self):
		PlayerTank.update_boss(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank_boss()

	# move tank
	def control_tank(self):
		keys = pygame.key.get_pressed() # reset all keyboard event
		# go straight
		if keys[pygame.K_w]: # di len
			self.rect.y -= constant.SPEED_TANK
			self.one_player.background_y += constant.SPEED_TANK
			if self.one_player.background_y > 0:
				self.one_player.background_y = 0
			self.rotate_image(self.facing, "n")
		if keys[pygame.K_s]: # di xuong
			self.rect.y += constant.SPEED_TANK
			self.one_player.background_y -= constant.SPEED_TANK
			if self.one_player.background_y <= -int(constant.SCREEN_HEIGHT - constant.REAL_SCREEN_HEIGHT):
				self.one_player.background_y = -int(constant.SCREEN_HEIGHT - constant.REAL_SCREEN_HEIGHT)
			self.rotate_image(self.facing, "s")
		if keys[pygame.K_a]: # di qua trai
			self.rect.x -= constant.SPEED_TANK
			self.one_player.background_x += constant.SPEED_TANK
			if self.one_player.background_x > 0:
				self.one_player.background_x = 0
			self.rotate_image(self.facing, "w")
		if keys[pygame.K_d]: # di qua phai
			self.rect.x += constant.SPEED_TANK
			self.one_player.background_x -= constant.SPEED_TANK
			if self.one_player.background_x <= -int(constant.SCREEN_WIDTH - constant.REAL_SCREEN_WIDTH):
				self.one_player.background_x = -int(constant.SCREEN_WIDTH - constant.REAL_SCREEN_WIDTH)
			self.rotate_image(self.facing, "e")
		if keys[pygame.K_SPACE] and self.can_shoot:
			if self.one_player.game.can_play_music:
				self.one_player.game.music.play_music("shot")
			self.can_shoot = False
			self.shoot()

	def control_tank_boss(self):
		keys = pygame.key.get_pressed() # reset all keyboard event
		# go straight
		if keys[pygame.K_w]: # di len
			self.rect.y -= constant.SPEED_TANK
			self.one_player.background_y_boss += constant.SPEED_TANK
			if self.one_player.background_y_boss > 0:
				self.one_player.background_y_boss = 0
			self.rotate_image(self.facing, "n")
		if keys[pygame.K_s]: # di xuong
			self.rect.y += constant.SPEED_TANK
			self.one_player.background_y_boss -= constant.SPEED_TANK
			if self.one_player.background_y_boss <= -int(constant.SCREEN_HEIGHT_BOSS - constant.REAL_SCREEN_HEIGHT):
				self.one_player.background_y_boss = -int(constant.SCREEN_HEIGHT_BOSS - constant.REAL_SCREEN_HEIGHT)
			self.rotate_image(self.facing, "s")
		if keys[pygame.K_a]: # di qua trai
			self.rect.x -= constant.SPEED_TANK
			self.one_player.background_x_boss += constant.SPEED_TANK
			if self.one_player.background_x_boss > 0:
				self.one_player.background_x_boss = 0
			self.rotate_image(self.facing, "w")
		if keys[pygame.K_d]: # di qua phai
			self.rect.x += constant.SPEED_TANK
			self.one_player.background_x_boss -= constant.SPEED_TANK
			if self.one_player.background_x_boss <= -int(constant.SCREEN_WIDTH_BOSS - constant.REAL_SCREEN_WIDTH):
				self.one_player.background_x_boss = -int(constant.SCREEN_WIDTH_BOSS - constant.REAL_SCREEN_WIDTH)
			self.rotate_image(self.facing, "e")
		if keys[pygame.K_SPACE] and self.can_shoot:
			if self.one_player.game.can_play_music:
				self.one_player.game.music.play_music("shot")
			self.can_shoot = False
			self.shoot()

	def rotate_image(self, past_di, present_di):
		if present_di == "n":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 90)
		if present_di == "s":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 270)
		if present_di == "e":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 0)
		if present_di == "w":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 180)
		self.facing = present_di


# xe tang trong che 2 nguoi choi , dai. dien. cho nguoi` choi chinh'
class Player2Tank(PlayerTank, pygame.sprite.Sprite):
	def __init__(self, one_player):
		self.one_player = one_player

		pygame.sprite.Sprite.__init__(self)
		PlayerTank.__init__(self)

		# load image tank of fist player
		if self.one_player.game.index_player == 0:
			self.image = pygame.image.load(constant.TANK_IMAGE_0)
		elif self.one_player.game.index_player == 1:
			self.image = pygame.image.load(constant.TANK_IMAGE_0_PLAYER_2)
		self.rect = self.image.get_rect()

		self.is_power = False


	def make_tank(self):
		if self.one_player.game.index_player == 0:
			self.image = pygame.image.load(constant.TANK_IMAGE_0)
		elif self.one_player.game.index_player == 1:
			self.image = pygame.image.load(constant.TANK_IMAGE_0_PLAYER_2)
		self.rect = self.image.get_rect()

		self.track = game_items.Track(self)
		self.barrel = game_items.Barrel(self)

		# add vao man choi normal
		self.one_player.all_sprite_list.add(self.track)
		self.one_player.barrel_sprite_list.add(self.barrel)

		# add vao man choi boss
		self.one_player.all_sprite_list_boss.add(self.track)
		self.init_postition() 

	def init_postition(self):
		# position
		self.rect.centerx = int(constant.REAL_SCREEN_WIDTH / 2)
		self.rect.centery = int(constant.REAL_SCREEN_HEIGHT / 2)

	# check boundaries
	# check event nhan' phim
	# xoay anh? tai. cho~ phu thuoc vao huong
	def update(self):
		PlayerTank.update(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank()

	def update_boss(self):
		PlayerTank.update_boss(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank_boss()

	def update_boss_2(self):
		PlayerTank.update_boss(self) # using "update()" in its superclass do class con va cha deu co method update()
		self.control_tank_boss()

	# move tank
	def control_tank(self):
		keys = pygame.key.get_pressed() # reset all keyboard event
		# go straight
		if keys[pygame.K_w]: # di len
			self.rect.y -= constant.SPEED_TANK
			self.one_player.background_y += constant.SPEED_TANK
			if self.one_player.background_y > 0:
				self.one_player.background_y = 0
			self.rotate_image(self.facing, "n")
		if keys[pygame.K_s]: # di xuong
			self.rect.y += constant.SPEED_TANK
			self.one_player.background_y -= constant.SPEED_TANK
			if self.one_player.background_y <= -int(constant.SCREEN_HEIGHT - constant.REAL_SCREEN_HEIGHT):
				self.one_player.background_y = -int(constant.SCREEN_HEIGHT - constant.REAL_SCREEN_HEIGHT)
			self.rotate_image(self.facing, "s")
		if keys[pygame.K_a]: # di qua trai
			self.rect.x -= constant.SPEED_TANK
			self.one_player.background_x += constant.SPEED_TANK
			if self.one_player.background_x > 0:
				self.one_player.background_x = 0
			self.rotate_image(self.facing, "w")
		if keys[pygame.K_d]: # di qua phai
			self.rect.x += constant.SPEED_TANK
			self.one_player.background_x -= constant.SPEED_TANK
			if self.one_player.background_x <= -int(constant.SCREEN_WIDTH - constant.REAL_SCREEN_WIDTH):
				self.one_player.background_x = -int(constant.SCREEN_WIDTH - constant.REAL_SCREEN_WIDTH)
			self.rotate_image(self.facing, "e")
		if keys[pygame.K_SPACE] and self.can_shoot:
			if self.one_player.game.can_play_music:
				self.one_player.game.music.play_music("shot")
			self.can_shoot = False
			self.shoot()

		# send toa do x,y cua xe tang de? nguoi choi ben kia ve~ duoc 
		self.one_player.game.Send({"action" : "tank", "x" : self.rect.x, "y" : self.rect.y, "face" : self.facing, "id" : self.one_player.game.index_player})

	# ban sung theo huong, tao sprite bullet va` add vao` sprite 
	def shoot(self):
		bullet = game_items.Bullet(self)
		# Neu tao khau sung' thi gui cho server
		self.one_player.game.Send({"action" : "bullet", "x" : self.rect.centerx, "y" : self.rect.centery, "face" : self.facing, "id" : self.one_player.game.index_player})
		self.bullets_sprite_list.add(bullet)
		self.one_player.all_sprite_list.add(bullet)


	def control_tank_boss(self):
		keys = pygame.key.get_pressed() # reset all keyboard event
		# go straight
		if keys[pygame.K_w]: # di len
			self.rect.y -= constant.SPEED_TANK
			self.one_player.background_y_boss += constant.SPEED_TANK
			if self.one_player.background_y_boss > 0:
				self.one_player.background_y_boss = 0
			self.rotate_image(self.facing, "n")
		if keys[pygame.K_s]: # di xuong
			self.rect.y += constant.SPEED_TANK
			self.one_player.background_y_boss -= constant.SPEED_TANK
			if self.one_player.background_y_boss <= -int(constant.SCREEN_HEIGHT_BOSS - constant.REAL_SCREEN_HEIGHT):
				self.one_player.background_y_boss = -int(constant.SCREEN_HEIGHT_BOSS - constant.REAL_SCREEN_HEIGHT)
			self.rotate_image(self.facing, "s")
		if keys[pygame.K_a]: # di qua trai
			self.rect.x -= constant.SPEED_TANK
			self.one_player.background_x_boss += constant.SPEED_TANK
			if self.one_player.background_x_boss > 0:
				self.one_player.background_x_boss = 0
			self.rotate_image(self.facing, "w")
		if keys[pygame.K_d]: # di qua phai
			self.rect.x += constant.SPEED_TANK
			self.one_player.background_x_boss -= constant.SPEED_TANK
			if self.one_player.background_x_boss <= -int(constant.SCREEN_WIDTH_BOSS - constant.REAL_SCREEN_WIDTH):
				self.one_player.background_x_boss = -int(constant.SCREEN_WIDTH_BOSS - constant.REAL_SCREEN_WIDTH)
			self.rotate_image(self.facing, "e")
		if keys[pygame.K_SPACE] and self.can_shoot:
			if self.one_player.game.can_play_music:
				self.one_player.game.music.play_music("shot")
			self.can_shoot = False
			self.shoot()

		# send toa do x,y cua xe tang de? nguoi choi ben kia ve~ duoc 
		self.one_player.game.Send({"action" : "tankBoss", "x" : self.rect.x, "y" : self.rect.y, "face" : self.facing, "id" : self.one_player.game.index_player})


	def rotate_image(self, past_di, present_di):
		if present_di == "n":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 90)
		if present_di == "s":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 270)
		if present_di == "e":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 0)
		if present_di == "w":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 180)
		self.facing = present_di


# xe tang trong che 2 nguoi choi , dai dien cho nguoi choi qua mang
class Player2Tank_Network(pygame.sprite.Sprite):
	def __init__(self, one_player):
		pygame.sprite.Sprite.__init__(self)
		self.one_player = one_player
		self.screen = self.one_player.screen

		self.facing = "s"

		# load image tank of fist player
		if self.one_player.game.index_player == 0:
			self.image = pygame.image.load(constant.TANK_IMAGE_0_PLAYER_2)
		elif self.one_player.game.index_player == 1:
			self.image = pygame.image.load(constant.TANK_IMAGE_0)
		self.rect = self.image.get_rect()

		self.is_power = False

		self.hp = constant.ENEMY_HP

		self.count = 0
		self.count_max = 60
		self.can_hurt = True

	def make_tank(self):
		# load image tank of fist player
		if self.one_player.game.index_player == 0:
			self.image = pygame.image.load(constant.TANK_IMAGE_0_PLAYER_2)
		elif self.one_player.game.index_player == 1:
			self.image = pygame.image.load(constant.TANK_IMAGE_0)
		self.rect = self.image.get_rect()

		self.track = game_items.Track(self)
		self.barrel = game_items.Barrel(self, True)
		# add vao man choi normal
		self.one_player.all_sprite_list.add(self.track)
		self.one_player.barrel_sprite_list.add(self.barrel)

		# add vao man choi boss
		self.one_player.all_sprite_list_boss.add(self.track)
		self.init_postition()

	def update_state(self, x, y, facing):
		self.rotate_image(self.facing, facing)
		self.rect.x = x
		self.rect.y = y


	def update(self):
		x = 0 # ko lam gi 
		# sau 2s moi cho tru HP
		#if not self.can_hurt:
			#self.count += 1
			#if self.count == self.count_max:
				#self.can_hurt = True
				#self.count = 0
	
	def update_boss_2(self):
		x = 0 # ko lam gi 

	def init_postition(self):
		# position
		self.rect.centerx = int(constant.REAL_SCREEN_WIDTH / 2)
		self.rect.centery = int(constant.REAL_SCREEN_HEIGHT / 2)

	def rotate_image(self, past_di, present_di):
		if present_di == "n":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 90)
		if present_di == "s":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 270)
		if present_di == "e":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 180)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 0)
		if present_di == "w":
			if past_di == "n":
				self.image = pygame.transform.rotate(self.image, 90)
			if past_di == "s":
				self.image = pygame.transform.rotate(self.image, 270)
			if past_di == "w":
				self.image = pygame.transform.rotate(self.image, 0)
			if past_di == "e":
				self.image = pygame.transform.rotate(self.image, 180)
		self.facing = present_di

