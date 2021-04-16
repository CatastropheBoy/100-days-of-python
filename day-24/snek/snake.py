from turtle import Turtle

MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            self.create_segment()
        self.head = self.segments[0]


    def create_segment(self):
        segment = Turtle(shape="square")
        segment.pu()
        if len(self.segments) > 0:
            last_seg_pos = self.segments[-1].pos()
            segment.setpos(last_seg_pos)
        segment.color("white")
        self.segments.append(segment)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            if seg > 0:
                next_seg = self.segments[seg - 1]
                self.segments[seg].goto(next_seg.pos())
        self.head.forward(MOVE_SPEED)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

