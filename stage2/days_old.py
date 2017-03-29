
daysOfMonths = {
1: 31, 
2: 28, 
3: 31, 
4: 30, 
5: 31, 
6: 30, 
7: 31, 
8: 31, 
9: 30, 
10: 31, 
11: 30, 
12: 31
}

def IsLeapYear(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
   		return False
   	elif year % 4 == 0:
   		return True
   	return False

def daysInMonth (year, month):
	if IsLeapYear(year) and month == 2:
		return 29
	return daysOfMonths.get(month)

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	days_count = 0 
	if y1 == y2: 									#case where the beginning and ending year are the same
		days_count += daysInMonth (y1, m1) - d1 	#add days remaining in m1
		for m in range (m1 + 1, m2): 				#add days in months between m1 and m2
			days_count += daysInMonth(y1, m)
		days_count += d2 							#add days in m2
		return days_count
		quit()
	for y in range (y1, y2 + 1): 					#case where the beginning and ending year are not the same
		if y == y1:
			days_count += daysInMonth (y1, m1) - d1
			for m in range (m1 + 1, 13):
				days_count += daysInMonth(y1, m)
		if y not in (y1, y2):
			for m in range (1, 13):
				days_count += daysInMonth(y, m)
		if y == y2:
			for m in range (1, m2):
				days_count += daysInMonth(y2, m)
			days_count += d2
	return days_count



'''
#Instructor's Approach

DaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def IsLeapYear(year):
    #if year in range (0, 3000, 4):
    if year % 400 == 0:
        return True
    elif year % 100 == 0: 
    	return False
    elif year % 4 == 0:
    	return True
    return False

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if IsLeapYear(year):
        DaysInMonth[1] = 29
    else: 
        DaysInMonth[1] = 28
    if day < DaysInMonth[month-1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

#print nextDay(2016, 2, 28)
#print nextDay(2015, 2, 28)
      
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print daysBetweenDates(1900,1,1,1999,12,31)
'''

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
