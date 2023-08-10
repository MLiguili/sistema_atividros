import math
import tkinter as tk

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
        return valor

def calcular_orcamento():
    codigo = codigo_entry.get()
    valor_md = valor_md_entry.get()
    altura = altura_entry.get()
    largura = largura_entry.get()
    vidro_tipo = vidro_tipo_var.get()

    quadro = Quadro(codigo, valor_md, vidro_tipo, altura, largura)
    valor_total = quadro.valor_quadro()

    resultado_var.set(f"Valor do quadro: R${valor_total:.2f}")

root = tk.Tk()
root.title("Orçamento de Molduras")

# Labels e Entradas
tk.Label(root, text="Código:").grid(row=0, column=0)
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=0, column=1)

tk.Label(root, text="Valor da moldura:").grid(row=1, column=0)
valor_md_entry = tk.Entry(root)
valor_md_entry.grid(row=1, column=1)

tk.Label(root, text="Altura (cm):").grid(row=2, column=0)
altura_entry = tk.Entry(root)
altura_entry.grid(row=2, column=1)

tk.Label(root, text="Largura (cm):").grid(row=3, column=0)
largura_entry = tk.Entry(root)
largura_entry.grid(row=3, column=1)

tk.Label(root, text="Tipo de vidro:").grid(row=4, column=0)
vidro_tipo_var = tk.StringVar()
vidro_tipo_var.set("1")
vidro_tipo_menu = tk.OptionMenu(root, vidro_tipo_var, "1", "2", "3")
vidro_tipo_menu.grid(row=4, column=1)

# Botão de cálculo
calcular_button = tk.Button(root, text="Calcular Orçamento", command=calcular_orcamento)
calcular_button.grid(row=5, columnspan=2, pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_var.set("Valor do quadro: R$0.00")
resultado_label = tk.Label(root, textvariable=resultado_var, font=("Helvetica", 12, "bold"))
resultado_label.grid(row=6, columnspan=2)

root.mainloop()
