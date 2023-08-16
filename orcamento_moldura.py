from valores import *


class Quadro:

    def __init__(self, codigo, valor_md, vidro_tipo, alt, larg):
        self.codigo = str(codigo)
        self.valor_md = int(valor_md)
        self.vidro_tipo = str(vidro_tipo)
        self.alt = alt/100 * 10000  # aceito sugestões
        self.larg = float(larg)/100 * 10000  # aceito sugestões
        self.perimetro = (self.larg + self.alt) * 2 / 10000
        self.valor_quadro()

    def get_perimetro(self):
        print(self.perimetro)

    def calc_md(self):
        calculo = self.perimetro*self.valor_md
        return calculo

    def calc_vidro(self):
        area = self.alt * self.larg
        if self.vidro_tipo == "1":
            valor_vidro = valor_vidro_comum
            return area * valor_vidro
        elif self.vidro_tipo == "2":
            valor_vidro = valor_vidro_anti_reflexo
            return area * valor_vidro
        elif self.vidro_tipo == "3":
            valor_vidro = valor_com_paspatour
            return area * valor_vidro
        elif self.vidro_tipo == "4":
            valor_vidro = valor_com_paspatour_e_anti_reflexo
            return area * valor_vidro

    def valor_quadro(self):
        vidro = self.calc_vidro() / 10000 / 10000
        moldura = self.calc_md()
        valor = vidro + moldura
        print(f"Valor do Vidro:R$ {vidro:.2f}")
        print(f"Valor do Moldura:R$ {moldura:.2f}")
        print(f"TOTAL: R$ {valor:.2f}")
        print("____________")


def tem_pasp():
    while True:
        tem_paspatour = input("Tem Paspatour? (S)im ou (N)ão?\n").casefold()
        if tem_paspatour == 's':
            tamanho_paspatour = float(input("Quantos cm?\n"))
            alt = float(input("Qual a altura em cm?\n"))
            larg = float(input("Qual a largura em cm?\n"))
            vidro_tipo = str(input("Que Tipo de Vidro: 3-Comum, 4-Anti-reflexo\n"))
            alt = (2 * tamanho_paspatour) + alt
            larg = (2 * tamanho_paspatour) + larg
            print(alt)
            print(larg)
            print(vidro_tipo)
            return vidro_tipo, alt, larg

        elif tem_paspatour == 'n':
            vidro_tipo = input("Que Tipo de Vidro: 1-Comum, 2-Anti-reflexo\n").casefold()
            alt = float(input("Qual a altura em cm?\n"))
            larg = float(input("Qual a largura em cm?\n"))
            return vidro_tipo, alt, larg

        else:
            print('Escolha uma opção Válida')


def orcamento_molduras():
    print('Orçamento molduras')
    codigo = input("Qual o modelo?")
    valor_md = lista_molduras.get(f'{codigo}')
    vidro_tipo, alt, larg = tem_pasp()
    quadro = Quadro(codigo, valor_md, vidro_tipo, alt, larg)
    return quadro
