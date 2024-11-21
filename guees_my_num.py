import random
def my_num():
    attempts = 0
    total_attempts = 5
    my_num = random.randint(0,99)
    while attempts<total_attempts:
        print(f"{total_attempts}-{attempts}")
        attempts+=1
        # my_num = random.randint(0,99)
        try:
            guess = int(input("what will be the number:"))
        except Exception as e:
            print(e)
        if guess == my_num:
            print("you are right!congratulations")
            continue
        elif guess < my_num:
            print("your number is too low")
        elif guess > my_num:
            print("your number is too high")
        
        if attempts == total_attempts and guess != my_num:
          print(f"You've used all attempts. The actual number was {my_num}")
my_num()
        