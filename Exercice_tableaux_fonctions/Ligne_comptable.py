def ligneEcriture(compteNum, compteLib, debit, credit):
    if debit > 0:
        print(f'{compteNum} | {compteLib} | Débit : {debit}')
    else:
        print(f'{compteNum} | {compteLib} | Débit : {credit}')

def main():
    ligneEcriture(607000, 'Achats de marchandises', 0, 200)


if __name__ == '__main__':
    main()