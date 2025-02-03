from manim import *
import numpy as np

class OrbitalMotionSimulation(Scene):
    def construct(self):
        # Create three celestial bodies (dots)
        body1 = Dot(color=BLUE, radius=0.2).move_to(np.array([-3, 1, 0]))
        body2 = Dot(color=GREEN, radius=0.2).move_to(np.array([3, -1, 0]))
        body3 = Dot(color=RED, radius=0.2).move_to(np.array([0, 3, 0]))

        # Add the bodies to the scene
        self.add(body1, body2, body3)

        # Animation: Circular motion for each body
        n_steps = 100
        for i in range(n_steps):
            angle = i * (2 * PI / n_steps)  # Angle for circular motion
            body1.move_to(np.array([-3 * np.cos(angle), 3 * np.sin(angle), 0]))
            body2.move_to(np.array([3 * np.cos(angle), -3 * np.sin(angle), 0]))
            body3.move_to(np.array([2 * np.cos(angle * 1.5), 2 * np.sin(angle * 1.5), 0]))

            # Update the scene
            self.wait(0.05)

        # Fade out all elements
        self.play(FadeOut(body1), FadeOut(body2), FadeOut(body3))

if __name__ == "__main__":
    from manim import config
    config.media_dir = './media'  # Ensure this path exists
    OrbitalMotionSimulation().render()
