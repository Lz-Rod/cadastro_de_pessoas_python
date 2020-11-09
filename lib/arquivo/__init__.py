from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')#essa variável usa a função open() que abre o arquivo read and text rd
        a.close()#fecha o arquivo aberto na variável a
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')#essa variável irá creiuar um arquivo de texto, basicamente o wt+ significa write text e cria o arquivo, e o + verifica se o arquivo não existe antes de criá-lo
        a.close()
    except:
        print('Houve um Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        '''print(a.readlines()) #pega o conteudo do arquivo txt e salva cada linha como um item de uma lista'''
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')#remove o \n do fim de cada linha do cadastro
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')#at é de appent text, ou seja, ele abre o arquivo e possibilita adicionar itens
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()#sempre lembrar de fechar o arquivo
