import pygame
import sys
import time

# todo: -> personeles event um das Spiel zu beenden

class Player(pygame.sprite.Sprite):
	# Constructor. Pass the color of the Player and 
	# it's x and y position.
	def __init__(self, color, width, height, initial_position):
		# Calling the parent class constructors
		pygame.sprite.Sprite.__init__(self)
		# Create an image of the block and fill it with color.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_position
		self.speed = 1

	# Move function to move the player down to the edge
	def move_down(self):
		if self.rect.topleft[1] < 250:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + self.speed)

	# Move function to move the player up to the edge
	def move_up(self):
		if self.rect.topleft[1] > 0:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - self.speed)


class Ball(pygame.sprite.Sprite):
	# Constructor
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,10))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.topleft = (50,50)

		# Flag that shows wether the ball is in game or not
		self.shot = False
		# shows the state of ball (0, 1, 2, 3)
		self.state = 0

	def update_position(self):
		if self.state == 0:
			if self.rect.topleft[1] > 0:
				self.rect.topleft = (self.rect.topleft[0] + 1, self.rect.topleft[1] - 1)
			else:
				self.state = 1
		elif self.state == 1:
			if self.rect.topleft[1] < 340:
				self.rect.topleft = (self.rect.topleft[0] + 1, self.rect.topleft[1] + 1)
			else:
				self.state = 0
		elif self.state == 2:
			if self.rect.topleft[1] < 340:
				self.rect.topleft = (self.rect.topleft[0] - 1, self.rect.topleft[1] + 1)
			else:
				self.state = 3
		elif self.state == 3:
			if self.rect.topleft[1] > 0:
				self.rect.topleft = (self.rect.topleft[0] - 1, self.rect.topleft[1] - 1)
			else:
				self.state = 2

def display_text(message, screen, x=150, y=150):
	font = pygame.font.SysFont("arial", 25)
	text = font.render(message, True, (255, 255, 255))
	textrect = text.get_rect()
	textrect.topleft = (x,y)
	screen.blit(text, textrect)
	pygame.display.flip()

def main(score_1=0, score_2=0, attached_1=True, attached_2=False):
	# zähler - bei jedem fünften Frame wird der User-Input verarbeitet
	player_cnt = 0
	ball_cnt = 0

	# Die Spieler erstellen
	player_1 = Player((255, 255, 255), 10, 100, (2, 0))
	player_2 = Player((255, 255, 255), 10, 100, (488,0))

	# scores der Spieler
	score_spieler_1 = score_1
	score_spieler_2 = score_2

	# Den Ball erstellen
	ball = Ball(100, 100)

	# Pygame-Mododule initialisieren
	# Fenster erstellen
	pygame.init()
	screen = pygame.display.set_mode((500, 350))

	# Titel des Fenster erstellen
	# Mauszeiger unsichtbar machen
	pygame.display.set_caption("Pong")
	pygame.mouse.set_visible(0)

	# Clock Object für Framerate erstellen
	clock = pygame.time.Clock()

	#Schleife für das Spiel erstellen
	running = True
	ended = False
	ball_attached_player_1 = attached_1
	ball_attached_player_2 = attached_2

	# Score darstellen
	display_text(str(score_spieler_1), screen, 10, 10)
	display_text(str(score_spieler_2), screen, 470, 10)

	#check if game is ended
	if score_spieler_1 == 5 or score_spieler_2 == 5:
		ended = True

	if not ended:
		time.sleep(3)

	while running:
		# Events abarbeiten
		for event in pygame.event.get():
			# Spiel beenden bei Quit-Event
			if event.type == pygame.QUIT:
				running = False
				sys.exit(0)

		if not ended:
			# Bewegungen bearbeiten
			if player_cnt % 10 == 0:
				state =pygame.key.get_pressed()
				if state[pygame.K_w]:
					player_1.move_up()
				elif state[pygame.K_s]:
					player_1.move_down()
				if state[pygame.K_DOWN]:
					player_2.move_down()
				elif state[pygame.K_UP]:
					player_2.move_up()
				elif (ball_attached_player_1 or ball_attached_player_2) and state[pygame.K_SPACE]:
					ball_attached_player_1 = False
					ball_attached_player_2 = False

			if ball_cnt % 20 == 0 and not ball_attached_player_1 and not ball_attached_player_2:
				# to the collision detection
				if ball.rect.topleft[0] < 10 or ball.rect.topleft[0] > 488:
					# scores anpassen
					if ball.rect.topleft[0] < 10:
						score_spieler_2 += 1
						ball_attached_player_1 = True
					else:
						score_spieler_1 += 1
						ball_attached_player_2 = True
					running = False
				else:
					if player_2.rect.colliderect(ball.rect):
						if ball.state == 0:
							ball.state = 3
						elif ball.state == 1:
							ball.state = 2
					elif player_1.rect.colliderect(ball.rect):
						if ball.state == 2:
							ball.state = 1
						elif ball.state == 3:
							ball.state = 0

					ball.update_position()

			# schwarzer Hintergrund
			screen.fill((0,0,0))

			# Die Spieler & Ball zeichnen
			screen.blit(player_1.image, player_1.rect)
			screen.blit(player_2.image, player_2.rect)
			# die Position des Balls an den Spieler anpassen
			if ball_attached_player_1:
				ball.rect.topleft = (player_1.rect.topleft[0] + 12, player_1.rect.topleft[1] + 47)
			elif ball_attached_player_2:
				ball.rect.topleft = (player_2.rect.topleft[0] - 10, player_2.rect.topleft[1] + 47)
			screen.blit(ball.image, ball.rect)
			
			# den Zähler erhöhen
			player_cnt += 1
			ball_cnt += 1

			# Das Bild aktualisieren
			pygame.display.flip()
		else:
			# den Sieger ermitteln und ausgeben
			if score_spieler_1 == 5:
				display_text("Spieler 1 hat gewonnen", screen)
			else:
				display_text("Spieler 2 hat gewonnen", screen)
			# auf weiteren befehl warten
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						main()
					elif event.key == pygame.K_ESCAPE:
						sys.exit(0)					

	main(score_spieler_1, score_spieler_2, ball_attached_player_1, ball_attached_player_2)

if __name__ == "__main__":
	# Main-Funktion aufrufen
	main()