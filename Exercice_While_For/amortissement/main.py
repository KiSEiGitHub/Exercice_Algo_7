def main():
    montant_imo = float(input('Montant immobilisation >> '))
    amo_year = int(input('Durée armotissement en années >> '))
    aqui_year = int(input("Année d'aquisition >> "))

    amo = montant_imo / amo_year
    for _ in range(amo_year):
        annee = aqui_year + 1

        depo = int(input(f'Dépréciation en {annee} en euro >> '))

        print(f'{annee} | VNC Déb: {montant_imo} | AMO: {amo} | VNC FIN: {montant_imo}-{amo}-{depo} | Dép : {depo}')

        montant_imo = montant_imo - amo - depo


if __name__ == '__main__':
    main()