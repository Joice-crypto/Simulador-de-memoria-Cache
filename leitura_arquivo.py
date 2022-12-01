# faz a leitura dos arquivos
def leituraArquivo():
    arquivo = open('arquivos_teste/trace.txt', 'r')
    enderecos = arquivo.readlines()
    arquivo.close()

    return enderecos