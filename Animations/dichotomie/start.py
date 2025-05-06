from manim import *
import copy

class Dichotomie(MovingCameraScene):
    def f(self, x):
        return x**2-7

    def construct(self):
        
        # set the frame
        self.camera.frame.set_width(10)
        self.camera.frame.set_height(18)
        
        # plot axes
        axes = Axes(
                x_range=[-4, 4], 
                y_range=[-8, 8],
                x_length = 8, # important to fix absolute coordinates and axis coordinates
                y_length = 16,
                tips=False,
                axis_config={"include_numbers": True},
        )


        #axes.add_coordinate_labels()
        self.play(Create(axes))


        # graph and labels
        f_graph = axes.plot(
                lambda x: self.f(x), # referencing f directly create an error?
                x_range=[-4,4],
                use_smoothing=True,
                color=BLUE,
        )

        self.play(Create(f_graph))
        #self.play(FadeIn(f_label))
        
        #dot_1 = Dot(axes.i2gp(1.5,f_graph))
        dot_1 = Dot(point=[3,0,0], radius=.1)
        self.add(dot_1)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
