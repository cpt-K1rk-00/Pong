import pygame

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


def main():
	# zähler - bei jedem fünften Frame wird der User-Input verarbeitet
	cnt = 0

	# Die Spieler erstellen
	player_1 = Player((255, 255, 255), 10, 100, (2, 0))
	player_2 = Player((255, 255, 255), 10, 100, (488,0))

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
	while running:
		# Events abarbeiten
		for event in pygame.event.get():
			# Spiel beenden bei Quit-Event
			if event.type == pygame.QUIT:
				running = False

		# Bewegungen bearbeiten
		if cnt % 10 == 0:
			state =pygame.key.get_pressed()
			if state[pygame.K_w]:
				player_1.move_up()
			elif state[pygame.K_s]:
				player_1.move_down()
			if state[pygame.K_DOWN]:
				player_2.move_down()
			elif state[pygame.K_UP]:
				player_2.move_up()


		# schwarzer Hintergrund
		screen.fill((0,0,0))

		# Die Spieler zeichnen
		screen.blit(player_1.image, player_1.rect)
		screen.blit(player_2.image, player_2.rect)

		# den Zähler erhöhen
		cnt += 1

		# Das Bild aktualisieren
		pygame.display.flip()


if __name__ == "__main__":
	# Main-Funktion aufrufen
	main()