"""
Essa é uma demonstração com linhas
"""

import pygame
import random
pygame.init()

# display settings
WIDTH = 500
HEIGHT = 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble sort visualization by magoninho")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = (255, 0, 0)

###################

heights = [random.randint(0, HEIGHT)
           for h in range(int(WIDTH))]  # todas as alturas para todas as linhas


# declarando o i e o j manualmente
i = 0
j = 0
# declarando os estados para serem as cores das linhas
states = [0 for s in range(int(WIDTH))]

ready = False

clock = pygame.time.Clock()
# game loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_SPACE:
                ready = True
    SCREEN.fill(BLACK)
    if ready:
        if i < len(heights):
            for j in range(len(heights) - i - 1):
                if heights[j] > heights[j + 1]:

                    states[j] = 0
                    states[j+1] = 0

                    # pra fazer o swap no python é só fazer uma declaração simultânea
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]

                else:
                    states[j] = 1
                    states[j + 1] = 1

        states[j] = 2
        states[j+1] = 2
        i += 1

    for line in range(len(heights)):
        # isso nao faz sentido, mas pelo menos deixa bonitinho e é isso que importa
        if states[line] == 0:
            color = (255, 255, 255)
        if states[line] == 1:
            color = (255, 0, 0)
        if states[line] == 2:
            color = (0, 255, 0)
        pygame.draw.line(SCREEN, color, (line, HEIGHT), (
            line, HEIGHT - heights[line]), 1)

    pygame.display.update()
