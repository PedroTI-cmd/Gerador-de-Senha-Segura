import tkinter as tk
import random
import string


def gerar_senha():
    tamanho = int(entry_tamanho.get())  
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    label_senha.config(text=senha)  

janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x200")


label_instrucao = tk.Label(janela, text="Digite o tamanho da senha:")
label_instrucao.pack(pady=10)


entry_tamanho = tk.Entry(janela)
entry_tamanho.pack(pady=10)

botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=10)


label_senha = tk.Label(janela, text="", font=("Arial", 14))
label_senha.pack(pady=10)

janela.mainloop()