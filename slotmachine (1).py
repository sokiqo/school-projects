#version 1.0
#a 3-Slot Machine

import random
money = 0
symbol = ['♠', '♣', '☆', '☆', '7', '♠', '♣']
slot = []

def spin():
        global money
        global spin
        for i in range(3):
            slot.append(random.choice(symbol))
        print(slot)
        if slot[0] == "♠" and "♠" == slot[1] and "♠" == slot[2]:
            print("It's a match")
            money = money + 100
            slot.clear()
        elif slot[0] == "♣" and "♣" == slot[1] and "♣" == slot[2]:
            print("It's a match")
            money = money + 100
            slot.clear()
        elif slot[0] == "☆" and "☆" == slot[1] and "☆" == slot[2]:
            print("It's a match")
            money = money + 100
            slot.clear()
        elif slot[0] == "7" and "7" == slot[1] and "7" == slot[2]:
            print("Jackpot")
            money = money + 1000
            slot.clear()
        else:
            print("You lost")
            slot.clear()

def main():
    global money
    print("Welcome to the 3-slot machine")
    print("Slot machine symbols : ['♠', '♣', '☆', '7']")
    print("It costs 10 credits per spin")
    amount = int(input("You have " + str(money) + " credits. Deposit 20, 50, or 100: "))
    money = 0 + amount
    while True:
        choice = input("Press 'S' to spin or 'Q' to quit/cash out: ")
        if choice == 'S':
            money = money - 10
            if money < 10:
                print("INSUFFICIENT FUNDS. PLEASE INSERT CREDITS.")
                continue
            elif money > 10 or money == 10:
                spin()
                print(f"You have {money} credits")
                continue
        elif choice == 'Q':
            print("Thank you for playing")
            print(f"Total credits {money} cashed out")
            break

def simulation():
    global money
    deposit = 0
    amount = int(input(f"You have {money} credits. Deposit: "))
    money = 0 + amount
    deposit = deposit + amount
    for i in range(1000):
        money = money - 10
        spin()
    print(f"Total credits spent {deposit}")
    print(f"Net profit/losses for casino: {deposit-money}")

simulation()
