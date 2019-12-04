import random
number = random.randint(0,20)

GuessTaken = 0
print("Hi There! I am thinking of a number! You will only get 5 chances to think of it!")

for GuessTaken in range(5):
    print("Guess!")
    guess = int(input())

    GuessTaken = GuessTaken + 1
    if guess > number:
        print ("Too High")
    elif guess < number:
        print ("Too Low")
    else:
        break

if guess != number:
    print("What the hell Dude the answer is ", number)
else: print("Keep Going! You Did it!")