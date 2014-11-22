import pygame, sys
import sharedvars

import intro, mainmenu

screen = None

def quit():
	pygame.quit()
	sys.exit(0)

if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((1280, 720), pygame.SRC_ALPHA)
	clock = pygame.time.Clock()

	intro.init(screen)
	mainmenu.init(screen)
	sharedvars.state = intro

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			else:
				sharedvars.state.onEvent(event)

		ms = clock.tick(sharedvars.fps)
		
		sharedvars.state.draw(screen, ms)
		pygame.display.flip()
