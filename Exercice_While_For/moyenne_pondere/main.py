def main():
    coff = int(input('Coefficient >> '))
    note = [int(input('note >> ')) for _ in range(5)]

    print(f'Note saisi {note}')
    moyenne = sum(note) / coff

    print(f'Moyenne = {round(moyenne, 2)}')


if __name__ == '__main__':
    main()