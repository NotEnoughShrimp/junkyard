# TODO: Probability is the likelihood of an event occurring.
# The find the the probably of an event happening we use the
# formula: Probably = Number of desired outcomes/total number of outcomes
# P = probability. D = Desired outcome. O = Outcome. Therefore P=D/O
# Probabilities range from 0 to 1. If P = 0, it is impossible. If
# P = 1 then it is certain. P is probability of an event.

import random

# possible_outcomes = random.randint(0,101)
# a = int(input("How many attempts do you have?\n> "))
# o = possible_outcomes
# probability = a/o*100
# rounded_probability = round(probability, 2)

# print(f"There is a {rounded_probability}% chance.")
# print(f"total possibilities: {o}")

def test():
    possible_outcomes = random.randint(0,101)
    a = int(input("How many attempts do you have?\n> "))
    o = possible_outcomes
    probability = a/o*100
    rounded_probability = round(probability, 2)
    if probability != 0:
        print(f"There is a {rounded_probability}% chance.")
    print(f"total possibilities: {o}")