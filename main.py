import random
from data import stages, word_list

letter = random.choice(word_list)
print(f"Word is {letter}")  # just for Testing purpose

under_scores = ["_" for _ in range(len(letter))]
index = []
stage = 6
is_on = True

while is_on:
    word = input("Guess a letter: ")
    if word in letter:
        for n in range(0, len(letter)):
            if letter[n] == word:
                under_scores[n] = word
        print(" ".join(under_scores))
        if "_" not in under_scores:
            is_on = False
            print("You Won")
    else:
        print(stages[stage])
        stage -= 1
        if stage >= 0:
            print(f"you have {stage + 1} Lives Remaining")
        else:
            is_on = False
            print("Game Over")
