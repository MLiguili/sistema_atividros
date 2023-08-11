from orcamento_moldura import orcamento_molduras
from orcamento_espelho import orcamento_espelhos


def menu():
    while True:
        opcao = input("Selecione a opção: (M)olduras, (E)spelhos, (S)air \n").casefold()

        if opcao == 'm':
            orcamento_molduras()
            break
        elif opcao == 'e':
            orcamento_espelhos()
            break
        elif opcao == 's':
            print('encerrando programa...')
            exit()
        else:
            print("Escolha uma opção válida")
