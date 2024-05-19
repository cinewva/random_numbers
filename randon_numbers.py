import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    Print 10 random numbers in the range 1 to 100.
    """
    for i in range(10):
        print(random.randint(1,100))

if __name__ == '__main__':
    main()
