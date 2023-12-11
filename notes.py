from datetime import date
import os
import re

def make_list():
    title = input("enter to-do list name: ")
    f = open(f"{title}.txt", "x")
    with open(f"{title}.txt", "w") as f:
        date_made = date.today().strftime("%B %d, %Y")
        f.write(f"Date: {date_made}\n\n")
        num_task = int(input("enter # of tasks: "))
        for item in range(1, num_task+1):
            task = input(f"task # {item}: ").capitalize()
            f.write(f"-{task}\nComplete [] - Incomplete []\n\n")
        print("List created.")
        return title
    
def modify_list():
    text_files = [file for file in os.listdir() if file.endswith(".txt")]
    print("Available lists: ")
    for text_file in text_files:
        print(text_file)
    title = input("enter list name to modify: ")
    try:
        with open(f"{title}.txt", "r") as f:
            content = f.read()
            print(f"current items:\n{content}")
    except FileNotFoundError:
        print(f"{title} does not exist.")
            

modify_list()

# while True:
#     user_input = input("[1] to create\n[2] to adjust\n[3] to exit\n")
