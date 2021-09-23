def main():

    ca = int(input("Chiffre d'affaire >> "))

    print('Paris | Orléans ?')
    loc = input('Ville: ')

    while loc not in ['Paris', 'Orléans']:
        print("Nom d'agence saisi incorrect")
        loc = input('Ville: ')

    if loc == 'Paris':
        if ca > 500_000:
            pourcent = 4
        elif 200_000 < ca < 500_000:
            pourcent = 2
        else:
            pourcent = 0

    elif loc == 'Orléans':
        if ca > 300_000:
            pourcent = 5
        elif 100_000 < ca < 300_000:
            pourcent = 3
        else:
            pourcent = 0

    print('-' * 50)
    print(f"Chiffre d'affaire: {ca}€")
    print(f'Ville: {loc}')
    print(f'Prime: {pourcent}%')
    print(f'Prime du commercial: {ca * pourcent / 100}€')

if __name__ == '__main__':
    main()