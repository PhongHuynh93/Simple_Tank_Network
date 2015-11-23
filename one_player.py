import pygame
import game_modes
import tank
import enemy
import random
import constant
import game_items

class OnePlayer(game_modes.GameMode):
	def __init__(self, game):
		game_modes.GameMode.__init__(self, game)

		# make player
		self.player = tank.Player1Tank(self)
		self.all_sprite_list.add(self.player)
		self.all_sprite_list_boss.add(self.player)

		# thoi gian tao nhung~ thu' xuat. hien trong game 
		self.enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX) - 100
		self.power_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX) # thoi gian xuat hien vat pham tang toc' cho xe tang

		self.count_power = 400

		# so luong enemy luc dau
		self.enemy_number = constant.ENEMY_NUMBER

		self.first_boss = True


	def generate_game_items(self):
		# tao enemy khi thoi gian het' 
		self.enemy_interval -= 1
		self.power_interval -= 1

		if self.player.is_power:
			self.count_power -= 1
			if self.count_power <= 0:
				self.player.is_power = False
				self.count_power = 400

		# vat pham tang toc xe tang
		if self.power_interval <= 0:
			item_obj = game_items.PowerBox(self.screen)
			self.upgrades_sprite_list.add(item_obj)
			self.all_sprite_list.add(item_obj)
			self.power_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX)
		
		# ke thu
		if self.enemy_interval == 0:
			if self.enemy_number > 0:
				enemy_obj = enemy.Enemy(self)
				snake_obj = enemy.Snake(self)
				self.enemy_sprite_list.add(enemy_obj)
				self.snakes_sprite_list.add(snake_obj)

				self.all_sprite_list.add(enemy_obj)
				self.all_sprite_list.add(snake_obj)
				self.enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX) - 100
			else:
				self.game.running_normal = False 


	def handle_collisions(self):
		if self.player.hp <= 0: # player die
				self.player.kill()
		# enemy
		for enemy in self.enemy_sprite_list: # enemy die
			if enemy.hp <= 0:
				self.enemy_number -= 1
				enemy.kill()
			# neu dan. cua dich. trung ta.
			bullets_hit_list = pygame.sprite.spritecollide(self.player, enemy.bullets_sprite_list, False)
			for bullet in bullets_hit_list:

				if self.game.can_play_music:
					self.game.music.play_music("player_hit")

				ex_obj = game_items.Explosion(self.player)
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				bullet.kill()
				self.player.hp -= 1
			# check neu' cua? ta trung dich
			bullet_hit_list = pygame.sprite.spritecollide(enemy, self.player.bullets_sprite_list, False)
			for bullet in bullet_hit_list:
				ex_obj = game_items.Explosion(enemy)
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				enemy.hp -= 1
				bullet.kill()

		# vat dung. ho~ tro. cho nhan vat
		upgrades_hit_list = pygame.sprite.spritecollide(self.player, self.upgrades_sprite_list, False)
		for upgrade in upgrades_hit_list:
			if upgrade.get_name() == "power":
				self.is_power = True
				upgrade.kill()

		snake_list = pygame.sprite.spritecollide(self.player, self.snakes_sprite_list, False)
		if self.player.can_hurt:
			for snake in snake_list:
				if self.game.can_play_music:
					self.game.music.play_music("player_hit")
				self.player.hp -= 1
				self.player.can_hurt = False





	def update_sprites(self):
		self.all_sprite_list.update()
		self.barrel_sprite_list.update()

	def draw_changes(self):
		x = 10
		self.all_sprite_list.draw(self.screen)
		self.barrel_sprite_list.draw(self.screen)


	def display_game_message(self):
		x = 10

	def check_for_game_over(self):
		x = 10


	####################################################################################
	# Boss
	####################################################################################
	def generate_game_items_boss(self):
		# make a boss
		if self.first_boss:
			self.first_boss = False
			boss_obj = enemy.Boss(self)
			self.all_sprite_list_boss.add(boss_obj)
			self.boss_sprite_list_boss.add(boss_obj)


	def handle_collisions_boss(self):
		# dung boss tru` 1 diem nhung sau 2 giay moi tru
		boss_list = pygame.sprite.spritecollide(self.player, self.boss_sprite_list_boss, False)
		if self.player.can_hurt:
			for boss in boss_list:
				if self.game.can_play_music:
					self.game.music.play_music("player_hit")
				self.player.hp -= 1
				self.player.can_hurt = False

		# dung trung dan tru 1 diem va xoa dan 
		bullet_list = pygame.sprite.spritecollide(self.player, self.bullet_sprite_list_boss, True)
		for i in bullet_list:
			if self.game.can_play_music:
					self.game.music.play_music("player_hit")
			self.player.hp -= 1

	def update_sprites_boss(self):
		for sprite in self.all_sprite_list_boss:
			sprite.update_boss()
		self.barrel_sprite_list.update()
		for bullet in self.player.bullets_sprite_list:
			bullet.update_boss()
		

	def draw_changes_boss(self):
		self.all_sprite_list_boss.draw(self.game.screen_boss)
		self.barrel_sprite_list.draw(self.game.screen_boss)
		self.player.bullets_sprite_list.draw(self.game.screen_boss)

	def display_game_message_boss(self):
		x = 10

	def check_for_game_over_boss(self):
		x = 10


