from manim import *

class RotatingSquare(Scene):
    '''Create a square.
Make it appear on the screen.
Rotate it by 45 degrees.
'''
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.wait(1)