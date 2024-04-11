'''
В Python, копия объекта всегда создается поверхностной

Shallow copy (дословно "мелкая копия" или "поверхностная копия") - это объект, который включает ссылки на те же элементы, что и исходный объект
Учитывая, что процесс копирования осуществляется не рекурсивно, фактически, создается поверхностная копия на "один уровень в глубину", когда создается новый объект, но его вложенными элементами являются ссылки на исходные

Deep copy (дословно - "глубокая копия") - это объект, который заполняет рекурсивным копированием элементов исходного объекта
Таким образом, выполняется обход всего дерева объектов целиком, и создается полностью независимый клон исходного объекта и всех его копий
'''
import copy

def id_identity_collection_elements(*collections) -> bool:
    '''Проверка элементов коллекций на тождественность по id их объектов'''
    list_setOfId = []
    comparison = True
    for i, col in enumerate(collections):
        list_setOfId.append({id(elm) for elm in col})
        if i > 0 and list_setOfId[i-1] != list_setOfId[i]:
            comparison = False
        print(f'ID Коллекции {i+1} ({id(collections[i])}):', *list_setOfId[i], sep = '\n  ')
    print()
    return comparison




if __name__ == '__main__':
    list_a = [1, 2, 3, [10, 20]]


    print('====== id элементов оригинального объекта и объекта-копии будут идентичны ======')
    list_b1 = list_a.copy()
    list_b2 = list(list_a)
    list_b3 = list(map(lambda elm: elm, list_a))
    list_b4 = list_a[:]
    list_b5 = [*list_a]
    list_b6 = [elm for elm in list_a]

    assert id_identity_collection_elements(list_a, list_b1) is True
    assert id_identity_collection_elements(list_a, list_b2) is True
    assert id_identity_collection_elements(list_a, list_b3) is True
    assert id_identity_collection_elements(list_a, list_b4) is True
    assert id_identity_collection_elements(list_a, list_b5) is True
    assert id_identity_collection_elements(list_a, list_b6) is True

    assert id_identity_collection_elements(list_a, [1, 2, 3]) is False
    assert id_identity_collection_elements(list_a) is True




    print()
    print()
    print()
    print()
    print('====== Преобразование элементов осуществляется в соответствии с их мутабельностью  ======')
    print('Изменение не мутабельного элемента в исходном объекте: collection[0] = 1000\n' \
        'Изменения приведут к получению нового элемента конкретно в этом объекте, что не повлияет на другие объекты')
    list_a[0] = 1000
    print(
        f'original: {list_a}',
        f'copy 1: {list_b1}',
        f'copy 2: {list_b2}',
        sep='\n')
    print('\nИзменение мутабельного элемента в исходном объекте: collection[3][0] = 1000\n' \
        'Изменения приведут к преобразованию изначального элемента во всех объектах, которые ссылаются на данный элемент')
    list_a[3][0] = 1000
    print(
        f'original: {list_a}',
        f'copy 1: {list_b1}',
        f'copy 2: {list_b2}',
        sep='\n')

    print()
    print('\nИзменение не мутабельного элемента в любом объекте-копии: collection[1] = 2000\n' \
        'Изменения приведут к получению нового элемента конкретно в этом объекте, что не повлияет на другие объекты')
    list_b1[1] = 2000
    print(
        f'original: {list_a}',
        f'copy 1: {list_b1}',
        f'copy 2: {list_b2}',
        sep='\n')
    print('\nИзменение мутабельного элемента в любом объекте-копии: collection[3][1] = 2000\n' \
        'Изменения приведут к преобразованию изначального элемента во всех объектах, которые ссылаются на данный элемент')
    list_b1[3][1] = 2000
    print(
        f'original: {list_a}',
        f'copy 1: {list_b1}',
        f'copy 2: {list_b2}',
        sep='\n')


    print()
    print()
    print()
    print()
    print('====== Для полной копии применяется функция deepcopy модуля copy  ======')
    print('Соответственно, полная копия позволяет производить независимые изменения для любого элемента копии и оригинального объекта')
    list_c1 = copy.deepcopy(list_a)
    list_c2 = copy.deepcopy(list_a)

    assert id_identity_collection_elements(list_a, list_c1) is False
    assert id_identity_collection_elements(list_a, list_c2) is False
