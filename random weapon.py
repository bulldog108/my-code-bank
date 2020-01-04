import random
import time

print("You have reached an opening of a cave")

print("you decide to arm your self with a ")

time.sleep(2)

quest_item = input("think of an object\n")

print("you look in your backpack for", quest_item)

print("you could not find ", quest_item)

print ("you select any item that comes to hand from your backpack instead")
print("you are armed with a")
time.sleep(3)
               

inventory = ["torch", "pencil", "rubber band", "catapult"]

print(random.choice(inventory))
