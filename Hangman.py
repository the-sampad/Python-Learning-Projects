import os
import random
def listToString(s): 
    string = "" 
    for element in s:
        string += element 
    return string 
movies = ['skyfall','quantum','spectre','casino','royale','solace']
random_movie = random.choice(movies)
random_movie = list(random_movie)
lives = 6
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman.reverse()
k = ''
for i in range(len(random_movie)):
    k+='-'
print(k)

sk = k
j = list(k)

for i in range(2*len(random_movie)):
    
    guess = input(f"Guess a letter of the word ({lives} lives remaining): ")
    os.system('cls')
    if guess in random_movie:
        for i in range(len(random_movie)):
            a = random_movie[i]
            if guess == a:
                j.pop(i)
                j.insert(i,a)
        sk = listToString(j)
        print('word :',sk)
    
    if sk == listToString(random_movie):
        print("|| YOU WIN || Remaining lives = ",lives)
        print(hangman[lives])
        break
    
    elif guess not in random_movie:
        lives-=1
        print(f'\n=========\nWRONG !! {guess} is not present in the word. You lose a life. Remaining Lives : ',lives)
        print('word :',sk)
        if lives == 0:
            print('Person Hanged. || GAME OVER ||')
            print(hangman[lives])
            break
    print(hangman[lives])