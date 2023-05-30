import pygame

import gameplay_variables
import graphic_engine
import gameplay


pygame.init()
pygame.display.set_caption('Chess Openings Trainer: French Defense')
icon = pygame.image.load('piece_textures/res_128/black_king_128.png')
icon = pygame.transform.smoothscale(icon, (32, 32))
pygame.display.set_icon(icon)

graphic_engine.draw()
gameplay.load_next_line()
while gameplay_variables.run:
    pygame.time.Clock().tick(60)
    graphic_engine.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay_variables.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameplay.mouse_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

pygame.quit()
