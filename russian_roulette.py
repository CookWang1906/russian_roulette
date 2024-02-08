import random
def pick():
    n = int(input("Pick how many times you want to try: "))
    die = random.randint(1,6)
    
    if n < die:
        print("You have survived!")
    elif n <= 0:
        print("TRY AGAIN!")
        return pick()
    else: #why else? > die, = die
        print("YOUR A DEATH MAN!")
pick()