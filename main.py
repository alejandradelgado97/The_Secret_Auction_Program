from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

auction = {}

biders = "yes"
while biders == "yes":
  name = input("What is your name? ")
  dollar = int(input("What is you bid? $"))
  auction[name] = dollar
  biders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  clear()
    
number = 0
for money in auction:
  if auction[money] > number:
    number = auction[money]
    winner = money

print(f'The winner is {winner} with a bid of ${number}')



