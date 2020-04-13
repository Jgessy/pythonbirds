class Pessoa:
    def __init__(self, nome = None, idade=48):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'ola {id(self)}'
if __name__ == '__main__':
    p = Pessoa('fabio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'james'
    print(p.nome)
    print(p.idade)