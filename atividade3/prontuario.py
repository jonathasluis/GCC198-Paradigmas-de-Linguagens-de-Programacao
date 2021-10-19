'''
Desenvolvido por Jonathas Luis de Sousa
Paradigmas de Linguagens de Programação - GCC198
Universidade Federal de Lavras

Paradigma Orientado a Objetos
'''

from medico import Medico
from medicamento import Medicamento
from datetime import datetime

class Prontuario():
    __procedimentos = []

    def __init__(self):
        self.__procedimentos = []

    def insere_procedimento(self,medicamento,posologia,medico,data,hora):
        self.dicionario = {}
        self.dicionario['medicamento'] = medicamento.nome_medicamento()
        self.dicionario['posologia'] = posologia
        self.dicionario['medico'] = medico.nome_medico()
        if '/' in data:
            data_formatada = datetime.strptime(data, '%d/%m/%Y').date() # Se estiver dd/mm/aa
        elif '-' in data:
            data_formatada = datetime.strptime(data, '%d-%m-%Y').date() # Se estiver dd-mm-aa
        self.dicionario['data'] = data_formatada
        self.dicionario['hora'] = hora

        self.__procedimentos.append(self.dicionario)

    def exibe_prontuario(self):
        for i in self.__procedimentos:
            lista = list(i.values())
            print(lista[0]+ " - " +lista[1]+ " - " +lista[2]+ " - " +str(lista[3])+ " - " +lista[4])
            
