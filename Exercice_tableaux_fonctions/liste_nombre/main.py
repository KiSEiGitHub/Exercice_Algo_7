def main():
    liste_nombre = []

    while True:
        u = int(input('Nombre >> '))
        liste_nombre.append(u)
        print('Continuer ? (oui / non)')
        u2 = ""
        while u2 not in ['oui', 'non']:
            u2 = input('>> ')

        if u2 == 'oui':
            continue
        elif u2 == 'non':
            break

    print(liste_nombre)

if __name__ == '__main__':
    main()