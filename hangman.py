import time
import random
words = ["unopiated", "pencillike", "primero", "circuitous", "moisturise", "canework", "gandzha", "outplease", "legislatively", "unrealizable", "soledad", "mammillary", "weskit", "polo", "screeching"]
preword = 'outplease'
word = random.choice(words)
while preword == word:
  word = random.choice(words)
preword = word
name = raw_input("What is your name? ")
print "Hello, " + name + ".", "Time to play Hangman! "
print"\n"
time.sleep(1)
print "Start guessing... "
guesses = ''
turns = 15
while turns > 0:
  failed = 0
  for x in word:
    if x in guesses:
      print x 
    else:
      print "-"
      failed += 1 
  if failed == 0:
    print "\n You Won!"
    break
  guess = raw_input("Guess a character: ")
  guesses += guess
  if guess not in word:
    turns -= 1 
    print "You have", + turns , 'more guesses'
  if turns == 0:
    print "You Lose!"
