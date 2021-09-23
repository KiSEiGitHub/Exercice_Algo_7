def main():
    all_notes = []
    print('Entrer 00 pour finir')
    flag = 0
    while True:
        note = int(input('Note >> '))
        if 0 < note < 20:
            all_notes.append(note)
            flag += 1
        elif note == 00:
            break
        else:
            print('Note entre 0 et 20')

    moyenne = sum(all_notes) / flag

    print(f'Moyenne = {round(moyenne, 2)}')


if __name__ == '__main__':
    main()