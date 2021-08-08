###############
#Henrique César
###############


#Importações
from random import randint
from palavras import *
from funcoes import *
import os
from time import sleep

#Devido a mudança de comando no cmd do windows e no terminal do linux
#Adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
else:
	limpar = 'clear'

os.system(limpar)

#Menu de tema

print(' [ 1 ] --> Frutas \n [ 2 ] --> Animais')

tema = int (input('--> '))
os.system(limpar)

#palavra definida com base no tema
if tema == 1:
	num = randint(0, len(frutas))
	palavra = frutas[num]
elif tema == 2:
	num = randint(0, len(animais))
	palavra = animais[num]

else:
	print('erro')
	(exit())


#Número de letras presentes na palavra
num = len(palavra)

#Cria uma lista do tamanho da lista da palavra
numletras = []
for c in range(num):
	numletras.append('-')

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
	print(f'Letras descobertas {numletras}')
	print(f'letras usadas: {letras_usadas}')
	letra = input ('-->  ')
	#Caso a letra esteja na palavra
	
	#Se a letra estiver presente na palavra
	if letra in palavra:
		for i in range(len(palavra)):
			if palavra[i] == letra:
				numletras.pop(i)
				numletras.insert(i, letra)

		#As forcas são desenhadas com base na variável erros (parte desnecessária [Apenas por estética])
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
			print(f'A palavra era {palavra}')
			sleep(8)
			(exit())

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
			print(f'A palavra era {palavra}')	
			sleep(8)
			(exit())
			