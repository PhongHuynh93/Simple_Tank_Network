import pygame
import game_modes
import tank
import enemy
import random
import constant
import game_items

class TwoPlayer(game_modes.GameMode):
	def __init__(self, game):
		game_modes.GameMode.__init__(self, game)

		self.count_power = 400
		self.count_power_2 = 400

		# so luong enemy luc dau
		self.enemy_number = constant.ENEMY_NUMBER

		self.first_boss = True

		self.count_boss_hurt = 100
		self.boss_hurt = True

		self.add_player()

	def add_player(self):
		# make player
		self.player = tank.Player2Tank(self)
		self.player_network = tank.Player2Tank_Network(self) # tao. nguoi choi thu 2

		self.all_sprite_list.add(self.player)
		self.all_sprite_list_boss.add(self.player)
		self.all_sprite_list.add(self.player_network)
		self.all_sprite_list_boss.add(self.player_network)

		# make a boss
		self.boss_obj = enemy.Boss(self)
		self.all_sprite_list_boss.add(self.boss_obj)
		self.boss_sprite_list_boss.add(self.boss_obj)


	def generate_game_items(self):

		# thoi` gian dc huong? che' do. ban' nhanh 
		if self.player.is_power:
			self.count_power -= 1
			if self.count_power <= 0:
				self.player.is_power = False
				self.count_power = 400

		

		"""
		if self.player_network.is_power:
			self.count_power_2 -= 1
			if self.count_power_2 <= 0:
				self.player_network.is_power = False
				self.count_power_2 = 400
		"""

	def make_power_box(self, x, y):
		item_obj = game_items.PowerBox(self.screen)
		item_obj.set_position(x, y)
		self.upgrades_sprite_list.add(item_obj)
		self.all_sprite_list.add(item_obj)

	def handle_collisions(self):
		if self.player.hp <= 0: # player die
			self.player.hp = 0
			self.player.track.kill()
			self.player.barrel.kill()
			self.player.kill()

		if self.player_network.hp <= 0:
			self.player_network.hp = 0
			self.player_network.track.kill()
			self.player_network.barrel.kill()
			self.player_network.kill()
		
		# enemy
		for enemy in self.enemy_sprite_list: # enemy die
			if enemy.hp <= 0:
				# khi giet duoc 1 con thi send cho 
				self.game.Send({"action" : "EnemyNumber", "id" : self.game.index_player})
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

			bullets_hit_list = pygame.sprite.spritecollide(self.player_network, enemy.bullets_sprite_list, False)
			for bullet in bullets_hit_list:
				ex_obj = game_items.Explosion(self.player)
				self.explosions_sprite_list.add(ex_obj)
				self.all_sprite_list.add(ex_obj)
				bullet.kill()
				#self.player_network.hp -= 1

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
				self.player.is_power = True
				upgrade.kill()

		# vat dung. ho~ tro. cho nhan vat
		upgrades_hit_list = pygame.sprite.spritecollide(self.player_network, self.upgrades_sprite_list, False)
		for upgrade in upgrades_hit_list:
			if upgrade.get_name() == "power":
				#self.player_network.is_power = True
				upgrade.kill()

		snake_list = pygame.sprite.spritecollide(self.player, self.snakes_sprite_list, False)
		if self.player.can_hurt:
			for snake in snake_list:
				if self.game.can_play_music:
					self.game.music.play_music("player_hit")
				self.player.hp -= 1
				self.player.can_hurt = False

		# send server HP cua nhan vat chinh
		self.game.Send({"action" : "HP", "hp" : self.player.hp, "id" : self.game.index_player})

	def update_sprites(self):
		self.all_sprite_list.update()
		self.barrel_sprite_list.update()

	def draw_changes(self):
		self.all_sprite_list.draw(self.screen)
		self.barrel_sprite_list.draw(self.screen)


	def display_game_message(self):
		x = 10

	def check_for_game_over(self):
		x = 10

	####################################################################################
	# Boss
	####################################################################################
	def generate_game_items_boss_2(self):
		# thoi` gian dc huong? che' do. ban' nhanh , muc. dich' xoa' ban' nhanh trong man` boss 
		if self.player.is_power:
			self.count_power -= 1
			if self.count_power <= 0:
				self.player.is_power = False
				self.count_power = 400

		if not self.boss_hurt:
			self.count_boss_hurt -= 1
			if self.count_boss_hurt <= 0:
				self.boss_hurt = True
				self.count_boss_hurt = 400 

	def handle_collisions_boss_2(self):
		# het' mau thi` xoa' nhan vat, xoa boss
		if self.player.hp <= 0: # player die
			self.player.hp = 0
			self.player.track.kill()
			self.player.barrel.kill()
			self.player.kill()

		if self.player_network.hp <= 0:
			self.player_network.hp = 0
			self.player_network.track.kill()
			self.player_network.barrel.kill()
			self.player_network.kill()

		if self.boss_obj.hp <= 0:
			self.boss_obj.hp = 0
			self.boss_obj.kill()

		# dung boss tru` 1 diem nhung sau 2 giay moi tru
		boss_list = pygame.sprite.spritecollide(self.player, self.boss_sprite_list_boss, False)
		if self.player.can_hurt:
			for boss in boss_list:
				if self.game.can_play_music:
					self.game.music.play_music("player_hit")
				self.player.hp -= 1
				self.player.can_hurt = False


		# dung trung dan cua? boss tru 1 diem va xoa dan 
		bullet_list = pygame.sprite.spritecollide(self.player, self.bullet_sprite_list_boss, True)
		for i in bullet_list:
			if self.game.can_play_music:
					self.game.music.play_music("player_hit")
			self.player.hp -= 1

		# neu' dan. cua ta trung' boss thi` tru mau' boss 
		for boss in self.boss_sprite_list_boss:
			bullet_list = pygame.sprite.spritecollide(boss, self.player.bullets_sprite_list, True)
			for i in bullet_list:
				if self.boss_hurt:
					print "so lan boss bi thuong khi trung 1 vien dan "
					# send cho server de? no tru` hp cho boss 
					self.boss_hurt = False
					self.game.Send({"action" : "BossHP", "id" : self.game.index_player})

		# gui? HP cho server de? no' send cho client kia 
		self.game.Send({"action" : "HP", "hp" : self.player.hp, "id" : self.game.index_player})

	def update_sprites_boss_2(self):
		# update vi tri cua boss + vi. tri' dan. cua boss (dan. lon' nho?)
		for sprite in self.all_sprite_list_boss:
			sprite.update_boss_2()
		# update vi. tri cua nong` sung'
		self.barrel_sprite_list.update()
		# update vi. tri' dan. cua ta
		for bullet in self.player.bullets_sprite_list:
			bullet.update_boss()
		

	def draw_changes_boss_2(self):
		self.all_sprite_list_boss.draw(self.game.screen_boss)
		self.barrel_sprite_list.draw(self.game.screen_boss) # ve~ vi tri' cua? sung' 
		self.player.bullets_sprite_list.draw(self.game.screen_boss) # ve~ dan cua ta 

	def display_game_message_boss_2(self):
		x = 10

	def check_for_game_over_boss_2(self):
		x = 10


