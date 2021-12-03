import random
import os
import time

#
#
#
#
# CLASSE LEITOR
#
#
#
#



# classe para leitura de arquivos
class Leitor:

    #funcao para leitura dos dados das propriedades
    @staticmethod
    def lerProps():

        #abre arquivo de texto com modo de leitura
        _arquivo = open("gameConfig.txt", "r")

        #le o arquivo linha a linha, gerando uma lista
        _txt = _arquivo.readlines()
        _propriedades = [[0,0]]

        #para cada indice da leitura realizada, divide o valor desse indice onde ha " ", transforma-os em int e insere como ultimo valor numa lista "propriedades"
        for _linha in _txt:

            #comando separa uma string em uma lista, como nao foi passado argumentos, separa a cada " "
            _linha = _linha.split()

            #transforma cada valor na lista gerada em int
            for _num in range(len(_linha)):
                _linha[_num] = int( _linha[_num])

            #insere essa lista de valores, na lista global, como ultimo valor
            _propriedades.append(_linha)

        #fecha o arquivo de texto
        _arquivo.close()

        #devolve a lista de valores de cada propriedade
        return _propriedades




#
#
#
#
# CLASSE DADO
#
#
#
#


# classe para rolagem do dado
class Dado:

    #gera um metodo estatico que retorna um numero inteiro aleatorio entre 1 e 6
    @staticmethod
    def jogar_dado ():
        return random.randint(1,6)



#
#
#
#
# CLASSE JOGADOR
#
#
#
#



#classe dos jogadores
class Jogador:

    # construtor, devemos passar o numero do jogador, e como valor opcional o comportamento
    # (caso seja um player bot utilizaremos 1,2,3 ou 4 para identificar o comportamento, caso seja um humano, nao passaremos nada)
    def __init__(self, numero, comportamento = None):
        self.coins = 300
        self.numero = numero
        self.comportamento = comportamento
        # lista de propriedades adquiridas
        self.props = []
        self.posicao = 0

    # metodo para compra das propriedades, contemplando cada comportamento, e dando opcao de compra caso o player seja humano
    # deve ser passado como argumento o indice da propriedade que o jogador se encontra (que vai de 1 a 21 (0 é a casa inicial)) 
    def comprar(self, prop, printar=0):
        # CASO PLAYER HUMANO
        if self.comportamento == None:

            # pede input de "s" ou "n" para comprar ou nao a propriedade passada como parametro, exibindo o indice, o valor de compra e de aluguel
            resposta = input(f"\n####Deseja comprar a propriedade número {prop} (s/n)?####\nSeu valor de compra é: {PROPRIEDADES[prop][0]}\nE seu aluguel é: {PROPRIEDADES[prop][1]}\n")

            # caso jogador escolha sim, verifica se tem cois suficientes, se sim, adiciona a propriedade em sua lista e subtrai o valor do imovel de seus coins 
            if resposta == "s":
                if self.coins > PROPRIEDADES[prop][0]:
                    self.props.append(PROPRIEDADES[prop])
                    self.coins -=  PROPRIEDADES[prop][0]

                    if printar:
                        time.sleep(2)
                        print("O jogador "+str(self.numero)+" comprou a propriedade número: "+str(prop))
                else:
                    if printar:
                        time.sleep(2)
                        print("Coins insuficientes para comprar!")

            # caso escolha nao, passa para o proximo a jogar        
            elif resposta =="n":
                pass
        
        # bot do comportamento 1, AGRESSIVO: compra tudo que ele pode!
        # por isso apenas comparamos se ele possui dinheiro suficiente para tal acao
        elif self.comportamento == 1: 
            if self.coins > PROPRIEDADES[prop][0]:
                    self.props.append(PROPRIEDADES[prop])
                    self.coins -=  PROPRIEDADES[prop][0]
                    
                    if printar:
                        time.sleep(2)
                        print("O jogador "+str(self.numero)+" comprou a propriedade número: "+str(prop))
            else:
                if printar:
                    time.sleep(2)
                    print("Coins insuficientes para comprar!")

        # bot do comportamento 2, EXIGENTE: compra toda propriedade que tiver aluguel maior que 50 coins
        # nesse caso comparamos se o valor do aluguel da propriedade atual é maior que 50, caso sim, verifica se o jogador tem coins o suficiente, e realiza a compra
        elif self.comportamento == 2:
            if PROPRIEDADES[prop][1] > 50:
                if self.coins > PROPRIEDADES[prop][0]:
                        self.props.append(PROPRIEDADES[prop])
                        self.coins -=  PROPRIEDADES[prop][0]

                        if printar:
                            time.sleep(2)
                            print("O jogador "+str(self.numero)+" comprou a propriedade número: "+str(prop))
                        
                else:

                    if printar:
                        time.sleep(2)
                        print("Coins insuficientes para comprar!")

        # bot do comportamento 3, CAUTELOSO: compra tudo, desde que apos a compra continue com 80 coins
        # verificamos se os coins dele menos o valor do imovel é maior ou igual a 80, caso sim, realizamos a compra 
        # (afinal para entrar na primeira condicao ele ja deve possuir coins suficientes)
        elif self.comportamento == 3:
            if self.coins - PROPRIEDADES[prop][0] >= 80:
                self.props.append(PROPRIEDADES[prop])
                self.coins -= PROPRIEDADES[prop][0]

                if printar:
                    time.sleep(2)
                    print("O jogador "+str(self.numero)+" comprou a propriedade número: "+str(prop))
                
        # bot do comportamento 4, ALEATORIO: chance de 50% de compra para cada propriedade que ele cai
        # para isso geramos um numero aleatorio entre 0 e 1 (que por si so representam False e True), caso retorne 1, 
        # verifica se o jogador possui coins o suficiente, e realiza a compra
        elif self.comportamento == 4:
            if random.randint(0,1):
                if self.coins > PROPRIEDADES[prop][0]:
                        self.props.append(PROPRIEDADES[prop])
                        self.coins -=  PROPRIEDADES[prop][0]

                        if printar:
                            time.sleep(2)
                            print("O jogador "+str(self.numero)+" comprou a propriedade número: "+str(prop))
                        
                else:
                    if printar:
                        time.sleep(2)
                        print("Coins insuficientes para comprar!")
            else:
                pass


    # metodo para andar, utiliza o metodo de dado para gerar os passos, e adiciona os passos sorteados na posição do jogador
    # caso a posicao passe de 20 (ultima posicao da lista de propriedades), subtrai da posicao o valor de casas existentes (20 propriedades + inicio) 
    # e adiciona 100 coins ao jogador
    def andar(self, printar =0):
        passos = Dado.jogar_dado()
        self.posicao+=passos

        if printar:
            time.sleep(2)
            print("O jogador "+str(self.numero)+" andou "+str(passos)+" passos!")
            

        if self.posicao>20:
            self.posicao -=21
            self.coins+=100

            if printar:
                time.sleep(2)
                print("O jogador "+str(self.numero)+" ganhou 100 coins por passar pelo início!")
                



#
#
#
#
# CLASSE CONTROLE
#
#
#
#


        



# classe com principais metodos de controle do jogo
class Controle:

   

    # metodo construtor do controle, entra-se com o argumento opcional de numero de jogadores humanos
    # o metodo cria a lista dos jogadores, em ordem de jogada gerada aleatoriamente pelo metodo "cria_jogadores",
    # e exibe em tela a ordem das jogadas de acordo com o numero de cada jogador
    def __init__(self,printar=0,jogs=0):

        # cria lista dos jogadores em ordem aleatoria como atributo do proprio controle
        self.lista_jogadores = self.cria_jogadores(jogs)

        self.total_rodadas=self.rodadas = 1000
        self.run = True
        self.printar = printar
        
        # exibe a ordem das jogadas
        if self.printar:
            print ("\nA ordem dos jogadores é a seguinte: ",self.lista_jogadores[0].numero, self.lista_jogadores[1].numero, self.lista_jogadores[2].numero, self.lista_jogadores[3].numero)

    # metodo de criacao dos objetos jogadores, e uma lista contendo cada um deles em ordem aleatoria, para ser seguida no jogo
    # recebe como argumento opcional o numero de jogadores humanos
    def cria_jogadores(self, jogs = 0):
        
        # identifica o numero de jogadores que serao bots, subtraindo do maximo de jogadores, a quantidade recebida de humanos
        _bots = 4-jogs

        # cria uma lista com digitos de 1 ao numero de jogadores
        _lista = [i for i in range(1, jogs+_bots+1)]

        # retira da lista criada anteriormente, "n" valores aleatorios, referentes a quantidade de bots no jogo e cria uma lista
        _lista_bots = random.sample(_lista, _bots)
        
        # separa a diferenca entre a lista criada de bots e a lista geral, para ser a lista dos jogadores
        _lista_jogs= list(set(_lista) - set(_lista_bots))
        
        # inicia a lista final que contera todos os jogadores em ordem de jogada
        _lista_jogadores = []

        # passa pela lista de bots criando os objetos de bot com o numero e comportamento aleatorio, e adiciona na lista final
        for _bot in _lista_bots:
            computador = Jogador(_bot,_bot)
            _lista_jogadores.append(computador)    

        # passa por todos os humanos e cria-os com numeros aleatorios
        for _jog in _lista_jogs:
            jogador = Jogador(_jog)
            _lista_jogadores.append(jogador)    

        # retorna a lista organizada aleatoriamente referente a ordem em que jogarão, de todos os objetos jogadores
        return random.sample(_lista_jogadores, len(_lista_jogadores))







    # metodo que verifica a propriedade em que o jogador se encontra e executa o pagamento do aluguel, se viavel
    # recebe o objeto do jogador na lista dos jogadores
    def verifica_posicao(self, jogador):


        # pega a lista (valores) da propriedade em que o jogador se encontra (utilizando a posicao do mesmo como indice da lista de propriedades)
        casa_atual = PROPRIEDADES[jogador.posicao]

        # caso a casa atual seja a inicial (indice 0 na lista de Propriedades), exibe na tela que o jogador esta na mesma
        
        if casa_atual[0] == 0:

            if self.printar:
                time.sleep(2)
                print("O jogador "+str(jogador.numero)+ " está na posição inicial")
                
        # caso a casa atual seja diferente da inicial, verifica se o proprio jogador possui essa propriedade, 
        # caso negativo, verifica se ela pertence a algum outro jogador
        else:
            # verifica se a propriedade atual pertence ao jogador, e exibe que ele a possui, caso positivo
            if casa_atual in jogador.props:
                if self.printar:
                    time.sleep(2)
                    print("O jogador "+str(jogador.numero)+ " caiu em uma propriedade que ele já possui!")
                    
            # caso a propriedade nao pertenca a ele
            else:

                # faz uma copia da lista de jogadores
                lista_temp = self.lista_jogadores[:]
                # apaga dessa copia, o jogador atual
                del lista_temp[lista_temp.index(jogador)]

                # inicializa a variavel dono
                dono = None
                # passa por cada adversario na lista criada anteriormente, e verifica se ele possui a propriedade,
                # caso positivo, atribui a variavel dono, o objeto adversario
                for adversario in lista_temp:

                    if casa_atual in adversario.props:

                        dono = adversario

                # caso a propriedade pertenca a um dos adversarios
                if dono != None:

                    # verifica se o jogador tem coins o suficiente para pagar o aluguel, caso positivo, paga ao adversario
                    if jogador.coins - casa_atual[1] > 0:

                        jogador.coins -= casa_atual[1]
                        dono.coins+= casa_atual[1]

                        if self.printar:
                            time.sleep(2)
                            print("O jogador "+str(jogador.numero)+" pagou "+str(casa_atual[1])+" coins de aluguel, para o jogador "+str(dono.numero))
                            
                    # caso o jogador nao possua coins suficientes, pega os coins restantes dele e passa ao adversario, 
                    # alem de declarar falencia do jogador, e apagar o objeto do jogador, liberando assim as propriedades que pertenciam a ele
                    else:

                        dono.coins+=jogador.coins
                        jogador.coins = 0
                        
                        jogador.props = []
                        del self.lista_jogadores[self.lista_jogadores.index(jogador)]
                        
                        if self.printar:
                            time.sleep(2)
                            print("O jogador "+str(jogador.numero)+" faliu!")
                            
                
                # caso a propriedade nao pertenca a ninguem, chama o metodo de compra do jogador
                else:

                    jogador.comprar(jogador.posicao, self.printar)



    # metodo verifica se há vencedor, caso só haja um jogador ativo ainda, ou as rodadas acabarem, declara o vencedor
    def verificar_vencedor(self):

        # deixa o ganhador como inexistente
        ganhador = 0

        # caso apenas exista um jogador na lista, coloca-o na variavel ganhador
        if len(self.lista_jogadores) == 1:
            
            ganhador = self.lista_jogadores[0]
            
        # caso as rodadas tenham acabado, verifica  qual jogador possui mais coins e o insere na variavel ganhador
        elif self.rodadas <= 0 :

           
            if self.printar:
                time.sleep(2)
                print("O número de rodadas chegou ao limite!")
            
            mais_coins = 0
            for jogador in self.lista_jogadores:
                if jogador.coins >= mais_coins:
                    ganhador = jogador

        # caso exista um ganhador, o declara como ganhador e encerra o jogo
        if ganhador != 0:

            if self.printar:
                time.sleep(2)
                print("O vencedor da partida é o jogador número: "+str(ganhador.numero))
            
            self.run = False    

            return ganhador.numero


#
#
#
#
# DECLARACAO DE CONSTANTES
#
#
#
#

# lista das propriedades lidas no arquivo gameConfig
PROPRIEDADES = Leitor.lerProps()


#
#
#
#
# FUNCAO MAIN
#
#
#
#

    
        
# funcao main para execucao do projeto
def main():
    
    # printa o menu e pede a opcao desejada para o usuario
    menu = int(input("#################### MENU BANKRUPT ####################\n\n 1 - Para rodar a simulação pedida no desafio \n 2 - Para jogar normalmente\n\n"))

    # caso o usuario escolha jogar
    if menu == 2:
        # pede quantas pessoas irao jogar a partida
        num_jogadores = int(input("\nPor favor, insira o número de jogadores Humanos! (de 0 a 4)\n"))
        
        # cria o controle do jogo, passando a opcao 1 para printar os resultados de cada acao, e o numero de jogadores humanos
        controle = Controle(1,num_jogadores)
        
        # enquanto a partida nao acabar
        while controle.run:

                # para cada jogador na lista de jogadores gerada no controle
                for jogador in controle.lista_jogadores:

                    # verifica se a partida ainda nao acabou
                    if controle.run:
                        # executa o metodo de andar, com o argumento 1 para printar as execucoes
                        jogador.andar(1)
                        # executa o metodo de verificar posicao, que verifica e paga o aluguel
                        controle.verifica_posicao(jogador)    
                        # diminui 1 das rodadas da partida
                        controle.rodadas -= 1
                        # executa o metodo para verificar o vencedor
                        controle.verificar_vencedor()
                    
                    #caso a partida tenha acabado, sai do loop for
                    else:
                        break
    


    # caso o usuario escolha executar a simulacao
    elif menu == 1:
       
        # printa a mensagem e espera dois segundos
        print("\nEspere um momento, executando as partidas...")
        time.sleep(2)

        # inicializa as listas para exibicao dos resultados, e as variaveis de numero de partidas da simulacao
        lista_vencedores = []
        lista_rodadas = []
        total_jogos=jogo_atual = 300


        # enquanto as partidas nao acabarem
        while jogo_atual>0:

            # seta a rodada para 0 (variavel utilizada para contabilizar as rodadas de cada partida)
            rodadas = 0
            # inicializa o controle
            controle = Controle()

            # enquanto nao acabarem as rodadas da partida
            while controle.run:

                # para cada jogador da lista
                for jogador in controle.lista_jogadores:

                    # enquanto a partida nao acabar
                    if controle.run:

                        # executa o metodo para andar
                        jogador.andar()
                        # executa o metodo de verificar a posicao do jogador
                        controle.verifica_posicao(jogador)    
                        # diminui 1 das rodadas da partida atual
                        controle.rodadas -= 1
                        # atribui a uma variavel o retorno do metodo de verificar o vencedor
                        vencedor = controle.verificar_vencedor()

                        # caso exista um vencedor
                        if vencedor != None:

                            # printa o vencedor da partida atual invertendo o numero da partida atual para exibir (se a partida é a numero 300, aparecera como 1)
                            print("O vencedor da "+str(-(jogo_atual-(total_jogos+1)))+"° partida é o jogador "+str(vencedor))
                            # adiciona na lista de vencedores o vencedor atual
                            lista_vencedores.append(vencedor)
                            # adiciona na lista de rodadas, o tanto de rodadas que demorou para acabar essa partida (caso o numero da rodada atual seja 0, a partida levou 1000 rodadas!)
                            lista_rodadas.append(-(controle.rodadas-controle.total_rodadas))
                            
                            # quando houver um vencedor, sai do loop for  
                            break

            # diminui 1 do jogo_atual
            jogo_atual-=1
        
        # aguarda 1 segundo
        time.sleep(1)
       
        # exibe o tanto de partidas que acabaram por timeout
        print("\n\n"+str(lista_rodadas.count(1000))+" partidas terminaram em Time Out")

        time.sleep(1)

        # exibe a media de rodadas das partidas executadas
        print("\nA média de rodadas nas "+str(total_jogos)+" partidas foi de: "+str(sum(lista_rodadas)//len(lista_rodadas)))
        
        # lista dos nomes dos comportamentos para melhor exibicao
        lista_comportamentos = [", Impulsivo",", Exigente", ", Cauteloso", ", Aleatório"]
        
        # lista contendo o numero de vitorias de cada um dos comportamentos
        lista_counts=[lista_vencedores.count(i) for i in range(1,5)]
        
        # pega o maior valor da lista criada
        moda = max(lista_counts)

        # inicializa a lista de vencedores
        vencedores =[]

        # para cada indice na lista de vitorias de cada um dos players
        for i in range(0,len(lista_counts)):

            # caso o indice atual do loop seja igual ao maior valor da lista
            if moda == lista_counts[i]:
                # adiciona o incice acrescido de 1 (equivalente ao numero do jogador/comportamento), 
                # mais o nome do comportamento (da lista criada anteriormente) em uma lista de vencedores 
                vencedores.append(str(i+1)+lista_comportamentos[i])
        

        time.sleep(1)


        # caso exista apenas um comportamento que venceu mais partidas
        if len(vencedores) == 1:
            print("\nO comportamento que mais venceu é: ")
        
        # caso exista algum comportamento empatado em numero de vitorias
        else:
            print("\nOs comportamentos que mais venceram são: ")

        # para cada comportamento na lista de vencedores
        for venc in vencedores:
            # exibe o comportamento e o numero de partidas que ele venceu
            print(venc+", com "+str(moda)+" vitórias!")
         
        # quebra de linha
        print()

        time.sleep(1)

        # para cada indice na lista de partidas vencidas
        for i in range(0,len(lista_counts)):
            # exibe a porcentagem de vitorias do total, que cada comportamento venceu
            print("("+ str(lista_counts[i])+") "+str(format(lista_counts[i]*100/total_jogos,'.2f'))+"% das partidas foram vencidas pelo jogador "+str(i+1)+lista_comportamentos[i])
        # quebra de linha
        print()

# executa a funcao main        
main()

os.system("pause")





