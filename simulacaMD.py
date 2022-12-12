
from leitura_arquivo import *
from cache import *

#simula mapeamento direto
def executa_MD(): 
    
        numeroDeLinhas = 256
        tamPalavra = 16
        TamTotalCache = 4096
        numDeconjunto = 0 # nao tenho conjuntos no mapeamento direto 
        linhasDoconjunto = 256 # apenas 1 unico bloco
        memoriaPrincipal = MemoriaPrincipal()
       
        politicaEscrita = int(input('\tPolitica de Escrita:\n 0 - write-through;\n1 - write-back\n '))

        if politicaEscrita == 0 : 
            memoriaCache = MemoriaCache(numDeconjunto, linhasDoconjunto) 
        
            resto = 0
            aux = tamPalavra
            enderecoPalavra = 0
            while resto != 1:
                aux = aux/2
                resto = aux
                enderecoPalavra += 1
            rotulo = 32 - (enderecoPalavra + 256)
            CalculaResultado(memoriaCache,rotulo,politicaEscrita,memoriaPrincipal,TamTotalCache,numeroDeLinhas)
        elif politicaEscrita == 1 :
           
            memoriaCache = MemoriaCache(numDeconjunto, linhasDoconjunto) 
        
            resto = 0
            aux = tamPalavra
            enderecoPalavra = 0
            while resto != 1:
                aux = aux/2
                resto = aux
                enderecoPalavra += 1
            rotulo = 32 - (enderecoPalavra + 256)
            CalculaResultado(memoriaCache,rotulo,politicaEscrita,memoriaPrincipal,TamTotalCache,numeroDeLinhas)
       
    

def CalculaResultado(memoriaCache,rotulo,politicaEscrita,memoriaPrincipal,TamTotalCache,numeroDeLinhas):
    
            enderecos = leituraArquivo()
            leituras = 0
            escritas = 0
            leiturasNaCache = 0
            leiturasNaMP = 0
            escritasNaCache = 0
            escritasNaMP = 0
            encontrouNaCacheLeitura = 0
            encontrouNaCacheEscrita = 0
            miss = 0
            missEscrita = 0
            encontrouNaMPLeitura = 0
            encontrouNaMPEscrita = 0


            for end in enderecos:
                    atributos = end.split(' ') #separo a operação dos numeros
                    operacao  = atributos[0] # r ou w
                    endereco = atributos[1] # o endereço bin
                    my_hexdata = endereco
                    scale = 16
                    # equals to hexadecimal
                    num_of_bits = 32
                   
                    endBinario = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
                    rotuloEndereco = endBinario[0:rotulo]
                    enderecoconjunto = endBinario[rotulo+1:rotulo+1+256]
                    operacao = operacao.replace('\n', '')
                    if operacao == "r":
                        conjunto = memoriaCache.procuraConjunto(enderecoconjunto)
                        leituras += 1
                        leiturasNaCache += 1
                        if conjunto:
                                # Procura rotulo pelo conjunto encontrado
                            retornoRotulo = Conjunto.procuraTAG(Conjunto,rotuloEndereco)
                            if retornoRotulo:
                                # Se encontrou o rótulo ocorre hit
                                encontrouNaCacheLeitura += 1
                            else:
                                # Caso não encontrou o rótulo da miss
                                miss += 1
                               
                        else:
                            conjunto = memoriaCache.gravaConjunto(enderecoconjunto)
                            if conjunto:
                                Conjunto.gravaTAG()
                                leiturasNaMP += 1
                                encontrouNaMPLeitura += 1
                    elif operacao == "w":
                        escritas += 1
                        conjunto = memoriaCache.procuraConjunto(enderecoconjunto)
                        escritasNaCache += 1
                        if not conjunto:
                            conjunto = memoriaCache.gravaConjunto(enderecoconjunto)
                            
                            Conjunto.gravaTAG()
                        else:
                            retornoRotulo = Conjunto.procuraTAG(Conjunto,rotuloEndereco)
                            if not retornoRotulo:
                                Conjunto.gravaTAG()
                                missEscrita += 1
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
                taxaDeMissCacheLeitura = ((miss*100.0)/leiturasNaCache)
            # Acerto Leitura MP
            if leiturasNaMP:
                taxaDeAcertoMPLeitura = (encontrouNaMPLeitura*100.0)/leiturasNaMP
            if escritasNaCache:
                taxaDeAcertoCacheEscrita = ((encontrouNaCacheEscrita*100.0)/escritasNaCache)
                taxaDeMissCacheEscrita = ((missEscrita*100.0)/escritasNaCache)
            totalLeituraEscrita = (float(encontrouNaCacheLeitura)+float(encontrouNaCacheEscrita))
            taxaAcerto = totalLeituraEscrita / (leiturasNaCache + escritasNaCache)
            taxaErro = (((encontrouNaCacheLeitura*100.0)- TamTotalCache) / TamTotalCache)
        

            # totalDeRegistros = leituras + escritas

            taxaDeAcertoCacheLeitura = format(taxaDeAcertoCacheLeitura, '.4f')
            taxaDeMissCacheLeitura = format(taxaDeMissCacheLeitura, '.4f')
            taxaDeAcertoCacheEscrita = format(taxaDeAcertoCacheEscrita, '.4f')
            taxaDeMissCacheEscrita = format(taxaDeMissCacheEscrita, '.4f')
            taxaAcerto = format(taxaAcerto, '.4f')
            taxaErro = format(taxaErro, '.4f')
                
                        
            
                    
                    
        
        
             
   

    


    
   
   
    
   
    




    


