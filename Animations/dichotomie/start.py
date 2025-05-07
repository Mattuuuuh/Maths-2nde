from manim import *
from numpy import array

class Dichotomie(MovingCameraScene):

    def f(self, x):
        return x**2-7

    def dichotomie(self,a, b):
        if b-a < self.precision:
            return 0

        axes = self.axes
        f_graph = self.f_graph

        xm = (a+b)/2
        ym = self.f(xm)
        MathTex.set_default(font_size=self.font_size)
        Tex.set_default(font_size=self.font_size)


        m = axes.get_graph_label(
                graph = f_graph,
                label=MathTex(f"\\bigl({xm} ; f({xm})\\bigr)"),
                direction = RIGHT,
                x_val = xm,
                dot = True,
                dot_config={"radius":.1*self.font_size/100},
                color=RED,
                buff=xm*self.font_size/100,
        )
        
        mtick = Dot(axes.coords_to_point(xm,0))
        mlabel = (Tex(f"{xm}", color=RED).next_to(mtick, direction=array([0.,1*self.font_size/100,0.])))
 
        #tick_length = .1 * self.font_size/100
        tick_length = .1 if self.font_size >= 25 else .05

        mline = Line(start=axes.c2p(xm,tick_length), end=axes.c2p(xm,-tick_length), color=RED)
        self.play(Create(mline))
        self.play(Create(mlabel))

        m_lines = axes.get_lines_to_point(axes.c2p(xm,self.f(xm)), stroke_width=1)

        self.play(Create(m_lines))
        self.play(FadeIn(m))

        text_sign = MathTex(f"f({xm})"+(">0" if ym>0 else "<0")).next_to(UR)
        self.play(Create(text_sign))
        
        if ym < 0:
            self.play(*[FadeOut(obj) for obj in self.aobjects])
            self.play(Uncreate(self.atick))
            self.aobjects = Group(m_lines, m, mlabel)
            self.atick = mline
            self.alabel = mlabel
        else:
            self.play(*[FadeOut(obj) for obj in self.bobjects])
            self.play(Uncreate(self.btick))
            self.bobjects = Group(m_lines, m, mlabel)
            self.btick = mline
            self.blabel = mlabel
        
        self.play(Uncreate(text_sign))

        # zoom and reduce sizes of a bunch of things
        #self.play(self.camera.frame.animate.scale(0.5).move_to(mtick))
        self.play(self.camera.frame.animate.set(width=20*self.font_size/100).move_to(mtick))

        self.axes.set_stroke(width=self.font_size/50)
        self.f_graph.set_stroke(width=self.font_size/50)
        self.alabel.font_size = self.font_size 
        self.blabel.font_size = self.font_size 
        self.atick.start[1] /= 2
        self.btick.start[1] /= 2

        #temp=self.alabel
        #temp.font_size = self.font_size 
        #self.play(Transform(self.alabel, temp)) # doesn't animate shit

        
        self.font_size /= 2


        if ym < 0:
            self.aobjects = Group(m_lines, m, mlabel)
            return self.dichotomie(xm, b)
        return self.dichotomie(a, xm) 

    def construct(self):
        self.font_size = 100
        MathTex.set_default(font_size=self.font_size)
        
        # set the frame
        self.camera.frame.set_width(20)
        self.camera.frame.set_height(20)
        
        # plot axes
        axes = NumberPlane(
                x_range=[-4, 4], 
                y_range=[-8, 8],
                x_length = 20,
                y_length = 20,
                tips=False,
                axis_config={"include_numbers": True},
        )
    
        axes.add_coordinates()

        self.play(Create(axes))

        # graph and labels
        f_graph = axes.plot(
                lambda x: self.f(x), # referencing f directly create an error?
                x_range=[-4,4],
                use_smoothing=True,
                color=BLUE,
        )

        self.play(Create(f_graph))
       
        b = axes.get_graph_label(
                graph = f_graph,
                label=MathTex("\\bigl(3 ; f(3)\\bigr)"),
                x_val = 3,
                dot = True,
                buff=3,
                direction = RIGHT,
        )
    
        btick = Dot(axes.coords_to_point(3,0), radius=.1)
        blabel = (Tex("3").next_to(btick, UP))
        
        self.atick = Line(start=axes.c2p(0,.1), end=axes.c2p(0,-.1), color=RED)
        self.btick = Line(start=axes.c2p(3,.1), end=axes.c2p(3,-.1), color=RED)
       
        self.play(Create(self.atick))
        self.play(Create(self.btick))

        self.blabel = (Tex("3", color=RED).next_to(btick, direction=array([0.,1*self.font_size/100,0.])))
        self.play(Create(self.blabel))

        b_lines = axes.get_lines_to_point(axes.c2p(3,self.f(3)))
        self.play(Create(b_lines))
        self.play(FadeIn(b))
       
        self.aobjects = Group(Dot())
        self.bobjects = Group(b,b_lines)
        self.alabel = Label("")

        
        self.axes = axes
        self.f_graph = f_graph
        
        self.precision = .1

        self.dichotomie(0, 3)





