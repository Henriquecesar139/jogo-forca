#==============#
#Henrique César#
#==============#

#Importações
from random import randint
from palavras import *
from funcoes import *
from time import sleep
import os

#Devido a mudança de comando no cmd do windows e no terminal do linux
#Adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
	reinicio = 'python forca.py'
else:
	reinicio = 'python3 forca.py'
	limpar = 'clear'

os.system(limpar)

#Menu de tema
titulo()
print(f' [ 1 ] --> {vermelho}Frutas{reset} \n [ 2 ] --> {vermelho}Animais{reset} \n [ 3 ] --> {vermelho}Países{reset}')

try:
	tema = int (input('\n [tema]--> '))
except:
	print('erro')
	os.system(reinicio)

os.system(limpar)

#palavra definida com base no tema
if tema == 1:
	num = randint(0, len(frutas) -1)
	palavra = frutas[num]
elif tema == 2:
	num = randint(0, len(animais) -1)
	palavra = animais[num]
elif tema == 3:
	num = randint(0, len(paises) -1)
	palavra = paises[num]
else:
	os.system(reinicio)

#Número de letras presentes na palavra
num = len(palavra)

#Cria uma lista do tamanho da lista da palavra
numletras = []
for c in range(num):
	numletras.append('_')

#Variável dos erros
erros = 0

#Interface
titulo()
forca()

#Lista com as letras descartadas
letras_usadas = []

#Loop que acontece o jogo
while True:

	print(f'Letras descobertas {verde + " ".join(numletras) + reset}')
	print(f'letras descartadas: {vermelho + " ".join(letras_usadas) + reset}')

	letra = input (f'[{magenta}digite uma letra{reset}]-->  ')

	os.system(limpar)
	titulo()

	if letra not in char or letra in letras_usadas:
		forcas(erros)

	else:
		#Se a letra estiver presente na palavra	
		if letra in palavra:
			for i in range(len(palavra)):
				if palavra[i] == letra:
					numletras.pop(i)
					numletras.insert(i, letra)

			#As forcas são desenhadas com base na variável erros
			forcas(erros)

			#Caso a lista numletras seja igual a lista palavras, o usuário vence
			if numletras == palavra:
				vitoria()
				print(f'A palavra era { magenta + "".join(palavra)}')
				sleep(10)
				break

		#caso não esteja
		else:
			erros = erros + 1
			letras_usadas.append(letra)
			#Desenha o personagem na forca quando o usuário erra
			forcas(erros)
			#se erros for igual a 6, o usuário perde
			if erros == 6:
				erro6()
				print(f'A palavra era {magenta + "".join(palavra)}')	
				sleep(10)
				break
		
os.system(reinicio)
			
