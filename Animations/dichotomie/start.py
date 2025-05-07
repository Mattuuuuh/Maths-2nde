from manim import *
from numpy import array

class Dichotomie(MovingCameraScene):

    def f(self, x):
        return x**2-7

    def dichotomie(self,a, b):
        # exit condition
        if b-a < self.precision:
            return 0

        axes = self.axes
        f_graph = self.f_graph

        # redefine fonts
        MathTex.set_default(font_size=self.font_size)
        Tex.set_default(font_size=self.font_size)
        
        # middle xm of the [a,b] interval
        # m(xm,ym) on C_f to check for sign
        xm = (a+b)/2
        ym = self.f(xm)

        """
        m = axes.get_graph_label(
                graph = f_graph,
                label=MathTex(f"f({xm})"),
                #direction = LEFT,
                #buff=xm*self.font_size/100,
                x_val = xm,
                dot = True,
                dot_config={"radius":.1*self.font_size/100},
                color=RED,
        )
        """

        m = Dot(point=axes.c2p(xm,ym), radius=.1, color=RED)
        
        # tick on [a,b] with xm label
        #tick_length = .1 * self.font_size/100
        tick_length = .1 if self.font_size >= 25 else .05
        mtick = Line(start=axes.c2p(xm,tick_length), end=axes.c2p(xm,-tick_length), color=RED)
        mlabel = (Tex(f"{xm}", color=RED).next_to(mtick, direction=array([0.,1*self.font_size/100,0.])))
 
        # show tick and label
        self.play(Create(mtick),Create(mlabel))

        # dashes lines for coordinates of m
        m_lines = axes.get_vertical_line(axes.c2p(xm,self.f(xm)), stroke_width=5)

        # show lines and point
        self.play(Create(m_lines))
        self.play(FadeIn(m))

        self.wait()

        # text specifying sign of ym
        # TODO: change width of frame somehow
        text_sign = Label(MathTex(f"f({xm})"+(">0" if ym>0 else "<0"), color=RED), box_config={"color":RED, "fill_opacity":0})
        text_sign = text_sign.next_to(m, direction=array([1*self.font_size/100,0,0]))
        self.play(Create(text_sign))
        
        self.wait()

        # remove box specifying sign of ym
        self.play(Uncreate(text_sign))
        
        # remove dashed lines
        self.play(Uncreate(m_lines))
        
        # if ym < 0: fadeout objects associated to a and replace them by objets of m
        if ym < 0:
            self.play(FadeOut(self.a))
            self.play(Uncreate(self.atick), Uncreate(self.alabel))
            self.a = m
            self.atick = mtick
            self.alabel = mlabel
            camera_center = axes.c2p((xm+b)/2,0)
        # if ym > 0: fadeout objects associated to b and replace them by objets of m
        else:
            self.play(FadeOut(self.b))
            self.play(Uncreate(self.btick), Uncreate(self.blabel))
            self.b = m
            self.btick = mtick
            self.blabel = mlabel
            camera_center = axes.c2p((a+xm)/2,0)
       

        # zoom in 
        #self.play(self.camera.frame.animate.scale(0.5).move_to(mtick))

        # cannot change both height and width idk why
        self.play(self.camera.frame.animate.set(height=max((b-a)*2,ym*2)).move_to(camera_center))

        # soften axes
        #self.axes.set_stroke(width=self.font_size/50)
        
        # soften C_f
        #self.play(FadeOut(self.f_graph), scale=2)
        #self.f_graph.set_stroke(width=self.font_size/50)
        #self.play(FadeIn(self.f_graph))

        # soften labels
        #self.play(FadeOut(self.alabel))
        #self.alabel.font_size = self.font_size 
        #self.play(FadeIn(self.alabel))
        #self.blabel.font_size = self.font_size 

        # soften tick lengths
        self.atick.start[1] /= 2
        self.btick.start[1] /= 2

        # redefine font size
        self.font_size /= 2

        if ym < 0:
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
                x_range=[-4,4, 0.01],
                color=BLUE,
        )

        self.play(Create(f_graph))
        
       
        # ticks
        self.atick = Line(start=axes.c2p(0,.1), end=axes.c2p(0,-.1), color=RED)
        self.btick = Line(start=axes.c2p(3,.1), end=axes.c2p(3,-.1), color=RED)
       
        self.play(Create(self.atick), Create(self.btick))

        self.blabel = (Tex("3", color=RED).next_to(self.btick, direction=array([1,-1,0])))
        self.alabel = (Tex("0", color=RED).next_to(self.atick, direction=array([-1,-1,0])))
        self.play(Create(self.blabel), Create(self.alabel))

        # only b line is necessary
        b_lines = axes.get_lines_to_point(axes.c2p(3,self.f(3)))
       
        self.play(Create(b_lines))

        # show a, b dots
        # dots a(x=0) and b(x=3)
        a = Dot(point=axes.c2p(0,-7), radius=.1, color=RED)
        b = Dot(point=axes.c2p(3,2), radius=.1, color=RED)
        self.play(Create(b), Create(a))
       
        # show sign of f(0) and f(3)
        text_signA = Label(MathTex(f"f(0)<0", color=RED), box_config={"color":RED, "fill_opacity":0})
        text_signA = text_signA.next_to(a, direction=array([-1,0,0]))
        text_signB = Label(MathTex(f"f(3)>0", color=RED), box_config={"color":RED, "fill_opacity":0})
        text_signB = text_signB.next_to(b, direction=array([1,0,0]))
        self.play(Create(text_signA), Create(text_signB))

        self.wait()

        # remove everything in reverse order except ticks and labels

        self.play(Uncreate(text_signA), Uncreate(text_signB))
        self.play(Uncreate(b), Uncreate(a))
        self.play(Uncreate(b_lines))

        # def class objects 
        self.a = a
        self.b = b
        self.axes = axes
        self.f_graph = f_graph
        
        self.precision = .1

        # recursive dichotomy
        self.dichotomie(0, 3)





