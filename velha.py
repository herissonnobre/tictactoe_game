class TicTacToe:

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.position_mapping = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1],
                                 9: [2, 2]}
        self.success_cases = [[[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                              [[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                              [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
        self.result = -1
        self.moves = 9
        self.state = 1
        pass

    def on_game(self):
        positions_filled = []
        while 0 < self.moves < 10 and self.result == -1:
            chosen_position = 0
            if self.moves % 2 == 1:
                while chosen_position < 1 or chosen_position > 9:
                    chosen_position = int(input('Please, inform the position to place the \'X\' (1 - 9):'))
                    if chosen_position not in positions_filled and (0 < chosen_position < 10):
                        positions_filled.append(chosen_position)
                        self.board[self.position_mapping[chosen_position][0]][
                            self.position_mapping[chosen_position][1]] = 1
                        self.moves -= 1
                    elif chosen_position in positions_filled:
                        print('This position is already filled!')
                    else:
                        print('The option taken is invalid!')
            else:
                while chosen_position < 1 or chosen_position > 9:
                    chosen_position = int(input('Please, inform the position to place the \'O\' (1 - 9):'))
                    if chosen_position not in positions_filled and (0 < chosen_position < 10):
                        positions_filled.append(chosen_position)
                        self.board[self.position_mapping[chosen_position][0]][
                            self.position_mapping[chosen_position][1]] = 2
                        self.moves -= 1
                    elif chosen_position in positions_filled:
                        print('This position is already filled!')
                    else:
                        print('The option taken is invalid!')

            board_for_print = [[], [], []]
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.board[i][j] == 1:
                        board_for_print[i].append('X')
                    elif self.board[i][j] == 2:
                        board_for_print[i].append('O')
                    else:
                        board_for_print[i].append(' ')

            print(
                f'{board_for_print[0][0]} | {board_for_print[0][1]} | {board_for_print[0][2]}\n---------\n'
                f'{board_for_print[1][0]} |'
                f' {board_for_print[1][1]} | {board_for_print[1][2]}\n---------\n{board_for_print[2][0]} | '
                f'{board_for_print[2][1]} |'
                f' {board_for_print[2][2]}')
            self.check_result()

    def check_result(self):
        for case in self.success_cases:
            if self.board[case[0][0]][case[0][1]] == self.board[case[1][0]][case[1][1]] == self.board[case[2][0]][
                case[2][1]] == 1:
                self.result = 1
                self.state = 0
                return
            elif self.board[case[0][0]][case[0][1]] == self.board[case[1][0]][case[1][1]] == self.board[case[2][0]][
                case[2][1]] == 2:
                self.result = 2
                self.state = 0
                return
            pass

        if all(field[0] == 1 and field[1] == 1 and field[2] == 1 for field in self.board) or all(field[0] == 2
                                                                                                 and field[
                                                                                                     1] == 2 and
                                                                                                 field[2] == 2 for
                                                                                                 field in
                                                                                                 self.board):
            self.result = -2
            self.state = 0
            return

        if self.moves == 0:
            self.result = 0
            self.state = 0
            return

    def show_result(self):
        board_for_print = [[], [], []]
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 1:
                    board_for_print[i].append('X')
                elif self.board[i][j] == 2:
                    board_for_print[i].append('O')
                else:
                    board_for_print[i].append(' ')

        print(
            f'{board_for_print[0][0]} | {board_for_print[0][1]} | {board_for_print[0][2]}\n---------\n'
            f'{board_for_print[1][0]} |'
            f' {board_for_print[1][1]} | {board_for_print[1][2]}\n---------\n{board_for_print[2][0]} | '
            f'{board_for_print[2][1]} |'
            f' {board_for_print[2][2]}')

        if self.result == 0:
            print('It\'s a draw!')
        elif self.result == 1:
            print('Player X won!')
        elif self.result == 2:
            print('Player O won!')
        else:
            print('What have you done?! It\'s a impossible case!')


pass
