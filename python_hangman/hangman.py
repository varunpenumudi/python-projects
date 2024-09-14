import random

HANGMANS = [
'''
+---+
|   |   
|    
|   
|   
|       
=========
''',

'''
+---+
|   |   
|   O   
|   
|    
|       
=========
''', 

'''
+---+
|   |   
|   O   
|   | 
|   
|       
=========
''',

'''
+---+
|   |   
|   O   
|  /|
|   
|       
=========
''', 

'''
+---+
|   |   
|   O   
|  /|\  
|    
|       
=========
''', 

'''
+---+
|   |   
|   O   
|  /|\  
|  /   
|       
=========
''', 

'''
+---+
|   |   
|   O   
|  /|\  
|  / \  
|       
=========
'''
]

l = len(HANGMANS)-1

libraries = [
    "pandas", "tensorflow", "keras", "sklearn", "scipy", 
    "numpy", "pytorch", "pil", "django", "flask", "fastapi",
]

you_lost = ''' 
 __   __  _______  __   __     ___      _______  _______  _______ 
|  | |  ||       ||  | |  |   |   |    |       ||       ||       |
|  |_|  ||   _   ||  | |  |   |   |    |   _   ||  _____||_     _|
|       ||  | |  ||  |_|  |   |   |    |  | |  || |_____   |   |  
|_     _||  |_|  ||       |   |   |___ |  |_|  ||_____  |  |   |  
  |   |  |       ||       |   |       ||       | _____| |  |   |  
  |___|  |_______||_______|   |_______||_______||_______|  |___|  
'''

you_won = '''
 __   __  _______  __   __     _     _  _______  __    _ 
|  | |  ||       ||  | |  |   | | _ | ||       ||  |  | |
|  |_|  ||   _   ||  | |  |   | || || ||   _   ||   |_| |
|       ||  | |  ||  |_|  |   |       ||  | |  ||       |
|_     _||  |_|  ||       |   |       ||  |_|  ||  _    |
  |   |  |       ||       |   |   _   ||       || | |   |
  |___|  |_______||_______|   |__| |__||_______||_|  |__|                                                                                          
'''


def write_man(state, res):
    word = " ".join(res)
    with open("hangman.txt", "w") as file:
        file.write(HANGMANS[state])
        file.write("\n")
        file.write("LIBRARY: ")
        file.write(word)

# choose a random library from the list of python libraries
random_library = random.choice(libraries)

# store the indexes of letter in a hashmap
char_index = {}
for i,c in enumerate(random_library):
    if c in char_index:
        char_index[c].append(i)
    else:
        char_index[c] = [i]

# variables to track the current state of user
cur_state = 0
cur_res = ["_"]*len(random_library)

# Draw the initial hangman
write_man(cur_state, cur_res)


# ASK the Person to Guess the letters in word until WIN/LOST situation occurs
while cur_state<l and "".join(cur_res) != random_library.upper():
    c = input("guess one of the remaining letters: ").lower()

    # if guessed letter is in the word display the letter at it's position in the word
    if char_index.get(c):
        idx = char_index[c].pop()
        cur_res[idx] = random_library[idx].upper()
    # continue drawing hangman otherwise
    else:
        cur_state += 1
    
    # Draw the current hangman
    write_man(cur_state, cur_res)


# if the hangman is fully drawn YOU LOST the game
if cur_state == l:
    with open("hangman.txt", "w") as file:
        file.write(HANGMANS[l])
        file.write("\n")
        file.write(you_lost)
# if guessed the word before the hangman is drawn YOU WON the game
else:
    with open("hangman.txt", "a") as file:
        file.write("\n")
        file.write(you_won)