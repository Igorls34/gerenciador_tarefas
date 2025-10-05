# imports
import json

def carregarDados():
    try:
        with open('dados.json', 'r', encoding='utf-8') as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        return {"tarefas": [], "ultimo_id": 0}


def salvarDados(dados, ultimo_id):
    with open('dados.json', 'w') as file:
        json.dump({"tarefas": dados, "ultimo_id": ultimo_id}, file, indent=4, ensure_ascii=False)

