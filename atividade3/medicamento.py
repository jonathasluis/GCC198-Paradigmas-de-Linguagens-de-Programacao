'''
Desenvolvido por Jonathas Luis de Sousa
Paradigmas de Linguagens de Programação - GCC198
Universidade Federal de Lavras

Paradigma Orientado a Objetos
'''

class Medicamento():
    def __init__(self,nome_medicamento):
        self.__nome_medicamento = nome_medicamento

    def nome_medicamento(self):
        return self.__nome_medicamento