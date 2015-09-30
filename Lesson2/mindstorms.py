import turtle
#learning module with graphics of a turtle
def draw_square():

  #creates a screen for turtle called window
  window = turtle.Screen()
  window.bgcolor("blue")


  #create an instance of a turtle
  brad = turtle.Turtle()
  #move turtle forward steps

  brad.shape("turtle")
  brad.color("purple")
  brad.speed(2)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  window.exitonclick()


draw_square()
