#sentence = "I had an awful day.  First, I woke up and there was a NOUN in my bed, then my son David decided to VERB all morning"

#print sentence.replace ("NOUN", "snake")

#def new_sentence(n, v):
	#sentence = sentence.replace ("NOUN", n)
	#print sentence
	#sentence = sentence.replace ("VERB", VERB)

#print new_sentence("snake", "scream")

import random

def print_random(n):
	count = 0
	random_list = []
	for number in range(n) :
		random_list.append(random.randint(0,10))
	print random_list

print_random(10)

#print "Hello"



def sum_of_3_5(n):
	threes = 0
	fives = 0
	for t in range (0, n, 3):
		threes += t
		#print threes
	for f in range (0, n, 5):
		fives += f
		#print fives
	return threes + fives 

print sum_of_3_5(10)

def sum_3_5(n):
	sum = 0
	for number in range(n):
		if number % 3 == 0 or number % 5 == 0:
			sum += number
	return sum

print sum_3_5(1000)

print 3 % 3