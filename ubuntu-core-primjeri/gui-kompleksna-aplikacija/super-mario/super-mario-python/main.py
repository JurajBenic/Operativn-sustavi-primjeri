import os
import pygame

# Use project root as working directory so legacy relative paths like
# "./sprites/..." and "./img/..." continue to work inside a snap.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario


windowSize = 640, 480


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    try:
        # Keep the original 640x480 game coordinates and scale to fullscreen output.
        screen = pygame.display.set_mode(windowSize, pygame.FULLSCREEN | pygame.SCALED)
    except pygame.error:
        # Fallback if the backend does not support SCALED with fullscreen.
        screen = pygame.display.set_mode(windowSize, pygame.FULLSCREEN)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption("Super Mario running with {:d} FPS".format(int(clock.get_fps())))
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()
