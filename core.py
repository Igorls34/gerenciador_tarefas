#imports
import storage
from models import tarefa

# variaveis globais
dados_json = storage.carregarDados()
tarefas_json = dados_json["tarefas"]
ultimo_id = dados_json["ultimo_id"]
tarefas = [tarefa.Tarefa.from_dict(t) for t in tarefas_json]

# funções   
def adicionarTarefa (nome, descricao):
    global ultimo_id
    ultimo_id += 1
    nova_tarefa = tarefa.Tarefa(nomeTarefa=nome, descricao=descricao, idTarefa=ultimo_id, statusConclusao=False)
    tarefas.append(nova_tarefa)
    storage.salvarDados([t.to_dict() for t in tarefas], ultimo_id)
    return nova_tarefa

def listarTarefas ():
    return tarefas


def getTarefaPorId (id):
    lista = listarTarefas()
    for t in lista:
        if t.idTarefa == id:
            return t
    return None


def marcarTarefaConcluida (id):
    tarefa = getTarefaPorId(id)
    if tarefa:
        tarefa.statusConclusao = True
        storage.salvarDados([t.to_dict() for t in tarefas], ultimo_id)
        return tarefa
    return None


def removeTarefa (id):
    global tarefas
    tarefa = getTarefaPorId(id)
    if tarefa:
        tarefas = [t for t in tarefas if t.idTarefa != id]
        storage.salvarDados([t.to_dict() for t in tarefas], ultimo_id)
        return True
    return False