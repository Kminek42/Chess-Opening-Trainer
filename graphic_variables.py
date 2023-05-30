import pygame


screen_resolution = 600
screen = pygame.display.set_mode((screen_resolution * 1.5, screen_resolution))
board_size = 0.925

correct_icon = pygame.image.load('correct.png')
correct_icon = pygame.transform.smoothscale(correct_icon, (screen_resolution / 8 * board_size, screen_resolution / 8 * board_size))

piece_surfaces_128 = [pygame.image.load('piece_textures/res_128/white_king_128.png'),  # 0
                      pygame.image.load('piece_textures/res_128/white_queen_128.png'),  # 1
                      pygame.image.load('piece_textures/res_128/white_rook_128.png'),  # 2
                      pygame.image.load('piece_textures/res_128/white_bishop_128.png'),  # 3
                      pygame.image.load('piece_textures/res_128/white_knight_128.png'),  # 4
                      pygame.image.load('piece_textures/res_128/white_pawn_128.png'),  # 5
                      pygame.image.load('piece_textures/res_128/black_king_128.png'),  # 6
                      pygame.image.load('piece_textures/res_128/black_queen_128.png'),  # 7
                      pygame.image.load('piece_textures/res_128/black_rook_128.png'),  # 8
                      pygame.image.load('piece_textures/res_128/black_bishop_128.png'),  # 9
                      pygame.image.load('piece_textures/res_128/black_knight_128.png'),  # 10
                      pygame.image.load('piece_textures/res_128/black_pawn_128.png')]  # 11

for i in range(0, 12):
    piece_surfaces_128[i] = pygame.transform.smoothscale(piece_surfaces_128[i],
                                                         (screen_resolution / 8 * board_size,
                                                          screen_resolution / 8 * board_size))

white_on_bottom = False
show_coordinates = True
text_color = (200, 200, 200, 200)
board_colors = [[200, 200, 200], [100, 75, 50]]
using_color_id = 0
# colors [text, dark_squares, background, buttons]
colors = [[240, 210, 144], [222, 131, 77], [163, 66, 60], [120, 29, 66]], \
         [[224, 192, 151], [184, 92, 56], [92, 61, 46], [45, 36, 36]], \
         [[236, 219, 186], [200, 75, 49], [45, 66, 99], [25, 25, 25]], \
         [[237, 237, 237], [218, 0, 55], [68, 68, 68], [23, 23, 23]], \
         [[245, 198, 165], [255, 119, 119], [162, 65, 107], [133, 39, 71]], \
         [[233, 166, 166], [134, 72, 121], [63, 51, 81], [31, 29, 54]], \
         [[219, 216, 227], [92, 84, 112], [53, 47, 68], [42, 36, 56]], \
         [[238, 238, 238], [0, 173, 181], [58, 71, 80], [48, 56, 65]], \
         [[164, 180, 148], [81, 152, 114], [59, 82, 73], [56, 41, 51]], \
         [[216, 233, 168], [78, 159, 61], [30, 81, 40], [25, 26, 25]], \
         [[239, 239, 239], [255, 192, 105], [164, 93, 93], [74, 64, 58]], \

show_colors = False
background_color = []
darker_background_color = []
for i in range(0, len(board_colors[1])):
    background_color.append(0.25 * board_colors[1][i] + 50)
    darker_background_color.append((background_color[i] + 50) * 0.5)

board_to_display = [[8, 10, 9, 7, 6, 9, 10, 8],
                    [11, 11, 11, 11, 11, 11, 11, 11],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [2, 4, 3, 1, 0, 3, 4, 2]]


buffered_piece = -1

transform_vector = 0.5 * screen_resolution * (1 - board_size)
