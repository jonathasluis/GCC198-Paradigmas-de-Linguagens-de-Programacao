# exercicio 1
soma = 1+2+3+4+5
print(soma)
media = (23+19+31)/3
print(media)

#2
lista = [3,6,23,67,-98,8,90,-8,0]
media = sum(lista)/len(lista)

for i in lista:
    if i > media:
        print(i)

#3
def meuIMC(peso,altura):
    imc = peso / (altura**2)

    if(imc < 18.5):
        return 'abaixo do peso'
    elif(imc >= 18.5 and imc < 25):
        return 'normal'
    else:
        'sobrepeso'


print(meuIMC(80,1.8))