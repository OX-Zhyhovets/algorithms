s = input("String:")

def getLastWord(string):
	word = ""

	i = -1
	while True:
		if string[i] != " ":
			word = word + string[i]

		else:
			if word != "":
				break

		i = i-1

	return word 

def lengthOfLastWord(string):
	word = getLastWord(string)
	print("Length of last word: " + str(len(word)))

lengthOfLastWord(s)