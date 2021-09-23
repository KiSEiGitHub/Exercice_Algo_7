import math


def main():
    a = int(input('a >> '))
    b = int(input('b >> '))
    c = int(input('c >> '))

    discriminant = b ** 2 - 4 * a * c

    print(f'{a}x² + {b}x + {c} = 0')

    if discriminant < 0:
        print('L\'équiation n\'admet aucune solution réelle')

    elif discriminant == 0:

        print(f'L\'équation admet une solution soit:')
        print(f'-{b} / 2 * {a}')
        print(f'= {-b / 2 * a}')

    elif discriminant > 0:
        print(f"L'équiation admet 2 solutions soit:")
        print(f'Solution 1 = -{b} + √{discriminant} / 2 * {a} ')
        print(f'Solution 2 = -{b} - √{discriminant} / 2 * {a}')
        print(f'-' * 15)
        r1 = -b + math.sqrt(discriminant) / 2 * a
        r2 = -b - math.sqrt(discriminant) / 2 * a
        print(f'Solution 1 = {round(r1, 2)}')
        print(f'Solution 2 = {round(r2, 2)}')


if __name__ == '__main__':
    main()