'''
variables defined in var.py
'''
import chess
import time
import thread
import var

# the functions


def show_board():
    print "a b c d e f g h \n"
    print var.board

def format_time(color):
    while(1):
        if color == "WHITE":
            second = var.white_time_remaining % 60
            minute = var.white_time_remaining / 60
            print "("+ str(minute) + ":" + str(second) + ")"
            var.white_time_remaining -= 1              
            time.sleep(1)
        else:
            second = var.black_time_remaining % 60
            minute = var.black_time_remaining / 60
            print "("+ str(minute) + ":" + str(second) + ")"
            var.black_time_remaining -= 1              
            time.sleep(1)

def read_move(color):
    if color == chess.WHITE:
        var.current_color = "WHITE"
    else:
        var.current_color = "BLACK"
    prompt = " Your Move: " + "(" + var.current_color + ")"
    var.current_move = raw_input(prompt)

def make_move(color):
    try:
        var.board.push_san(var.current_move)
    except:
        print("Invalid Move")
        read_move(color)
        make_move(color)

def check():
    if var.board.is_check():
        print "\n CHECK "



def show_result():
    print var.board
    print "---------------------------- GAME OVER ---------------------------------"
    print "|\t\t\t\t\t" + var.current_color + " WINS \t\t\t\t\t\t|"
    print "|\t\t\t\t\t" + var.game_over_reason + "\t\t\t\t\t\t|"
    print "|\t\t\t\t\t black moves : " ,var.black_move_count ,"\t\t\t\t\t\t|"
    print "|\t\t\t\t\t white moves : " ,var.white_move_count ,"\t\t\t\t\t\t|"
    print "-----------------------------------------------------------------------"

def is_over():
    gameover = var.board.is_game_over()
    if gameover:
        var.game_status = False
        if var.board.is_checkmate():
            var.game_over_reason = "CHECKMATE"
        if var.board.is_insufficient_material():
            var.game_over_reason = " INSUFFICIENT MATERIAL"
        if var.board.is_stalemate():
            var.game_over_reason = "STALEMATE"

          
def start_game():
    while var.game_status :
        show_board()
        color = chess.WHITE

        # white moves
        thread.start_new_thread(format_time,(var.current_color,))
        thread.start_new_thread(read_move,(var.current_color,))
        make_move(color)
        var.white_move_count += 1

        check()
        is_over()

        if not var.game_status:
            return

        show_board()
        color = chess.BLACK

        # black moves
        read_move(color)
        make_move(color)
        var.black_move_count += 1

        check()
    show_result()         
