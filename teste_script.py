import tkinter as tk
from tkinter import messagebox

def clicar():
    messagebox.showinfo("Mensagem", "Funcionou! 🎉")

# criar janela
janela = tk.Tk()
janela.title("Meu App Teste")
janela.geometry("300x200")

# texto
label = tk.Label(janela, text="Teste de Aplicativo", font=("Arial", 12))
label.pack(pady=20)

# botão
botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack(pady=10)

# rodar app
janela.mainloop()
