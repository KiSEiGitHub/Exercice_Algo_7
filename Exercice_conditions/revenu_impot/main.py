def main():
    r1 = int(input('R1 >> '))
    r2 = int(input('R2 >> '))
    n = int(input('Parts >> '))

    total_salaire = (r1 + r2) * 0.9
    print(total_salaire)
    quotient_famille = total_salaire / n
    print(quotient_famille)

    if quotient_famille <= 9807:
        IR = 0

    elif quotient_famille <= 27086:
        IR = (quotient_famille * 0.14) - 1372.98 * n

    elif quotient_famille <= 72617:
        IR = (quotient_famille * 0.30) - 5706.74 * n

    elif quotient_famille <= 153783:
        IR = (quotient_famille * 0.41)- 13694.61 * n

    else:
        IR = (quotient_famille * 0.45) - 19845.93 * n


    print(f'Impôt = {round(IR, 2)}€')


if __name__ == '__main__':
    main()