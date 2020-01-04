hp = 30

def get_input(prompt, accepted):
    while True:
        value = input(prompt).lower()

        if value in accepted:
            def handle_room(location):
                global hp

                if location == "start":

                    print("You are standing on a path at the edge of a jungle. There is a cave to your left and a beach to your right")
                    direction = get_input(" do you want to go left or right?\n", ["left", "right"])

                    if direction == "left":
                        return "cave"
                    elif direction == "right":
                        return "beach"

                elif location =="cave":
                    print("you walk to a cave and notice there is an opening")
                    print("a small snake bites you and you lose 20 HP")
                    hp = hp - 20

                    answwer = get_input("do you want to go deeper", ["yes", "no"])
                    if answer == "yes":
                        return "deep_cave"
                    else:
                        return "start"

                elif location == "beach":
                    print("you walk to the beach but remember you do no0t have any swimewear")
                    print("The cool water revitalizes you. You never felt mopre alive. you gain 70 HP")
                    hp += 70

                    return "end"

                else:
                    print("programmer error, room", location, "is unkown")
                    return "end"

            location = "start"
            while location != "end":
                location = handle_room(location)

                print(" you now have ", hp, "hp.")
                if hp <= 0:
                    print("you are dead. I am sorry")
                    break
            print("Your adventure has ended, goodbye")
    
