import random 
Word_bank=['Games','Cake','Curtain','Cupboard','Steve','Silence','Kohli',"Pikachu",'Ronaldo','Pancake']
word=random.choice(Word_bank).lower()
Guessed_word=['_']*len(word)
used_letters = set()
print("All Aplphates are in Lower Case")
difficulty = input("Choose difficulty (Easy/Hard): ").lower()
if difficulty=="easy":
     attempts=7
else:
     attempts=3
responses = ["Awesome!", "Great Job!", "You're killing it!", "Legend!"]

while attempts > 0:

   
    print('\nCurrent word: ' + ' '.join(Guessed_word))

    guess = input('Guess a letter: ').lower()

    if guess in used_letters:
        print('You already guessed that letter!')
        continue
    used_letters.add(guess)
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                    Guessed_word[i] = guess
        print(random.choice(responses))
        # print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in Guessed_word:
        print("\nYay.......")
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if attempts==0:
     print('\nYou have run out of attempts! The word was: ' + word)
