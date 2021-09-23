def main():
    a = int(input('nombre a diviser >> '))
    n = int(input('diviseur >> '))

    reste = a % n
    quotient = a // n

    print(f'{a} = {quotient} * {n} + {reste}')

if __name__ == '__main__':
    main()