from time import sleep
from random import randint
from tkinter import Canvas, Event

from DIRECTIONS import DIRECTIONS
from COLORS import COLORS

class Snake:
    direction = DIRECTIONS.RIGHT
    body = []
    end = False
    times = 0
    
    def __init__(self, canva: Canvas) -> None:
        self.canva = canva
        self.head = self.create_body_part(0, 10, 20, 30)
        self.register_key()
        self.move()

    def register_key(self):
        self.canva.winfo_toplevel().bind("<Right>", lambda event: self.change_direction(event))
        self.canva.winfo_toplevel().bind("<Down>", lambda event: self.change_direction(event))
        self.canva.winfo_toplevel().bind("<Left>", lambda event: self.change_direction(event))
        self.canva.winfo_toplevel().bind("<Up>", lambda event: self.change_direction(event))
    
    def create_body_part(self, posx_1, posy_1, posx_2, posy_2, color=COLORS.WHITE, tag=""):
        return self.canva.create_rectangle(posx_1, posy_1, posx_2, posy_2, fill=color, tag=tag)

    def move(self, event: Event = None):
        coords_past = self.canva.coords(self.head)
        self.canva.delete(self.head)
        coords = self.update_position(coords_past, self.direction)
        self.head = self.create_body_part(coords[0], coords[1], coords[2], coords[3])
        for part in list(reversed(self.body)):
            index = self.body.index(part)
            tag = self.canva.find_withtag(self.body[index])
            self.canva.delete(tag)
            if index != 0:
                coords = self.canva.coords(self.body[index-1])
                self.body[index] = self.create_body_part(coords[0], coords[1], coords[2], coords[3], COLORS.RED)
            else:
                self.body[index] = self.create_body_part(coords_past[0], coords_past[1], coords_past[2], coords_past[3], COLORS.RED)
        if not self.end:
            self.times += 1
            self.job = self.canva.winfo_toplevel().after(200, self.move)
            print(self.job)
        elif self.end:
            self.canva.winfo_toplevel().after_cancel(f"after#{self.times}")
            self.times -= 1
            print("acabou")

    def change_direction(self, event):
        self.direction = event.keysym.lower()
        
    def update_position(self, coords: list[float], direction: str):
        if coords[2] > 640 or coords[0] < 0 or coords[1] < 0 and coords[3] > 480:
            self.end = True
        match direction:
            case DIRECTIONS.UP:
                return [coords[0], coords[1]-20, coords[2], coords[3]-20]
            case DIRECTIONS.RIGHT:
                return [coords[0]+20, coords[1], coords[2]+20, coords[3]]
            case DIRECTIONS.DOWN:
                return [coords[0], coords[1]+20, coords[2], coords[3]+20]
            case DIRECTIONS.LEFT:
                return [coords[0]-20, coords[1], coords[2]-20, coords[3]]


class Fruit:    
    def __init__(self, canva: Canvas) -> None:
        self.canva = canva
        self.x = randint(0, 619)
        while self.x % 10 != 0:
            self.x += 1
        self.y = randint(0, 459)
        while self.y % 10 != 0:
            self.y += 1
        self.fruit = self.create_fruit(self.x, self.y, self.x+20, self.y+20)

    def create_fruit(self, posx_1, posy_1, posx_2, posy_2):
        return self.canva.create_rectangle(posx_1, posy_1, posx_2, posy_2, fill=COLORS.WHITE)
