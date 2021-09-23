def main():
    ca = float(input("Chiffre d'affaire >> "))

    if ca > 500_000:
        prime = 2
    elif 150_000 < ca < 500_000:
        prime = 1
    else:
        prime = 0

    print(f"Chiffre d'affaire: {ca}")
    print(f'Pourcentage prime: {prime}')
    print(f'Prime du commercial: {ca * prime / 100}')


if __name__ == '__main__':
    main()