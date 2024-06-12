class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def gameboard(self):
        for row in self.board:
            print(" | ".join(row))
            print("--" * 5)

    def check_win(self):
        # Rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def get_move(self):
        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move >= 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
                row, col = divmod(move, 3)
                if self.board[row][col] != " ":
                    print("Invalid move. The cell is already occupied. Try again.")
                    continue
                return row, col
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play(self):
        while True:
            self.gameboard()
            row, col = self.get_move()

            self.board[row][col] = self.current_player
            winner = self.check_win()

            if winner:
                self.gameboard()
                print(f"Player {winner} wins!")
                break

            if self.check_draw():
                self.gameboard()
                print("It's a draw!")
                break

            self.switch_player()


game=TicTacToe()
game.play()
