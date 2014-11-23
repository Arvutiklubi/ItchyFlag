import pygame, sys

import sharedvars
import intro, mainmenu, map_load, in_game_menu

initializedStates = []

screen = None

def initState(state):
        global screen
        if not state in initializedStates:
                state.init(screen)
                initializedStates.append(state)
                
def setState(state):
        initState(state)
        sharedvars.state = state

def quit():
        pygame.quit()
        sys.exit(0)

if __name__ == '__main__':
        pygame.init()

        global screen
        screen = pygame.display.set_mode((1280, 720), pygame.SRCALPHA)
        clock = pygame.time.Clock()

        initState(mainmenu)
        setState(intro)

        if mainmenu.fullscreen == "True":
                screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                fail = open("config.txt", "w")
                                fail.write("fullscreen="+ mainmenu.fullscreen)
                                fail.close()
                                quit()
                        else:
                                sharedvars.state.onEvent(event)

                ms = clock.tick(sharedvars.fps)

                print(screen)
                sharedvars.state.draw(screen, ms)
                pygame.display.flip()

