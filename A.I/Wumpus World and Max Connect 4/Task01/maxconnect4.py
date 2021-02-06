#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos


import sys
from MaxConnect4Game import MaxConnect4game
import time

def play_human(board_table):
    while board_table.getPieceCount() != 42:
        print("It is Human's turn.")
        userMove = int(input("Enter a column number between 1 - 7 for your play : "))
        if not 0 < userMove < 8:
            print("Column invalid! Enter Again.")
            continue
        if not board_table.human_play(userMove - 1):
            print("Column number: %d is full. Try other column." % userMove)
            continue
        print("You made a move in column : " + str(userMove))
        board_table.display_board_table()
        board_table.gameFile = open("human.txt", 'w')
        board_table.printboard_tableToFile()
        board_table.gameFile.close()
        if board_table.getPieceCount() == 42:
            print("No more moves possible, Game Over !")
            board_table.count_score()
            print('Score: Player-1 = %d, Player-2 = %d\n' % (board_table.P1S, board_table.P2S))
            break
        else:
            print("AI is computing based on next " + str(board_table.depth) + " steps!")
            board_table.move_shift()
            board_table.AI_Play()
            board_table.display_board_table()
            board_table.gameFile = open('computer.txt', 'w')
            board_table.printboard_tableToFile()
            board_table.gameFile.close()
            board_table.count_score()
            print('Score: Player-1 = %d, Player-2 = %d\n' % (board_table.P1S, board_table.P2S))



class play_mode:

    def one_move(self,board_table):
        start_time = time.time()
        if board_table.piece_count >= 42:
            print('Game board is full !\n Game Over !')
            sys.exit(0)
        print ('board_table state before move:')
        board_table.display_board_table()
        board_table.AI_Play()
        print ('board_table state after move:')
        board_table.display_board_table()
        board_table.count_score()
        print('Score: Player-1 = %d, Player-2 = %d\n' % (board_table.P1S, board_table.P2S))
        board_table.printboard_tableToFile()
        board_table.gameFile.close()
        print("Total Execution Time:")
        print (time.time() - start_time)




    def interactive(self, board_table, next_player):
        print('Current Board state')
        board_table.display_board_table()
        board_table.count_score()
        print('Score: Player-1 = %d, Player-2 = %d\n' % (board_table.P1S, board_table.P2S))
        if next_player == 'human-next':
            play_human(board_table)
        else:
            board_table.AI_Play()
            board_table.gameFile = open('computer.txt', 'w')
            board_table.printboard_tableToFile()
            board_table.gameFile.close()
            board_table.display_board_table()
            board_table.count_score()
            print('Score: Player-1 = %d, Player-2 = %d\n' % (board_table.P1S, board_table.P2S))
            play_human(board_table)

        if board_table.getPieceCount() == 42:
            if board_table.P1S > board_table.P2S:
                print("Player 1 wins !")
            if board_table.P1S == board_table.P2S:
                print("The game is a Tie !")
            if board_table.P1S < board_table.P2S:
                print("Player 2 wins !")
            print("Game Over")


def main(argv):
    board_table = MaxConnect4game()
    mode = play_mode()
    try:
        board_table.gameFile = open(argv[2], 'r')
        file_lines = board_table.gameFile.readlines()
        board_table.board_table = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        board_table.current_move = int(file_lines[-1][0])
        board_table.gameFile.close()
    except:
        print('File not found, begin new game.')
        board_table.current_move = 1
    board_table.count_piece()
    board_table.depth = argv[4]
    if argv[1] == 'interactive':
        mode.interactive(board_table, argv[3])
    else:
        try:
            board_table.gameFile = open(argv[3], 'w')
        except:
            sys.exit('Error while opening output file.')
        mode.one_move(board_table)



main(sys.argv)
