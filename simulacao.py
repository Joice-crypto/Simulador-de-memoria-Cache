# vou escrever e ler os valores do txt e imprimir os resuktados dda cache

def executa_MD(): 
    print("oi")
    

def executa_MA():
     politicaEscrita = int(input('\tPolitica de Escrita:\n 0 - write-through;\n1 - write-back; '))
    #  tamanhoDaLinha = int(input('\tTamanho da Linha : ')) #16 bits AINDA NÃO SEEEIIII
    #  numeroDeLinhas = 256
     numDeConjunto = int(input('\tAssossiatividade por conjunto:\n 0 - 2 vias;\n 1 - 4 vias;\n 2- 8 vias '))
    #  tempoAcesso = int(input('\tTempo de acesso quando encontra (hit-time): '))
     politicaSubstituicao = int(input('\tPolitica de Substituição:\n 0 - LFU;\n1 - LRU;\n2 - Aleatório;'))
    #  tempoMP = int(input('\tTempo de leitura/escrita:'))

    
   

     if politicaEscrita == 0: # se for write-through e
        if  numDeConjunto == 0: # se for Associatividade de 2 vias
             qtdDeLinhasConjuntos = numeroDeLinhas/numDeConjunto
             print("AAAAA")