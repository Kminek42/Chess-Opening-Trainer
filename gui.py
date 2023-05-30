import pygame

import gameplay_variables
import graphic_variables


def click_on_gui(position_x, position_y):
    tile_size = graphic_variables.screen_resolution / 12 * graphic_variables.board_size
    position_y -= graphic_variables.transform_vector

    if graphic_variables.show_colors:
        y = position_y - (graphic_variables.transform_vector + (0.5 * (-1) + 5.125) * tile_size)
        if y >= 0:
            y = int(y / tile_size * 2)
            if 0 <= y < len(graphic_variables.colors):
                graphic_variables.using_color_id = y

    if tile_size <= position_y <= 2 * tile_size:
        gameplay_variables.hint = True

    elif 2 * tile_size < position_y <= 3 * tile_size:
        gameplay_variables.attempts = 0
        gameplay_variables.correct_attempts = 0

    elif 3 * tile_size < position_y <= 4 * tile_size:
        gameplay_variables.max_moves += 1
        if gameplay_variables.max_moves > 8:
            gameplay_variables.max_moves = 4
        print('depth:', gameplay_variables.max_moves)

    elif 4 * tile_size < position_y <= 5 * tile_size:
        graphic_variables.show_colors = True


def draw_gui():
    draw_main_texts()
    draw_available_colors()


def draw_main_texts():
    tile_size = graphic_variables.screen_resolution / 12 * graphic_variables.board_size
    font = pygame.font.Font('font_texts.ttf', int(graphic_variables.screen_resolution / 25))
    texts = ['Accuracy: ', 'Hint', 'Reset Accuracy', 'Lines depth: ', 'Change Color']
    for i in range(0, 5):
        background_rect = (graphic_variables.screen_resolution, graphic_variables.transform_vector + i * tile_size, graphic_variables.screen_resolution * 0.5 - graphic_variables.transform_vector, tile_size * 0.9)
        pygame.draw.rect(graphic_variables.screen, graphic_variables.colors[graphic_variables.using_color_id][3], background_rect, 0, int(graphic_variables.screen_resolution * graphic_variables.board_size / 100))

        text = texts[i]
        if i == 0:
            if gameplay_variables.attempts != 0:
                text += str(int(gameplay_variables.correct_attempts / gameplay_variables.attempts * 100))
                text += '%'
            else:
                text += '0%'
        if i == 3:
            if gameplay_variables.max_moves == 8:
                text += 'unlimited'
            else:
                text += str(gameplay_variables.max_moves)

        img = font.render(text, True, (255, 255, 255))
        img.set_alpha(220)
        graphic_variables.screen.blit(img, (graphic_variables.screen_resolution + 0.5 * graphic_variables.transform_vector, graphic_variables.transform_vector + (0.15 + i) * tile_size))


def draw_available_colors():
    if graphic_variables.show_colors:
        tile_size = graphic_variables.screen_resolution * graphic_variables.board_size / 12
        background_rect = (graphic_variables.screen_resolution, graphic_variables.transform_vector + 5 * tile_size,
                           graphic_variables.screen_resolution * 0.5 - graphic_variables.transform_vector,
                           tile_size * 5.65)
        pygame.draw.rect(graphic_variables.screen, graphic_variables.colors[graphic_variables.using_color_id][3], background_rect, 0,
                         int(graphic_variables.screen_resolution * graphic_variables.board_size / 100))

        color_bars_translation = graphic_variables.screen_resolution / 120
        for i in range(0, len(graphic_variables.colors)):
            background_rect = (graphic_variables.screen_resolution + color_bars_translation, graphic_variables.transform_vector + (0.5 * i + 5.125) * tile_size, graphic_variables.screen_resolution * 0.5 - graphic_variables.transform_vector - 2 * color_bars_translation, tile_size * 0.4)
            pygame.draw.rect(graphic_variables.screen, graphic_variables.colors[i][1], background_rect, 0, int(graphic_variables.screen_resolution * graphic_variables.board_size / 100))
