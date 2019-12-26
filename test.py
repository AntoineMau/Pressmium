#------------------------------------------------------------------------------#
# Find the smallest number
#------------------------------------------------------------------------------#

def findSmallest(ptr):
	min = ptr[0]
	for x in ptr:
		if min > x :
			min = x
	return (min)

# print(findSmallest([1, 2, 5, 9, 3, 4]))

#------------------------------------------------------------------------------#
# Order a list of numbers
#------------------------------------------------------------------------------#

def orderList(ptr):
	lenght = 0
	for x in ptr:
		lenght += 1
	i = 0
	count = 0
	while count < lenght:
		if i + 1 == lenght:
			i = 0
		if ptr[i] > ptr[i + 1]:
			tmp = ptr[i]
			ptr[i] = ptr[i + 1]
			ptr[i + 1] = tmp
			count = 0
		else:
			count += 1
		i += 1
	return (ptr)

# print(orderList([4,2,7,5,1]))

#------------------------------------------------------------------------------#
# Writing a sentence
#------------------------------------------------------------------------------#

def writeSentence(file):
	if "name" in file and "surname" in file and "age" in file:
		return ("%s %s is %d old." % (file["name"], file["surname"], file["age"]))
	else:
		return ("The dictionary don't have the good key (name | surname | age)")

d = {
"name" : "Joe",
"surname" : "Doe",
"age" : 20,
}

# print(writeSentence(d))

#------------------------------------------------------------------------------#
# Test cases
#------------------------------------------------------------------------------#

def testCase(number):
	try:
		if number == 0:
			raise ValueError("number = 0")
		else:
			return (2 * number + 1 if number % 2 == 0 else 0)
	except ValueError:
		return ("ValueError: Number = 0")

# print(testCase(1))
# print(testCase(2))

#------------------------------------------------------------------------------#
# Bonus
#------------------------------------------------------------------------------#

def isPrimeNumber(number):
	i = 2
	if (number <= 1):
		return (False)
	while (i * i <= number):
		if (number % i == 0):
			return (False)
		i += 1
	return (True)

# print(isPrimeNumber(17))
# print(isPrimeNumber(9))