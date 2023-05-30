import pygame
import graphic_variables
import gameplay_variables
import gui


def draw_buttons():
    tile_size = graphic_variables.screen_resolution / 8
    pygame.draw.rect(graphic_variables.screen, (200, 50, 50),
                     [8 * tile_size + graphic_variables.transform_vector, 0 * tile_size + graphic_variables.transform_vector, tile_size + 1, tile_size + 1])


def draw_coordinates():
    tile_size = graphic_variables.screen_resolution / 8 * graphic_variables.board_size
    font = pygame.font.Font('font_coordinates.ttf', int(graphic_variables.screen_resolution / 40))
    for y in range(0, 8):
        text = chr(7 - y + 49)
        img = font.render(text, True, graphic_variables.colors[graphic_variables.using_color_id][0])
        txt_size = img.get_size()
        img.set_alpha(150)
        if graphic_variables.white_on_bottom:
            graphic_variables.screen.blit(img, (0.5 * (graphic_variables.transform_vector - txt_size[0]),
                        y * tile_size + 0.5 * (tile_size - txt_size[1]) + graphic_variables.transform_vector))

        else:
            graphic_variables.screen.blit(img, (0.5 * (graphic_variables.transform_vector - txt_size[0]),
                        (7 - y) * tile_size + 0.5 * (tile_size - txt_size[1]) + graphic_variables.transform_vector))

    for x in range(0, 8):
        text = chr(7 - x + 97)
        img = font.render(text, True, graphic_variables.colors[graphic_variables.using_color_id][0])
        txt_size = img.get_size()
        img.set_alpha(150)
        if graphic_variables.white_on_bottom:
            graphic_variables.screen.blit(img, ((7 - x) * tile_size + 0.5 * (tile_size - txt_size[0]) + graphic_variables.transform_vector,
                                                graphic_variables.screen_resolution - 0.7 * graphic_variables.transform_vector))
        else:
            graphic_variables.screen.blit(img, (x * tile_size + 0.5 * (tile_size - txt_size[0]) + graphic_variables.transform_vector,
                                                graphic_variables.screen_resolution - 0.9 * graphic_variables.transform_vector))


def draw_pieces():
    tile_size = graphic_variables.screen_resolution / 8 * graphic_variables.board_size
    for y in range(0, 8):
        for x in range(0, 8):
            if graphic_variables.white_on_bottom:
                if graphic_variables.board_to_display[y][x] != -1:
                    graphic_variables.screen.blit(
                        graphic_variables.piece_surfaces_128[graphic_variables.board_to_display[y][x]],
                        (x * tile_size + graphic_variables.transform_vector, y * tile_size + graphic_variables.transform_vector))
            else:
                if graphic_variables.board_to_display[y][x] != -1:
                    graphic_variables.screen.blit(
                        graphic_variables.piece_surfaces_128[graphic_variables.board_to_display[y][x]],
                        ((7 - x) * tile_size + graphic_variables.transform_vector, (7 - y) * tile_size + graphic_variables.transform_vector))

    if graphic_variables.buffered_piece != -1:
        graphic_variables.screen.blit(graphic_variables.piece_surfaces_128[graphic_variables.buffered_piece],
                                      (pygame.mouse.get_pos()[0] - tile_size / 2, pygame.mouse.get_pos()[1] - tile_size / 2))


def draw_board():
    tile_size = graphic_variables.screen_resolution / 8 * graphic_variables.board_size
    for y in range(0, 8):
        for x in range(0, 8):
            pygame.draw.rect(graphic_variables.screen, graphic_variables.colors[graphic_variables.using_color_id][(y + x) % 2],
                             [x * tile_size + graphic_variables.transform_vector, y * tile_size + graphic_variables.transform_vector, tile_size + 1, tile_size + 1])


def draw():
    graphic_variables.screen.fill(graphic_variables.colors[graphic_variables.using_color_id][2])
    draw_board()
    show_hint()
    draw_pieces()
    draw_coordinates()
    gui.draw_gui()
    pygame.display.flip()


def show_hint():
    if gameplay_variables.hint:
        tile_size = graphic_variables.screen_resolution / 8 * graphic_variables.board_size
        next_move = [gameplay_variables.target_line[gameplay_variables.move_number * 4],
                     gameplay_variables.target_line[gameplay_variables.move_number * 4 + 1]]
        x = ord(next_move[0]) - 97
        y = int(next_move[1]) - 1
        if graphic_variables.white_on_bottom:
            y = 7 - y
        else:
            x = 7 - x
        hint_color = [127, 127, 127]
        pygame.draw.rect(graphic_variables.screen, hint_color,
                         [x * tile_size + graphic_variables.transform_vector,
                          y * tile_size + graphic_variables.transform_vector, tile_size + 1, tile_size + 1])


def draw_correct():
    print('drawing correct icon')
    transform_vector = graphic_variables.screen_resolution / 8 * graphic_variables.board_size / 2
    graphic_variables.screen.blit(graphic_variables.correct_icon, (graphic_variables.screen_resolution / 2 - transform_vector, graphic_variables.screen_resolution / 2 - transform_vector))
    pygame.display.flip()
    pygame.time.delay(1000)
