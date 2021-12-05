x = int(input("int:"))

def reverseNumber(number):
	str_num = str(number)
	reverse = ""

	i = -1

	while i >= -len(str_num):
		reverse = reverse + str_num[i]
		i = i-1

	return int(reverse)

def palindromeNumber(number):
	if "-" in str(number):
		print("false")

	else:
		reverse_number = reverseNumber(number)

		if number == reverse_number:
			print("true")

		else:
			print("false")

palindromeNumber(x)