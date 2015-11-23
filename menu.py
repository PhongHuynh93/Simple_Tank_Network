import pygame, sys
import constant 

class Menu():
	def __init__(self, game):
		self.game = game
		self.screen = self.game.real_screen
		self.state = "menu" # luc dau se ve man hinh menu
		self.pos = (0, 0) # luu vi tri x, y cua chuot
		self.pos_click = (0, 0) # luu vi tri x, y cua chuot

		# man hinh menu
		self.menu = []
		self.menu.append(pygame.image.load(constant.MENU_IMAGE))
		self.menu.append(pygame.image.load(constant.MENU_IMAGE_CHOOSE_STARTGAME))
		self.menu.append(pygame.image.load(constant.MENU_IMAGE_CHOOSE_OPTION))
		self.menu.append(pygame.image.load(constant.MENU_IMAGE_CHOOSE_SETTING))
		self.sur_startgame = pygame.Surface((300, 71))
		self.sur_startgame_rect = self.sur_startgame.get_rect()
		self.sur_startgame_rect.x = 470
		self.sur_startgame_rect.y = 300

		self.sur_about = pygame.Surface((300, 71))
		self.sur_about_rect = self.sur_about.get_rect()
		self.sur_about_rect.x = 470
		self.sur_about_rect.y = 410

		self.sur_setting = pygame.Surface((300, 71))
		self.sur_setting_rect = self.sur_setting.get_rect()
		self.sur_setting_rect.x = 470
		self.sur_setting_rect.y = 510

		# man hinh option
		self.option = []
		self.option.append(pygame.image.load(constant.MENU_OPTION_IMAGE_NOCHOOSE_BACK))
		self.option.append(pygame.image.load(constant.MENU_OPTION_IMAGE_CHOOSE_BACK))

		self.sur_option = pygame.Surface((300, 71))
		self.sur_option_rect = self.sur_option.get_rect()
		self.sur_option_rect.x = 460
		self.sur_option_rect.y = 500

		# man hinh setting
		self.setting = []
		self.setting.append(pygame.image.load(constant.MENU_MUSIC_ON_IMAGE_NOCHOOSE_BACK))
		self.setting.append(pygame.image.load(constant.MENU_MUSIC_ON_IMAGE_CHOOSE_BACK))
		self.setting.append(pygame.image.load(constant.MENU_MUSIC_OFF_IMAGE_NOCHOOSE_BACK))
		self.setting.append(pygame.image.load(constant.MENU_MUSIC_OFF_IMAGE_CHOOSE_BACK))

		self.sur_music = pygame.Surface((60, 71))
		self.sur_music_rect = self.sur_music.get_rect()
		self.sur_music_rect.x = 530
		self.sur_music_rect.y = 350

		self.sur_setting = pygame.Surface((300, 71))
		self.sur_setting_rect = self.sur_setting.get_rect()
		self.sur_setting_rect.x = 460
		self.sur_setting_rect.y = 500

		# man hinh player
		self.player = []
		self.player.append(pygame.image.load(constant.MENU_PLAYER_IMAGE))
		self.player.append(pygame.image.load(constant.MENU_PLAYER_IMAGE_1_PLAYER))
		self.player.append(pygame.image.load(constant.MENU_PLAYER_IMAGE_2_PLAYER))
		self.player.append(pygame.image.load(constant.MENU_PLAYER_IMAGE_BACK))

		self.sur_player_1p = pygame.Surface((300, 71))
		self.sur_player_1p_rect = self.sur_player_1p.get_rect()
		self.sur_player_1p_rect.x = 470
		self.sur_player_1p_rect.y = 330

		self.sur_player_2p = pygame.Surface((300, 71))
		self.sur_player_2p_rect = self.sur_player_2p.get_rect()
		self.sur_player_2p_rect.x = 470
		self.sur_player_2p_rect.y = 450

		self.sur_player_back = pygame.Surface((300, 71))
		self.sur_player_back_rect = self.sur_player_back.get_rect()
		self.sur_player_back_rect.x = 470
		self.sur_player_back_rect.y = 570


		self.image = self.menu[0]

		self.can_play_music = True

		self.ngoai = True
		self.trong = False

	def draw(self):
		self.pos_click = (0, 0)
		# do` event di chuyen chuot va click chuot
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
				if keys[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()

			if event.type == pygame.MOUSEMOTION:
				# luu vi tri x, y
				self.pos = event.pos
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.pos_click = event.pos

		# neu dang o tren man hinh 
		if self.state == "menu":
			if self.sur_startgame_rect.collidepoint(self.pos): # neu ta re^ chuot vao chu~ "startgame"
				self.image = self.menu[1]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")

			elif self.sur_about_rect.collidepoint(self.pos):
				self.image = self.menu[2]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.sur_setting_rect.collidepoint(self.pos):
				self.image = self.menu[3]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			else:
				self.image = self.menu[0]
				# dat lai state 
				self.ngoai = True
				self.trong = False

			if self.sur_startgame_rect.collidepoint(self.pos_click): # neu ta click chuot vao chu~ "startgame"
				self.state = "player"
				#self.game.running_normal = False
			elif self.sur_about_rect.collidepoint(self.pos_click):
				self.state = "about"
			elif self.sur_setting_rect.collidepoint(self.pos_click):
				self.state = "setting"

		elif self.state == "about":
			if self.sur_option_rect.collidepoint(self.pos):
				self.image = self.option[1]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			else:
				self.image = self.option[0]
				# dat lai state 
				self.ngoai = True
				self.trong = False

			if self.sur_option_rect.collidepoint(self.pos_click):
				self.state = "menu"

		elif self.state == "setting":
			# neu click vao nut 
			if self.sur_music_rect.collidepoint(self.pos) and self.can_play_music:
				self.image = self.setting[2] # load hinh off nhac 
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.sur_music_rect.collidepoint(self.pos) and not self.can_play_music:
				self.image = self.setting[0] #load hinh on nhac
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.can_play_music and self.sur_setting_rect.collidepoint(self.pos): # load hinh on nhac va re^ vao nut click
				self.image = self.setting[1]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif not self.can_play_music and self.sur_setting_rect.collidepoint(self.pos):
				self.image = self.setting[3]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.can_play_music:
				self.image = self.setting[0]
				# dat lai state 
				self.ngoai = True
				self.trong = False
			elif not self.can_play_music:
				self.image = self.setting[2]
				# dat lai state 
				self.ngoai = True
				self.trong = False

			if self.sur_music_rect.collidepoint(self.pos_click) and self.can_play_music:
				self.can_play_music = False
			elif self.sur_music_rect.collidepoint(self.pos_click) and not self.can_play_music:
				self.can_play_music = True
			elif self.sur_setting_rect.collidepoint(self.pos_click):
				self.state = "menu"

		elif self.state == "player":
			if self.sur_player_1p_rect.collidepoint(self.pos):
				self.image = self.player[1]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.sur_player_2p_rect.collidepoint(self.pos):
				self.image = self.player[2]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			elif self.sur_player_back_rect.collidepoint(self.pos):
				self.image = self.player[3]
				if self.ngoai and not self.trong:
					# phat nhac va gan' lai
					self.ngoai = False
					self.trong = True
					if self.can_play_music:
						self.game.music.play_music("mouse_hover")
			else:
				self.image = self.player[0]
				# dat lai state 
				self.ngoai = True
				self.trong = False

			if self.sur_player_1p_rect.collidepoint(self.pos_click):
				self.game.is_one_player = True
				self.game.running_normal = False 
				#self.game.playGame(self.game.one_player)
			elif self.sur_player_2p_rect.collidepoint(self.pos_click):
				self.game.is_two_player = True
				self.game.running_normal = False 
				#self.game.waitingConnection()#self.game.two_player)
			elif self.sur_player_back_rect.collidepoint(self.pos_click):
				self.state = "menu"


		self.screen.blit(self.image, (0, 0))











