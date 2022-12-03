
from cache import *
from leitura_arquivo import leituraArquivo
from simulacao import *



print('+--------------------------------------+')
print('+====================+')
print('| SIMULADOR DE CACHE |')
print('+====================+')
print('Tipos de Mapeamento\n')
print('Escolha\n 1- Mapeamento Direto\n 2- Mapeamento Associativo')


TM = int(input ('Qual o tipo de mapeamento?\n')) # Guarda o tipo do mapeamneto
if TM == 1 :   # se o usuario escolher mapeamento direto 
    executa_MD() # executa o mapeamento direto

elif TM == 2: 
    executa_MA() #executa mapeamento associativo



   



