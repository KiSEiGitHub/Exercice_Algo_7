def main():
    while True:
        montant_ht = float(input('Montant: '))
        print(f'Motant ht: {montant_ht} €')
        print(f'Montant ttc: {round(montant_ht * 20 / 100, 2)} €')
        print('-' * 50)


if __name__ == '__main__':
    main()