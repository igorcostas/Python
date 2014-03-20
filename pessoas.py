# -*- coding: utf-8 -*-
def converteLista(arq):
    Arq = arq
    listaEnv = []

    for i in Arq.readlines():
        if (i!='') and (i!='\n'):
            val = i.split()
            print('Nome, Idade: ',val)
            listaEnv.append(val)

    return listaEnv

ArqPessoas = open('pessoas.txt')

listaPessoas = converteLista(ArqPessoas)

print(listaPessoas)


totalmaior = 0 #mudei de lista para um contador
totalmenor = 0

for i in range(len(listaPessoas)):
    if (listaPessoas[i][1]) >= str(18):
        totalmaior+=1 #ao invés de jogar num array, adiciona +1 ao contador
    else:
        totalmenor+=1

print('Maiores: ', totalmaior, 'Menores: ', totalmenor)
