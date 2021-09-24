'''
Desenvolvido por Jonathas Luis de Sousa
Universidade Federal de Lavras
'''

from math import sqrt
import sys

class Excecao(Exception):
    def __init__(self, message):
        super().__init__(message)

def triggerException(num):
    if (num == 0):
        raise Excecao('arquivo vazio')


def leituraArquivo(nomeArquivo):

    try:
        arq = open(nomeArquivo,"r")
        n = sum(1 for line in arq) # conta quantas linhas ha no arquivo
        arq.seek(0,0) #volta o cursor ao inicio do arquivo

        try:
            triggerException(n) #excecao arquivo vazio
            x= [] #lista para os valores de x
            y= [] #lista para os valores de y

            for i in arq: #percorre o arquivo 
                try: #excecao para string
                    x.append(float(i.split(',')[0]))
                    y.append(float(i.split(',')[1]))
                except ValueError as err:
                   print(err)
            
            cp(x,y,n)
            arq.close()

        except Excecao as erro:
            print(erro)
    except FileNotFoundError as err:
        print(err)


def cp(x,y,n):
    xBar = sum(x)/n
    yBar = sum(y)/n

    valor1 = 0
    valor2 = 0
    valor3 = 0

    for i,j in zip(x,y):
        valor1 += (i-xBar)*(j-yBar)
        valor2 += (i-xBar)**2
        valor3 += (j-yBar)**2

    print(valor1 / (sqrt(valor2*valor3)))


leituraArquivo(sys.argv[1])
