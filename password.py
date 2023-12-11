import random

""" This is just a password generator."""

symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",",",".","<",">","?","/"]  # list of symbols for future use.

pass_length = int(input("enter password length: "))

password = [chr(random.randint(97,122)) for _ in range(pass_length)]  # generates a default pass_length list of lower case letters.


capitals = int(input("how many capital letters? ")) 

# initializes empty set.
c_position = set() 

# iterates for c-characters in range of capitals.
for c in range(capitals):
    
    # generates a random position
    position = random.randint(0, pass_length-1)
    
    # while position in c_position: generate  new position.
    while position in c_position:
        position = random.randint(0, pass_length-1)
    
    # add position into c_position. c_position goes from c_position = set() to c_position = set(random_position,...)
    c_position.add(position)
    # in that position of password, insert an ascii int equivalent of capitalized letter.
    password[position] = chr(random.randint(65,90))

numbers = int(input("how many numbers? "))
n_position = set()
for n in range(numbers):
    position = random.randint(0, pass_length-1)
    
    while position in n_position or position in c_position:
        position = random.randint(0, pass_length-1)
        
    n_position.add(position)
    password[position] = chr(random.randint(48,57))
    
num_symbols = int(input("how many symbols?\nenter 0 for no symbols. "))

# If greater than 0, follow the same as numbers and capitals. If not, move on.
if num_symbols > 0:
    s_position = set()
    for s in range(num_symbols):
        position = random.randint(0, pass_length-1)
        
        while position in s_position or position in n_position or position in c_position:
            position = random.randint(0,pass_length-1)
            
        s_position.add(position)
        password[position] = random.choice(symbols)  # the ascii values are all over the place, better to just use a list.

# A simple while loop that shuffles the finalized password 100 times.
shuffle_time = 0
while shuffle_time < 100:
    random.shuffle(password)
    shuffle_time += 1
    
print(''.join(password))  # finally, prints out the password.

