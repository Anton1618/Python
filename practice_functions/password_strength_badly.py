'''
Функция проверки пароля на сложность
- Недостаточная длина пароля. Если пароль короче 8 символов, то вернуть Too Weak
- Содержит только один из наборов символов. Если пароль содержит только цифры, только строчные или только заглавные символы, то вернуть Weak
- Содержит два любых набора симвлов. Если пароль содержит символы любых 2 наборов, то вернуть Good
- Содержит наборы всех симвлов. Если пароль содержит символы всех наборов, то вернуть Very Good
'''

from string import digits, ascii_lowercase, ascii_uppercase, punctuation

def password_strength(value: str) -> str:
	'''Проверка на соответствие длины'''
	if len(value) < 8:
		return 'Too Weak'

	# Проверка на вхождение пароля только В ОДИН любой набор символов
	if \
			all(i in digits for i in value) or \
					all(i in ascii_lowercase for i in value) or \
					all(i in ascii_uppercase for i in value) or \
					all(i in punctuation for i in value):
		return 'Weak'

	# Проверка на вхождение пароля ВО ВСЕ наборы символов
	if \
			any(i in digits for i in value) and \
					any(i in ascii_lowercase for i in value) and \
					any(i in ascii_uppercase for i in value) and \
					any(i in punctuation for i in value):
		return 'Very Good'

	# Проверка на вхождение пароля В ДВА любых набора символов
	if \
			(any(i in digits for i in value) and any(i in punctuation for i in value)) or \
					(any(i in digits for i in value) and any(i in ascii_lowercase for i in value)) or \
					(any(i in digits for i in value) and any(i in ascii_uppercase for i in value)) or \
					(any(i in ascii_lowercase for i in value) and any(i in ascii_uppercase for i in value)) or \
					(any(i in punctuation for i in value) and any(i in ascii_lowercase for i in value)) or \
					(any(i in punctuation for i in value) and any(i in ascii_uppercase for i in value)):
		return 'Good'


if __name__ == '__main__':
	assert password_strength('') == 'Too Weak'
	assert password_strength('1234567') == 'Too Weak'
	assert password_strength('abcdefg') == 'Too Weak'
	assert password_strength('ABCDEFG') == 'Too Weak'
	assert password_strength('?*^`,/|') == 'Too Weak'
	assert password_strength('123qweQ') == 'Too Weak'
	assert password_strength('0987123424') == 'Weak'
	assert password_strength('asdfasfawega') == 'Weak'
	assert password_strength('ASDFASGASGA') == 'Weak'
	assert password_strength('?*^`,/|:\\"@&%$!-+') == 'Weak'
	assert password_strength('sadfsSGASGA') == 'Good'
	assert password_strength('1234SGASGA') == 'Good'
	assert password_strength('23432sdfsfsf') == 'Good'
	assert password_strength('^`,/|ASGASGA') == 'Good'
	assert password_strength('^`,/|sdfsdsd') == 'Good'
	assert password_strength('123asdfSDF!') == 'Very Good'
	assert password_strength('-/asd123A') == 'Very Good'
	assert password_strength('00000*aA') == 'Very Good'
	assert password_strength('.,1A-2True') == 'Very Good'



