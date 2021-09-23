def main():
    libelle = input('Nom produit >> ')
    product_price = float(input('Prix du produit >> '))
    quantite_produit = int(input('Nombre de produit >> '))

    print('-' * 50)

    print(f'Nom du produit: {libelle}')
    print(f'Prix du produit: {product_price}')
    print(f'Quantité: {quantite_produit}')

    print('-' * 50)

    user_product = int(input('Combien de produit voulez-vous ? >> '))

    while user_product > quantite_produit:
        print('Pas assez de produit')
        user_product = int(input('Combien de produit voulez-vous ? >> '))

    HT = (product_price / 1.2) * user_product
    TVA = (product_price / 100 * 20) * user_product
    TTC = HT + TVA

    print('-' * 50)

    print(f'HT: {round(HT, 2)}')
    print(f'TVA: {round(TVA, 2)}')
    print(f'TTC: {round(TTC, 2)}')


if __name__ == '__main__':
    main()