import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}")
    print(f"""
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}
        """)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

while running:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting...")
            running = False

    screen.fill("black")
    pygame.display.flip()

if __name__ == "__main__":
    main()
