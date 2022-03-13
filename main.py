
import pygame
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu inédit")


PINK = (255, 225, 255)

FPS = 60


def draw_window():
    WIN.fill(PINK)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
