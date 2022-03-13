
import pygame


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.quit():
                running = False

    pygame.quit()
