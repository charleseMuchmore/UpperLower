#title art
from d_art import * 
print(logo)

#pick and display 2 random options
from c_data import * 
from random import randint
last_in_data = data[-1]
last_index = data.index(last_in_data)
# last_index += 1

    # random_index = randint(0, last_index)
optionA = data[randint(0, last_index)]

optionB = data[randint(0, last_index)]

print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}.")
print(vs)
print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}.")

#ask which one 
user_input = input("Who has a larger instagram following? Type 'A' or 'B': ")

#determine if correct
from b_functions import *
user_score = 0 
if optionA['follower_count'] > optionB['follower_count'] and user_input == 'A':
    user_score += 1
    print(user_score)
elif optionB['follower_count'] > optionA['follwer_count'] and user_input == 'B':
    user_score += 1
    print(user_score)
else:
    print("you lost")
    
#move on with one point, or not