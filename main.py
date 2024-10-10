import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calcular_media():
    try:    
        numeros_str = entry_numeros.get()
        numeros = [float(num) for num in numeros_str.split(',')]
        media = sum(numeros) / len(numeros)
        label_resultado.config(text=f'Média: {media:.2f}')
        emoji_label.config(image=emoji_happy)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos separados por vírgula.")
        emoji_label.config(image=emoji_sad)
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Nenhum número foi inserido.")
        emoji_label.config(image=emoji_sad)

janela = tk.Tk()
janela.title("Calculadora de Média")

janela.configure(bg="#f0f0f0")

label_instrucoes = tk.Label(janela, text="Insira números separados por vírgula:", font=("Helvetica", 12), bg="#f0f0f0")
label_instrucoes.pack(pady=10)

entry_numeros = tk.Entry(janela, width=30, font=("Helvetica", 12), bd=2, relief="solid")
entry_numeros.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="raised", padx=10, pady=5)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="Média: N/A", font=("Helvetica", 12), bg="#f0f0f0")
label_resultado.pack(pady=10)

emoji_happy_img = Image.open("happy_emoji.png").resize((30, 30), Image.LANCZOS)


emoji_happy = ImageTk.PhotoImage(emoji_happy_img)

emoji_sad_img = Image.open("sad_emoji.png").resize((30, 30), Image.LANCZOS)
emoji_sad = ImageTk.PhotoImage(emoji_sad_img)

emoji_label = tk.Label(janela, bg="#f0f0f0")
emoji_label.pack(pady=5)

label_rodape = tk.Label(janela, text="Feita por Maurício Soares (:", font=("Helvetica", 10), bg="#f0f0f0", fg="gray")
label_rodape.pack(side="bottom", pady=5)

janela.geometry("400x250")
janela.mainloop()
