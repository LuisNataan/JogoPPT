import random

class Jogo:
    def jogar(self):
        vitorias_jogador = 0
        vitorias_pc = 0
        empates = 0

        jog = Jogador.jogar_rodada_jogador()
        comp = Pc.jogar_rodada_pc()

        while jog > 3 or jog < 1:
            jog = False
            print("Jogada inválida.")
            jog = int(input(" Selecione uma carta: "))

        while not jog > 3 or jog < 1:
            if jog == comp:
                print("Empate!")
                empates += 1
            elif comp == 1 and jog == 2:
                print("Jogador venceu!")
                vitorias_jogador += 1
            elif comp == 1 and jog == 3:
                print("PC venceu!")
                vitorias_pc += 1
            elif comp == 2 and jog == 1:
                print("PC venceu!")
                vitorias_pc += 1
            elif comp == 2 and jog == 3:
                print("Jogador venceu!")
                vitorias_jogador += 1
            elif comp == 3 and jog == 1:
                print("Jogador venceu!")
                vitorias_jogador += 1
            elif comp == 3 and jog == 2:
                print("PC venceu!")
                vitorias_pc += 1




class Jogador:

    def sorteio_cartas(self):
        cartas_sorteadas = [random.randint(1, 3)]
        return cartas_sorteadas

    def jogar_rodada_jogador(self):
        cartas_jogador = [random.randint(1, 3)]

        while True:
            print("Estas são suas cartas: " + cartas_jogador + "\n")
            escolha = int(input("Selecione uma para jogar: "))
            #
            # while escolha > 3 or escolha < 1:
            #     escolha = int(input("Selecione uma carta válida: "))
            #
            # if escolha == 1:
            #     self.jogada = "Pedra"
            # elif escolha == 2:
            #     self.jogada = "Papel"
            # else:
            #     self.jogada = "Tesoura"
            # print("Você escolheu: " + escolha + "\n")
            # print("Vez do Computador!")
            return escolha

class Pc:
    def jogar_rodada_pc(self):
        jogada_pc = random.randint(1, 3)
        return jogada_pc

        # while jogada_pc == escolha_pc:
        #     jogada_pc = random.randint(1, 3)
        #
        # if jogada_pc == 1:
        #     self.escolha = "Pedra"
        # elif jogada_pc == 2:
        #     self.escolha = "Papel"
        # else:
        #     self.escolha = "Tesoura"
        #
        # print("Computador escolheu: " + escolha_pc + "\n")
