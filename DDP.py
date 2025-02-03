from manim import *
import numpy as np

class ChaoticPendulumWithForce(Scene):
    def pendulum_angle(self, t, gamma, beta, omega0, omega_d, initial_conditions):
        # RK4 method to solve the differential equation
        def F(state, t):
            phi, phi_dot = state
            phi_ddot = -2 * beta * phi_dot - omega0**2 * np.sin(phi) + gamma * omega0**2 * np.cos(omega_d * t)
            return np.array([phi_dot, phi_ddot])

        phi, phi_dot = initial_conditions
        time_step = 0.05
        n_steps = int(t / time_step)
        for _ in range(n_steps):
            k1 = F([phi, phi_dot], t)
            k2 = F([phi + 0.5 * time_step * k1[0], phi_dot + 0.5 * time_step * k1[1]], t + 0.5 * time_step)
            k3 = F([phi + 0.5 * time_step * k2[0], phi_dot + 0.5 * time_step * k2[1]], t + 0.5 * time_step)
            k4 = F([phi + time_step * k3[0], phi_dot + time_step * k3[1]], t + time_step)
            phi += (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) * time_step / 6
            phi_dot += (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) * time_step / 6
        return phi, phi_dot

    def construct(self):
        # Pendulum settings
        length = 3
        origin = ORIGIN
        initial_conditions = [0.2, 0]  # [initial angle, initial angular velocity]
        gamma = 1.2
        beta = 0.75
        omega0 = 1.5
        omega_d = 0.9
        max_time = 20

        # Pendulum rod and bob
        pendulum_rod = Line(origin, [0, -length, 0], stroke_width=6)
        pendulum_bob = Dot(radius=0.2).move_to(pendulum_rod.get_end())
        pendulum_group = VGroup(pendulum_rod, pendulum_bob)
        self.add(pendulum_group)

        # Driving force arrow
        force_arrow = Arrow(ORIGIN, RIGHT, buff=0, color=YELLOW).shift(UP * 3)

        # XY-plane trajectory graph
        trajectory_path = TracedPath(pendulum_bob.get_center, stroke_color=BLUE, stroke_width=2)
        self.add(trajectory_path)

        # Secondary XY-plane axis for plotting rotation
        plane = NumberPlane(x_range=[-length, length], y_range=[-length, length], background_line_style={"stroke_opacity": 0.4})
        plane.shift(DOWN * 3)
        self.add(plane)

        # Animation
        for t in np.arange(0, max_time, 0.05):
            angle, _ = self.pendulum_angle(t, gamma, beta, omega0, omega_d, initial_conditions)
            new_end = [length * np.sin(angle), -length * np.cos(angle), 0]
            
            # Update pendulum position
            pendulum_rod.put_start_and_end_on(origin, new_end)
            pendulum_bob.move_to(pendulum_rod.get_end())

            # Update driving force arrow (amplitude varies with driving force)
            force_amplitude = gamma * np.cos(omega_d * t)
            force_arrow.put_start_and_end_on(UP * 3, UP * 3 + RIGHT * force_amplitude)

            # Wait for each frame to show smooth animation
            self.wait(0.02)

