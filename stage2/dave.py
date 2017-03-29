#print "Hello"
#variable = "string"
#<string>[<starting position>:<ending position>]  #output will be characters starting in first position and ending before the last position
#<string>.find (<value you are trying to find>)  #output will be 1st starting position of the string you are trying to find
#<list>.index (<value you are trying to find>)
#<string>.replace (<old string>, <new string>)  #will only work with strings
#def <procedure> (<input>, <input>, ...):
#	return 
#	Once a return is executed within a procedure, the procedure ends and nothing else is executed
#Loops will continue to execute the <block> until the <test> evaluates to False
#	while <test>:
#		<block>
#	for <name> in <list>: #Here, the new variable <name> is assigned to each value in the <list> and then the loop ends. # a range() can be a list
#		<block>
#<list> = ['Jason', 'Male', 12]
#	mutations <list>[0] = 'Fred' #this will "mutate" the first expression in the list from "Jason" to "Fred"
#	<list>[0][1] = 'i' #This will "mutate" the 2nd character of the first expression from "a" to "i" so that "Jason" become "Jison"
#	strings cannot be mutated
#<list>.append('Blue') #This will append 'Blue' to the list  
#	<list>.append[3,4] #This will append [3,4] as a single element to the list.  Therefore, if list = [1,2] then the result will be [1,2[3,4]]
#	If you want the result to be [1,2,3,4], you can use "+"  #[1,2] + [3,4] will result in [1,2,3,4]
#len(<string>) will return the number of characters in the string
#len(<list>) will return the number of elements in the list, but this will not include if lists are created within lists
#	len[0, 1, [9, 10]] will return 3, not 4, because it evaluates [9, 10] as a single element because it is a list within the main list
#<value> in <list> #if the value is in the list, the output is True, otherwise, the output is False
#<value> not in <list> #if the value is NOT in the list, the output is True
#<variable> += 1 is equivalent to saying <variable> = <variable> + 1
#range(5) #this will return a list from 1 to 4, or [1, 2, 3, 4]
#<number> % <number>  #this will return the remainder of dividing the first number by the second number.  if num1 % num2 = 0, then num1 is a multiple of num2

'''
n = "snake"
v = "scream"

sentence =  "I had an awful day.  First, I woke up and there was a NOUN in my bed, then my son David decided to VERB all morning"

def new_sentence (n, v):
	return sentence.replace("NOUN", n).replace("VERB", v)

print new_sentence (n, v)
'''

'''
numbers_to_strings = {
	
	"1" : "one",
	"2" : "two",
	"3" : "three",
	"4" : "four",
	"5" : "five",
	"6" : "six",
	"7" : "seven",
	"8" : "eight",
	"9" : "nine",
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen",
	"16": "sixteen",
	"17": "seventeen",
	"18": "eighteen",
	"19": "nineteen",
	"20": "twenty",
	"30": "thirty",
	"40": "forty",
	"50": "fifty",
	"60": "sixty",
	"70": "seventy",
	"80": "eighty",
	"90": "ninety",
	"100": "hundred",
	"1000": "thousand"
}


def letter_counter(n):
	if n > 9999:
		return "ERROR: Dictionary only setup to handle number to string conversion up to 9999"
		quit()
	list_of_numbers = range(1, n + 1)
	sum_of_letters = 0
	string = ''
	for number in list_of_numbers:
		str_num = str(number)
		if len(str_num) in (1, 2):
			if str_num in numbers_to_strings:
				string += numbers_to_strings.get(str_num) #convert number to word
			else:
				#break down number so that we can concatenate the strings in the dictionary in order to derive the correct string
				string += numbers_to_strings.get(str_num[0] + "0") + numbers_to_strings.get(str_num[1])  
		elif len(str_num) == 3:
			string += numbers_to_strings.get(str_num[0]) + "hundred"
			if str_num[1] != "0":
				if str_num[1:] in numbers_to_strings:
					string += numbers_to_strings.get(str_num[1:])
				else:
					string += numbers_to_strings.get(str_num[1] + "0")
			if str_num[2] != "0":
				string += numbers_to_strings.get(str_num[2])
		elif len(str_num) == 4:
			string += numbers_to_strings.get(str_num[0]) + "thousand"
			if str_num[1] != "0":
				string += numbers_to_strings.get(str_num[1]) + "hundred"
			if str_num[2] != "0":
				if str_num[2:] in numbers_to_strings:
					string += numbers_to_strings.get(str_num[2:])
				else:
					string += numbers_to_strings.get(str_num[2] + "0")
			if str_num[3] != "0":
				string += numbers_to_strings.get(str_num[3])
		
	sum_of_letters = len(string) #count total number of letters
	return sum_of_letters

print letter_counter(9999)

#print numbers_to_strings



def word_transformer(word):
    new_word = word
    while new_word.find("NOUN") >= 0 or new_word.find("VERB") >= 0:
        noun = random_noun()
        verb = random_verb()
        new_word = new_word.replace("NOUN", noun, 1).replace("VERB", verb, 1)
    return new_word

#These 2 functions refer to problem 1 on project euler https://projecteuler.net/problem=1
import random

def print_random(n):
	count = 0
	random_list = []
	for number in range(n) :
		random_list.append(random.randint(0,10))
	print random_list

print_random(10)


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


7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "thousand"
}


import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

count_list = [0] * 11
index = 0

# Write code here to loop through every number in random_list and
# update count_list appropriately

for num in range(11):
    count = 0
    for number in random_list:
        if number == num:
            count += 1
        count_list[num] = count
    print count_list

print random_list




# Check the list we created
print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print sum(count_list)
'''

def rotate_left3(nums):
  result = nums[1:]
  result.append(nums[0])
  return result

print rotate_left3([1, 2, 3])