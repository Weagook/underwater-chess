from pygame import transform, image
from config import IMG_BLACK_BLOCK, IMG_WHITE_BLOCK

class Square:
    def __init__(self, picture: str, size: tuple, pos: tuple):
        self.size = size
        self.pos = pos
        self.image = transform.scale(image.load(picture), self.size)
    
class ChessTable:
    def __init__(self, size:tuple = (500, 500), pos: tuple = (0, 0)):
        self.size = size
        self.pos = pos
        self.sq_width = size[0] / 8
        self.sq_height = size[1] / 8
        self.blocks = list()
        self.__create_blocks()

    def __create_blocks(self):
        x = self.pos[0]
        y = self.pos[1]
        color = True
        for col in range(8):
            for row in range(8):
                if color:
                    image = IMG_WHITE_BLOCK
                else:
                    image = IMG_BLACK_BLOCK
                color = not color
                block = Square(image, (self.sq_width, self.sq_height), (x, y))
                self.blocks.append(block)
                x += self.sq_width
            color = not color
            y += self.sq_height
            x = self.pos[0]


    
    