import busca_bfs as bfs

class BuscaProfundidade:
    def __init__(self, problema):
        self.problema = problema
        self.fronteira = [problema.inicial]
        self.visitados = [problema.inicial.estado]
        self.solucao = []
        self.situacao = bfs.BUSCA_INICIANDO

    def executar(self):
        while self.situacao != bfs.BUSCA_FALHOU and self.situacao != bfs.BUSCA_SUCESSO:
            self.passo_busca()

        if self.situacao == bfs.BUSCA_FALHOU:
            print("Busca falhou")
        elif self.situacao == bfs.BUSCA_SUCESSO:
            print("Busca teve sucesso")
            print(f"Solucao: {self.solucao}")

        return

    def passo_busca(self):
        if self.situacao == bfs.BUSCA_FALHOU:
            print("Busca falhou")
            return

        if self.situacao == bfs.BUSCA_SUCESSO:
            print("Busca chegou ao objetivo com sucesso")
            return

        try:
            '''
            A diferença entre o algoritmo BFS e DFS ocorre na hora de remover
            um elemento da fronteira, enquanto que no BFS é usado o conceito (FIFO) para remover um elemento da fila
            no DFS é usado o conceito (LIFO) para remover um elemento da pilha
            '''
            no = self.fronteira.pop(-1)
        except IndexError:
            self.situacao = bfs.BUSCA_FALHOU
            return

        # faz teste do objetivo
        if self.problema.objetivo(no):
            self.situacao = bfs.BUSCA_SUCESSO
            self.solucao = no.constroi_solucao()
            return

        # obtem os filhos do no
        for filho in no.filhos(self.problema):
            if not (filho in self.fronteira) and not (filho.estado in self.visitados):
                self.fronteira.append(filho)
                self.visitados.append(filho.estado)

        return

