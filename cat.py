def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n # immediately stop the funtion which also stops the loop

def meow(n):
    for _ in range(n): # naming it _ instead of i which shows that we are not using the variable
        print ("meow")