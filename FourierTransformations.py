from manim import *
import numpy as np

class FourierTransformVisualization(Scene):
    def construct(self):
        # Create axes for the time domain
        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],  # Range for x-axis
            y_range=[-1.5, 1.5, 0.5],       # Range for y-axis
            axis_config={"color": BLUE},
        )

        # Create a sinusoidal wave
        t = np.linspace(-2 * PI, 2 * PI, 100)
        wave = np.sin(t)

        # Create the graph for the wave
        wave_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-2 * PI, 2 * PI])

        # Labels for the axes
        axes_labels = axes.get_axis_labels(x_label="t", y_label="f(t)")

        # Add the axes and wave to the scene
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(wave_graph))
        self.wait(2)

        # Fourier Transform: Create a complex exponential representation
        self.play(FadeOut(wave_graph), FadeOut(axes_labels))

        # Create axes for the frequency domain
        freq_axes = Axes(
            x_range=[-5, 5, 1],  # Range for frequency axis
            y_range=[0, 1.5, 0.5],  # Amplitude range for frequencies
            axis_config={"color": GREEN},
        )

        # Add frequency axes to the scene
        self.play(Create(freq_axes))
        self.wait(1)

        # Create the Fourier Transform graph
        freq_values = np.array([1, 0, 0, 0, 0])  # Fourier coefficients for the frequencies
        freq_graph = freq_axes.plot(lambda x: (1/2) * np.abs(np.sin(x)), color=RED, x_range=[-5, 5])

        # Display the Fourier Transform
        self.play(Create(freq_graph))
        self.wait(2)

        # Final fade out
        self.play(FadeOut(freq_graph), FadeOut(freq_axes))

if __name__ == "__main__":
    from manim import config
    config.media_dir = './media'  # Ensure this path exists
    FourierTransformVisualization().render()
