def main():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    print(f'{a}x + {b} = {c}')

    x = (c - b) / a
    s = (a - b) / c

    print(f'x = ({c} - {b}) / {a}')
    print(f'x = {x}')

    print(f's = ({c} - {b}) / {a} = {x}')


if __name__ == '__main__':
    main()