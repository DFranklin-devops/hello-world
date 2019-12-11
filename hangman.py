import random as rnd
guesses = 5

def generate_answer():
    f = open("/usr/share/dict/words")
    lines = f.readlines()
    noquotes = [lines[i] for i in range(len(lines)) if lines[i].find('\'') == -1]
    return noquotes[rnd.randint(0, len(noquotes))][0:-1]


answer = generate_answer()
reveal = ['_'] * len(answer)
already_guessed = []
while guesses > 0 and ''.join(reveal) != answer:
    ch = input("The word is: " + ''.join(reveal) + ", please enter a guess (" + str(guesses) +") remaining: ")
    if not ch.isalpha() or len(ch) != 1:
        print("Invalid input " + ch + " please try another guess")
    elif ch in already_guessed:
        print("You already guessed " + ch + " please try a different letter")
    else:
        ch = ch.lower()
        already_guessed.append(ch)
        loc = answer.find(ch)
        if (loc == -1):
            guesses -= 1
        else:
            while (loc != -1):
                reveal[loc] = answer[loc]
                loc = answer.find(ch, loc+1)

if guesses > 0:
    print("You got it")
else:
    print("Sorry, the word was " + answer)
