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
print(' [ 1 ] --> Frutas \n [ 2 ] --> Animais \n [ 3 ] --> Países')

try:
	tema = int (input('---> '))
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
	#Algumas informações
	print(f'Letras descobertas {" ".join(numletras)}')
	print(f'letras descartadas: {" ".join(letras_usadas)}')
	letra = input ('-->  ')
	
	#Se a letra estiver presente na palavra
	if letra in palavra:
		for i in range(len(palavra)):
			if palavra[i] == letra:
				numletras.pop(i)
				numletras.insert(i, letra)

		#As forcas são desenhadas com base na variável erros
		os.system(limpar)
		if erros == 0:
			forca()
		if erros == 1:
			erro1()
		if erros == 2:
			erro2()
		if erros == 3:
			erro3()
		if erros == 4:
			erro4()
		if erros == 5:
			erro5()
		#Caso a lista numletras seja igual a lista palavras
		if numletras == palavra:
			vitoria()
			print(f'A palavra era {"".join(palavra)}')
			sleep(10)
			break

	#caso não esteja
	else:
		#Adiciona um valor a variável erros
		erros = erros + 1
		#Adiciona a letra a lista de letras descartadas
		letras_usadas.append(letra)
		#Desenha o personagem na forca quando o usuário erra
		if erros == 1:
			erro1()
		elif erros == 2:
			erro2()
		elif erros == 3:
			erro3()
		elif erros == 4:
			erro4()
		elif erros == 5:
			erro5()
		elif erros == 6:
			erro6()
			print(f'A palavra era {"".join(palavra)}')	
			sleep(10)
			break
		
os.system(reinicio)
			
