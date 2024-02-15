'''Генераторная функция
Принимает коллекцию элементов и возвращает итератор,
который возвращает из коллекции числовые элементы, преобразуя строки, при необходимости

Имеет одноразовое уведомление (чтобы не перегружать информацией консоль)
Которое гласит, что коллекция содержит элементы не подходящего типа
'''

def num_filter(collection=[]):
	if type(collection) not in (list, tuple, dict, str, set):
		raise TypeError('Аргументом функции может быть только итерируемая коллекция')

	er_flag = False
	for num in collection:
		if type(num) not in (str, int, float):
			raise TypeError('Элементами коллекции могут быть только строки и числа')

		match num:
			case str():
				try:
					num = int(num)
					if num % 2 == 0:
						yield num
				except:
					if er_flag == False:
						print('В аргументе присутствуют элементы, не соответствующие формату числа')
					er_flag = True
			case int():
				if num % 2 == 0:
					yield num 




if __name__ == '__main__':
	assert [i for i in num_filter([1, 2, 3, 4, 5])] == [2, 4]
	assert [i for i in num_filter(['1', 2, '3', '4', 5])] == [2, 4]
	assert {i for i in num_filter({'1', 2, '3', '4', 5, 6, 7, 8, 9, 10})} == {2, 4, 6, 8, 10}
	assert [i for i in num_filter({'1': None, 2: None, '3': None, '4': None, 5: None})] == [2, 4]
	assert [i for i in num_filter('hello, world')] == []
	print('Все тесты пройдены')
