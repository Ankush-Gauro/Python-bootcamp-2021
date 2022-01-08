import random
def hangman():
    word = random.choice(["jon", "thor", "harry", "ragnar","jack", "sherlock", "batman", "thomas", "star", "ertugrul"])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("Yay! you won!")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid chareacter:")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left!")
                print(" --------- ")
            if turns == 8:
                print("8 turns left!")
                print("  ---------  ")
                print("      0      ")
            if turns == 7:
                print("7 turns left!")
                print("  ---------  ")
                print("      0      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left!")
                print("  ---------  ")
                print("      0      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left!")
                print("  ---------  ")
                print("      0      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left!")
                print("  ---------  ")
                print("    \ 0      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left!")
                print("  ---------  ")
                print("    \ 0 /    ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left!")
                print("  ---------  ")
                print("    \ 0 /|   ")
                print("      |      ")
                print("     / \     ")
            if turns == 1:
                print("Only 1 turn left!")
                print("Last breaths counting, take care!")
                print("  ---------  ")
                print("    \ 0_|/    ")
                print("      |      ")
                print("     / \     ")
            if turns == 0:
                print("You loose :(")
                print("You let an innocent man die! \n Game Over!")
                print("  ---------  ")
                print("      0_|    ")
                print("     /|\     ")
                print("     / \     ")
                break
            


name = input("Enter your name:")
print("Welcome", name)
print("----------------")
print("Try to guess the movie/series character in less than 10 attempts")
hangman()
print()