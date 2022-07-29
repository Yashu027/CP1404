import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?"""
# 19 (random integers)
# smallest is 5 and largest is 20

"""What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?"""
# 3 (random integers)
# smallest is 3 and largest is 9
# No, line 2 did not produce a 4

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# 2.5142141014826205 (random float number)
# smallest is 2.5 and largest is 5.5

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
print(random.randint(1, 100))
