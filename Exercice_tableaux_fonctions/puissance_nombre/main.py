def puissance(x, n):
    return x ** n

def main():
    while True:
        n = int(input('Nombre >> '))
        p = int(input('Puissance >> '))
        calcul = puissance(n, p)
        print(f'{n} puissance {p} = {calcul}')
        print('-' * 50)


if __name__ == '__main__':
    main()