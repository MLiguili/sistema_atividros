from valores import lista_molduras


class Quadro:

    def __init__(self, codigo, valor_md, vidro_tipo, alt, larg):
        self.codigo = str(codigo)
        self.valor_md = int(valor_md)
        self.vidro_tipo = vidro_tipo
        self.alt = float(alt)/100 * 10000  # aceito sugestões
        self.larg = float(larg)/100 * 10000  # aceito sugestões
        self.perimetro = (self.larg + self.alt) * 2 / 10000
        self.valor_quadro()

    def get_perimetro(self):
        print(self.perimetro)

    def calc_md(self):
        calculo = self.perimetro*self.valor_md
        return calculo

    def calc_vidro(self):
        area = self.alt * self.larg / 10000 / 10000
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
        print(f"Valor do vidro:R$ {vidro:.2f}")
        print(f"Valor do moldura:R$ {moldura:.2f}")
        print(f"Valor Quadro:R$ {valor:.2f}")
        print("____________")


def orcamento_molduras():
    print('Orçamento molduras')
    codigo = input("Qual o modelo?")
    valor_md = lista_molduras.get(f'{codigo}')
    alt = input("Qual a altura em cm?\n")
    larg = input("Qual a largura em cm?\n")
    vidro_tipo = input("Que Tipo de Vidro: 1-Comum, 2-Anti-reflexo, 3- com Paspatour\n")
    quadro = Quadro(codigo, valor_md, vidro_tipo, alt, larg)
    return quadro
