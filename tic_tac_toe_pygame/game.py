"""
Main game module.
"""
import sys

import pygame

from tic_tac_toe_pygame.config import WINDOW_SIZE, GRID_SIZE, CELL_SIZE, BLACK, WHITE, FPS
from tic_tac_toe_pygame.handlers.state import GameState
from tic_tac_toe_pygame.handlers.event import EventHandler


class TicTacToe:
    """" A class to represent a Tic-Tac-Toe game. """

    def __init__(self):
        """ Initialise the game board and the game state."""
        self.game_state = GameState()
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption('Tic-Tac-Toe')
        self.clock = pygame.time.Clock()
        self.events = EventHandler(self.screen, self.game_state)

    def handle_events(self):
        """ Handle events."""
        for event in pygame.event.get():
            self.events.handle_event(event)

    def update(self):
        """ Update the game state after each move. """
        self.game_state.update()

    def draw_grid(self):
        """Draw the Tic-Tac-Toe grid."""
        for i in range(1, GRID_SIZE):
            pos = i * CELL_SIZE
            pygame.draw.line(self.screen, BLACK, (pos, 0), (pos, WINDOW_SIZE[1]), 2)
            pygame.draw.line(self.screen, BLACK, (0, pos), (WINDOW_SIZE[1], pos), 2)

    def draw_markers(self):
        """Draw the markers (X and O) on the board."""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                pos = row * GRID_SIZE + col
                marker = self.game_state.board[pos]
                if marker != ' ':
                    x = col * CELL_SIZE + CELL_SIZE // 2
                    y = row * CELL_SIZE + CELL_SIZE // 2
                    font = pygame.font.Font(None, 74)
                    text = font.render(marker, True, BLACK)
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)

    def draw_board(self):
        """Draw the Tic-Tac-Toe board."""
        self.draw_grid()
        self.draw_markers()

    def draw_game_over(self):
        """Draw the game over message."""
        font = pygame.font.Font(None, 74)
        if self.game_state.winner == 'Draw':
            text = font.render('Draw!', True, BLACK)
        else:
            text = font.render(f'{self.game_state.winner} Wins!', True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_SIZE[1] + (WINDOW_SIZE[0] - WINDOW_SIZE[1]) // 2, WINDOW_SIZE[1] // 2))
        self.screen.blit(text, text_rect)

    def render(self):
        """ Render the game state to the screen. """
        self.screen.fill(WHITE)
        self.draw_board()
        if self.game_state.game_over:
            self.draw_game_over()
        pygame.display.flip()

    def run(self):
        """ Run the game."""
        while self.game_state.running:
            self.handle_events()
            self.render()

            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
