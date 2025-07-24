"""
Configuration settings for the Tic Tac Toe game using Pygame.
"""
# Pygame configuration
WINDOW_SIZE = (640, 480)
FPS = 60

# Grid configuration
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE[1] // GRID_SIZE

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Winning combinations for Tic Tac Toe
WINNING_COMBINATIONS = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
