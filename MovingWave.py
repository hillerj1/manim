from manim import *
import numpy as np

class MovingWave(Scene):
    def construct(self):
        self.draw_axis()
        self.draw_sine_wave()

    def draw_axis(self):
        x_axis = Line(np.array([-4, 0, 0]), np.array([4, 0, 0]))
        y_axis = Line(np.array([0, -2, 0]), np.array([0, 2, 0]))

        self.add(x_axis, y_axis)
        self.x_min = -4
        self.x_max = 4

    def draw_sine_wave(self):
        sine_wave = self.get_sine_wave()
        vt = ValueTracker(0)

        def update_wave(wave):
            wave.become(self.get_sine_wave(dx=vt.get_value()))

        sine_wave.add_updater(update_wave)

        self.add(sine_wave)
        self.wait(2)

        self.play(vt.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        self.wait()

    def get_sine_wave(self, dx=0):
        return FunctionGraph(
            lambda x: np.sin(x + dx),
            x_range=[self.x_min, self.x_max]
        )

