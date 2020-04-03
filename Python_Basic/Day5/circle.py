# encoding:utf-8
from __future__ import print_function

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('1' if person else '0', end='')
    print()


if __name__ == '__main__':
    main()
