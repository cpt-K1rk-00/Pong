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

	# Move function to move the player down to the edge
	def move_down():
		pass

	# Move function to move the player up to the edge
	def move_up():
		pass


def main():
	# Die Spieler erstellen
	player_1 = Player((255, 255, 255), 10, 100, (2, 0))
	player_2 = Player((255, 255, 255), 10, 100, (488,0))

	# Pygame-Mododule initialisieren
	# Fenster erstellend
	pygame.init()
	screen = pygame.display.set_mode((500, 350))

	# Titel des Fenster erstellen
	# Tastendrücke wiederholt senden
	# Mauszeiger unsichtbar machen
	pygame.display.set_caption("Pong")
	pygame.key.set_repeat(1, 30)
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

			# Die gedrückten Tasten bearbeiten
			if event.type == pygame.KEYDOWN:
				# Wenn Escape gedrückt wird, dann QUIT-Event versenden
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))

		# schwarzer Hintergrund
		screen.fill((0,0,0))

		# Die Spieler zeichnen
		screen.blit(player_1.image, player_1.rect)
		screen.blit(player_2.image, player_2.rect)

		pygame.display.flip()


if __name__ == "__main__":
	# Main-Funktion aufrufen
	main()