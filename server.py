import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

import constant, random

class ClientChannel(PodSixNet.Channel.Channel):
	# nhan toa. do. cua xe tang client 
	def Network_tank(self, data):
		tank_x = data["x"]
		tank_y = data["y"]
		tank_facing = data["face"]
		tank_id = data["id"]
		self._server.sendTank(tank_x, tank_y, tank_facing, tank_id)

	def Network_bullet(self, data):
		self._server.sendBullet(data["x"], data["y"], data["face"], data["id"])

	def Network_HP(self, data):
		self._server.sendHP(data["hp"], data["id"])

	def Network_EnemyNumber(self, data):
		self._server.sendEnemyNumber(data["id"])

	def Network_Boss(self, data):
		self._server.sendBossPosition(data["id"])

	def Network_tankBoss(self, data):
		tank_x = data["x"]
		tank_y = data["y"]
		tank_facing = data["face"]
		tank_id = data["id"]
		self._server.sendTankBoss(tank_x, tank_y, tank_facing, tank_id)

	def Network_BossHP(self, data):
		id = data["id"]
		self._server.sendBossHP(id)


class TankServer(PodSixNet.Server.Server):
	channelClass = ClientChannel

	# tham so cua server de? tao socket
	def __init__(self, *args, **kwargs):
		PodSixNet.Server.Server.__init__(self, *args, **kwargs)
		# the number of player
		self.index_player = 0 # luc dau chua co nguoi 
		self.game = None # object chua' game chinh' cua server
		self.is_client_waiting = True # khi chi? co 1 nguoi choi 1 send True cho 1 client, khi 2 nguoi choi thi send False cho 2 client
		self.map_normal = False
		self.map_boss = False
		self.enemy_number = 10
		self.boss_HP = 20

	# goi khi co new cllient ket noi den server 
	def Connected(self, channel, addr):
		print 'new connection: ' + str(addr)

		if self.index_player == 0: # neu chua co ai ket noi' thi` nguoi ket noi la nguoi dau` tien, nen^ ta tao. game 
			self.game = Game(channel, self.index_player) # tao game va` luu channel(nguoi choi 1) va ID (so thu' tu nguoi choi 1) vao game 
			self.is_client_waiting = True 
		else:   # neu da~ co nguoi choi thi` them^ nguoi` choi thu 2 vao game hien co'
			print 'hello new Player ' + str(self.index_player)
			self.game.player.append(channel)
			self.is_client_waiting = False
			self.map_normal = True # load man 1 

		# gui trang. thai' dc choi hay ko dc choi de? client biet' bat' dau choi chua
		for client in self.game.player:
			client.Send({"action" : "Waiting", "waiting" : self.is_client_waiting})

		# khi co' nguoi ket noi thi send ID cho nguoi choi
		self.game.player[self.index_player].Send({"action" : "IndexPlayer", "index_player" : self.index_player})

		self.index_player += 1

	def sendTank(self, tank_x, tank_y, tank_facing, tank_id):
		self.game.sendTank(tank_x, tank_y, tank_facing, tank_id)

	def sendTankBoss(self, tank_x, tank_y, tank_facing, tank_id):
		self.game.sendTankBoss(tank_x, tank_y, tank_facing, tank_id)

	def sendPowerBox(self, x, y):
		self.game.sendPowerBox(x, y) 

	def sendBullet(self, x, y, face, id):
		self.game.sendBullet(x, y, face, id)

	def sendEnemy(self, x_pos, y_pos, x_pos_snake, y_pos_snake, x, y, time, die):
		self.game.sendEnemy(x_pos, y_pos, x_pos_snake, y_pos_snake, x, y, time, die)

	def sendHP(self, hp, id):
		self.game.sendHP(hp, id)

	def sendEnemyNumber(self, id):
		if id == 0: # chi? tru` so' luong enemy khi la` nguoi choi thu' 0 
			self.enemy_number -= 1
			self.game.sendEnemyNumber(id, self.enemy_number)

	def loadBoss(self):
		self.game.loadBoss()

	def sendBossPosition(self, id):
		self.game.sendBossPosition(id)

	def sendBossHP(self, id):
		self.boss_HP -= 1
		self.game.sendBossHP(id, self.boss_HP)


class Game():
	def __init__(self, channel, index_player):
		print 'hello new Player ' + str(index_player)

		self.index_player = index_player
		self.player = [] # chua' nguoi choi
		self.player.append(channel) # lua nguoi choi thu' 1 vao` game

	# ham` xu? ly' toa. do. x,y cua cua chiec xe tank do client gui? len
	def sendTank(self, tank_x, tank_y, tank_facing, tank_id):
		if tank_id == 0:
			self.player[1].Send({"action" : "OtherPlayer", "x" : tank_x, "y" : tank_y, "facing" : tank_facing, "id" : tank_id})
		elif tank_id == 1:
			self.player[0].Send({"action" : "OtherPlayer", "x" : tank_x, "y" : tank_y, "facing" : tank_facing, "id" : tank_id})

	# gui toa. do cho client khac'
	def sendTankBoss(self, tank_x, tank_y, tank_facing, tank_id):
		if tank_id == 0:
			self.player[1].Send({"action" : "OtherPlayerBoss", "x" : tank_x, "y" : tank_y, "facing" : tank_facing, "id" : tank_id})
		elif tank_id == 1:
			self.player[0].Send({"action" : "OtherPlayerBoss", "x" : tank_x, "y" : tank_y, "facing" : tank_facing, "id" : tank_id})

	# gui client vi tri item box
	def sendPowerBox(self, x, y):
		for player in self.player:
			player.Send({"action" : "PowerBox", "x" : x, "y" : y})

	# gui toa do dan. cho client
	def sendBullet(self, x, y, face, id):
		if id == 0:
			self.player[1].Send({"action" : "Bullet", "x" : x, "y" : y, "face" : face, "id" : id})
		elif id == 1:
			self.player[0].Send({"action" : "Bullet", "x" : x, "y" : y, "face" : face, "id" : id})

	# tao enemy
	def sendEnemy(self, x_pos, y_pos, x_pos_snake, y_pos_snake, x, y, time, die):
		for player in self.player:
			player.Send({"action" : "Enemy", "x_pos" : x_pos, "y_pos" : y_pos, "x_pos_snake" : x_pos_snake, "y_pos_snake" : y_pos_snake, "x" : x, "y" : y, "time" : time, "die" : die})

	# gui HP cua client
	def sendHP(self, hp, id):
		if id == 0:
			self.player[1].Send({"action" : "HP", "hp" : hp, "id" : id})
		elif id == 1:
			self.player[0].Send({"action" : "HP", "hp" : hp, "id" : id})

	# gui client so luong quai tren man hinh
	def sendEnemyNumber(self, id, enemy_number):
		for player in self.player:
			player.Send({"action" : "EnemyNumber", "id" : id, "enemy_number" : enemy_number})

	# bao cho client biet' la` load man` boss
	def loadBoss(self):
		for player in self.player:
			player.Send({"action" : "LoadBoss", "running" : True})

	# send cho client vi tri va huong' cua? boss
	def sendBossPosition(self, id):
		x = random.randint(0, constant.SCREEN_WIDTH_BOSS - 100)
		y = random.randint(0, constant.SCREEN_WIDTH_BOSS - 100)
		die_x = random.choice([1, -1])
		die_y = random.choice([1, -1])
		if id == 0: # cap nhat vi tri' chi? dua. vao du~ lieu. cua nguoi choi thu' 1
			for player in self.player:
				player.Send({"action" : "Boss", "x" : x, "y" : y, "die_x" : die_x, "die_y" : die_y})

	# send HP cua boss cho 2 ben biet
	def sendBossHP(self, id, hp):
		for player in self.player:
			player.Send({"action" : "BossHP", "hp" : hp})



print "STARTING SERVER ON LOCAL HOST"
# try:
address = raw_input("Host:Port (localhost:8000): ")
if not address:
    host, port="localhost", 8000
else:
    host,port=address.split(":")
tankServer = TankServer(localaddr=(host, int(port))) # tao socket dua. vao IP va Port ta nhap vao 

power_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX) # thoi gian xuat hien vat pham tang toc' cho xe tang
enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX) 

while True:
	tankServer.Pump()
	# khi thoi gian tao vat pham da het thi gui? client tin' hieu. tao vat pham
	if tankServer.map_normal:
		enemy_interval -= 1
		power_interval -= 1
		if power_interval <= 0:
			tankServer.sendPowerBox(random.randint(0, constant.SCREEN_WIDTH), random.randint(0, constant.SCREEN_HEIGHT))
			power_interval = random.randint(constant.HEALTH_MIN, constant.HEALTH_MAX) # thoi gian xuat hien vat pham tang toc' cho xe tang
		if enemy_interval <= 0:
			direction = ('n', 'e', 's', 'w')
			tankServer.sendEnemy(random.randint(0, constant.SCREEN_WIDTH), random.randint(0, constant.SCREEN_HEIGHT), random.randint(0, constant.SCREEN_WIDTH), random.randint(0, constant.SCREEN_HEIGHT), random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX), random.randint(constant.ENEMY_SPEED_MIN, constant.ENEMY_SPEED_MAX), random.randint(constant.ENEMY_MIN_BULLET_SPEED, constant.ENEMY_MAX_BULLET_SPEED), direction[random.randint(0, 3)] )
			enemy_interval = random.randint(constant.ENEMY_MIN, constant.ENEMY_MAX) 

		if tankServer.enemy_number <= 0:
			tankServer.enemy_number = 0
			tankServer.map_normal = False
			tankServer.map_boss = True
			# bao' hieu. client biet' la load map boss
			tankServer.loadBoss()

	if tankServer.map_boss:
		# 2 thiet bi dang chay map boss
		x = 0

	sleep(0.01)
