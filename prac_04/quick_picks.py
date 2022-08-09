import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("That makes no sense!")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
