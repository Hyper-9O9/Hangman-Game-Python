import random

print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                    \n """)

# in this version you can only guess by letters not an entire sentence


def drawHangman(position):
    HANGMAN_PICS = [r"""
    +--+
    |  |
       |
       |
       |
       |
    =====""",
     r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    print(HANGMAN_PICS[position])



# the list of possible words to be chosen from
word_list = ["apple", "banana", "orange", "strawberry", "pineapple",
             "jackfruit", "peach", "apricot", "fig", "pear"]
# randomly picking a word from the list
chosen_word = random.choice(word_list)

# answer shows the user the place of the letters
answer = []
#  in hangman after 6 wrong answers you lose
tries = 6
# counter for counting if the user got the correct answer
answer_counter = 0
# progress is a variable for checking if the answer is the same as chosen word
progress = ""
animation = 0
# populate answer list with spaces
for _ in range(len(chosen_word)):
    answer += "_"


# game starts, it will continue till life is not equal to zero
while tries != 0:
    # getting user input
    guess = input("Guess the word: ").lower()
    # going through the chosen word letters

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # if the guessed letter is in the chosen word, add it to answer
        if guess == letter:
            answer[position] = letter
        elif guess != letter:
            answer_counter += 1
        # combine shows how many words the user got right
        progress += answer[position]

    print(progress)
    # if combine and chosen word are equal then the user won
    if progress == chosen_word:
        print("You win!")
        break
    progress =""
    # if answer counter is not equal to the length of chosen word, user got the letter correct
    if answer_counter == len(chosen_word):
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        tries -= 1
        animation += 1
    #after answering draws the hangman
    drawHangman(animation)
    answer_counter = 0

exit = input("Press enter to exit: ")

