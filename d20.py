import random

difficulty_scale = [10, 15, 20, 25, 30]
difficulty = random.choice(difficulty_scale)
dice = random.randint(1,20)
positive_mod = 5


apply_bonus = input("apply bonus?\n> ")
match apply_bonus:
    case 'yes':
        total = dice+positive_mod
        print(f"Difficulty: {difficulty}\nYour roll: {dice} + {positive_mod}\nTotal: {total}")
        match dice:
            case 20:
                print("Critical Success.")
            case 1:
                print("Critical Failure.")
            case _ if total >= difficulty:
                print("Success")
            case _:
                print("Unsuccessful.")
    case _:
        print(f"Difficulty {difficulty}\nYour roll: {dice}")
        match dice:
            case 20:
                print("Critical Success.")
            case 1:
                print("Critical Failure.")
            case _ if dice >= difficulty:
                print("Success")
            case _:
                print("Unsuccessful.")
