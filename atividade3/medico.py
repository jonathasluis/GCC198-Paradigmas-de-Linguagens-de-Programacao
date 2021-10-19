'''
Desenvolvido por Jonathas Luis de Sousa
Paradigmas de Linguagens de Programação - GCC198
Universidade Federal de Lavras

Paradigma Orientado a Objetos
'''

from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    
    def definir_id(self, id):
        if (len(id) > 3):
            print('erro id') # não foi utilizado o "raise Exception" para não encerrar!
        else:
            self.id = id
        
    def nome_medico(self):
        return self.nome