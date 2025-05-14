import pygame
import sys

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_state = 'running'
        self.win_combinations = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # For Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # for Columns
            (0, 4, 8), (2, 4, 6)              # For Diagonals
        )

    def make_move(self, position):
        if self.board[position] == ' ' and self.game_state == 'running':
            self.board[position] = self.current_player
            if self.check_win():
                self.game_state = 'win'
            elif self.check_tie():
                self.game_state = 'tie'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for combo in self.win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return True
        return False

    def check_tie(self):
        return ' ' not in self.board

class GameGUI:
    def __init__(self):
        pygame.init()
        self.size = 300
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Tic Tac Toe")
        self.cell_size = self.size // 3
        self.game = TicTacToe()

    def draw_board(self):
        self.screen.fill((255, 255, 255))
        
        # Draw grid lines
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), 
                (i * self.cell_size, 0), 
                (i * self.cell_size, self.size), 3)
            pygame.draw.line(self.screen, (0, 0, 0), 
                (0, i * self.cell_size), 
                (self.size, i * self.cell_size), 3)
        
        # For drawing X's and O's to TIC TAC
        for i in range(9):
            x = (i % 3) * self.cell_size + self.cell_size//2
            y = (i // 3) * self.cell_size + self.cell_size//2
            if self.game.board[i] == 'X':
                pygame.draw.line(self.screen, (255, 0, 0), 
                    (x - 30, y - 30), (x + 30, y + 30), 3)
                pygame.draw.line(self.screen, (255, 0, 0), 
                    (x + 30, y - 30), (x - 30, y + 30), 3)
            elif self.game.board[i] == 'O':
                pygame.draw.circle(self.screen, (0, 0, 255), 
                    (x, y), 30, 3)

    def handle_click(self, pos):
        x, y = pos
        col = x // self.cell_size
        row = y // self.cell_size
        position = row * 3 + col
        self.game.make_move(position)

    def show_message(self, text):
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (0, 255, 0))
        text_rect = text.get_rect(center=(self.size//2, self.size//2))
        self.screen.blit(text, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())

            self.draw_board()
            
            if self.game.game_state == 'win':
                self.show_message(f"Player {self.game.current_player} wins!")
            elif self.game.game_state == 'tie':
                self.show_message("Game Tied!")
            
            pygame.display.update()

if __name__ == "__main__":
    game = GameGUI()
    game.run()
