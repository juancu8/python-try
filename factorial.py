
def factorial(number):
	if number == 0:
		return 1

	return number * factorial(number - 1)

def run():
	number = int(input('Put your number: '))

	result = factorial(number)

	print(result)

if __name__ == '__main__':
	run()