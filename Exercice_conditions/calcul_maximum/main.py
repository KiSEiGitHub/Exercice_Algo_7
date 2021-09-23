def main():
    n1 = int(input('n1 >> '))
    n2 = int(input('n2 >> '))

    print(f'{n1} - {n2}')

    if n1 > n2:
        print(f'Le maximum est {n1}')
        print(f'le minimum est {n2}')
    else:
        print(f'Le maximum est {n2}')
        print(f'le minimum est {n1}')


if __name__ == '__main__':
    main()