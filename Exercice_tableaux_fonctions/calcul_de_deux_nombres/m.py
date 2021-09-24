class min_max:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def minimum(self):
        if self.a > self.b:
            print(f'{self.b} est le minimum')
        else:
            print(f'{self.a} est le minimum')

    def maximum(self):
        if self.a < self.b:
            print(f'{self.b} est le maximum')
        else:
            print(f'{self.a} est le maximum')


def main():
    number = min_max(20, 19)
    number.minimum()
    number.maximum()


if __name__ == '__main__':
    main()