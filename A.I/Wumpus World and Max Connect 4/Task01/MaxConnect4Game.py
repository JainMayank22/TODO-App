#!/usr/bin/env python
# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos



import random
import sys
from copy import copy
import scorecalc as sc

utility_value = {}
score_list = []
infinity = float('inf')


class MaxConnect4game:


    def __init__(self):
        self.board_table = [[0 for i in range(7)] for j in range(6)]
        self.current_move = 0
        self.piece_count = 0
        self.P1S = 0
        self.P2S = 0
        self.gameFile = None
        self.computer_column = None
        self.depth = 1

    def Moves_Possible(board_table):
    	Moves_Possible = []
    	for col, colVal in enumerate(board_table[0]):
    		if colVal == 0:
    			Moves_Possible.append(col)
    	return Moves_Possible

    def func_eval(self):
        if self.current_move == 2:
            o_color = 1
        elif self.current_move == 1:
            o_color = 2
        return o_color

    def eval_playercalc(self, state):
        player_fours = self.Calc_Streak(state, self.current_move, 4)
        player_threes = self.Calc_Streak(state, self.current_move, 3)
        player_twos = self.Calc_Streak(state, self.current_move, 2)

        return (player_fours * 37044 + player_threes * 882 + player_twos * 21)

    def eval_compcalc(self, state):
        o_color = self.func_eval()
        comp_fours = self.Calc_Streak(state, o_color, 4)
        comp_threes = self.Calc_Streak(state, o_color, 3)
        comp_twos = self.Calc_Streak(state, o_color, 2)
        return (comp_fours * 37044 + comp_threes * 882 + comp_twos * 21)

    def eval_calculation(self, state):
        self.eval_playercalc(state)
        self.eval_compcalc(state)
        return self.eval_playercalc(state) - self.eval_compcalc(state)



    def getPieceCount(self):
        return sum(1 for row in self.board_table for piece in row if piece)

    def utility(self,state):
        if self.currentTurn == 1:
            utility = state.player1Score * 2 - state.player2Score
        elif self.currentTurn == 2:
            utility = state.player2Score * 2 - state.player1Score
        return utility

    def printboard_tableToFile(self):
        for row in self.board_table:
            self.gameFile.write(''.join(str(col) for col in row) + '\r')
        self.gameFile.write('%s\r' % str(self.current_move))

    def minimax(self, depth):
        current_state = copy.deepcopy(self.board_table)
        for i in range(7):
            if self.human_play(i) != None:
                if self.piece_count == 42 or self.depth == 0:
                    self.board_table = copy.deepcopy(current_state)
                    return i
                else:
                    val = self.beta_alpha(self.board_table, -infinity, infinity, depth - 1)

                    utility_value[i] = val
                    self.board_table = copy.deepcopy(current_state)

        max_utility_value = max([i for i in utility_value.values()])
        for i in range(7):
            if i in utility_value:
                if utility_value[i] == max_utility_value:
                    utility_value.clear()
                    return i
    def count_piece(self):
        self.piece_count = sum(1 for row in self.board_table for piece in row if piece)

    def max_val(self, current_node):
        main_node = copy.deepcopy(current_node)
        child_nodes = []
        for i in range(7):
            current_state = self.human_play(i)
            if current_state != None:
                child_nodes.append(self.board_table)
                self.board_table = copy.deepcopy(main_node)
        return child_nodes

    def alpha_beta(self, current_node, alpha, beta, depth):
        value = -infinity
        child_nodes = self.max_val(current_node)
        if child_nodes == [] or depth == 0:
            sc.get_score(self, self.board_table)
            return self.eval_calculation(self.board_table)
        else:
            for node in child_nodes:
                self.board_table = copy.deepcopy(node)
                value = max(value, self.beta_alpha(node, alpha, beta, depth - 1))
                if value >= beta:
                    return value
                alpha = max(alpha, value)
            return value

    def min_val(self, current_node):
        main_node = copy.deepcopy(current_node)
        if self.current_move == 1:
            opponent = 2
        elif self.current_move == 2:
            opponent = 1
        child_nodes = []
        for i in range(7):
            current_state = self.check_piece(i, opponent)
            if current_state != None:
                child_nodes.append(self.board_table)
                self.board_table = copy.deepcopy(main_node)
        return child_nodes

    def beta_alpha(self,current_node, alpha, beta, depth):
        value = infinity
        child_nodes = self.min_val(current_node)
        if child_nodes == [] or depth == 0:
            sc.get_score(self, self.board_table)
            return self.eval_calculation(self.board_table)
        else:
            for node in child_nodes:
                self.board_table = copy.deepcopy(node)
                value = min(value, self.alpha_beta(node, alpha, beta, depth - 1))
                if value <= alpha:
                    return value
                beta = min(beta, value)
        return value
    def Calc_Streak(self, state, color, streak):
        count = 0
        for i in range(6):
            for j in range(7):
                if state[i][j] == color:
                    count += self.Checkvertical(i, j, state, streak)
                    count += self.Checkhorizontal(i, j, state, streak)
                    count += self.Checkdiagonal(i, j, state, streak)
        return count

    def Checkvertical(self, row, column, state, streak):
        consecutiveCount = 0
        for i in range(row, 6):
            if state[i][column] == state[row][column]:
                consecutiveCount += 1
            else:
                break
        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def Checkhorizontal(self, row, column, state, streak):
        count = 0
        for j in range(column, 7):
            if state[row][j] == state[row][column]:
                count += 1
            else:
                break
        if count >= streak:
            return 1
        else:
            return 0

    def Checkdiagonal(self, row, column, state, streak):
        total = 0
        count = 0
        j = column
        for i in range(row, 6):
            if j > 6:
                break
            elif state[i][j] == state[row][column]:
                count += 1
            else:
                break
            j += 1
        if count >= streak:
            total += 1
        count = 0
        j = column
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j] == state[row][column]:
                count += 1
            else:
                break
            j += 1
        if count >= streak:
            total += 1
        return total

    def AI_Play(self):
        random_column = self.minimax(int(self.depth))
        result = self.human_play(random_column)
        if result:
            print('Player: %d, Column: %d\n' % (self.current_move, random_column + 1))
            self.move_shift()
        else:
            print('No Result')

    # Place the current player's piece in the requested column
    def human_play(self, column):
        if not self.board_table[0][column]:
            for i in range(5, -1, -1):
                if not self.board_table[i][column]:
                    self.board_table[i][column] = self.current_move
                    self.piece_count += 1
                    return 1

    def move_shift(self):
        if self.current_move == 2:
            self.current_move = 1
        elif self.current_move == 1:
            self.current_move = 2

    def display_board_table(self):
        print(' ---------------')
        for i in range(6):
            print('|', end=' ')
            for j in range(7):
                x = (self.board_table[i][j])
                print(x, end=' ')
            print('| ')
        print(' ---------------')



    def check_piece(self, column, opponent):
        if not self.board_table[0][column]:
            for i in range(5, -1, -1):
                if not self.board_table[i][column]:
                    self.board_table[i][column] = opponent
                    self.piece_count += 1
                    return 1

    def count_score(self):
        self.P1S = 0;
        self.P2S = 0;
        # Check horizontally
        for row in self.board_table:
            # Check player 1
            if row[0:4] == [1] * 4:
                self.P1S += 1
            if row[1:5] == [1] * 4:
                self.P1S += 1
            if row[2:6] == [1] * 4:
                self.P1S += 1
            if row[3:7] == [1] * 4:
                self.P1S += 1
            # Check player 2
            if row[0:4] == [2] * 4:
                self.P2S += 1
            if row[1:5] == [2] * 4:
                self.P2S += 1
            if row[2:6] == [2] * 4:
                self.P2S += 1
            if row[3:7] == [2] * 4:
                self.P2S += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.board_table[0][j] == 1 and self.board_table[1][j] == 1 and
                    self.board_table[2][j] == 1 and self.board_table[3][j] == 1):
                self.P1S += 1
            if (self.board_table[1][j] == 1 and self.board_table[2][j] == 1 and
                    self.board_table[3][j] == 1 and self.board_table[4][j] == 1):
                self.P1S += 1
            if (self.board_table[2][j] == 1 and self.board_table[3][j] == 1 and
                    self.board_table[4][j] == 1 and self.board_table[5][j] == 1):
                self.P1S += 1
            # Check player 2
            if (self.board_table[0][j] == 2 and self.board_table[1][j] == 2 and
                    self.board_table[2][j] == 2 and self.board_table[3][j] == 2):
                self.P2S += 1
            if (self.board_table[1][j] == 2 and self.board_table[2][j] == 2 and
                    self.board_table[3][j] == 2 and self.board_table[4][j] == 2):
                self.P2S += 1
            if (self.board_table[2][j] == 2 and self.board_table[3][j] == 2 and
                    self.board_table[4][j] == 2 and self.board_table[5][j] == 2):
                self.P2S += 1
        # Check diagonally

        # Check player 1
        if (self.board_table[2][0] == 1 and self.board_table[3][1] == 1 and
                self.board_table[4][2] == 1 and self.board_table[5][3] == 1):
            self.P1S += 1
        if (self.board_table[1][0] == 1 and self.board_table[2][1] == 1 and
                self.board_table[3][2] == 1 and self.board_table[4][3] == 1):
            self.P1S += 1
        if (self.board_table[2][1] == 1 and self.board_table[3][2] == 1 and
                self.board_table[4][3] == 1 and self.board_table[5][4] == 1):
            self.P1S += 1
        if (self.board_table[0][0] == 1 and self.board_table[1][1] == 1 and
                self.board_table[2][2] == 1 and self.board_table[3][3] == 1):
            self.P1S += 1
        if (self.board_table[1][1] == 1 and self.board_table[2][2] == 1 and
                self.board_table[3][3] == 1 and self.board_table[4][4] == 1):
            self.P1S += 1
        if (self.board_table[2][2] == 1 and self.board_table[3][3] == 1 and
                self.board_table[4][4] == 1 and self.board_table[5][5] == 1):
            self.P1S += 1
        if (self.board_table[0][1] == 1 and self.board_table[1][2] == 1 and
                self.board_table[2][3] == 1 and self.board_table[3][4] == 1):
            self.P1S += 1
        if (self.board_table[1][2] == 1 and self.board_table[2][3] == 1 and
                self.board_table[3][4] == 1 and self.board_table[4][5] == 1):
            self.P1S += 1
        if (self.board_table[2][3] == 1 and self.board_table[3][4] == 1 and
                self.board_table[4][5] == 1 and self.board_table[5][6] == 1):
            self.P1S += 1
        if (self.board_table[0][2] == 1 and self.board_table[1][3] == 1 and
                self.board_table[2][4] == 1 and self.board_table[3][5] == 1):
            self.P1S += 1
        if (self.board_table[1][3] == 1 and self.board_table[2][4] == 1 and
                self.board_table[3][5] == 1 and self.board_table[4][6] == 1):
            self.P1S += 1
        if (self.board_table[0][3] == 1 and self.board_table[1][4] == 1 and
                self.board_table[2][5] == 1 and self.board_table[3][6] == 1):
            self.P1S += 1

        if (self.board_table[0][3] == 1 and self.board_table[1][2] == 1 and
                self.board_table[2][1] == 1 and self.board_table[3][0] == 1):
            self.P1S += 1
        if (self.board_table[0][4] == 1 and self.board_table[1][3] == 1 and
                self.board_table[2][2] == 1 and self.board_table[3][1] == 1):
            self.P1S += 1
        if (self.board_table[1][3] == 1 and self.board_table[2][2] == 1 and
                self.board_table[3][1] == 1 and self.board_table[4][0] == 1):
            self.P1S += 1
        if (self.board_table[0][5] == 1 and self.board_table[1][4] == 1 and
                self.board_table[2][3] == 1 and self.board_table[3][2] == 1):
            self.P1S += 1
        if (self.board_table[1][4] == 1 and self.board_table[2][3] == 1 and
                self.board_table[3][2] == 1 and self.board_table[4][1] == 1):
            self.P1S += 1
        if (self.board_table[2][3] == 1 and self.board_table[3][2] == 1 and
                self.board_table[4][1] == 1 and self.board_table[5][0] == 1):
            self.P1S += 1
        if (self.board_table[0][6] == 1 and self.board_table[1][5] == 1 and
                self.board_table[2][4] == 1 and self.board_table[3][3] == 1):
            self.P1S += 1
        if (self.board_table[1][5] == 1 and self.board_table[2][4] == 1 and
                self.board_table[3][3] == 1 and self.board_table[4][2] == 1):
            self.P1S += 1
        if (self.board_table[2][4] == 1 and self.board_table[3][3] == 1 and
                self.board_table[4][2] == 1 and self.board_table[5][1] == 1):
            self.P1S += 1
        if (self.board_table[1][6] == 1 and self.board_table[2][5] == 1 and
                self.board_table[3][4] == 1 and self.board_table[4][3] == 1):
            self.P1S += 1
        if (self.board_table[2][5] == 1 and self.board_table[3][4] == 1 and
                self.board_table[4][3] == 1 and self.board_table[5][2] == 1):
            self.P1S += 1
        if (self.board_table[2][6] == 1 and self.board_table[3][5] == 1 and
                self.board_table[4][4] == 1 and self.board_table[5][3] == 1):
            self.P1S += 1

        # Check player 2
        if (self.board_table[2][0] == 2 and self.board_table[3][1] == 2 and
                self.board_table[4][2] == 2 and self.board_table[5][3] == 2):
            self.P2S += 1
        if (self.board_table[1][0] == 2 and self.board_table[2][1] == 2 and
                self.board_table[3][2] == 2 and self.board_table[4][3] == 2):
            self.P2S += 1
        if (self.board_table[2][1] == 2 and self.board_table[3][2] == 2 and
                self.board_table[4][3] == 2 and self.board_table[5][4] == 2):
            self.P2S += 1
        if (self.board_table[0][0] == 2 and self.board_table[1][1] == 2 and
                self.board_table[2][2] == 2 and self.board_table[3][3] == 2):
            self.P2S += 1
        if (self.board_table[1][1] == 2 and self.board_table[2][2] == 2 and
                self.board_table[3][3] == 2 and self.board_table[4][4] == 2):
            self.P2S += 1
        if (self.board_table[2][2] == 2 and self.board_table[3][3] == 2 and
                self.board_table[4][4] == 2 and self.board_table[5][5] == 2):
            self.P2S += 1
        if (self.board_table[0][1] == 2 and self.board_table[1][2] == 2 and
                self.board_table[2][3] == 2 and self.board_table[3][4] == 2):
            self.P2S += 1
        if (self.board_table[1][2] == 2 and self.board_table[2][3] == 2 and
                self.board_table[3][4] == 2 and self.board_table[4][5] == 2):
            self.P2S += 1
        if (self.board_table[2][3] == 2 and self.board_table[3][4] == 2 and
                self.board_table[4][5] == 2 and self.board_table[5][6] == 2):
            self.P2S += 1
        if (self.board_table[0][2] == 2 and self.board_table[1][3] == 2 and
                self.board_table[2][4] == 2 and self.board_table[3][5] == 2):
            self.P2S += 1
        if (self.board_table[1][3] == 2 and self.board_table[2][4] == 2 and
                self.board_table[3][5] == 2 and self.board_table[4][6] == 2):
            self.P2S += 1
        if (self.board_table[0][3] == 2 and self.board_table[1][4] == 2 and
                self.board_table[2][5] == 2 and self.board_table[3][6] == 2):
            self.P2S += 1

        if (self.board_table[0][3] == 2 and self.board_table[1][2] == 2 and
                self.board_table[2][1] == 2 and self.board_table[3][0] == 2):
            self.P2S += 1
        if (self.board_table[0][4] == 2 and self.board_table[1][3] == 2 and
                self.board_table[2][2] == 2 and self.board_table[3][1] == 2):
            self.P2S += 1
        if (self.board_table[1][3] == 2 and self.board_table[2][2] == 2 and
                self.board_table[3][1] == 2 and self.board_table[4][0] == 2):
            self.P2S += 1
        if (self.board_table[0][5] == 2 and self.board_table[1][4] == 2 and
                self.board_table[2][3] == 2 and self.board_table[3][2] == 2):
            self.P2S += 1
        if (self.board_table[1][4] == 2 and self.board_table[2][3] == 2 and
                self.board_table[3][2] == 2 and self.board_table[4][1] == 2):
            self.P2S += 1
        if (self.board_table[2][3] == 2 and self.board_table[3][2] == 2 and
                self.board_table[4][1] == 2 and self.board_table[5][0] == 2):
            self.P2S += 1
        if (self.board_table[0][6] == 2 and self.board_table[1][5] == 2 and
                self.board_table[2][4] == 2 and self.board_table[3][3] == 2):
            self.P2S += 1
        if (self.board_table[1][5] == 2 and self.board_table[2][4] == 2 and
                self.board_table[3][3] == 2 and self.board_table[4][2] == 2):
            self.P2S += 1
        if (self.board_table[2][4] == 2 and self.board_table[3][3] == 2 and
                self.board_table[4][2] == 2 and self.board_table[5][1] == 2):
            self.P2S += 1
        if (self.board_table[1][6] == 2 and self.board_table[2][5] == 2 and
                self.board_table[3][4] == 2 and self.board_table[4][3] == 2):
            self.P2S += 1
        if (self.board_table[2][5] == 2 and self.board_table[3][4] == 2 and
                self.board_table[4][3] == 2 and self.board_table[5][2] == 2):
            self.P2S += 1
        if (self.board_table[2][6] == 2 and self.board_table[3][5] == 2 and
                self.board_table[4][4] == 2 and self.board_table[5][3] == 2):
            self.P2S += 1
