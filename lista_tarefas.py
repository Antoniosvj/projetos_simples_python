import tkinter as tk

def adicionar_tarefa():
    tarefa = tarefa_entry.get()
    lista_tarefa.append(tarefa)
#    print(lista_tarefa)
    exibir_tarefas()

def exibir_tarefas():
    lista_tarefa_text.delete("1.0", tk.END)

    for tarefa in lista_tarefa:
        lista_tarefa_text.insert(tk.END, f"- {tarefa}\n")

window = tk.Tk()
window.title('Lista de tarefas')
window.geometry('400x400')

tarefa_entry = tk.Entry(window, width=30)
tarefa_entry.pack(pady=10)

tarefa_btn = tk.Button(window, text='Adicionar Tarefa', command=adicionar_tarefa).pack(pady=10)

lista_tarefa_text = tk.Text(window, width=40, height=15)
lista_tarefa_text.pack(pady=10)

lista_tarefa = []

window.mainloop()