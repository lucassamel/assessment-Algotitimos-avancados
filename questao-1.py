from random import random


class Individuo():
    def __init__(self, genes, geracao=0):
        self.genes = genes
        self.aptidao = 0
        self.geracao = geracao
        self.cromossomo = []
        for i in range(genes + 1):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")

    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))

        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]

        filhos = [Individuo(self.genes, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        return filhos

    def avaliacao(self):
        nota = 0
        for i in range(len(self.cromossomo)):
           if self.cromossomo[i] == '1':
               nota += 1
        self.aptidao = nota

    def mutacao(self, taxa_mutacao):
        maximo_mutacao = 0
        if maximo_mutacao == 3:
            pass
        else:
            for i in range(len(self.cromossomo)):
                if random() < taxa_mutacao:
                    if self.cromossomo[i] == '1':
                        self.cromossomo[i] = '0'
                    else:
                        self.cromossomo[i] = '1'
            return self


class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []

    def inicializa_populacao(self, genes):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(genes))
        self.melhor_solucao = self.populacao[0]


    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key=lambda populacao: populacao.aptidao,
                                reverse=True)
        if len(self.populacao) > 20:
            for i in range(10):
                self.populacao.pop()

    def melhor_individuo(self, individuo):
        if individuo.aptidao > self.melhor_solucao.aptidao:
            self.melhor_solucao = individuo

    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.aptidao
        return soma


    def seleciona_pai(self, apitidao):
        pai = -1
        valor_sorteado = random() * apitidao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].aptidao
            pai += 1
            i += 1
        return pai


    def resolver(self, taxa_mutacao, numero_geracoes, genes):
        self.inicializa_populacao(genes)



        for individuo in self.populacao:
            individuo.avaliacao()

        self.ordena_populacao()



        for geracao in range(numero_geracoes):
            nova_populacao = []
            apitidao = self.soma_avaliacoes()

            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(apitidao)
                pai2 = self.seleciona_pai(apitidao)

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))


            self.populacao = list(nova_populacao)

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordena_populacao()
            melhor = self.populacao[0]
            self.melhor_individuo(melhor)

        return print("População atigiu 1000 gerações"), self.populacao




if __name__ == '__main__':

    # lista_individuos = []
    # for i in range(20):
    #     lista_individuos.append((Individuo(6)))

    genes = 6
    tamanho_populacao = 20
    taxa_mutacao = 0.005
    numero_geracoes = 1000
    objetivo = 6
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes,genes)
    print(resultado)

