import turtle
 
n = 5
turtle.shape('turtle')
for i in range(n):
    turtle.forward(100)
    turtle.right((360 / n) * 2)
    turtle.forward(100)
    turtle.left(360 / n)