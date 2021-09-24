def main():
    t = [int(input('nombre >> ')) for _ in range(5)]
    moyenne = sum(t) / 5

    print(f'moyenne: {moyenne}')

if __name__ == '__main__':
    main()