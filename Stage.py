from tkinter import Canvas

from Actor import Snake, Fruit
from COLORS import COLORS


class Stage(Canvas):
    def __init__(self, width=640, height=480, bg=COLORS.BLACK, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.snake = Snake(self)
        self.fruit = Fruit(self)
        self.configure(bg=bg)
        self.configure(width=width)
        self.configure(height=height)
        self.colision()

    def colision(self):
        a = self.coords(self.snake.head)
        b = self.coords(self.fruit.fruit)
        colisions = list(self.find_overlapping(b[0], b[1], b[2], b[3]))
        print(colisions)
        if b is not None and self.snake.head in colisions:
            self.delete(self.fruit.fruit)
            if len(self.snake.body) > 0:
                coords = self.coords(self.snake.body[-1])
                self.snake.body.append(self.snake.create_body_part(coords[0], coords[1], coords[2], coords[3], COLORS.RED, tag=f"{len(self.snake.body)}"))
            else:
                coords = self.coords(self.snake.head)
                self.snake.body.append(self.snake.create_body_part(coords[0], coords[1], coords[2], coords[3], COLORS.RED, tag=f"{len(self.snake.body)}"))
            self.fruit = Fruit(self)
        if not self.snake.end:
            self.after(200, self.colision)
