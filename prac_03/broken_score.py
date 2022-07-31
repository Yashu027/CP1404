import random


def main():
    score = float(input("Enter score: "))

    display_results(score)


def display_results(score):
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def random_result():
    return random.randint(1, 100)


random_score = random_result()

print(random_score)

if random_score > 100 or random_score < 0:
    print("Invalid score")
elif random_score >= 90:
    print("Excellent")
elif random_score >= 50:
    print("Passable")
else:
    print("Bad")

main()
