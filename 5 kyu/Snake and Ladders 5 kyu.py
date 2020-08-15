class SnakesLadders():

    def __init__(self):
        self.board = {i: i for i in range(101)}
        self.player1_pos = 0
        self.player2_pos = 0
        self.player1_active = True
        self.player2_active = False
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"
        self.player1_status = False
        self.player2_status = False
        self.double = False
        self.update_board()
        self.message = ""

    def play(self, die1, die2):
        if self.player1_status or self.player2_status:
            return "Game over!"
        if die2 == die1 and self.double is False:
            self.double = True
        if self.player1_active:
            self.player1_pos += die2 + die1
            if self.player1_pos > 100:
                self.player1_pos = self.board[100 - (self.player1_pos - 100)]
            self.player1_pos = self.board[self.player1_pos]
            self.message = f"{self.player1_name} is on square {self.player1_pos}"
            if self.player1_pos == 100:
                self.message = f"{self.player1_name} Wins!"
                self.player1_status = True
            if not self.double:
                self.player1_active = False
                self.player2_active = True
            else:
                self.double = False
        elif self.player2_active:
            self.player2_pos += die1 + die2
            if self.player2_pos > 100:
                self.player2_pos = self.board[100 - (self.player2_pos - 100)]
            self.player2_pos = self.board[self.player2_pos]
            self.message = f"{self.player2_name} is on square {self.player2_pos}"
            if self.player2_pos == 100:
                self.message = f"{self.player2_name} Wins!"
                self.player2_status = True
            if not self.double:
                self.player2_active = False
                self.player1_active = True
            else:
                self.double = False
        return self.message

    def update_board(self):
        # Ladders
        self.board[2] = 38
        self.board[7] = 14
        self.board[8] = 31
        self.board[15] = 26
        self.board[21] = 42
        self.board[28] = 84
        self.board[36] = 44
        self.board[51] = 67
        self.board[71] = 91
        self.board[78] = 98
        # Snakes
        self.board[16] = 6
        self.board[46] = 25
        self.board[49] = 11
        self.board[62] = 19
        self.board[64] = 60
        self.board[74] = 53
        self.board[89] = 68
        self.board[92] = 88
        self.board[95] = 75
        self.board[99] = 80



game = SnakesLadders()
print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
print(game.play(1, 1))
