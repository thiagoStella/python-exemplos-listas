'''Crie um dicionário com o nome e a profissão de duas pessoas e adicione uma terceira pessoa com nome e profissão.'''
pessoas = {}
for i in range(2):
    nome = input('Digite o nome: ')
    profissao  = input('Digite a profisão: ')
    pessoas[nome] = profissao
nome = input('Digite o nome da terceira pessoa: ')
profissao = input('Digite a profissão da terceira pessoa: ')
pessoas[nome] = profissao

print(pessoas)
