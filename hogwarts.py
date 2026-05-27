#hogwarts
#program asks for a name and assigns that person to one of the four harry potter houses

#init
import time
import random

#functions
def main():
    while True:
        print("welcome to Hogwarts")
        name = input("Enter your name: ").lower()
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print(".......")
        print(house(name))
        ask = input("Do you want to play again? (yes,no): ").lower()
        if ask == "yes":
            print("Okay, restarting")
            continue
        if ask == "no":
            print("Okay, goodbye")
            break
    #house(name) will return one of the four houses
def house(name):
    if name == "harry" or name == "ron" or name =="hermione":
        return "Gryffindor"
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return "Hufflepuff"
    elif name == "luna" or name == "cho" or name == "filius":
        return "Ravenclaw"
    elif name == "severus" or name == "draco" or name == "voldemort":
        return "Slytherin"
    else:
        x = random.randint(1,4)
        if x == 1:
            return "Gryffindor"
        if x == 2:
            return "Hufflepuff"
        if x == 3:
            return "Ravenclaw"
        if x == 4:
            return "Slytherin"

#main
main()
