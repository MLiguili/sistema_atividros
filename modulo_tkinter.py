import tkinter as tk
from tkinter import messagebox

class Pedido:
    def __init__(self, nome, sobrenome, telefone, descricao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.descricao = descricao

def criar_pedido():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    telefone = entry_telefone.get()
    descricao = text_descricao.get("1.0", "end").strip()

    if nome and sobrenome and telefone and descricao:
        pedido = Pedido(nome, sobrenome, telefone, descricao)
        pedidos.append(pedido)
        limpar_campos()
        messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

def exibir_pedidos():
    if not pedidos:
        messagebox.showinfo("Sem Pedidos", "Ainda não há pedidos registrados.")
    else:
        pedidos_text = ""
        for i, pedido in enumerate(pedidos, 1):
            pedidos_text += f"Pedido {i}:\n"
            pedidos_text += f"Nome do Cliente: {pedido.nome} {pedido.sobrenome}\n"
            pedidos_text += f"Telefone: {pedido.telefone}\n"
            pedidos_text += f"Descrição do Pedido: {pedido.descricao}\n"
            pedidos_text += "--------------------------\n"
        messagebox.showinfo("Pedidos Registrados", pedidos_text)

def limpar_campos():
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_telefone.delete(0, "end")
    text_descricao.delete("1.0", "end")

pedidos = []

# Configuração da janela principal
root = tk.Tk()
root.title("Gerador de Pedidos")

# Etiquetas
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, sticky="e")
label_sobrenome = tk.Label(root, text="Sobrenome:")
label_sobrenome.grid(row=1, column=0, sticky="e")
label_telefone = tk.Label(root, text="Telefone:")
label_telefone.grid(row=2, column=0, sticky="e")
label_descricao = tk.Label(root, text="Descrição:")
label_descricao.grid(row=3, column=0, sticky="e")

# Entradas de texto
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)
entry_sobrenome = tk.Entry(root)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=5)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

# Área de texto
text_descricao = tk.Text(root, height=5, width=30)
text_descricao.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_criar_pedido = tk.Button(root, text="Criar Pedido", command=criar_pedido)
btn_criar_pedido.grid(row=4, column=0, padx=10, pady=10)
btn_exibir_pedidos = tk.Button(root, text="Exibir Pedidos", command=exibir_pedidos)
btn_exibir_pedidos.grid(row=4, column=1, padx=10, pady=10)
btn_limpar_campos = tk.Button(root, text="Limpar Campos", command=limpar_campos)
btn_limpar_campos.grid(row=4, column=2, padx=10, pady=10)

# Executar o loop principal da janela
root.mainloop()
