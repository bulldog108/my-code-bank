import turtle
bob= turtle.Turtle()
bob.color("darkgreen")
bob.pensize(10)
bob.shape("turtle")

print (range(5,100,2))
for size in range(5,100,2):
    bob.forward(size)
    bob.left(25)
    
       
