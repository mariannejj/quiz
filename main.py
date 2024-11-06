#importações necessárias para o funcionamento do código
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd 
import random 

# a variável df lê o arquivo excel dito dentro dos parênteses
df = pd.read_excel('questoes.xlsx')
questoes = df.sample(n=10).values.tolist() 
# questoes escolhe até 10 questoes da lista de questoes 

SCORE = 0 # pontuação
PERGUNTA_ATUAL = 0 # índice da pergunta atual

def checar_questao(opcao_escolhida): 
    #Verifica se a resposta escolhida pelo usuário está correta.
    global PERGUNTA_ATUAL, SCORE
    if opcao_escolhida == resposta_certa.get():
        SCORE += 1  
        # Incrementa a pontuação se a resposta estiver correta.
    PERGUNTA_ATUAL += 1  
    # Incrementa o índice da pergunta atual.

    if PERGUNTA_ATUAL < len(questoes):
        #se pergunta atual for < que 10:
        display_question()  
        # chama a função display question
    else:
        # se não, chama a função mostrar resultado
        mostrar_resultado()
        #consequentemente, mostrando a caixa de de texto (messagebox)

def display_question():
    global PERGUNTA_ATUAL
    # Verifica se ainda há perguntas
    if PERGUNTA_ATUAL < len(questoes):
        questao, opcao1, opcao2, opcao3, opcao4, resposta = questoes[PERGUNTA_ATUAL]
        #Se houver, configura os labels e botões com a próxima pergunta e suas opções
        question_label.config(text=questao)
        opcao1_botao.config(text=opcao1, state=tk.NORMAL, command=lambda: checar_questao(1))
        opcao2_botao.config(text=opcao2, state=tk.NORMAL, command=lambda: checar_questao(2))
        opcao3_botao.config(text=opcao3, state=tk.NORMAL, command=lambda: checar_questao(3))
        opcao4_botao.config(text=opcao4, state=tk.NORMAL, command=lambda: checar_questao(4))

        # Define a resposta correta usando :
        resposta_certa.set(resposta)
    else:
        # Se todas as perguntas foram feitas, desativar os botões e mostrar "Jogar de Novo"
        opcao1_botao.config(state=tk.DISABLED)
        opcao2_botao.config(state=tk.DISABLED)
        opcao3_botao.config(state=tk.DISABLED)
        opcao4_botao.config(state=tk.DISABLED)
        jogar_de_novo_botao.pack()  # Mostrar botão para jogar de novo

def mostrar_resultado():
    #Exibe uma mensagem com a pontuação final
    messagebox.showinfo('Quiz Finalizado!', f'Parabéns, sua pontuação foi de: {SCORE}/{len(questoes)}')
    # Desativa os botões e mostra o botão "Jogar de novo"
    opcao1_botao.config(state=tk.DISABLED)
    opcao2_botao.config(state=tk.DISABLED)
    opcao3_botao.config(state=tk.DISABLED)    
    opcao4_botao.config(state=tk.DISABLED)
    jogar_de_novo_botao.pack()

def jogar_de_novo():
    global SCORE, PERGUNTA_ATUAL
    # Reinicia a pontuação e o índice da pergunta atual
    SCORE = 0
    PERGUNTA_ATUAL = 0 
    random.shuffle(questoes)  # embaralha as perguntas para o novo jogo
    opcao1_botao.config(state=tk.NORMAL)
    opcao2_botao.config(state=tk.NORMAL)
    opcao3_botao.config(state=tk.NORMAL)    
    opcao4_botao.config(state=tk.NORMAL)
    jogar_de_novo_botao.pack_forget()  # Esconder o botão de "jogar de novo"
    display_question()  # Mostrar a primeira pergunta

janela = tk.Tk() #criação da janela principal para a  aplicação gráfica e a armazena na variável janela
janela.title('Quiz') # definição do título da janela
janela.geometry('500x550') # define o tamanho da janela, sendo: 500 pixels de largura e 550 pixels de altura.
background_collor = '#00ffff' # define a cor de fundo da janela 
text_color = '#000000' # define a cor do texto
button_color = '#CCFFCC' #define a cor do botão
button_text_collor = '#000000' # define a cor do texto que está dentro do botão

janela.config(bg = background_collor)
# define a cor de fundo da janela para o valor armazenado em background_collor (um azul claro)
janela.option_add('*Font', 'Arial') 
# define a fonte padrão para todos os elementos da janela como Arial.

app_icon = PhotoImage(file='logo.png')
# carrega a imagem/ícone indicado e a armazena na variável app_icon
app_label = tk.Label(janela, image=app_icon, bg=background_collor)
# cria um rótulo que exibe a imagem carregada em app icon e define a cor de fundo do rótulo para o valor em background collor
app_label.pack(pady=10)
# O argumento pady=10 adiciona um espaçamento de 10 pixels ao redor do rótulo.

question_label = tk.Label(janela, text="", wraplength=380, bg=background_collor, fg=text_color, font=('Arial', 12, 'bold'))
question_label.pack(pady=20)
#cria um rótulo para exibir a pergunta do quiz. A largura de quebra de linha é definida como 380 pixels para permitir texto extenso, as cores de fundo e texto são definidas e a fonte é configurada como Arial, tamanho 12 e negrito
#adiciona um espaçamento de 20 pixels ao redor do rótulo.

resposta_certa = tk.IntVar()
opcao1_botao = tk.Button(janela, text='',width=30, bg=button_color, fg=button_text_collor, state=tk.DISABLED, font=('Arial', 10,'bold'))
opcao1_botao.pack(pady=10)

opcao2_botao = tk.Button(janela, text='',width=30, bg=button_color, fg=button_text_collor, state=tk.DISABLED, font=('Arial', 10,'bold'))
opcao2_botao.pack(pady=10)

opcao3_botao = tk.Button(janela, text='',width=30, bg=button_color, fg=button_text_collor, state=tk.DISABLED, font=('Arial', 10,'bold'))
opcao3_botao.pack(pady=10)

opcao4_botao = tk.Button(janela, text='',width=30, bg=button_color, fg=button_text_collor, state=tk.DISABLED, font=('Arial', 10,'bold'))
opcao4_botao.pack(pady=10)

jogar_de_novo_botao = tk.Button(janela, command=jogar_de_novo ,text='Jogar novamente', width=30, bg=button_color, fg=button_text_collor, font=('Arial', 10,'bold'))

display_question()

janela.mainloop()