import random

class Jogo:
    def jogar(self):

        jog = Jogador.jogar_rodada_jogador(self)
        comp = Pc.jogar_rodada_pc(self)
        jogando = True
        continuar = 'N'

        vitorias_jogador = 0
        vitorias_pc = 0
        empates = 0

        while jogando:
                if jog == comp:
                    print("Empate!")
                    empates += 1
                    jogando = False
                elif comp == 'Pedra' and jog == 'Papel':
                    print("Jogador venceu!")
                    vitorias_jogador += 1
                    jogando = False

                elif comp == 'Pedra' and jog == 'Tesoura':
                    print("PC venceu!")
                    vitorias_pc += 1
                    jogando = False

                elif comp == 'Papel' and jog == 'Pedra':
                    print("PC venceu!")
                    vitorias_pc += 1
                    jogando = False

                elif comp == 'Papel' and jog == 'Tesoura':
                    print("Jogador venceu!")
                    vitorias_jogador += 1
                    jogando = False

                elif comp == 'Tesoura' and jog == 'Pedra':
                    print("Jogador venceu!")
                    vitorias_jogador += 1
                    jogando = False

                elif comp == 'Tesoura' and jog == 'Papel':
                    print("PC venceu!")
                    vitorias_pc += 1
                    jogando = False

        print("Pontuação Jogador: " + str(vitorias_jogador) + "\n"
              "Pontuação PC: " + str(vitorias_pc) + "\n"
              "Empates: " + str(empates))

        continuar = input("Deseja continuar jogando? \n")
        if continuar == 'S' or continuar.lower() == 's':
           Jogo.jogar(self)
        else:
           print("Jogo finalizado.")

class Jogador:

    def sorteio_cartas(self):
        cartas_sorteadas = [random.randint(1, 3)]
        return cartas_sorteadas

    def jogar_rodada_jogador(self):
        cartas_jogador = ['1', '2', '3']
        random.shuffle(cartas_jogador)

        while True:
            print("Estas são suas cartas: " + str(cartas_jogador) + "\n")
            escolha = int(input("Selecione uma para jogar: "))

            while escolha > 3 or escolha < 1:
                escolha = int(input("Selecione uma carta válida: "))

            if escolha == 1:
                escolha = "Pedra"
            elif escolha == 2:
                escolha = "Papel"
            elif escolha == 3:
                escolha = "Tesoura"
            else:
                print("Jogada inválida.")

            print("Você escolheu: " + str(escolha) + "\n")
            print("Vez do Computador!")
            return escolha

class Pc:
    def jogar_rodada_pc(self):
        jogada_pc = random.randint(1, 3)
        escolha_pc = jogada_pc
        while jogada_pc == escolha_pc:
           if jogada_pc == 1:
               escolha_pc = "Pedra"
           elif jogada_pc == 2:
               escolha_pc = "Papel"
           else :
               escolha_pc = "Tesoura"


        print("Computador escolheu: " + str(escolha_pc) + "\n")
        return escolha_pc
