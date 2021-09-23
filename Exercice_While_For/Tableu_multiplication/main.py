def main():
    table = int(input('Table >> '))

    for i in range(1, 11):
        print(f'{table} * {i} = {table * i}')


if __name__ == '__main__':
    main()