#Chutes and Ladders Simulator
import pygame, sys, random, math

#game constants
WIN_WIDTH = 800
WIN_HEIGHT = 550
FPS = 30
ROWS = 10
MARGIN = 20
SQ_SIZE = int(WIN_WIDTH*0.618/ROWS)
FNT_OS = 5

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OCC_COLOR = (0, 0, 255)

#init game
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Chutes and Ladders Simulator")
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 14)
big_font = pygame.font.Font('freesansbold.ttf', 72)
super_big_font = pygame.font.Font('freesansbold.ttf', 144)

#game vars
squares = []

class Player():
	def __init__(self):
		self.turns = 0
		self.pos = 0
	
	def move(self):
		if self.pos < 100:
			n = random.randint(1, 6)
			self.turns += 1
			if self.pos + n <= 100:
				squares[self.pos-1].occ = False
				self.pos += n
				squares[self.pos-1].occ = True
		

class Space():
	def __init__(self, n):
		self.n = n
		self.occ = False
		self.x = 0
		self.y = 0
		
	def draw(self):
		if self.occ:
			pygame.draw.rect(screen, OCC_COLOR, (self.x, self.y, SQ_SIZE, SQ_SIZE))
			text_surf = font.render(str(self.n), True, WHITE)
			screen.blit(text_surf, (self.x+FNT_OS, self.y+FNT_OS, SQ_SIZE, SQ_SIZE))
		else:
			pygame.draw.rect(screen, BLACK, (self.x, self.y, SQ_SIZE, SQ_SIZE), 3)
			text_surf = font.render(str(self.n), True, BLACK)
			screen.blit(text_surf, (self.x+FNT_OS, self.y+FNT_OS, SQ_SIZE, SQ_SIZE))
	
class Portal():
	def __init__(self, start, stop):
		self.start = start
		self.stop = stop
		
	def ride(self, player):
		if player.pos == self.start:
			player.pos = self.stop

def create_squares():
	for i in range(ROWS*ROWS):
		squares.append(Space(i+1))

def draw_board():
	n = 100
	for i in range(ROWS):
		for j in range(ROWS):
			squares[n-1].n = n
			squares[n-1].x = j*SQ_SIZE+MARGIN
			squares[n-1].y = i*SQ_SIZE+MARGIN
			squares[n-1].draw()
			if n % 20 > 11 or n % 20 == 0:
				n -= 1
			elif n % 20 == 11:
				n -= 10
			elif n % 20 == 10:
				n -= 10
			elif n % 20 < 11:
				n += 1

create_squares()
player_one = Player()
player_two = Player()
players = [player_one, player_two]
ladder_one = Portal(13, 56)
chute_one = Portal(50, 4)

portals = []
portals.append(Portal(80, 100))
portals.append(Portal(98, 78))
portals.append(Portal(95, 75))
portals.append(Portal(93, 73))
portals.append(Portal(71, 91))
portals.append(Portal(87, 24))
portals.append(Portal(64, 60))
portals.append(Portal(62, 19))
portals.append(Portal(56, 53))
portals.append(Portal(51, 67))
portals.append(Portal(21, 42))
portals.append(Portal(1, 38))
portals.append(Portal(36, 44))
portals.append(Portal(28, 84))
portals.append(Portal(4, 14))
portals.append(Portal(48, 26))
portals.append(Portal(49, 11))
portals.append(Portal(9, 31))

def check_portals(port, play):
	result = False
	for portal in port:
		for player in play:
			if portal.start == player.pos:
				squares[player.pos-1].occ = False
				portal.ride(player)
				result = True
	return result

#game loop
while True:
	screen.fill(WHITE)
	draw_board()
	
	text_surf = big_font.render(str(player_one.turns), True, BLACK)
	screen.blit(text_surf, (SQ_SIZE*10+MARGIN+FNT_OS, MARGIN+FNT_OS, WIN_WIDTH-SQ_SIZE*10+MARGIN, WIN_HEIGHT-MARGIN))
	
	if not check_portals(portals, players):
		player_one.move()
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	
	pygame.display.update()
	clock.tick(FPS)
