import pygame, sys

import sharedvars
import intro, mainmenu,map_load

def setState(state):
	sharedvars.state = state

def quit():
	pygame.quit()
	sys.exit(0)

if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
	clock = pygame.time.Clock()

	intro.init(screen)
	map_load.init(screen)
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
