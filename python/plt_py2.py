#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# The Pyg Latin Translator from Codecademy written for Python 2 and modified

import sys

pyg = "ay"

print "Welcome to the Pyg Latin Translator"
print "Type #about to learn what the PTL actually does."
print "Type #exit to quit the program.\n"

while True:
    original = raw_input("Enter a word: ")
    word = original.lower()
    first = word[0]
    new_word = word + pyg

    if original == "#about":
        print "\nThe Pyg Latin Translator is an easy and fun Python project for beginners.\n"
        print "When a word is entered that begins with a vowel,"
        print "the translator appends the word ‘ay’ to it like so: Amadeus > amadeusay"
        print "If the input has got a consonant as its first letter, the translator takes it away,"
        print "appends it to the end of the word and adds ‘ay’ to the consonant.\n"
        print "Example: Foobar > oobarfay"
        print "Another task of the PTL is converting all given input to lowercase.\n"

    elif original == "#exit":
        sys.exit(0)

    elif len(original) > 0 and original.isalpha():
        if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
            print "\n" + new_word + "\n"
        else:
            new_word = word[1:] + first + pyg
            print "\n" + new_word + "\n"
    else:
        print "\nYou entered more than one word or no words at all!\n"
