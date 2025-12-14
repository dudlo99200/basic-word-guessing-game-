import random
name = input("Enter your name: ")
print(f"Good Luck, {name}!")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 10

#Progress logic
while turns > 0:
    failed = 0
    for i in word:
       if i in guesses:
         print(i, end=" ")
       else:
         print("_", end=" ")  
         failed += 1
    print()  

#Checking if the user won
    if failed == 0:
       print("You Win")
       print("The word is :", word)
       break

    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
       turns -= 1
       print("Wrong")
       print(f"You have {turns} more guesses")

    if turns == 0:
       print("You loose!")
