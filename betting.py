                                                          #       Betting App
import random as rd

money = 30
print('Heelo......')
print(f"Welcome to my Bet.Com!You're starting  with #{money}.")
 
while money > 0:
    print(f'current Balance:#{money}')
    guess =int(input('Enter your guess (between 1 and 10): '))
    num = rd.randint(1,10)
    print(f'The number was: {num}')
    if guess == num:
        print('Congratulations,You are in')
        money += 1
    else:
        print("Oops!That's incorrect.")
        money -= 2

    if money <= 0:
        print("Game Over! you are out of money.")

    else:
        play_again = input("Do you want to play again?(YES/NO):").lower()
        if play_again != 'yes':
            print("Thank you for playing.Your final balance is #",money)