move_number = 0  # index of the move in the current line
attempts = 0
correct_attempts = 0
line = ''  # current line
line_id = 0
candidate_line = ''
target_line = ''
filename = 'openings/lines_black_french_defense.txt'
lines = open(filename).readlines()  # lines in the database
run = True
move = ''
hint = False
max_moves = 3
