# IPND Stage 2 Final Project

intro = '''####################################
Welcome to Dave's Python Challenger!
Please choose your quiz level:
0 - Easy
1 - Medium
2 - Hard 
3 - Expert
4 - Advanced

'''

quizzes = [
'''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',

'''A programming language that depends on the indenting structure in order to run properly is ___1___.
In the ___1___ language, ___2___s are like arrays that can be used to group data such as strings, numbers,
or even other ___2___s.  When defining a ___2___, it is important to separate each expression within the 
___2___ with a ___3___, and to enclose the entire ___2___ in ___4___s.''',

'''A ___1___ should be used anytime you need to repeat the same block of code more than once.  There are 
different kinds of ___1___s.  A ___2___ ___1___ should be used when a block of code should be repeated 
until a certain condition is met.  On the other hand, a ___3___ ___1___ should be used when the code should
be repeated a defined number of times, or for each element in a list.  If the loop is written such that it 
never ends, and repeats forever, this is called an ___4___ loop.''',

'''An expression that can only be evaluated as either True of False, is called a ___1___.  A ___1___ can be 
very useful for functions in which you wish to produce some output if a certain condition, or group of 
conditions is met.  ___2___ expressions are used to invoke some output WHEN a certain condition is met.
The lines of code underneath this expression should be indented and will only run WHEN the defined condition
in this expression is met.  The ___3___ statement is used after the ___2___ statement, to invoke some output 
when the ___2___ statement evaluates to False.  When using an ___2___ statement, followed by an ___3___ 
statement, the code under the ___2___ statement will be executed when the statement evaluates to the boolean
___4___, while the ___3___ code will be executed if the ___2___ statement evaluates to the boolean ___5___''',

'''There are a number of "built in" functions in the Python language.  The <string>.___1___() function takes a 
string as input and will return the starting position of that string within a larger <string>.  The 
<string>.___2___() function takes 2 strings as input and will substitute the 2nd string for the 1st string, 
wherever it exists within the larger <string>.  The ___3___() function will return a list of numbers within the
specified ___3___.  For example ___3___(5) will return a list of numbers: 0,1,2,3,4.  The ___4___() function
can be used with both strings and lists, and will return the number of characters in the string, or the number 
of elements within the list.'''
]

answers = [
	["function", "arguments", "none", "list"], 
	["python", "list", "comma", "bracket"],
	["loop", "while", "for", "infinite"],
	["boolean", "if", "else", "true", "false"],
	["find", "replace", "range", "len"]
]

quiz_type = [
"This is the easy quiz!", 
"This is the medium quiz!", 
"This is the hard quiz!", 
"This is the expert quiz!", 
"This is the advanced quiz!"
]

print intro

level = int(raw_input())
print "\n"
chances = raw_input("Please input the number of guesses you'd like to have for each question (1-10) : ")

quiz = str(quizzes[level])						#Assign the appropriate quiz, given the level chosen by the user
quiz_questions = len(answers[level])			#Detirmine the number of blanks that the user will have to fill in for the given quiz

print "\nYou have " + str(chances) + " guesses per question.\n###########################################\n" + quiz_type[level] + "\n"

def correct_answer(count):						#This function is used to derive the correct answer for each blank space
	right_answer = answers[level][count - 1]	#The level remains constant throughout the entire quiz, so it can be hard coded into the function
	return right_answer

for i in range(1, quiz_questions + 1):			#Loop through each of the blank spaces
	answer = "X"
	chance_count = int(chances)		
	while answer.lower() != correct_answer(i):	#Repeat this loop until the user gives the correct answer
		if chance_count < 1:					#End the game if the number of guesses remaining drops below 1
			print "You lose. Game over!"
			quit()
		if chance_count < int(chances):
			print "Try again!\n"
		print quiz                              #Print the quiz chosen by the user
		print "\nNumber of guesses left: " + str(chance_count) +"\n"
		answer = raw_input("Your answer for " + str(i) + ": ")
		if answer.lower() == correct_answer(i):	#If the correct answer is given, replace the blank space with the answer and move onto the next question
	 		print "\nCorrect!\n"
			fill = "___" + str(i) + "___"
			quiz = quiz.replace(fill, correct_answer(i))
	 	else:									#If the answer given by the user is not the correct answer, subtract one from the number of guesses remaining
	 		chance_count -= 1
	 		print "\nI'm sorry, that's not the correct answer\n" 

print "Great job! You passed the quiz!"


# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1
