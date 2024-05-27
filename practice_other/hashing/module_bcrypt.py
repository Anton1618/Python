import bcrypt

# Объект строки пароля и кодирование
password = '123'
password_bytes = password.encode('utf-8')

# Генерация соли
salt = bcrypt.gensalt()

# Создание хеш пароля
hashed_password = bcrypt.hashpw(password_bytes, salt)
print('Хешированный пароль:', hashed_password)



def check_password(pw):
    '''Проверка пароля на истинность'''
    # Получение нового объекта строки пароля и кодирование
    pw_bytes = pw.encode('utf-8')
    
    # Проверка первого аргумента на соответствие истинности со вторым аргументом - истинным значением
    if bcrypt.checkpw(pw_bytes, hashed_password):
        print('\n✅ Пароль принят')
        return True
    else:
        print('\n❌ Неверный пароль')
        return False




if __name__ == '__main__':    
    assert check_password('abracadabra') == '❌ Неверный пароль'
    assert check_password('123') == '✅ Пароль принят'
