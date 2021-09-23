def main():
    a = int(input('a >> '))
    b = int(input('b >> '))
    c = int(input('c >> '))
    d = int(input('d >> '))
    e = int(input('e >> '))
    f = int(input('f >> '))

    print('-' * 50)
    print(f'{a}x + {b}y = {c}')
    print(f'{d}x + {e}y = {f}')
    print('-' * 50)

    print(f'Delta = ae - bd')
    print(f'Delta = {a} * {e} - {b} * {d}')
    delta = a * e - b * d
    print('-' * 50)

    if delta != 0:
        print(f'x = ce - bd / delta')
        print(f'y = af - cd / delta')
        print('-' * 50)
        print(f'x = ({c} * {e}) - ({b} * {d}) / {delta}')
        print(f'y = ({a} * {f}) - ({c} * {d}) / {delta}')
        print('-' * 10)
        print(f'x = {(c * e) - (b * d) / delta}')
        print(f'y = {(a * f) - (c * d) / delta}')

    else:
        print('Aucune solution')


if __name__ == '__main__':
    main()