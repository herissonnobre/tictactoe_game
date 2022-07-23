import velha


class TestTicTacToe:
    def test_game(self):
        tictactoe = velha.TicTacToe()
        while tictactoe.state == 1:
            tictactoe.on_game()
        tictactoe.show_result()


if __name__ == '__main__':
    tictactoe_game = TestTicTacToe()
