import pygame

# FPS
FPS = 30

# dimentions
SCREEN_WIDTH = 1936 #1200
SCREEN_HEIGHT = 1936 * 2 #800

# dimensions in boss
SCREEN_WIDTH_BOSS = 2152
SCREEN_HEIGHT_BOSS = 2152

REAL_SCREEN_WIDTH = 1200
REAL_SCREEN_HEIGHT = 800

# image background
# BACKGROUND_WIDTH = 1936
# BACKGROUND_HEIGHT = 1936

# colors
WHITE = (255, 255, 255)

# background
BACKGROUND_MENU = "./image/background.png"
BACKGROUND_PLAY = "./image/map.png"
BACKGROUND_BOSS = "./image/map_boss.png"

# cac' tham so cua game
PLAYER_HP = 1000

HEALTH_BOOST_MIN = 50
HEALTH_BOOST_MAX = 300
DELAY_PRESS_F = 3 

# cac' tham so' cua tank
SPEED_TANK = 16
BULLET_COUNTER = 10 # thoi gian dan cach giua 2 lan ban sung 
AMMO = 500
TANK_IMAGE_0 = "./image/Tanks/tankRed_outline.png" # xe mau do
TANK_IMAGE_0_PLAYER_2 = "./image/Tanks/tankGreen_outline.png" # xe mau do
TANK_IMAGE_1 = "./image/Tanks/tracksSmall.png" # vet sau xe
TANK_IMAGE_2 = "./image/Tanks/barrelRed_outline.png" # nong sung 
TANK_IMAGE_2_PLAYER_2 = "./image/Tanks/barrelGreen_outline.png" # nong sung 
TANK_IMAGE_POWER = "./image/Obstacles/barrelRed_up.png" # tang toc do ban



# item giup nhan vat trong game
HEALTH_IMAGE = "./image/item/health.png"
AMMO_IMAGE = "./image/item/ammo.png"
AMMO_BOOST_MIN = 100 # tang dan. se~ ngau nhien trong khoang nay 
AMMO_BOOST_MAX = 200
HEALTH_MIN = 500 # thoi gian xuat hien tui' mau'
HEALTH_MAX = 1000

# enemy
ENEMY_NUMBER = 10 
ENEMY_MIN = 100 # thoi gian xuat hien quai
ENEMY_MAX = 300
ENEMY_IMAGE = "./image/Tanks/tankBlack_outline.png"
ENEMY_SPEED_MIN = 5
ENEMY_SPEED_MAX = 10
ENEMY_MIN_BULLET_SPEED = 50 # toc do vien dan 
ENEMY_MAX_BULLET_SPEED = 100
ENEMY_HP = 5 # chi chiu duoc 5 dan 
ENEMY_BULLET = "./image/Bullets/bulletBeige_outline.png"


# explosions
EXPLOSION_IMAGE_PLAYER1_0 = "./image/Smoke/smokeOrange0.png"
EXPLOSION_IMAGE_PLAYER1_1 = "./image/Smoke/smokeOrange1.png"
EXPLOSION_IMAGE_ENEMY_0 = "./image/Smoke/smokeGrey0.png"
EXPLOSION_IMAGE_ENEMY_1 = "./image/Smoke/smokeGrey1.png"

# bullet
BULLET_ENEMY = "./image/bullet/bullet_enemy.png"
BULLET_PLAYER = "./image/Bullets/bulletRedSilver_outline.png"
BULLET_PLAYER_2 = "./image/Bullets/bulletGreenSilver_outline.png"
BULLET_BOSS = "./image/Obstacles/oil.png"
BULLET_BOSS_SMALL = "./image/Obstacles/oil_small.png"
BULLET_SPEED = 20

# stone
STONE_IMAGE = "./image/block/stone/"
SO_LUONG_STONE_IMAGE = 4
STONE_MAX_SIZE = 180 


# man hinh menu
MENU_IMAGE = "./image/Menu_tank/Menu1.png"
MENU_IMAGE_CHOOSE_STARTGAME = "./image/Menu_tank/Menu2.png"
MENU_IMAGE_CHOOSE_OPTION = "./image/Menu_tank/Menu3.png"
MENU_IMAGE_CHOOSE_SETTING = "./image/Menu_tank/Menu4.png"
# man hinh option
MENU_OPTION_IMAGE_CHOOSE_BACK = "./image/Menu_tank/Menu6.png"
MENU_OPTION_IMAGE_NOCHOOSE_BACK = "./image/Menu_tank/Menu5.png"
# man hinh music
MENU_MUSIC_ON_IMAGE_NOCHOOSE_BACK = "./image/Menu_tank/Menu8.png"
MENU_MUSIC_ON_IMAGE_CHOOSE_BACK = "./image/Menu_tank/Menu7.png"
MENU_MUSIC_OFF_IMAGE_NOCHOOSE_BACK = "./image/Menu_tank/Menu9.png"
MENU_MUSIC_OFF_IMAGE_CHOOSE_BACK = "./image/Menu_tank/Menu10.png"
# man hinh chon 1 nguoi choi hay 2 nguoi choi
MENU_PLAYER_IMAGE = "./image/Menu_tank/Menu11.png"
MENU_PLAYER_IMAGE_1_PLAYER = "./image/Menu_tank/Menu12.png"
MENU_PLAYER_IMAGE_2_PLAYER = "./image/Menu_tank/Menu13.png"
MENU_PLAYER_IMAGE_BACK = "./image/Menu_tank/Menu14.png"
# man hinh chon nguoi choi
MENU_IMAGE_FIND_PARTNER = "./image/Menu_tank/Menu15.png"

# text ready, go
IMAGE_TEXT_READY = "./image/Text/text_ready.png"
IMAGE_TEXT_GO = "./image/Text/text_go.png"

# nhac
BACKGROUND_MUSIC = "./music/bg.ogg"
