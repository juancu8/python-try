# For python 2 input_raw()
# age = int(input('Age?'))

# def human_age_to_dog_age(age):
# 	dog_age = age * 4
# 	print('If you are a dog, you age is:' + str(dog_age))

# human_age_to_dog_age(age)

import turtle

def main():
	window = turtle.Screen()
	square = turtle.Turtle()

	make_square(square)

	turtle.mainloop()

def make_square(square):
	length = int(input('Size of square?'))

	for i in range(4):
		make_line_and_turn(square, length)

def make_line_and_turn(square, length):
	square.forward(length)
	square.left(90)


if __name__ == '__main__':
	main()
