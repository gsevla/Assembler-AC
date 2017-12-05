# lib para trabalhar com argumentos
import sys

# String de paramentro na chamada no terminal
file_name = sys.argv[1]

# Acessa um arquivo para leitura
arq = open(file_name, 'r')

# Lê cada linha do arquivo e transforma em uma lista de strings
lista = arq.readlines()

for l in lista:
	print(l[:-1])

