import random
from art import logo

print(logo)

n = random.randint(1,100)
attempt = 0

dif = input(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPsst the number is {n}\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

if dif == "easy":
  attempt = attempt + 10
else:
  attempt = attempt + 5

def guess_again(attempt):
  if attempt>=1:
    print("Guess again")

num_guess=0
while num_guess!=n and attempt!=0:
  print(f"You have {attempt} attempts remaining to guess the number.")
  attempt -= 1
  num_guess = int(input("Make a guess: "))
  if num_guess == n:
    print(f"You got it. The answer was {num_guess}")
    break
  elif num_guess < n:
    print("Too low")
  elif num_guess > n:
    print("Too High")
  guess_again(attempt)

if attempt==0:
  print("You've run out of guesses, you lose.")