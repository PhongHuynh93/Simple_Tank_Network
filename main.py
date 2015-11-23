import one_player
import two_player
import pygame, sys
import constant
import menu
import game_items
import enemy

# thu vien network
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

# it's a object of our game, control and run game
class Game(ConnectionListener):
    def __init__(self):
        pygame.init()

        # set screen
        self.screen_width = constant.SCREEN_WIDTH
        self.screen_height = constant.SCREEN_HEIGHT
        self.screen = pygame.Surface([self.screen_width, self.screen_height])
        self.screen_boss = pygame.Surface([constant.SCREEN_WIDTH_BOSS, constant.SCREEN_HEIGHT_BOSS])
        self.real_screen = pygame.display.set_mode([constant.REAL_SCREEN_WIDTH, constant.REAL_SCREEN_HEIGHT], False, 32)

        # font
        self.font = pygame.font.Font("./font/trebucbd.ttf", 60)
        self.clock = pygame.time.Clock()

        # che do. man choi thuong 
        self.running_normal = True

        self.can_play_music = True

        
        self.bg_menu = menu.Menu(self)

        ############# bien' trang thai cua client
        # bien' luu ID cua client khi client ket noi' duoc voi server
        self.index_player = 0
        self.is_waiting = True
        self.image_waiting = pygame.image.load(constant.MENU_IMAGE_FIND_PARTNER)# ve man hinh luc' dang cho` doi. doi' thu?

        
        # che do 1 nguoi choi hay 2 nguoi choi
        self.one_player = one_player.OnePlayer(self)
        self.two_player = two_player.TwoPlayer(self)
        
        self.is_one_player = False # xet xem 1 nguoi choi hay 2 nguoi choi
        self.is_two_player = False # xet xem 1 nguoi choi hay 2 nguoi choi
        self.Connect()

    # make menu game
    def menuGame(self):
        while self.running_normal:
            # listen server 
            connection.Pump()
            self.Pump()

            self.bg_menu.draw()
            pygame.display.flip()
            self.clock.tick(constant.FPS)

        self.running_normal = True

        if self.is_one_player:
            self.playGame(self.one_player)
        if self.is_two_player:
            self.waitingConnection()

    # day la vong lap. tro` choi
    def playGame(self, game):
        self.can_play_music = self.bg_menu.can_play_music

        while self.running_normal:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_normal = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        self.running_normal = False

            game.update()
            self.clock.tick(constant.FPS)

        # sau khi thoat khoi? che do. choi game binh thuong thi choi boss
        self.running_normal = True
        self.one_player.player.init_postition()
        self.playGameBoss(self.one_player)

    # choi game voi boss
    def playGameBoss(self, game):
        while self.running_normal:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_normal = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        self.running_normal = False

            game.update2()
            self.clock.tick(constant.FPS)

    # vong lap cho` nguoi choi thu 2
    def waitingConnection(self):

        while self.running_normal:
            # listen server 
            connection.Pump()
            self.Pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_normal = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        self.running_normal = False
                        pygame.quit()
                        sys.exit()

            # neu dang doi. nguoi choi khac thi ve~ background waiting

            if self.is_waiting:
                self.real_screen.blit(self.image_waiting, (0, 0))
                pygame.display.flip()
                self.clock.tick(constant.FPS)
            else:# neu da~ tim duoc nguoi choi khac' thi choi game thoi
                self.two_player.update_network() # bat' dau vong lap cua game 
                self.clock.tick(constant.FPS)


        # sau khi thoat khoi? che do. choi game binh thuong thi choi boss
        self.running_normal = True
        #self.two_player.player.init_postition()
        self.playGameBoss_2player(self.two_player)

    # load man boss trong che do choi 2 nguoi 
    def playGameBoss_2player(self, game):
        # set lai vi tri cho nguoi choi
        self.two_player.player.init_postition()
        # choi boss 
        while self.running_normal:
            # listen server 
            connection.Pump()
            self.Pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running_normal = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        self.running_normal = False
                        pygame.quit()
                        sys.exit()

            game.update_network_boss()
            self.clock.tick(constant.FPS)

    # ham` lay' ID tu` server gan' cho client
    def Network_IndexPlayer(self, data):
        self.index_player = data["index_player"]
        self.two_player.player.make_tank()
        self.two_player.player_network.make_tank()

    def Network_Waiting(self, data):
        self.is_waiting = data["waiting"]

    # ham lay' lay' toa do. x, y cua? nguoi` choi thu' 2
    def Network_OtherPlayer(self, data):
        self.two_player.player_network.update_state(data["x"], data["y"], data["facing"])

    # ham lay' lay' toa do. x, y cua? nguoi` choi thu' 2
    def Network_OtherPlayerBoss(self, data):
        self.two_player.player_network.update_state(data["x"], data["y"], data["facing"])


    # tao item tang vat pham
    def Network_PowerBox(self, data):
        self.two_player.make_power_box(data["x"], data["y"])

    # tao vien dan
    def Network_Bullet(self, data):
        bullet = game_items.Bullet(self.two_player.player)
        bullet.set_state(data["x"], data["y"], data["face"], data["id"])
        self.two_player.player.bullets_sprite_list.add(bullet)
        self.two_player.all_sprite_list.add(bullet)

    # tao enemy
    def Network_Enemy(self, data):
        # tao xe tang
        enemy_obj = enemy.Enemy(self.two_player)
        enemy_obj.set_state(data["x_pos"], data["y_pos"], data["x"], data["y"], data["time"], data["die"])
        self.two_player.enemy_sprite_list.add(enemy_obj)
        self.two_player.all_sprite_list.add(enemy_obj)
        # tao con ran
        snake_obj = enemy.Snake(self.two_player)
        snake_obj.set_state(data["x_pos_snake"], data["y_pos_snake"])
        self.two_player.snakes_sprite_list.add(snake_obj)
        self.two_player.all_sprite_list.add(snake_obj)

    # nhan. HP cua parter
    def Network_HP(self, data):
        self.two_player.player_network.hp = data["hp"]

    # nhan. so' luong quai' hien co' tren man hinh
    def Network_EnemyNumber(self, data):
        self.two_player.enemy_number = data["enemy_number"]

    # load man boss
    def Network_LoadBoss(self, data):
        self.running_normal = False

    def Network_Boss(self, data):
        # set lai vi tri cua cho x va y 
        print str(data["x"]) + " va " + str(data["y"])
        self.two_player.boss_obj.set_state(data["x"], data["y"], data["die_x"], data["die_y"])

    def Network_BossHP(self, data):
        self.two_player.boss_obj.set_HP(data["hp"])

if __name__ == "__main__":
    game = Game()
    game.menuGame() # run menu game
    pygame.quit()
    sys.exit()