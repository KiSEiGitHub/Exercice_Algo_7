class ab_op:
    def __init__(self, a):
        self.a = a

    def absolue(self):
        if self.a < 0:
            return -self.a
        return self.a

    def oppose(self):
        return -self.a

    def affich(self):
        print(f'Abs de {self.a} = {self.absolue()}')
        print(f'Opp de {self.a} = {self.oppose()}')

def main():
    n = ab_op(20)
    n.affich()


if __name__ == '__main__':
    main()