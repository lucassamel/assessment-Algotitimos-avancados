import math

class HeapMinimo:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_heap(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.nos

class Grafo_G:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo_G  = [[0] * self.vertices for i in range(self.vertices)]

    def insere_aresta (self, u, v, peso):
        self.grafo_G [u-1][v-1] = peso
        self.grafo_G [v-1][u-1] = peso

    def dijkstra(self, origem):
        custo_consumo_oriundo_de = [[-1, 0] for i in range(self.vertices)]
        custo_consumo_oriundo_de[origem - 1] = [0, origem]
        h = HeapMinimo()
        h.adiciona_heap(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo_G [v-1][i] != 0:
                    if custo_consumo_oriundo_de[i][0] == -1 \
                    or custo_consumo_oriundo_de[i][0] > dist + self.grafo_G [v-1][i]:
                        custo_consumo_oriundo_de[i] = [dist + self.grafo_G [v-1][i], v]
                        h.adiciona_heap(dist + self.grafo_G [v - 1][i], i + 1)
        return custo_consumo_oriundo_de



g = Grafo_G (7)

g.insere_aresta(1, 2, 5)
g.insere_aresta(1, 3, 6)
g.insere_aresta(1, 4, 10)
g.insere_aresta(2, 5, 13)
g.insere_aresta(3, 4, 3)
g.insere_aresta(3, 5, 11)
g.insere_aresta(3, 6, 6)
g.insere_aresta(4, 5, 6)
g.insere_aresta(4, 6, 4)
g.insere_aresta(5, 7, 3)
g.insere_aresta(6, 7, 8)

resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)