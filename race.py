# Initial Conditions
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake
import random

# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
    x = random.randint(1,3)
    e = random.randint(1,10)
    number = random.randint(1,100)
    tortoise_pos = tortoise_pos + x
    if number <= 30:
        is_hare_asleep = True
    if number >= 31:
        is_hare_asleep = False
        hare_pos = hare_pos + e
    print("🐢 - ", tortoise_pos, " | 🐇 - ", hare_pos)

if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")

