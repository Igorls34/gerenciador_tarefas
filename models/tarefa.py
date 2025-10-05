# imports
from datetime import date


class Tarefa:
    def __init__(self, nomeTarefa, descricao, idTarefa=None, statusConclusao=None, dataCriacao=None):
        self.idTarefa = idTarefa
        self.nomeTarefa = nomeTarefa
        self.descricao = descricao
        self.statusConclusao = statusConclusao
        self.dataCriacao = dataCriacao or date.today()
    
    def to_dict(self):
        return {
            "idTarefa": self.idTarefa,
            "nomeTarefa": self.nomeTarefa,
            "descricao": self.descricao,
            "statusConclusao": self.statusConclusao,
            "dataCriacao": str(self.dataCriacao)
        }
    
    @staticmethod
    def from_dict(data):
        return Tarefa(
            idTarefa=data["idTarefa"],
            nomeTarefa=data["nomeTarefa"],
            descricao=data["descricao"],
            statusConclusao=data["statusConclusao"],
            dataCriacao=date.fromisoformat(data["dataCriacao"])
        )