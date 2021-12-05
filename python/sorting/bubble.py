from random import randint

N = int(input("Size:"))

def generateArray(N):
	array = []
	i = 0
	while N > i:
		array.append(randint(0, 999999))
		i = i + 1

	return array

def sorting(array):
	i = 0
	while i < len(array) - 1:
		j = 0
		while j < len(array) - 1 - i:
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

			j = j + 1

		i = i + 1

	return array

array = generateArray(N)
print(array)
print(sorting(array))