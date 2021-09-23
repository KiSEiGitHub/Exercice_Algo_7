def main():
    ca = int(input("Chiffre d'affaire >> "))

    if ca > 500_000:
        pourcent = 10
        prime = (ca - 500_000) * 1 / 100 + 15500
    elif 100_000 < ca < 250_000:
        pourcent = 2
        prime = (ca - 100_000) * 2 / 100
    elif 250_000 < ca < 500_000:
        pourcent = 5
        prime = (250_000 - 100_000) * 2 / 100 + (ca - 250_000) * 5 / 100
        prime += (ca - 250_000) * 5 / 100
    else:
        pourcent = 0
        prime = 0

    print(f"Chiffre d'affaire: {ca} €")
    print(f'Prime: {pourcent} %')
    print(f'Montant de la prime: {prime} €')

if __name__ == '__main__':
    main()