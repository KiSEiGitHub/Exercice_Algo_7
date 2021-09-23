def main():
    n = int(input('n >> '))

    if n < 0:
        print(f'Valeur aboslue de {n} est {n - n * 2}')
    else:
        print(f'Valeur absolue de {n} est {n}')

if __name__ == '__main__':
    main()