from wonderwords import RandomWord

def ask(lives, w):
    
    if lives == 0:
        return "Dead"
    if "_" not in display:
        return "Won"
    lg = input("Enter your new letter guess: ")
    if lg in w:
        pos = w.index(lg)
        w[pos] = lg
        print(f"The letter {lg} comes in my word! Now my new word is {w}.")
        print(f"You have {lives} more live, they stay the same as before since you got it right.")
        return ask(lives, w)
    elif lg not in w:
        lives -=1
        print(f"Sorry! {lg} is not in my word")
        print(f"Now you have {lives} lives left.")
        return ask(lives, w)
            
    

def deathword(word, chc):
    if chc == 1: #Choice one is where the user guesses the word, choice 2 is where the computer guesses.
        print("Ok. Do you want to go:\n   Level Easy => 5 Letters\n   Level Medium => 6 Letters\n   Level Hard => 7 Letters?")
        while True:
            try:
                lvl = int(input("Please enter 5, 6, or 7 for Easy, Medium, or Hard respectively:  "))
                if lvl in [5,6,7]:
                    print(f"{lvl}! That's a good one.")
                    break
                elif lvl not in [5,6,7]:
                    if type(lvl) == float:
                        print("Aww hellna no decimal numbers here!")
                    print("5 is for Easy(A 5 lettered word), 6 is for Medium(A 6 lettered word), and 7 is for Hard(A 7 lettered word).")
            except:
                print("Blah")