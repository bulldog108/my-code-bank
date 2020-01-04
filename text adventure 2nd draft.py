import time
hp = 30

print("you are standing on a path at the edge of a jungle. There is a cave to your left and a beach to your right")
time.sleep(1)

while True:
    direction1 = input("do you want to go left or right?\n")
    direction1 = direction1.lower()
    if direction1 == "left":
        print("you walk to the cave and notice there is an opening")
        print("a small snake bites you, and you lose 20 health points.")
        hp = hp - 20
        break
    elif direction == "right":
        print("you walk to the beach but remember that you don't have any swimwear.")
        print("the cool water reavilates you. you have never felt more alive gain 70 health points")
        hp += 70
        break
    else:
        print("you think for a while")
        time.sleep(1)
print("you now have", hp, "health points")
if hp <= 0:
    print("you are dead. I'm sorry")

print("your adventure has come to an end")

    
    
