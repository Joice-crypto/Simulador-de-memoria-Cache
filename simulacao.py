# vou escrever e ler os valores do txt e imprimir os resuktados dda cache
from leitura_arquivo import *
from cache import *

def executa_MD(): 
    print("oi")
    


# Simula a cache por associação
def executa_MA():
    politicaEscrita = int(input('\tPolitica de Escrita:\n 0 - write-through;\n1 - write-back\n '))
    numeroDeLinhas = 256
    numDeconjunto = int(input('\tAssossiatividade por conjunto:\n 0 - 2 vias;\n 1 - 4 vias;\n 2- 8 vias\n'))
    #  tempoAcesso = int(input('\tTempo de acesso quando encontra (hit-time): '))
    politicaSubstituicao = int(input('\tPolitica de Substituição:\n 0 - LFU;\n1 - LRU;\n2 - Aleatório\n'))
    #  tempoMP = int(input('\tTempo de leitura/escrita:'))
    TamTotalCache = 4096
    TamLinha = 16
    memoriaPrincipal = MemoriaPrincipal()
    
   

    if politicaEscrita == 0 and numDeconjunto == 0 and politicaSubstituicao == 0: # se for write-through e #associativiade 2 vias e politica sub LFU
                                                        
        #Calcula o tamanho do endereço do conjunto
        resto = 0
        tamanhoEnderecoconjunto = 0
        numDeconjunto = 2
        aux = numDeconjunto
        linhasPorconjunto = 128  #256 / 2
        while resto != 1:
            aux = aux/2
            resto = aux
            tamanhoEnderecoconjunto += 1
        # Calcula o tamanho do endereço da palavra
        resto = 0
        aux = TamLinha
        enderecoPalavra = 0
        while resto != 1:
            aux = aux/2
            resto = aux
            enderecoPalavra += 1
        # Calcula o rótulo
        rotulo = 32 - (enderecoPalavra + tamanhoEnderecoconjunto)
        memoriaCache = MemoriaCache(numDeconjunto, linhasPorconjunto) #tenho que fazer essa função
        CalculaResultado(memoriaCache,rotulo,tamanhoEnderecoconjunto,politicaSubstituicao,politicaEscrita,
        memoriaPrincipal,TamLinha,TamTotalCache,numeroDeLinhas,numDeconjunto)


    elif politicaEscrita == 0 and numDeconjunto == 1 and politicaSubstituicao == 0:
                                                     
        #Calcula o tamanho do endereço do conjunto
        resto = 0
        tamanhoEnderecoconjunto = 0
        numDeconjunto = 4
        aux = numDeconjunto
        linhasPorconjunto = 64  #256 / 4
        while resto != 1:
            aux = aux/2
            resto = aux
            tamanhoEnderecoconjunto += 1
        # Calcula o tamanho do endereço da palavra
        resto = 0
        aux = TamLinha
        enderecoPalavra = 0
        while resto != 1:
            aux = aux/2
            resto = aux
            enderecoPalavra += 1
        # Calcula o rótulo
        rotulo = 32 - (enderecoPalavra + tamanhoEnderecoconjunto)
        memoriaCache = MemoriaCache(numDeconjunto, linhasPorconjunto) #tenho que fazer essa função
        CalculaResultado(memoriaCache,rotulo,tamanhoEnderecoconjunto,politicaSubstituicao,politicaEscrita,
        memoriaPrincipal,TamLinha,TamTotalCache,numeroDeLinhas,numDeconjunto)

    elif politicaEscrita == 1 and numDeconjunto == 0 and politicaSubstituicao == 2:
                                                      
        #Calcula o tamanho do endereço do conjunto
        resto = 0
        tamanhoEnderecoconjunto = 0
        numDeconjunto = 8
        aux = numDeconjunto
        linhasPorconjunto = 32  #256 / 8
        while resto != 1:
            aux = aux/2
            resto = aux
            tamanhoEnderecoconjunto += 1
        # Calcula o tamanho do endereço da palavra
        resto = 0
        aux = TamLinha
        enderecoPalavra = 0
        while resto != 1:
            aux = aux/2
            resto = aux
            enderecoPalavra += 1
        # Calcula o rótulo
        rotulo = 32 - (enderecoPalavra + tamanhoEnderecoconjunto)
        memoriaCache = MemoriaCache(numDeconjunto, linhasPorconjunto) #tenho que fazer essa função
        CalculaResultado(memoriaCache,rotulo,tamanhoEnderecoconjunto,politicaSubstituicao,politicaEscrita,
        memoriaPrincipal,TamLinha,TamTotalCache,numeroDeLinhas,numDeconjunto)


def CalculaResultado(memoriaCache,rotulo,tamanhoEnderecoconjunto,politicaSubstituicao,politicaEscrita,memoriaPrincipal,
    TamLinha,TamTotalCache,numeroDeLinhas,numDeconjunto):
                enderecos = leituraArquivo()
                leituras = 0
                escritas = 0
                leiturasNaCache = 0
                leiturasNaMP = 0
                escritasNaCache = 0
                escritasNaMP = 0
                encontrouNaCacheLeitura = 0
                encontrouNaCacheEscrita = 0
                miss= 0
                encontrouNaMPLeitura = 0
                encontrouNaMPEscrita = 0
                for end in enderecos:
                    atributos = end.split(' ') #separo a operação dos numeros
                    operacao  = atributos[0] # r ou w
                    endereco = atributos[1] # o endereço bin

                        # Transforma em binário
                    my_hexdata = endereco
                    scale = 16
                    # equals to hexadecimal
                    num_of_bits = 32
                    endBinario = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
                    rotuloEndereco = endBinario[0:rotulo]
                    enderecoconjunto = endBinario[rotulo+1:rotulo+1+tamanhoEnderecoconjunto]
                    operacao = operacao.replace('\n', '')
                    if operacao == "r":
                        conjunto = memoriaCache.procuraConjunto(enderecoconjunto)
                        leituras += 1
                        # Contador de leituras
                        leiturasNaCache += 1
                        if conjunto:
                            # Procura rotulo pelo conjunto encontrado
                            retornoRotulo = Conjunto.procuraTAG(Conjunto,rotuloEndereco)
                            if retornoRotulo:
                                # Se encontrou o rótulo ocorre hit
                                encontrouNaCacheLeitura += 1
                            else:
                                # Caso não encontrou o rótulo da miss
                                Conjunto.gravaRotulo(
                                    Conjunto, rotuloEndereco, politicaSubstituicao, politicaEscrita,
                                    memoriaPrincipal, endBinario
                                )
                                miss += 1
                                leiturasNaMP += 1
                                encontrouNaMPLeitura += 1
                        else:
                            conjunto = memoriaCache.gravaConjunto(enderecoconjunto)
                            if conjunto:
                                Conjunto.gravaRotulo(Conjunto,
                                    rotuloEndereco, politicaSubstituicao, politicaEscrita,
                                    memoriaPrincipal, endBinario
                                )
                                miss += 1
                                leiturasNaMP += 1
                                encontrouNaMPLeitura += 1
                    elif operacao == "w":
                        escritas += 1
                        conjunto = memoriaCache.procuraConjunto(enderecoconjunto)
                        escritasNaCache += 1
                        if not conjunto:
                            conjunto = memoriaCache.gravaConjunto(enderecoconjunto)
                            
                            Conjunto.gravaRotulo(Conjunto,rotuloEndereco, politicaSubstituicao, politicaEscrita,memoriaPrincipal, endBinario)
                        else:
                            retornoRotulo = conjunto.procuraTAG(rotuloEndereco)
                            if not retornoRotulo:
                                Conjunto.gravaRotulo(Conjunto,
                                    rotuloEndereco, politicaSubstituicao, politicaEscrita,
                                    memoriaPrincipal, endBinario
                                )
                            else:
                                encontrouNaCacheEscrita += 1
                        if politicaEscrita == 0:
                            escritasNaMP += 1
                            encontrouNaMPEscrita += 1

                totalDeRegistros = leituras + escritas
                # Seta total de escritas;
                totalDeEscritas = escritas
                totalDeLeituras = leituras
                taxaDeAcertoCacheLeitura = 0
                taxaDeAcertoCacheEscrita =0
                # Acerto Leitura Cache
                if leiturasNaCache:
                    taxaDeAcertoCacheLeitura = ((encontrouNaCacheLeitura*100.0)/leiturasNaCache)
                # Acerto Leitura MP
                if leiturasNaMP:
                    taxaDeAcertoMPLeitura = (encontrouNaMPLeitura*100.0)/leiturasNaMP
                if escritasNaCache:
                    taxaDeAcertoCacheEscrita = ((encontrouNaCacheEscrita*100.0)/escritasNaCache)
                totalLeituraEscrita = (float(encontrouNaCacheLeitura)+float(encontrouNaCacheEscrita))
                taxaAcerto = totalLeituraEscrita / (leiturasNaCache + escritasNaCache)
            

                # totalDeRegistros = leituras + escritas

                taxaDeAcertoCacheLeitura = format(taxaDeAcertoCacheLeitura, '.4f')
                taxaDeAcertoCacheEscrita = format(taxaDeAcertoCacheEscrita, '.4f')
                taxaAcerto = format(taxaAcerto, '.4f')

                texto = ""
                texto += "\nDADOS DE ENTRADA:\n"
                if politicaEscrita == 0:
                    texto += "Politica de Escrita: " + str(politicaEscrita)
                    texto += " - write-through\n"
                else:
                    texto += "Politica de Escrita: " + str(politicaEscrita)
                    texto += " - write-back\n"
                texto += "Tamanho da linha: " + str(TamLinha) + ", \n"
                texto += "Numero de linhas: " + str(numeroDeLinhas) + ", \n"
                texto += "Associatividade por conjunto: " + str(numDeconjunto) + "\n"
            

                if politicaSubstituicao == 0:
                    texto += "Politica de Substituição: " + str(politicaSubstituicao)
                    texto += " - LFU\n"
                elif politicaSubstituicao == 1:
                    texto += "Politica de Substituição: " + str(politicaSubstituicao)
                    texto += " - LRU\n"
                else:
                    texto += "Politica de Substituição: " + str(politicaSubstituicao)
                    texto += " - Aleatorio\n"

                texto += "\tRESULTADOS:\n"
                texto += "Tamanho da Cache: " + str(TamTotalCache) + "\n"
                texto += "\tTotal de endereços no arquivo de entrada:\n"
                texto += "Total de registros: " + str(totalDeRegistros) + "\n"
                texto += "Total de leituras: " + str(totalDeLeituras) + "\n"
                texto += "Total de escritas: " + str(totalDeEscritas) + "\n"

                texto += "\tDados da Cache:\n"
                texto += "Total de leituras: " + str(leiturasNaCache) + "\n"
                texto += "Total de acertos: " + str(encontrouNaCacheLeitura) + "\n"
                texto += "Taxa de acerto de Leitura: " + str(taxaDeAcertoCacheLeitura) + "%\n"

                texto += "Total de escritas: " + str(escritasNaCache) + "\n"
                texto += "Total de acertos: " + str(encontrouNaCacheEscrita) + "\n"
                texto += "Taxa de acerto de Escrita: " + str(taxaDeAcertoCacheEscrita) + "%\n"

                texto += "\tTaxa de acertos: " + str(taxaAcerto) + "%\n"

                texto += "Dados da Memória Principal:\n"
                texto += "Total de escritas: " + str(encontrouNaMPEscrita) + "\n"
                texto += "Total de leituras: " + str(encontrouNaMPLeitura) + "\n"
                texto += "Acessos: " + str(leiturasNaMP+escritasNaMP) + "\n"

                print (texto)

                EscreveResultados(texto)

                return

    


