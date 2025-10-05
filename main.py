import core
import time
import os
import sys
from colorama import Fore, Style, init
init(autoreset=True)

# Atalhos de cores
V = Fore.GREEN
R = Fore.RED
A = Fore.YELLOW
B = Fore.BLUE
RESET = Style.RESET_ALL

# Ícones simplificados para compatibilidade com .exe
USANDO_EXE = getattr(sys, 'frozen', False)
CHECK = "[OK]"
CROSS = "[X]"
TRASH = "[DEL]"
WARNING = "[!]"
LOADING = "[...]"

# Padroniza o layout do menu
titulo = [f"{B}=============================={RESET}",
          f"{B}    Gerenciador de Tarefas     {RESET}",
          f"{B}=============================={RESET}"]

opcoes = f"""
{V} Menu:
{V}1.{RESET} Adicionar Tarefa
{V}2.{RESET} Listar Tarefas
{V}3.{RESET} Marcar Tarefa como Concluída
{V}4.{RESET} Remover Tarefa
{V}5.{RESET} Sair
{V}6.{RESET} Sobre o Dev
"""

# Função para simular carregamento
def animacaoCarregamento(mensagem="Carregando", duracao=1):
    print(f"{LOADING} {mensagem}", end="", flush=True)
    for _ in range(3):
        time.sleep(duracao / 3)
        print(".", end="", flush=True)
    time.sleep(0.2)
    print("\n")

# Limpar tela para manter interface limpa
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu principal
def exibirMenu():
    limparTela()
    print("\n".join(titulo))
    print(opcoes)
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha in [1, 2, 3, 4, 5, 6]:
            return escolha
        return -1
    except ValueError:
        return 0

# Adicionar tarefa
def adicionarTarefa():
    limparTela()
    nome = input("Nome da Tarefa: ")
    descricao = input("Descrição da Tarefa: ")
    animacaoCarregamento("Adicionando Tarefa", 1.2)
    tarefa = core.adicionarTarefa(nome, descricao)
    print(f"{CHECK} {V}Tarefa '{tarefa.nomeTarefa}' adicionada com ID {tarefa.idTarefa}.{RESET}")
    input("Pressione Enter para continuar...")

# Listar tarefas
def listarTarefas():
    limparTela()
    tarefas = core.listarTarefas()
    animacaoCarregamento("Carregando Tarefas", 1.5)
    if not tarefas:
        print(f"{WARNING} Nenhuma tarefa encontrada.{RESET}")
    else:
        for t in tarefas:
            status = f"{CHECK} Concluída" if t.statusConclusao else f"{WARNING} Pendente"
            print(f"{B}ID: {t.idTarefa} | Nome: {t.nomeTarefa} | Descrição: {t.descricao} | Status: {status} | Data: {t.dataCriacao}{RESET}")
            print("-" * 60)
        print(f"{A}Total: {len(tarefas)} | Concluídas: {sum(t.statusConclusao for t in tarefas)} | Pendentes: {len(tarefas) - sum(t.statusConclusao for t in tarefas)}{RESET}")
    input("\nPressione Enter para continuar...")

# Marcar como concluída
def marcarTarefaConcluida():
    limparTela()
    try:
        id = int(input("ID da Tarefa a ser marcada como concluída: "))
        animacaoCarregamento("Atualizando Tarefa", 1.2)
        tarefa = core.marcarTarefaConcluida(id)
        if tarefa:
            print(f"{CHECK} {V}Tarefa '{tarefa.nomeTarefa}' marcada como concluída.{RESET}")
        else:
            print(f"{CROSS} {R}Tarefa não encontrada.{RESET}")
    except ValueError:
        print(f"{CROSS} {R}ID inválido.{RESET}")
    input("Pressione Enter para continuar...")

# Remover tarefa
def removerTarefa():
    limparTela()
    try:
        id = int(input("ID da Tarefa a ser removida: "))
        animacaoCarregamento("Removendo Tarefa", 1.2)
        sucesso = core.removeTarefa(id)
        if sucesso:
            print(f"{TRASH} {V}Tarefa com ID {id} removida.{RESET}")
        else:
            print(f"{CROSS} {R}Tarefa não encontrada.{RESET}")
    except ValueError:
        print(f"{CROSS} {R}ID inválido.{RESET}")
    input("Pressione Enter para continuar...")

# Função para simular digitação de texto
def digitar(texto, delay=0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Função sobre o desenvolvedor
def sobreODev():
    texto = f"""
============================== SOBRE O DEV ==============================

[DEV] Olá! Me chamo Igor, e este projeto foi uma forma de testar e aplicar meus conhecimentos em Python puro.

[+] O que eu mais gostei:
 - Aperfeiçoei minha lógica e conhecimento de Python
 - Entendi melhor arquitetura de sistemas
 - Apliquei POO na prática
 - Aprendi sobre persistência de dados com JSON
 - Melhorei o CLI com colorama
 - Criei um executável com PyInstaller

[>] O que ainda quero melhorar:
 - Adicionar múltiplos usuários
 - Exportar relatórios por data
 - Criar versão GUI (Tkinter ou PyQt)
 - Talvez transformar em API com Flask/Django
 - Rodar análise com IA (brincadeira... ou não)

[TECNOLOGIAS]
 - Python 3
 - colorama
 - JSON
 - PyInstaller

[DATA] Projeto feito em Outubro de 2025
Feito com carinho por Igor

=========================================================================

"""
    digitar(texto, delay=0.005)
    input("\nPressione Enter para retornar ao menu...")

# Execução principal
if __name__ == "__main__":
    while True:
        escolha = exibirMenu()
        if escolha == 1:
            adicionarTarefa()
        elif escolha == 2:
            listarTarefas()
        elif escolha == 3:
            marcarTarefaConcluida()
        elif escolha == 4:
            removerTarefa()
        elif escolha == 5:
            limparTela()
            print(f"{V}Saindo... Até mais!{RESET}")
            time.sleep(1)
            break
        elif escolha == 6:
            limparTela()
            sobreODev()
        elif escolha == -1:
            print(f"{CROSS} {R}Opção inválida. Tente novamente.{RESET}")
            time.sleep(1)
        else:
            print(f"{CROSS} {R}Entrada inválida. Tente novamente.{RESET}")
            time.sleep(1)