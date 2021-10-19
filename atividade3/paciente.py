'''
Desenvolvido por Jonathas Luis de Sousa
Paradigmas de Linguagens de Programação - GCC198
Universidade Federal de Lavras

Paradigma Orientado a Objetos
'''

from prontuario import Prontuario
from pessoa import Pessoa

class Paciente(Pessoa):
    __total_pacientes = 0

    def __init__(self,nome):
        super().__init__(nome)
        Paciente.__total_pacientes +=1

    def definir_id(self, id):
        if (len(id) > 5):
            print('erro id') # não foi utilizado o "raise Exception" para não encerrar!
        else:
            self.id = id

    def definir_prontuario(self,p):
        self.prontuario = p

    @classmethod
    def pacientes_ativos(cls):
        return cls.__total_pacientes


    def __del__(self):
        Paciente.__total_pacientes -=1

