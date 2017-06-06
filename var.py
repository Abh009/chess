'''
variables are used in func.py
'''
import chess


# The variables


board = chess.Board()

game_status = True
current_move = None
current_color = "WHITE"
game_over_reason = None
white_move_count = 0
black_move_count = 0
white_time_remaining = 360 # 6 minutes
black_time_remaining = 300 # 5 minutes
