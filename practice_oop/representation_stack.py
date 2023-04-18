'''Стек (stack) это упорядоченная коллекция элементов,
организованная по принципу LIFO (last in - first out), последним пришёл первым вышел
'''

class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.is_empty():
            return 'Empty Stack!'
        el = self.values[-1]
        del self.values[-1]
        return el

    def peek(self):
        if self.is_empty():
            return 'Empty Stack!'
        return self.values[-1]

    def is_empty(self):
        return True if len(self.values) == 0 else False

    def size(self):
        return len(self.values)


if __name__ == '__main__':
    s = Stack()
    assert s.push('dog') == None
    assert s.peek() == 'dog'
    assert s.push('cat') == None
    assert s.size() == 2
    assert s.pop() == 'cat'
    assert s.pop() == 'dog'
    assert s.size() == 0
    assert s.is_empty() == True
    assert s.peek() == 'Empty Stack!'
    print('Все тесты пройдены')

