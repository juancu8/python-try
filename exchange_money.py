
def foreign_exchange_calculator(ammount):
	dol_to_eu_rate = 0.9

	return dol_to_eu_rate * ammount

def run():
	print('****** CURRENCY EXCHANGE ************')
	print('Exchange dollars-euros')
	print('')

	ammount = float(input('How many dollars do you like exchange? '))

	result = foreign_exchange_calculator(ammount)

	print('${} dollars are ${} euros'.format(ammount, result))
	print('')


if __name__ == '__main__':
	run()