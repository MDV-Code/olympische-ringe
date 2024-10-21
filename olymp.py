from turtle import Turtle

RADIUS_OLYMP = 100

class OlympischeRinge(Turtle):
    def __init__(self, screen):
        
        self.zeichne_ringe(screen)
    
    def zeichne_ringe(self, screen):
        screen.tracer(0)
        self.blauer_ring()
        self.gelber_ring()
        self.schwarzer_ring()
        self.gruener_ring()
        self.roter_ring()
        self.blauer_ring2()
        self.gelber_ring2()
        self.schwarzer_ring2()
        self.gruener_ring2()
        screen.update()
        
    def blauer_ring(self):
        blau = Turtle("circle")
        blau.color("blue")
        blau.penup()
        blau.goto(-220,0)
        blau.hideturtle()
        blau.pendown()
        blau.pensize(15)
        blau.speed(speed="slowest")
        blau.circle(RADIUS_OLYMP)
        
    
    def gelber_ring(self):
        gelb = Turtle("circle")
        gelb.color("yellow")
        gelb.penup()
        gelb.goto(-100,+100)
        gelb.hideturtle()
        gelb.pendown()
        gelb.pensize(15)
        gelb.speed(speed="fast")
        gelb.circle(-RADIUS_OLYMP)

    def schwarzer_ring(self):
        schwarz = Turtle("circle")
        schwarz.color("black")
        schwarz.penup()
        schwarz.goto(20,0)
        schwarz.hideturtle()
        schwarz.pendown()
        schwarz.pensize(15)
        schwarz.circle(RADIUS_OLYMP)
        
    def gruener_ring(self):
        gruen = Turtle("circle")
        gruen.color("green")
        gruen.penup()
        gruen.goto(140,100)
        gruen.hideturtle()
        gruen.pendown()
        gruen.pensize(15)
        gruen.circle(-RADIUS_OLYMP)
    
    def roter_ring(self):
        rot = Turtle("circle")
        rot.color("red")
        rot.penup()
        rot.goto(260,0)
        rot.hideturtle()
        rot.pendown()
        rot.pensize(15)
        rot.circle(RADIUS_OLYMP)
        
    def blauer_ring2(self):
        blau = Turtle("circle")
        blau.color("blue")
        blau.penup()
        blau.goto(-220,0)
        blau.hideturtle()
        blau.pensize(15)
        blau.speed(speed="slowest")
        blau.penup()
        blau.circle(RADIUS_OLYMP, 55)
        blau.pendown()
        blau.circle(RADIUS_OLYMP,40)
        
    
    def gelber_ring2(self):
        gelb = Turtle("circle")
        gelb.color("yellow")
        gelb.penup()
        gelb.goto(-100,+100)
        gelb.hideturtle()
        gelb.pensize(15)
        gelb.speed(speed="fast")
        gelb.penup()
        gelb.circle(-RADIUS_OLYMP, 0)
        gelb.pendown()
        gelb.circle(-RADIUS_OLYMP, 50)

    def schwarzer_ring2(self):
        schwarz = Turtle("circle")
        schwarz.color("black")
        schwarz.penup()
        schwarz.goto(20,0)
        schwarz.hideturtle()
        schwarz.pensize(15)
        schwarz.penup()
        schwarz.circle(RADIUS_OLYMP, 55)
        schwarz.pendown()
        schwarz.circle(RADIUS_OLYMP,40)
        
    def gruener_ring2(self):
        gruen = Turtle("circle")
        gruen.color("green")
        gruen.penup()
        gruen.goto(140,100)
        gruen.hideturtle()
        gruen.pensize(15)
        gruen.penup()
        gruen.circle(-RADIUS_OLYMP, 0)
        gruen.pendown()
        gruen.circle(-RADIUS_OLYMP, 50)