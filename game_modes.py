import pygame
import constant

class GameMode(object):
	def __init__(self, game):
		self.game = game
		self.screen = game.screen
		# background
		self.image = pygame.image.load(constant.BACKGROUND_PLAY)
		self.image_boss = pygame.image.load(constant.BACKGROUND_BOSS)

		# croll
		self.background_x = 0
		self.background_y = 0

		self.background_x_boss = 0
		self.background_y_boss = 0

		# sprite
		self.all_sprite_list = pygame.sprite.Group()
		self.barrel_sprite_list = pygame.sprite.Group()
		self.enemy_sprite_list = pygame.sprite.Group()
		self.explosions_sprite_list = pygame.sprite.Group()
		self.upgrades_sprite_list = pygame.sprite.Group()
		self.snakes_sprite_list = pygame.sprite.Group()

		# sprite boss
		self.first_boss = True
		self.all_sprite_list_boss = pygame.sprite.Group()
		self.boss_sprite_list_boss = pygame.sprite.Group()
		self.bullet_sprite_list_boss = pygame.sprite.Group()

	# 1 game chinh' gom` cac' buoc' sau
	def update(self):
		#self.screen.fill((255, 255, 255))
		self.screen.blit(self.image, (0, 0))
		self.screen.blit(self.image, (0, 1936))
		self.generate_game_items()
		self.handle_collisions()
		self.update_sprites()
		self.draw_changes()
		self.display_game_message()
		self.check_for_game_over()
		self.game.real_screen.blit(self.screen, (self.background_x, self.background_y))
		# text
		textHP = self.game.font.render("HP:" + str(self.player.hp), False, (255, 255, 255))
		self.game.real_screen.blit(textHP, (10, 10))
		textEnemy = self.game.font.render("ENEMY:" + str(self.enemy_number), False, (255, 255, 255))
		self.game.real_screen.blit(textEnemy, (300, 10))
		pygame.display.flip()

	# update game network
	def update_network(self):
		self.screen.blit(self.image, (0, 0))
		self.screen.blit(self.image, (0, 1936))
		self.generate_game_items()
		self.handle_collisions()
		self.update_sprites()
		self.draw_changes()
		self.display_game_message()
		self.check_for_game_over()
		self.game.real_screen.blit(self.screen, (self.background_x, self.background_y))
		# text HP cua ta
		textHP = self.game.font.render("HP_1 : " + str(self.player.hp), False, (255, 255, 255))
		self.game.real_screen.blit(textHP, (10, 10))
		# text HP cua ban. ta
		textHP_2 = self.game.font.render("HP_2 : " + str(self.player_network.hp), False, (255, 255, 255))
		textHP_2_rect = textHP_2.get_rect()
		self.game.real_screen.blit(textHP_2, (constant.REAL_SCREEN_WIDTH - 10 - textHP_2_rect.width, 10))
		textEnemy = self.game.font.render("ENEMY : " + str(self.enemy_number), False, (255, 255, 255))
		textEnemy_rect = textEnemy.get_rect()
		self.game.real_screen.blit(textEnemy, (int(constant.REAL_SCREEN_WIDTH / 2 - textEnemy_rect.width / 2), 10))
		pygame.display.flip()

	def generate_game_items(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def handle_collisions(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def update_sprites(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def draw_changes(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def display_game_message(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def check_for_game_over(self):
		raise Exception('Day la Abstract method, class con se~ override')

	# update danh' boss
	def update2(self):
		self.game.screen_boss.blit(self.image_boss, (0, 0))

		self.generate_game_items_boss()
		self.handle_collisions_boss()
		self.update_sprites_boss()
		self.draw_changes_boss()
		self.display_game_message_boss()
		self.check_for_game_over_boss()

		self.game.real_screen.blit(self.game.screen_boss, (self.background_x_boss, self.background_y_boss))#(self.background_boss_x, self.background_boss_y))
		# text
		textHP = self.game.font.render("HP:" + str(self.player.hp), False, (255, 255, 255))
		self.game.real_screen.blit(textHP, (10, 10))
		pygame.display.flip()

	def generate_game_items_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def handle_collisions_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def update_sprites_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def draw_changes_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def display_game_message_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def check_for_game_over_boss(self):
		raise Exception('Day la Abstract method, class con se~ override')


	# update danh' boss cho che' do. choi 2 nguoi 
	def update_network_boss(self):
		self.game.screen_boss.blit(self.image_boss, (0, 0))

		self.generate_game_items_boss_2()
		self.handle_collisions_boss_2()
		self.update_sprites_boss_2()
		self.draw_changes_boss_2()
		self.display_game_message_boss_2()
		self.check_for_game_over_boss_2()

		self.game.real_screen.blit(self.game.screen_boss, (self.background_x_boss, self.background_y_boss))#(self.background_boss_x, self.background_boss_y))
		# text
		textHP = self.game.font.render("HP:" + str(self.player.hp), False, (255, 255, 255))
		self.game.real_screen.blit(textHP, (10, 10))

		# text HP cua ban. ta
		textHP_2 = self.game.font.render("HP_2 : " + str(self.player_network.hp), False, (255, 255, 255))
		textHP_2_rect = textHP_2.get_rect()
		self.game.real_screen.blit(textHP_2, (constant.REAL_SCREEN_WIDTH - 10 - textHP_2_rect.width, 10))

		# enemy 
		textEnemy = self.game.font.render("BOSS : " + str(self.boss_obj.hp), False, (255, 255, 255))
		textEnemy_rect = textEnemy.get_rect()
		self.game.real_screen.blit(textEnemy, (int(constant.REAL_SCREEN_WIDTH / 2 - textEnemy_rect.width / 2), 10))

		pygame.display.flip()

	def generate_game_items_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def handle_collisions_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def update_sprites_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def draw_changes_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def display_game_message_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')
	def check_for_game_over_boss_2(self):
		raise Exception('Day la Abstract method, class con se~ override')