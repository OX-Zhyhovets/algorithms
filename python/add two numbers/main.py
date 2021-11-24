list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]

#Вывести число из списка
def returnNumber(l):
	number = ""
	i = -1
	while i >= -len(l):
		number = number + str(l[i])
		i = i-1
	return int(number)

#Вывести список из числа
def returnList(number):
	rlist = []
	i = -1
	while i >= -len(number):
		rlist.append(number[i])
		i = i-1
	return rlist

#Основная функция
def addTwoNumbers(l1, l2):
	number1 = returnNumber(l1)
	number2 = returnNumber(l2)
	number3 = number1 + number2
	print(returnList(str(number3)))

addTwoNumbers(list1, list2)