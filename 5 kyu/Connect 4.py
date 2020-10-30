class Connect4():
    def __init__(self):
        self.player1 = {'status': True, 'name': 'Player 1'}
        self.player2 = {'status': False, 'name': 'Player 2'}
        self.board = [[0] * 7 for _ in range(6)]
        self.turn_counter = 0
        self.victory = False

    def play(self, col):
        if not self.victory:
            row = self.find_empty_row(col)
            if row is False:
                return "Column full!"

            self.check_turn()
            self.drop_disc(row, col)

            if self.check_board():
                self.victory = True
                return f'{self.get_active_player()} wins!'
            return f'{self.get_active_player()} has a turn'
        else:
            return "Game has finished!"

    def find_empty_row(self, c):
        for row in range(5, -1, -1):
            if self.board[row][c] == 0:
                return row
        return False

    def check_turn(self):
        self.turn_counter += 1
        if self.turn_counter % 2 == 0:
            self.player1['status'] = False
            self.player2['status'] = True
        else:
            self.player1['status'] = True
            self.player2['status'] = False

    def drop_disc(self, row, col):
        if self.player1['status']:
            self.board[row][col] = "R"
        else:
            self.board[row][col] = "B"

    def check_board(self):
        # Col Check
        for col in range(7):
            cnt = 0
            for row in range(5):
                if self.board[row][col] != 0:
                    cnt += 1
                    if cnt == 4:
                        return True
                    if cnt == 3 and self.board[row][col] == self.board[row + 1][col]:
                        # print(self.board)
                        return True
                    if self.board[row][col] != self.board[row + 1][col]:
                        cnt = 0

        # Row Check
        for row in range(6):
            cnt = 0
            for col in range(6):
                if self.board[row][col] != 0:
                    cnt += 1
                    if cnt == 4:
                        return True
                    if cnt == 3 and self.board[row][col] == self.board[row][col + 1]:
                        # print(self.board)
                        return True
                    if self.board[row][col] != self.board[row][col + 1]:
                        cnt = 0

        # Diagonal Check
        # left_bottom -> righ_topt
        for row in range(3, 6):
            for col in range(0, 4):
                if self.board[row][col] != 0:
                    if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == \
                            self.board[row - 3][col + 3]:
                        return True
            # letf_top -> right
        for row in range(3):
            for col in range(0, 4):
                if self.board[row][col] != 0:
                    if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == \
                            self.board[row + 3][col + 3]:
                        return True

    def swap_players(self):
        self.player1['status'] = not self.player1['status']
        self.player2['status'] = not self.player2['status']

    def get_active_player(self):
        if self.player1['status']:
            return self.player1['name']
        else:
            return self.player2['name']


game = Connect4()

print(game.play(1))  # r
print(game.play(2))  # b
print(game.play(2))  # r
print(game.play(3))  # b
print(game.play(6))  # r
print(game.play(3))  # b
print(game.play(3))  # r
print(game.play(4))  # b
print(game.play(4))  # r
print(game.play(4))  # b
print(game.play(4))  # r

