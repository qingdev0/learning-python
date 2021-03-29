#!/usr/bin/env python
###################################################################################################
# file name : exercise/20201225/hangman.py                                                        #
# created   : 2020-12-25                                                                          #
# tested in : Python 3.6.4                                                                        #
###################################################################################################
import random

##########################
# backward compatibility #
##########################

# from __future__ import print_function

def hangman() :
    fruit_list = ["apple", "mango", "banana", "orange", "kiwi", "cherry", "pear", "grape", "lemon", "melon"]
    word = fruit_list[random.randint(0,len(fruit_list)-1)]

    wrong = 0
    stages = [ ""
             , "___________________"
             , "|         |        "
             , "|         |        "
             , "|         O        "
             , "|        /|\       "
             , "|        / \       "
             , "|                  "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman. Guess a popular fruit name please.")

    while wrong < len(stages) - 1:
        print("\n")
        mesg = "[read] guess a letter: "
        char = input(mesg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))

        if "_" in board:
            e = wrong + 1
            print("\n".join(stages[0:e]))
        else:
            print("[info] You win!")
            # print(" ".join(board))
            win = True
            break

    if not win :
        # print("\n".join(stages[0:wrong]))
        print("[oops] You lose! It was {}...".format(word))



if __name__ == '__main__':
    hangman()

#######
# EOF #
#######