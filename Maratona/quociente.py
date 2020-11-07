#Em município não muito distante, chamado Nlogônia, nessa última eleição, a população ficou indignada
#com um candidato a vereador que foi menos votado para o cargo que venceu outro vereador mais votado.
#Essa população não entendeu o tal quociente eleitoral e pediu ajuda a um desenvolvedor para calcular o
#número de candidatos cada partido terá direito.
#Para o cálculo do quociente eleitoral são utilizados os votos válidos. Para isso, obtém-se o número de
#eleitores que foram votar, excluindo os votos brancos e nulos. Em seguida, calcula-se o quociente eleitoral
#dividindo-se os votos válidos pela quantidade de lugares a preencher, desprezando-se a fração se menor que
#0,5 e se igual ou superior a 0,5 arredonda-se para 1.
#Para exemplificar, vamos tomar como base que tenhamos: votos válidos (46.322) ÷ número de vagas (17) =
#2.724,8 = quociente eleitoral (2.725). A seguir, calcula-se o quociente partidário, dividindo-se a quantidade
#de votos de cada partido pelo quociente eleitoral. Despreza-se a fração, qualquer que seja. Os partidos que
#não alcançaram quociente partidário (menor que 1), não concorrem à distribuição de lugares.
#Caso a soma do quociente partidário seja menor que o número de vagas, essa diferença precisa ser distribuída
#(VAGAS = quantidade de vagas - soma do quociente partidário). Os partidos que não conseguiram ao menos
#uma vaga (quociente partidário=0) não entrarão na distribuição das vagas. Para distribuição das vagas,
#calcula-se a média de cada partido que obteve quociente, dividindo a quantidade de votos pelo quociente
#partidário obtido acrescido de 1.
#Exemplo: Partido 1 -> 15.992/(5+1) = 2665,3
#O partido que obter a maior média, tem seu quociente partidário aumentado em 1. Repete-se a operação até
#que as vagas sejam todas distribuídas (vagas =0).
#Como estamos no ano de eleição, seria uma ótima oportunidade para ajudar os eleitores entenderem essa
#relação do quociente eleitoral.
#Entrada
#Cada caso de teste contém dois números inteiros N (1 6 N 6 20) e NP (1 6 NP 6 20), que correspondem, respectivamente, ao número de vagas e ao número de partidos. As próximas NP linhas terão um
#inteiro NV P, correspondente ao número de votos válidos obtidos por cada partido (1 6 NV P 6 100.000).
#Saída
#A saída deverá conter uma linha com dois valores inteiros. O primeiro indicando o total de votos válidos
#T V V e o segundo correspondente ao quociente eleitoral QE. Nas próximas N linhas, deverá ser exibida
#a quantidade do quociente partidário no seguinte formato: "Partido N: V "(sem aspas), onde N representa
#o número do partido (sequencialmente e iniciado em 1) e V representa o número de vagas do quociente
#partidário. Finalize com uma quebra de linha.


vagas_partidos = input()
lista = vagas_partidos.split()
vagas = int(lista[0])
partidos = int(lista[1])
votos_partido = []
total = 0

for partido in range(partidos):
    votos_partido.append(int(input()))
    total += votos_partido[partido]


QE = round(total/vagas)


soma_QP = 0
QP = []
for partido in range(partidos):
    QP.append( int(votos_partido[partido]/QE))
    soma_QP +=QP[partido]

if soma_QP<vagas:
    distribuir = vagas-soma_QP
    
    while distribuir>0:
        maior =0
        media = [0 for i in range(partidos)]
        for partido in range(partidos):
            if QP[partido]>0:
                media[partido] = (votos_partido[partido]/(QP[partido]+1))
        vencedor = media.index(max(media))
        QP[vencedor] += 1
        distribuir-=1

print(total, QE)
for partido in range(partidos):
    print("Partido "+ str(partido+1) +": "+str( QP[partido]))
