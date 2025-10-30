import random
n = random.randint(1, 101)
a = -1
guesses = 0

while(a != n):
    guesses +=1
    a = int(input("Guess a Number: "))
    if a > n:
        print("Lower Number Plz!")
    elif a < n:
        print("Higher Number Plz!")
    else:
        print(f"Congrats! You Got it, you guessed {guesses} Time")        


