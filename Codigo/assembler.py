# lib para trabalhar com argumentos
import sys

# String de paramentro na chamada no terminal
file_name = sys.argv[1]

if(file_name.endswith(".asm")):	# Verfica se o arquivo informado tem a extensão correta (ACHAR UM FORMA DE INTERROMPER O PROGRAMA)
	try:
		# Acessa um arquivo para leitura
		arq = open(file_name, 'r')

		# Lê cada linha do arquivo e transforma em uma lista de strings
		lista = arq.readlines()

		for l in lista:
			print(l[:-1])

	except FileNotFoundError:
		print("O arquivo informado não existe!")
else:	# Finaliza o programa caso a extensão seja incorreta
	print("O arquivo informado não é válido! (!= .asm)")