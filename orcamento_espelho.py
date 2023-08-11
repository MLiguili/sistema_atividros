from valores import *


class Espelho:

    def __init__(self, alt, larg, tipo):
        self.altura = alt
        self.largura = larg
        self.tipo = float(tipo)
        self.area = self.largura * self.altura
        self.calculo = self.area * self.tipo
        self.valor_espelho()

    def valor_espelho(self):
        print(f'''
*************************************************************************************************************
 Espelho no tamanho de {self.altura}m de Altura e {self.largura}m de Largura, no valor de R${self.calculo:.2f}                          
*************************************************************************************************************
''')


def define_tipo_espelho():
    while True:
        opcao = input('''

Qual Modelo? 
(1) 3mm 
(2) 4mm
(3) 4mm lapidado
(4) 4mm bisotado
(5) retroiluminado
(6) iluminação frontal 

    ''')

        if opcao == '1':
            tipo = valor_3mm
            return tipo
            break
        elif opcao == '2':
            tipo = valor_4mm
            return tipo
            break
        elif opcao == '3':
            tipo = valor_4mm_lapidado
            return tipo
            break
        elif opcao == '4':
            tipo = valor_4mm_bisotado
            return tipo
            break
        elif opcao == '5':
            tipo = valor_4mm_retroiluminado
            return tipo
            break
        elif opcao == '6':
            tipo = valor_4mm_iluminacao_frontal
            return tipo
            break
        else:
            print('Opção invalida')


def orcamento_espelhos():
    print('Orçamento de Espelho \n')
    alt = float(input("Qual a altura?\n"))
    larg = float(input("Qual a largura?\n"))
    tipo = define_tipo_espelho()
    print(alt)
    print(larg)
    print(tipo)
    espelho = Espelho(alt, larg, tipo)
    return espelho
