from tiles import *
import pygame

pygame.init()

w = 600
h = 600

window = pygame.display.set_mode((w, h))

white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
blue = (0, 0, 255)

purple = (138,43,226)
grey = (169,169,169)
black = (0, 0, 0)

tile = Tiles(w, h, window, white, grey, red, orange, yellow, green, blue, purple, black)
tile_map = tile.create_map()
bar_ys = [20, 50, 80, 110, 140, 170]
radius = 10


def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick()
        tile.draw_tiles()
        tile.draw()

        pygame.display.update()

main()