import math


class Quadro:

    def __init__(self, codigo, valor_md, vidro_tipo, alt, larg):
        self.codigo = str(codigo)
        self.valor_md = int(valor_md)
        self.vidro_tipo = vidro_tipo
        self.alt = int(alt)/100
        self.larg = int(larg)/100
        self.perimetro = math.ceil((self.larg + self.alt) * 2)
        self.valor_quadro()

    def get_perimetro(self):
        print(self.perimetro)

    def calc_md(self):
        calculo = self.perimetro*self.valor_md
        return calculo

    def calc_vidro(self):
        area = self.alt * self.larg
        if self.vidro_tipo == "1":
            valor_vidro = 250
            return area * valor_vidro
        if self.vidro_tipo == "2":
            valor_vidro = 300
            return area * valor_vidro
        if self.vidro_tipo == "3":
            valor_vidro = 350
            return area * valor_vidro

    def valor_quadro(self):
        vidro = self.calc_vidro()
        moldura = self.calc_md()
        valor = vidro + moldura
        print("Valor do vidro:R$", vidro)
        print("Valor do moldura:R$", moldura)
        print("Valor Quadro:R$", valor)
        print("____________")


def orcamento_molduras():
    print('Orçamento molduras')
    codigo = 2016  #input("Qual o modelo?")
    valor_md = input("Qual o valor da Moldura?")
    alt = int(input("Qual a altura?\n"))
    larg = int(input("Qual a largura?\n"))
    vidro_tipo = input("Que Tipo de Vidro: 1-Comum, 2-Anti-reflexo, 3- com Paspatour\n")
    quadro = Quadro(codigo, valor_md, vidro_tipo, alt, larg)
    return quadro
