#! /usr/bin/env python
# filename:

def main():
    print "Guess a number between 1 an 100"
    randomNumber = 30
    found  = False
    while not found:
        userGuess = input("Your Guess: ")
        if userGuess == randomNumber:
            print "You got it!"
        else:
            print "That's not it."
            
           
if __name__ = "__main__":
    main()

