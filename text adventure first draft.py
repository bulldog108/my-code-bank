import time
hp = 30

print("you are standing on a path at the edge of a jungle. There is a cave to your left and a beach to your right")

time.sleep(1)

direction1 = input("do you want to go left or right ?\n")

if direction1 == "left":
    print ("you walk to the cave and notice there is an opening.")

elif direction1 == "right":
    print("you walk to the beach but remember that you don't have any swimwear. ")

else:
    print("you think for a while. ")

    
