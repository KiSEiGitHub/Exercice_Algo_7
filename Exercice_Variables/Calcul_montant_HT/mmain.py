def main():
    while True:
        ttc = float(input('TTC: '))
        print(f'TTC: {ttc}')
        ht = ttc / 1.2
        print(f'HT: {round(ht, 2)}')
        print(f'TVA: {ht * 0.2}')
        print('-' * 50)


if __name__ == '__main__':
    main()