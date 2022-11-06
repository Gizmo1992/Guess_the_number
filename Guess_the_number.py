from random import randint
num= randint(1, 100)
tries=8
user_name=str(input("What is your name? "))
answer=int(input(f"Welcome, {user_name} I have tought of a number between 1 and 100. Guess the number: "))
if answer == num:
    print(f"Congratulations {user_name}! You have won!")
elif answer < num:
    print("Too low")
elif answer > num:
    print("Too high")
while answer != num:
    tries -= 1
    if tries == 0:
        print(f"Sorry {user_name}, You have no more tries left. The number was {num}.")
        break
    elif tries > 0:
        print(f"You have {tries} tries left")
        answer = int(input("Guess the number: "))
        if answer < num:
            print("Too low")
        elif answer > num:
            print("Too high")
        else:
            print(f"Congratulations {user_name}, You have won! You have guessed it it in {8-tries} attempts!")






