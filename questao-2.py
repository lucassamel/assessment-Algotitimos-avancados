moedas = [50,25,21,10,5,1]
troco = 63
def minTroco(moedas, troco):
   minMoedas = troco
   if troco in moedas:
     return 1
   else:
      for i in [c for c in moedas if c <= troco]:
         numMoedas = 1 + minTroco(moedas, troco - i)
         if numMoedas < minMoedas:
            minMoedas = numMoedas
   return minMoedas

print("A quatidade minima de moedas são: " + str(minTroco(moedas, troco)))


def calculaTroco(moedas, troco, listMoedas):
   for i in range(troco + 1):
      qntMoedas = i
      for j in [c for c in moedas if c <= i]:
            if listMoedas[i - j] + 1 < qntMoedas:
               qntMoedas = listMoedas[i - j] + 1
      listMoedas[i] = qntMoedas
   return listMoedas[troco]

print("A quatidade minima de moedas são: " + str(calculaTroco(moedas,troco,[0]*(troco+1))))