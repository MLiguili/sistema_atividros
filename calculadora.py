x = float(input('Digite o primeiro valor\n'))
operador = input('Digite a operação\nDigite +, -, / ou *\n')
y = float(input('Digite o segundo valor\n'))

if x or y != int or float:
    print('Digite apenas numeros')

match operador:
    case '+':
        resultado = x + y
    case '-':
        resultado = x - y
    case '/':
        resultado = x / y
    case '*':
        resultado = x * y
    case _:
        print('Digite +, -, / ou * apenas')

print(f'O resultado de {x} {operador} {y} é {resultado}')
