from flat_iterator import FlatListIterator
from flat_gen import flat_list_gen


def run():
    nested_list = [
        ['a', ['list', 1, ['new_list']], 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None, ['deep_list', 333, ['again_list', [555]]]],
        12
    ]
    print('[ITERATOR ELEMENTS]:')
    for i in FlatListIterator(nested_list):
        print(i)
    print()
    print('[GENERATOR ELEMENTS]:')
    for i in flat_list_gen(nested_list):
        print(i)
    flat_list_1 = [i for i in FlatListIterator(nested_list)]
    flat_list_2 = [i for i in flat_list_gen(nested_list)]
    print()
    print('[FROM ITERATOR]:', flat_list_1)
    print('[FROM GENERATOR]:', flat_list_2)


if __name__ == '__main__':
    run()
