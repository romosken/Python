#Yves is a receptionist at an art gallery and is organizing the opening of a new collection by a famous painter
#in the city. To save space on the pages and speed up the entry of each guest, he wants to put only an
#abbreviation of the full names of the guests in the entry list. For each guest, the first and last name must be
#inserted in full and the others in short form. Help Yves to create a program to accomplish this task.
#Input
#The entry contains several test cases, each case is a guest’s name, containing from 2 to 100 characters,
#without special characters. The entry ends with EOF.
#Output
#The program must print the guest list so that it is ordered by the names with the middle names of each guest
#abbreviated.

nomes = []
nomes.append(input().split())

while len(nomes[-1])> 0:
    nomes.append(input().split())

lista = []
nome_certo=""
del nomes[-1]
for pessoa in nomes:
    if len(pessoa)<3:
        for nome in pessoa:
            nome_certo += nome +" " 
    else:
        for nome in range(len(pessoa)):
            if nome == 0 or nome == len(pessoa)-1:
                nome_certo += pessoa[nome] +" "
            else:
                nome_certo+= pessoa[nome][0:1].upper()+". "

    lista.append(nome_certo)
    nome_certo = ""
lista.sort()
for nome in lista:
    print(nome)
