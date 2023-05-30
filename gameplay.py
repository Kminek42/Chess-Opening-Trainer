import random

import pygame.time

import gameplay_variables
import graphic_engine
import graphic_variables
import gameplay_variables
import gui


def load_next_line():
    gameplay_variables.move_number = 0
    gameplay_variables.move = ''
    gameplay_variables.line = ''
    gameplay_variables.candidate_line = ''
    gameplay_variables.target_line = ''
    graphic_variables.board_to_display = board_to_display = [[8, 10, 9, 7, 6, 9, 10, 8],
                    [11, 11, 11, 11, 11, 11, 11, 11],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1],
                    [5, 5, 5, 5, 5, 5, 5, 5],
                    [2, 4, 3, 1, 0, 3, 4, 2]]
    gameplay_variables.line_id = random.randrange(0, len(gameplay_variables.lines))
    gameplay_variables.target_line = gameplay_variables.lines[gameplay_variables.line_id]
    if not graphic_variables.white_on_bottom:
        load_next_move()


def reset_line():
    gameplay_variables.move_number = 0
    gameplay_variables.move = ''
    gameplay_variables.line = ''
    gameplay_variables.candidate_line = ''
    gameplay_variables.target_line = ''
    graphic_variables.board_to_display = board_to_display = [[8, 10, 9, 7, 6, 9, 10, 8],
                                                             [11, 11, 11, 11, 11, 11, 11, 11],
                                                             [-1, -1, -1, -1, -1, -1, -1, -1],
                                                             [-1, -1, -1, -1, -1, -1, -1, -1],
                                                             [-1, -1, -1, -1, -1, -1, -1, -1],
                                                             [-1, -1, -1, -1, -1, -1, -1, -1],
                                                             [5, 5, 5, 5, 5, 5, 5, 5],
                                                             [2, 4, 3, 1, 0, 3, 4, 2]]
    gameplay_variables.target_line = gameplay_variables.lines[gameplay_variables.line_id]
    load_next_move()


def load_next_move():
    gameplay_variables.move_number += 1
    temp = gameplay_variables.max_moves
    if temp == 8:
        temp = 99

    if len(gameplay_variables.line) + 4 >= len(gameplay_variables.target_line) or len(gameplay_variables.line) + 4 >= temp * 4 * 2:
        graphic_engine.draw()
        graphic_engine.draw_correct()
        load_next_line()
    else:
        gameplay_variables.move = gameplay_variables.target_line[len(gameplay_variables.line)]
        gameplay_variables.move += gameplay_variables.target_line[len(gameplay_variables.line) + 1]
        gameplay_variables.move += gameplay_variables.target_line[len(gameplay_variables.line) + 2]
        gameplay_variables.move += gameplay_variables.target_line[len(gameplay_variables.line) + 3]
        gameplay_variables.candidate_line += gameplay_variables.move
        gameplay_variables.line += gameplay_variables.move

        if gameplay_variables.move == 'e1g1':
            graphic_variables.board_to_display[7][4] = -1
            graphic_variables.board_to_display[7][5] = 2
            graphic_variables.board_to_display[7][6] = 0
            graphic_variables.board_to_display[7][7] = -1

        elif gameplay_variables.move == 'e1c1':
            graphic_variables.board_to_display[7][0] = -1
            graphic_variables.board_to_display[7][1] = -1
            graphic_variables.board_to_display[7][2] = 0
            graphic_variables.board_to_display[7][3] = 2
            graphic_variables.board_to_display[7][4] = -1

        elif gameplay_variables.move == 'e8g8':
            graphic_variables.board_to_display[0][4] = -1
            graphic_variables.board_to_display[0][5] = 8
            graphic_variables.board_to_display[0][6] = 6
            graphic_variables.board_to_display[0][7] = -1

        elif gameplay_variables.move == 'e8c8':
            graphic_variables.board_to_display[0][0] = -1
            graphic_variables.board_to_display[0][1] = -1
            graphic_variables.board_to_display[0][2] = 6
            graphic_variables.board_to_display[0][3] = 8
            graphic_variables.board_to_display[0][4] = -1

        else:
            temp_piece = graphic_variables.board_to_display[48 + 8 - ord(gameplay_variables.move[1])][ord(gameplay_variables.move[0]) - 97]
            graphic_variables.board_to_display[48 + 8 - ord(gameplay_variables.move[3])][ord(gameplay_variables.move[2]) - 97] = temp_piece
            graphic_variables.board_to_display[48 + 8 - ord(gameplay_variables.move[1])][ord(gameplay_variables.move[0]) - 97] = -1


def compare_lines():
    gameplay_variables.attempts += 1
    matching = True
    for i in range(0, len(gameplay_variables.candidate_line)):
        if gameplay_variables.candidate_line[i] != gameplay_variables.target_line[i]:
            matching = False
    if matching:
        gameplay_variables.correct_attempts += 1
        gameplay_variables.line = gameplay_variables.candidate_line
        gameplay_variables.move_number += 1
        load_next_move()
    else:
        temp = gameplay_variables.move_number
        reset_line()
        for i in range(0, temp - 1):
            load_next_move()


def update_line():
    gameplay_variables.candidate_line += gameplay_variables.move


def make_move(position_x, position_y):
    if graphic_variables.buffered_piece == -1:  # if first click
        # show board
        graphic_variables.buffered_piece = graphic_variables.board_to_display[position_y][position_x]
        graphic_variables.board_to_display[position_y][position_x] = -1
        # store move
        gameplay_variables.move = chr(position_x + ord('a')) + str(8 - position_y)
    else:  # if second click
        # show board
        graphic_variables.board_to_display[position_y][position_x] = graphic_variables.buffered_piece
        # store move
        gameplay_variables.move += chr(position_x + ord('a')) + str(8 - position_y)
        if gameplay_variables.move == 'e1g1':
            graphic_variables.board_to_display[7][4] = -1
            graphic_variables.board_to_display[7][5] = 2
            graphic_variables.board_to_display[7][6] = 0
            graphic_variables.board_to_display[7][7] = -1

        if gameplay_variables.move == 'e1c1':
            graphic_variables.board_to_display[7][0] = -1
            graphic_variables.board_to_display[7][1] = -1
            graphic_variables.board_to_display[7][2] = 0
            graphic_variables.board_to_display[7][3] = 2
            graphic_variables.board_to_display[7][4] = -1

        if gameplay_variables.move == 'e8g8':
            graphic_variables.board_to_display[0][4] = -1
            graphic_variables.board_to_display[0][5] = 8
            graphic_variables.board_to_display[0][6] = 6
            graphic_variables.board_to_display[0][7] = -1

        if gameplay_variables.move == 'e8c8':
            graphic_variables.board_to_display[0][0] = -1
            graphic_variables.board_to_display[0][1] = -1
            graphic_variables.board_to_display[0][2] = 6
            graphic_variables.board_to_display[0][3] = 8
            graphic_variables.board_to_display[0][4] = -1
        graphic_variables.buffered_piece = -1

        if gameplay_variables.move[0] == gameplay_variables.move[2] and gameplay_variables.move[1] == gameplay_variables.move[3]:
            gameplay_variables.move = []
        else:
            update_line()
            compare_lines()


def click_on_board(position_x, position_y):
    graphic_variables.show_colors = False
    gameplay_variables.hint = False
    position_x = (position_x - graphic_variables.transform_vector) / graphic_variables.board_size
    position_y = (position_y - graphic_variables.transform_vector) / graphic_variables.board_size
    position_x = int(position_x / graphic_variables.screen_resolution * 8)
    position_y = int(position_y / graphic_variables.screen_resolution * 8)

    if not graphic_variables.white_on_bottom:
        position_x = 7 - position_x
        position_y = 7 - position_y

    make_move(position_x, position_y)


def mouse_click(position_x, position_y):
    if graphic_variables.transform_vector < position_x < graphic_variables.screen_resolution - graphic_variables.transform_vector and graphic_variables.transform_vector < position_y < graphic_variables.screen_resolution - graphic_variables.transform_vector:
        click_on_board(position_x, position_y)
    else:
        gui.click_on_gui(position_x, position_y)
