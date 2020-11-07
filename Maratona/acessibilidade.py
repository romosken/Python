#Um dos equipamentos fundamentais para acessibilidade do cidadão cadeirante é a rampa, que consiste de um
#plano inclinado cuja máxima declividade é definida pela NBR 9050. Para ser acessível ao cadeirante autônomo (que depende apenas de suas próprias forças para realizar a subida), uma rampa precisa contemplar
#diversos detalhes e seu projeto deve ser executado por profissional de engenharia habilitado e devidamente
#treinado nos termos da Norma.
#O primeiro passo é calcular sua inclinação, cujo valor máximo deve ser de 8,33% (relação 1:12 entre altura
#e comprimento). Tal cálculo é feito com a fórmula:
#i = H × 100 ÷ C
#onde:
#i é a inclinação da rampa expressa em porcentagem;
#H é a altura do desnível;
#C é o comprimento da projeção horizontal da rampa.
#O segundo parâmetro fundamental é a largura da rampa para circulação em linha reta, cujo valor mínimo
#admissível é de 0,80 metros.
#Rampas onde haja espaço para atender simultaneamente os dois requisitos i 6 8, 334% e L > 0, 80m são
#consideradas como Projeto Simples. Quando pelo menos um desses dois requisitos não for atendido trata-se
#de um Projeto Especial, que demanda um profissional mais experiente.
#Nesta tarefa, você deve elaborar um programa de computador que irá ler as dimensões principais de altura,
#comprimento e largura e, em seguida, calcular a inclinação, bem como definir se o projeto é simples ou especial.
#Entrada
#A entrada contém diversos casos de teste. Em cada linha, há três números reais separados por um caractere
#em branco. O primeiro é a altura H (H > 0) da rampa. O segundo é o comprimento da projeção horizontal
#C (C > 0). O terceiro é a Largura L (L > 0) da rampa. Para indicar o fim da entrada de dados, a última linha três valores iguais a 0.0. Utilize números reais de precisão dupla.
#Saída
#A saída deve conter uma linha para cada linha da entrada informando com letras maiúsculas se é um PROJETO SIMPLES ou um PROJETO ESPECIAL. Ao final de cada linha deve ser impresso o final de linha,
#inclusive na última.

lista_retornos = []
lista=input().split()
lista = [float(i) for i in lista]

while lista[0]!= 0 and lista[1]!= 0 and lista[2]!= 0:
    
    if lista[2]>=0.8:
        inclinacao = lista[0]*100/lista[1]
        if inclinacao> 8.334:
            retorno = "PROJETO ESPECIAL"
        else:
            retorno = "PROJETO SIMPLES"
    else:
        retorno = "PROJETO ESPECIAL"
    lista_retornos.append(retorno)

    lista=input().split()
    lista = [float(i) for i in lista]

for ret in lista_retornos:
    print(ret)
