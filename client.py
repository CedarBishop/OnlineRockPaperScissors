import pygame
from network import Network
from helper import *
from player import Player

w = 500
h = 500

window = pygame.display.set_mode((w, h))
pygame.display.set_caption("Client")


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_player()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(window, p, p2)


main()
