from manim import *

LOW_OPACITY = .3

class Dichotomie(MovingCameraScene):

    def comma(self, x):
        return f'{x}'.replace('.', ',')

    def f(self, x):
        return x**2-7

    def dichotomie(self,a,b):
        # exit condition
        if b-a < self.precision:
            return 0
        
        # aliases
        axes = self.axes
        f_graph = self.f_graph
        
        # images of a, b
        ya = self.f(a)
        yb = self.f(b)
        
        # middle xm of the [a,b] interval
        xm = (a+b)/2
        ym = self.f(xm)
        sign_of_ym = 1 if ym>0 else -1

        # halve font size for next step
        # and redefine fonts
        scale_factor=.5
        #self.scale = self.width_ratio
        scale_factor = max(.5, min(abs(ym/self.ym), 1))
        self.ym = ym
        self.scale *= scale_factor
        self.font_size *= scale_factor 
        MathTex.set_default(font_size=self.font_size)
        Tex.set_default(font_size=self.font_size)
        
        # Dot m(xm,ym)        
        m = Dot(
                point=axes.c2p(xm,ym), 
                #radius=.5*self.scale, 
                radius=min(.05*abs(ym), .05*self.scale), 
                color=GREEN
        )
        
        # tick on [a,b] with xm label
        # half the size of the bounds
        tick_length = .25 * self.scale
        #tick_length = .05*abs(ym)
        mtick = Line(
                start=axes.c2p(xm,tick_length),
                end=axes.c2p(xm,-tick_length),
                color=GREEN,
                stroke_width=3*self.scale,
        )
        mlabel = (Tex(f"{self.comma(xm)}", color=GREEN).next_to(mtick, direction=-sign_of_ym*.5*self.scale*UP))
        
        # dashes lines for coordinates of m
        m_lines = axes.get_vertical_line(
                axes.c2p(xm,ym),
                #stroke_width=.5*abs(ym),
                stroke_width=2*self.scale,
                color=WHITE,
                line_config={"dashed_ratio": .5, 
                    "dash_length": abs(ym)/20,
                    "color":GREEN, 
                    #"stroke_opacity": LOW_OPACITY
                },
        )

        # show lines and point
        
        # text specifying sign of ym
        text_sign = Label(
                MathTex(f"f({self.comma(xm)})"+(">0" if ym>0 else "<0"), color=GREEN),
                frame_config={"stroke_width":self.scale, "buff":0*.05*self.scale, "color":GREEN},
                box_config={"buff":0*.05*self.scale},
        )
        text_sign.next_to(m, direction=.5*self.scale*(RIGHT-sign_of_ym*UP))
        
        # zoom in relative to the objects_in_frame group i want to keep in frame
        # soften axes and C_f
        objects_in_frame = Group(
                Dot(axes.c2p(xm,ym)),
                Dot(axes.c2p(xm,-ym)),
                self.alabel,
                self.atick,
                self.blabel,
                self.btick,
                text_sign
        )

        self.play(
                self.camera.auto_zoom(objects_in_frame),
                self.axes.animate.set_stroke(width=2*self.scale),
                self.f_graph.animate.set_stroke_width(2*self.scale),
                self.atick.animate(run_time=.5).set_stroke_width(4*self.scale).scale(scale_factor),
                self.alabel.animate(run_time=.5).set_font_size(self.font_size).next_to(self.atick, .5*self.scale*UP),
                self.btick.animate(run_time=.5).set_stroke_width(4*self.scale).scale(scale_factor),
                self.blabel.animate(run_time=.5).set_font_size(self.font_size).next_to(self.btick, .5*self.scale*DOWN),
        )
        
        """
        # this sucks because it's one iterate behind what it should be
        # because i generate text before zooming in...
        new_width = self.camera.frame.width
        self.width_ratio = new_width/self.frame_width
        self.frame_width = new_width
        """

        # wait after zoom a bit
        self.wait(.5)

 
        # show tick and label
        self.play(Create(mtick),FadeIn(mlabel))

        self.play(Create(m_lines))
        self.play(Create(m))

        self.wait()

        # text specifying sign of ym
        self.play(FadeIn(text_sign))
        
        self.wait()

        # remove in order
        self.play(FadeOut(text_sign))
        self.play(Uncreate(m))
        self.play(Uncreate(m_lines))
        
        # if ym < 0: fadeout objects associated to a and replace them by objets of m
        if ym < 0:
            # fade out all a stuff
            # turn mtick red
            self.play(
                    FadeOut(self.a),
                    Uncreate(self.atick),
                    FadeOut(self.alabel),
                    mtick.animate(run_time=.5).set_color(RED),
                    mlabel.animate(run_time=.5).set_color(RED).set_opacity(LOW_OPACITY),
            )
            
            # scale btick down, move and soften blabel
            """            
            self.play(
                    self.btick.animate(run_time=.5).set_stroke_width(4*scale_factor).scale(.5),
                    self.blabel.animate(run_time=.5).set_font_size(self.font_size).next_to(self.btick, .5*scale_factor*DOWN)
            )
            """

            # replace a by m
            self.a = m
            self.atick = mtick
            self.alabel = mlabel

        # if ym > 0: fadeout objects associated to b and replace them by objets of m
        else:
            # fade out all b stuff
            # turn mtick red
            self.play(
                    FadeOut(self.b),
                    Uncreate(self.btick),
                    FadeOut(self.blabel),
                    mtick.animate(run_time=.5).set_color(BLUE),
                    mlabel.animate(run_time=.5).set_color(BLUE).set_opacity(.2),
            )

            # scale atick down, move and soften alabel
            """            
            self.play(
                    self.atick.animate(run_time=.5).set_stroke_width(4*self.scale).scale(.5),
                    self.alabel.animate(run_time=.5).set_font_size(self.font_size).next_to(self.atick, .5*self.scale*DOWN)
            )
            """
            
            # replace b by m
            self.b = m
            self.btick = mtick
            self.blabel = mlabel

        # recursion :)
        if ym < 0:
            return self.dichotomie(xm, b)
        return self.dichotomie(a, xm) 

    def construct(self):
        self.font_size = 48
        self.scale = 1
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
                    "stroke_width": 2,
                    "stroke_opacity": .3,
                },
        )
    
        #axes.add_coordinates()

        self.play(Create(axes))

        # graph and labels
        f_graph = axes.plot(
                lambda x: self.f(x), # referencing self.f directly create an error?
                x_range=[-4,4, 0.01],
                color=GOLD,
                stroke_width=2,
        )
        equation = Label(MathTex("y = x^2 - 7"))
        equation.move_to(axes.c2p(6.5,7), RIGHT)

        self.play(Create(f_graph), Create(equation))
        
       
        # ticks
        tick_length = .25 * self.scale
        self.atick = Line(start=axes.c2p(0,tick_length), end=axes.c2p(0,-tick_length), color=RED, stroke_width=4)
        self.btick = Line(start=axes.c2p(3,tick_length), end=axes.c2p(3,-tick_length), color=BLUE, stroke_width=4)
       
        self.play(Create(self.atick), Create(self.btick))

        self.alabel = (Tex("0", color=RED).next_to(self.atick, direction=LEFT + UP))
        self.blabel = (Tex("3", color=BLUE).next_to(self.btick, direction=DOWN))
        self.play(Create(self.blabel), Create(self.alabel))

        # a and b lines
        a_lineV = axes.get_vertical_line(
                axes.c2p(0,self.f(0)),
                stroke_width=5*self.scale,
                color=RED,
                line_config={"dashed_ratio": .5, "dash_length": 7/20},
        )
        a_lineH = axes.get_horizontal_line(
                axes.c2p(0,self.f(0)),
                stroke_width=5*self.scale,
                color=RED,
                line_config={"dashed_ratio": .5, "dash_length": 7/20},
        )


        b_lineV = axes.get_vertical_line(
                axes.c2p(3,self.f(3)),
                stroke_width=5*self.scale,
                color=BLUE,
                line_config={"dashed_ratio": .5, "dash_length": 2/20},
        )
        b_lineH = axes.get_horizontal_line(
                axes.c2p(3,self.f(3)),
                stroke_width=5*self.scale,
                color=BLUE,
                line_config={"dashed_ratio": .5, "dash_length": 2/20},
        )
        
        # dots a(x=0) and b(x=3)
        a = Dot(point=axes.c2p(0,-7), radius=.05*self.scale, color=RED)
        b = Dot(point=axes.c2p(3,2), radius=.05*self.scale, color=BLUE)
            
        # f(a), f(b) texts
        text_signA = Label(MathTex("f(0)<0", color=RED))
        text_signA = text_signA.next_to(a, direction=LEFT)
        text_signB = Label(MathTex("f(3)>0", color=BLUE))
        text_signB = text_signB.next_to(b, direction=RIGHT)
        
        # show a, b lines then dots and signs f(.)
        self.play(Create(b_lineV))
        self.play(Create(b))
        self.play(Create(b_lineH), Write(text_signB))
        
        self.play(Create(a_lineV))
        self.play(Create(a))
        self.play(Create(a_lineH), Write(text_signA))

        self.wait()

        # remove everything in reverse order except ticks and labels
        self.play(
                FadeOut(text_signA),
                FadeOut(text_signB),
                Uncreate(b),
                Uncreate(a),
                Uncreate(b_lineH),
                Uncreate(b_lineV),
                Uncreate(a_lineH),
                Uncreate(a_lineV),
                FadeOut(equation),
        )
        
        # lower opacity of a, b labels
        self.play(
                self.alabel.animate.set_opacity(LOW_OPACITY), 
                self.blabel.animate.set_opacity(LOW_OPACITY),
        )

        # def class objects 
        self.a = a
        self.b = b
        self.axes = axes
        self.f_graph = f_graph
        self.frame_width = self.camera.frame.width
        self.width_ratio = .5  
        self.ym = self.f(1.5)

        self.precision = .01

        # recursive dichotomy
        self.dichotomie(0, 3)





