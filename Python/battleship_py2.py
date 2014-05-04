#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Python 2 version of the Codecademy battleship game

"""
Extra Credit

You can also add on to your Battleship! program to make it more complex and fun to play.
Here are some ideas for enhancements—maybe you can think of some more!

    01. Make multiple battleships: you'll need to be careful because you need to make sure
        that you don’t place battleships on top of each other on the game board.
        You'll also want to make sure that you balance the size of the board
        with the number of ships so the game is still challenging and fun to play.

    02. Make battleships of different sizes: this is trickier than it sounds.
        All the parts of the battleship need to be vertically or horizontally touching and
        you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

    03. Make your game a two-player game.

    04. Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson.
Think about coming back to Battleship! after a few more lessons and see what other changes you can make!
"""

# Another idea: Simple multiplayer functionality

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Codecademy inspired CLI Python battleship game\n"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if guess_row < 0 or guess_row > len(board) - 1 or guess_col < 0 or guess_col > len(board[0]) - 1:
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        print "Turn: " + str(turn + 1)
        print_board(board)

        if turn == 3:
            print "\nGame Over"
