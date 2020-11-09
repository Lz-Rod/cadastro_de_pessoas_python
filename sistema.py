from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):#caso o arquivo não exista ele cria o novo arquivo
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #lista o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Opção inválida.\033[m')
    sleep(1)
