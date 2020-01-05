import sys
from random import randint

movies = ['tron', 'et', 'blade runner', 'game of thrones']

print (movies)

randomIndex = randint(0,len(movies)-1)
movie  = movies[randomIndex]

words = movie.split(' ')

for word in words:
  print ('-' * len(word)),
  print(' '),

guesses = []
livesLost = 0

while 1:
  guess = sys.stdin.readline()

  print (len(guess))
  print (movie)
  if guess[0] in movie:
    print ('yes')
    guesses.append(guess)
  else:
    print ('no')
    livesLost +=1

def fred(guesses, movie):
  for letter in movie:
    if letter in guesses:
      print(letter),
    else 
      print('-')

      


    