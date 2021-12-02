x = 123

#Вывести обратное число
def getReverse(num):
	str_num = str(num)
	reverse_num = ""
	
	i = -1
	while i >= -len(str_num):
		if str_num[i] != "0":
			reverse_num = reverse_num + str_num[i]
			i = i-1

	return int(reverse_num)

#основная функция
def reverseInteger(num):
	if num > 0:
		print(getReverse(num))

	if num == 0:
		print("0")

	else:
		print(-getReverse(-num))


reverseInteger(x)