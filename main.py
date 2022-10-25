#HELENA KUCHINSKI FERREIRA
#Sua  tarefa  será  construir  um  grafo,  com  100  vértices  cujos  valores  serão  aleatoriamente  selecinados em um conjunto de inteiros contendo números inteiros entre 1 e 1000. Cada vértice terá um número aleatório de arestas menor ou igual a três.  
#Você  deverá  criar  este  grafo,  armazenando  estes vértices  e  arestas  em  uma  tabela  de adjacências e em uma lista de adjacências, medindo o tempo necessário para criar estas estruturas de dados. Estas duas tabelas deverão ser salvas em arquivos de texto chamados de tabela_adjacencias.txt e lista_adjacencias.txt respectivamente. Estes arquivos devem ser salvos no site repl.it 
# Para que seja possível verificar as diferenças de tempos de criação destas estruturas, uma vez que o algoritmo esteja pronto, você deverá mudar o tamanho do gráfico para 100.000 de itens e repetir o processo de ciração no mínimo 50 vezes, anotando os tempos de criação apresentando estas médias para a tabela de adjacencias e para a lista de adjacencias. 

import time
import random
 
class NoAdj:
  def __init__(self, data):
    self.vertice = data
    self.proximo = None
 
class Grafo:
  def __init__(self, vertices):
    self.V = vertices
    self.grafo = [None] * self.V
 
  def add_aresta(self, src, dest):
    no = NoAdj(dest)
    no.proximo = self.grafo[src]
    self.grafo[src] = no
      
    no = NoAdj(src)
    no.proximo = self.grafo[dest]
    self.grafo[dest] = no
 
   
  def imprime_grafo(self):
    for i in range(self.V):
      print("Lista de adjacencias do vertice {}\ntopo".format(i), end="")
      temp = self.grafo[i]
      while temp:
        print(" -> {}".format(temp.vertice), end="")
        temp = temp.proximo
      print(" \n")

'--------------------------------------------------------------'
'Lista de adjacencia'


def IteraGrafo():
  V = 100000
  grafo = Grafo(V)

  tPInicio = time.process_time() 
  for i in range(100000):
    grafo.add_aresta(i, random.randint(1,99999))
  tPFinal = time.process_time()

  with open("lista_adj.txt", "a") as f:
    f.write(str(tPFinal - tPInicio) + "s\n")
    f.close

if __name__ == "__main__":
  for i in range(50):
      IteraGrafo()

