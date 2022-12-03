
from datetime import datetime
from random import randint

#precisa usar o date para verificar o menos acessado na memoria

# AQUI EU VOU FAZER A INICIALIZAÇÃO DA MINHA CACHE 

class Linha:

    TAG = ''
    enderecoTotal = ''
    lru = ''
    lfu = 0
    fifo = ''

    def __init__(self, TAG, enderecoTotal):
        self.TAG = TAG
        self.enderecoTotal = enderecoTotal


class Conjunto:
    linha = []
    conjunto = ''
    tamanho = 0
    prox = 0

    def __init__(self, qtdeLinhas):
        self.linhas = []
        self.tamanho = qtdeLinhas
        self.prox = 0

    def getConjunto(self):
        return self.conjunto

    def setConjunto(self, conjunto):
        self.conjunto = conjunto

    def procuraTAG(self, TAGEndereco):
        for lin in self.linha:
            if lin.TAG == TAGEndereco:
                lin.lfu += 1
                data = datetime.now()
                lin.lru = data
                return True
        return False

    def buscaUltimaUsada(self):
        aux = self.linha[0].lru
        menosUsado = 0
        for i, x in enumerate(self.linha):
            if x.lru < aux:
                aux = x.lru
                menosUsado = i
        return menosUsado

    def buscaMenosUsada(self):
        aux = self.linha[0].lfu
        menosUsado = 0
        for i, x in enumerate(self.linha):
            if x.lfu < aux:
                aux = x.lfu
                menosUsado = i
        return menosUsado

    def gravaRotulo(self, rotuloEndereco, politicaSubstituicao, politicaGravacao, mp,enderecoTotal):
        if self.prox == self.tamanho and self.linha != []:
            # LFU
            if politicaSubstituicao == 0:
                poslinhaMenosUsada = self.buscaMenosUsada()
                linha_object = Linha(rotuloEndereco, enderecoTotal)
                del self.linha[poslinhaMenosUsada]
                self.linha.insert(poslinhaMenosUsada, linha_object)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha_object.enderecototal)
            # LRU
            elif politicaSubstituicao == 1:
                poslinhaMenosRecUsada = self.buscaUltimaUsada()
                data = datetime.now()
                linha_object = Linha(rotuloEndereco, enderecoTotal)
                linha_object.lru = data
                del self.linha[poslinhaMenosRecUsada]
                self.linha.insert(poslinhaMenosRecUsada, linha_object)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha_object.enderecoTotal)
            # Aleatorio
            else:
                linhaAleatoria = randint(0, self.prox)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(self.linha[linhaAleatoria].enderecoTotal)
                linha_object = Linha(rotuloEndereco, enderecoTotal)
                self.linha.insert(linhaAleatoria, linha_object)

        else:
            linha_object = Linha(rotuloEndereco, enderecoTotal)
            if politicaSubstituicao == 0:
                linha_object.lfu += 1
            elif politicaSubstituicao == 1:
                data = datetime.now()
                linha_object.lru = data
            self.linha.append(linha_object)
            self.prox = self.prox + 1


def gravaTAG(self, TAGEndereco, politicaSubstituicao, politicaGravacao, mp, enderecoTotal):
        if self.prox == self.tamanho and self.linha != []:
            # LFU
            if politicaSubstituicao == 0:
                poslinhaMenosUsada = self.buscaMenosUsada()
                linha_object = Linha(TAGEndereco, enderecoTotal)
                del self.linha[poslinhaMenosUsada]
                self.linha.insert(poslinhaMenosUsada, linha_object)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha_object.enderecototal)
            # LRU
            elif politicaSubstituicao == 1:
                poslinhaMenosRecUsada = self.buscaUltimaUsada()
                data = datetime.now()
                linha_object = Linha(TAGEndereco, enderecoTotal)
                linha_object.lru = data
                del self.linha[poslinhaMenosRecUsada]
                self.linha.insert(poslinhaMenosRecUsada, linha_object)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha_object.enderecoTotal)
            # Aleatorio
            else:
                linhaAleatoria = randint(0, self.prox)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(self.linha[linhaAleatoria].enderecoTotal)
                linha_object = Linha(TAGEndereco, enderecoTotal)
                self.linha.insert(linhaAleatoria, linha_object)

        else:
            linha_object = Linha(TAGEndereco, enderecoTotal)
            if politicaSubstituicao == 0:
                linha_object.lfu += 1
            elif politicaSubstituicao == 1:
                data = datetime.now()
                linha_object.lru = data
            self.linha.append(linha_object)
            self.prox = self.prox + 1


class MemoriaPrincipal:
    enderecos = []
    total = 0

    def __init__(self):
        self.enderecos = []
        self.total = 0

    def adicionaNaMP(self, enderecoTotal):
        self.enderecos.append(enderecoTotal)
        self.total += 1

    def buscaNaMP(self, enderecoTotal):
        for i in self.enderecos:
            if i == enderecoTotal:
                return True
        return False


class MemoriaCache:
    conjuntos = []
    tamanho = 0
    proximo = 0

    def __init__(self, qtdeConjuntos, qtdeLinhas):
        self.tamanho = qtdeConjuntos
        for i in range(0, qtdeConjuntos):
            self.conjuntos.append(Conjunto(qtdeLinhas))
        self.proximo = 0

    def setConjuntos(self, conjuntos):
        self.conjuntos = conjuntos

    def getConjuntos(self):
        return self.conjuntos

    def procuraConjunto(self, enderecoConjunto):
        for i in range(0, self.proximo):
            if self.conjuntos[i].getConjunto() == enderecoConjunto:
                return self.conjuntos[i]
        return False

    def gravaConjunto(self, enderecoConjunto):
        if self.proximo != self.tamanho:
            self.conjuntos[self.proximo].setConjunto(enderecoConjunto)
            self.proximo += 1
            return self.conjuntos[self.proximo-1]
        return None



    
   


 