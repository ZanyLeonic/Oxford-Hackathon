import ctypes
import threading

BLOCK_SIZE = 64

TETRIS_SQUARE = [
    [0,0,0],
    [0,0,0],
    [0,1,1],
    [0,1,1]
]

TETRIS_LINE = [
    [0,0,1],
    [0,0,1],
    [0,0,1],
    [0,0,1]
]

ALT = list(zip(*TETRIS_LINE))

TETRIS_TEE = [
    [0,0,0],
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

TETRIS_LEL = [
    [0,0,0],
    [1,0,0],
    [1,0,0],
    [1,1,0]
]


TETRIS_SKEW = [
    [0,0,0],
    [0,0,0],
    [0,1,1],
    [1,1,0]
]

TETRIS = [TETRIS_SKEW, TETRIS_SQUARE, TETRIS_TEE, TETRIS_LEL, TETRIS_LINE]
TETRIS_S = ["Skew", "Square", "Tee", "L", "Line"]
COLOURS = ["blue", "red", "purple", "yellow", "green", "white"]

class Game():
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.screensize = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        self.grid = [[None for i in range(self.screensize[0] // BLOCK_SIZE)] for k in range(self.screensize[1] // BLOCK_SIZE)]
        self.current_block = None
        self.bottom = (1535, 1150)
        self.blocks = []
        # self.rows = [[0 for i in range(15)] for k in range(10)]
        self.next_shape = None
        
    def add_block(self, block):
        self.current_block = block
        self.blocks.append(block)

    def on_tick(self):
        pass


if __name__ == "__main__":
    game = Game()