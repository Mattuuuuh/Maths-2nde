from manim import *

class Dichotomie(MovingCameraScene):

    def comma(self, x):
        return f'{x}'.replace('.', ',')

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
        
        sign_of_ym = 1 if ym>0 else -1

        m = Dot(point=axes.c2p(xm,ym), radius=.1*self.font_size/100, color=RED)
        
        # tick on [a,b] with xm label
        tick_length = .1 * self.font_size/50
        #tick_length = .1 if self.font_size >= 25 else .05
        mtick = Line(
                start=axes.c2p(xm,tick_length),
                end=axes.c2p(xm,-tick_length),
                color=RED,
                stroke_width=2*self.font_size/50,
                #width=2*self.font_size/50,
        )
        mlabel = (Tex(f"{self.comma(xm)}", color=RED).next_to(mtick, direction=-sign_of_ym*1*self.font_size/100*UP))
 
        # show tick and label
        self.play(Create(mtick),Write(mlabel))

        # dashes lines for coordinates of m
        m_lines = axes.get_vertical_line(axes.c2p(xm,self.f(xm)), stroke_width=5*self.font_size/100)

        # show lines and point
        self.play(Create(m_lines))
        self.play(FadeIn(m))

        self.wait()

        # text specifying sign of ym
        # TODO: change width of frame somehow
        text_sign = Label(MathTex(f"f({self.comma(xm)})"+(">0" if ym>0 else "<0"), color=RED), frame_config={"stroke_width":self.font_size/50})
        text_sign.next_to(m, direction=1*self.font_size/100*RIGHT)
        self.play(Write(text_sign))
        
        self.wait()

        # remove in order
        self.play(FadeOut(text_sign))
        self.play(Uncreate(m))
        self.play(Uncreate(m_lines))
        
        # if ym < 0: fadeout objects associated to a and replace them by objets of m
        if ym < 0:
            self.play(FadeOut(self.a))
            self.play(Uncreate(self.atick))
            self.play(FadeOut(self.alabel))
            self.a = m
            self.atick = mtick
            self.alabel = mlabel
            camera_center = axes.c2p((xm+b)/2,0)
        # if ym > 0: fadeout objects associated to b and replace them by objets of m
        else:
            self.play(FadeOut(self.b))
            self.play(Uncreate(self.btick))
            self.play(FadeOut(self.blabel))
            self.b = m
            self.btick = mtick
            self.blabel = mlabel
            camera_center = axes.c2p((a+xm)/2,0)
       
        
        # soften labels
        self.alabel.font_size = self.font_size
        # ya < 0, always
        self.alabel = self.alabel.next_to(self.atick, direction=1*self.font_size/100*UP)
        self.blabel.font_size = self.font_size 
        # yb > 0, always
        self.blabel = self.blabel.next_to(self.btick, direction=-1*self.font_size/100*UP)

        # zoom in 
        # cannot change both height and width idk why
        #self.play(self.camera.frame.animate.set(height=max((b-a)*2,ym*2)).move_to(camera_center))
        yb = self.b.arc_center[1]
        self.play(self.camera.frame.animate.set(height=max(yb*16/9,(b-a))).move_to(camera_center))

        # soften axes
        self.axes.set_stroke(width=self.font_size/50)
        
        # soften C_f
        #self.play(FadeOut(self.f_graph), scale=2)
        self.f_graph.set_stroke(width=self.font_size/50)
        #self.play(FadeIn(self.f_graph))


        # soften tick lengths
        self.atick.start[1] /= 2
        self.atick.end[1] /= 2
        self.btick.start[1] /= 2
        self.btick.end[1] /= 2
        self.atick.stroke_width /= 2
        self.btick.stroke_width /= 2

        # redefine font size
        self.font_size /= 2

        if ym < 0:
            return self.dichotomie(xm, b)
        return self.dichotomie(a, xm) 

    def construct(self):
        self.font_size = 48
        MathTex.set_default(font_size=self.font_size)
        
        # set the frame
        self.camera.frame.width = 16
        self.camera.frame.height = 9
        self.camera.frame.pixel_height = 1080
        self.camera.frame.pixel_width = 1920

        # plot axes
        axes = NumberPlane(
                x_range=(-16, 16, 1), 
                y_range=(-16, 16, 1),
                x_length = 16*2,
                y_length = 9*2,
                tips=False,
                background_line_style={
                    #"stroke_width": 1,
                    "stroke_opacity": .5,
                },
        )
    
        #axes.add_coordinates()

        self.play(Create(axes))

        # graph and labels
        f_graph = axes.plot(
                lambda x: self.f(x), # referencing f directly create an error?
                x_range=[-4,4, 0.01],
                color=BLUE,
        )
        equation = Label(MathTex("y = x^2 - 7"))
        equation.move_to(axes.c2p(6.5,7), RIGHT)

        self.play(Create(f_graph), Create(equation))
        
       
        # ticks
        self.atick = Line(start=axes.c2p(0,.1), end=axes.c2p(0,-.1), color=RED)
        self.btick = Line(start=axes.c2p(3,.1), end=axes.c2p(3,-.1), color=RED)
       
        self.play(Create(self.atick), Create(self.btick))

        self.blabel = (Tex("3", color=RED).next_to(self.btick, direction=RIGHT+DOWN))
        self.alabel = (Tex("0", color=RED).next_to(self.atick, direction=LEFT + DOWN))
        self.play(Create(self.blabel), Create(self.alabel))

        # only b line is necessary
        b_lines = axes.get_lines_to_point(axes.c2p(3,self.f(3)))
       
        self.play(Create(b_lines))

        # show a, b dots
        # dots a(x=0) and b(x=3)
        a = Dot(point=axes.c2p(0,-7), radius=.05, color=RED)
        b = Dot(point=axes.c2p(3,2), radius=.05, color=RED)
        self.play(Create(b), Create(a))
       
        # show sign of f(0) and f(3)
        text_signA = Label(MathTex(f"f(0)<0", color=RED))
        text_signA = text_signA.next_to(a, direction=LEFT)
        text_signB = Label(MathTex(f"f(3)>0", color=RED))
        text_signB = text_signB.next_to(b, direction=RIGHT)
        self.play(Write(text_signA), Write(text_signB))

        self.wait()

        # remove everything in reverse order except ticks and labels

        self.play(FadeOut(text_signA), FadeOut(text_signB))
        self.play(Uncreate(b), Uncreate(a))
        self.play(Uncreate(b_lines))
        self.play(FadeOut(equation))

        # def class objects 
        self.a = a
        self.b = b
        self.axes = axes
        self.f_graph = f_graph
        
        self.precision = .01

        # recursive dichotomy
        self.dichotomie(0, 3)





