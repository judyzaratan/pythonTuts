import turtle
#learning module with graphics of a turtle

def create_screen():
  window = turtle.Screen()
  window.bgcolor("pink")
  draw_square()
  draw_circle()
  draw_triangle()
  window.exitonclick()


def draw_square():
  #create an instance of a turtle
  brad = turtle.Turtle()
  #move turtle forward steps

  brad.shape("turtle")
  brad.color("purple")
  brad.speed(2)

  for x in range(0, 4):
    brad.forward(100)
    brad.right(90)


def draw_circle():
  angie = turtle.Turtle()
  angie.shape("arrow")
  angie.color("green")
  angie.circle(100)

def draw_triangle():
  herb = turtle.Turtle()
  herb.shape("circle")
  herb.color("blue")

  for x in range(0, 2):
    herb.forward(60)
    herb.left(180 - 60)
  herb.forward(60)

create_screen()
