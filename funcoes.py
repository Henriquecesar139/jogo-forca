#Funções

import os

#Devido a mudança de comando no cmd do windows e no terminal do linux
#Adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
else:
	limpar = 'clear'

#Funções que desenha o titulo e as forcas

def titulo():
    print('##############')
    print('    forca')
    print('##############')

def forca():
    print('''

    ___________
    |         |
    |
    |
    |
____|____
    ''')

def erro1():
    os.system(limpar)
    print('''
    ___________
    |         |
    |        ( )
    |
    |
____|____
        ''')

def erro2():
    os.system(limpar)
    print('''

    ___________
    |         |
    |        ( )
    |         |
    |         |
____|____
        ''')

def erro3():
    os.system(limpar)
    print('''

    ___________
    |         |
    |        ( )
    |         |\ 
    |         |
____|____
        ''')

def erro4():
    os.system(limpar)
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____
        ''')

def erro5():
    os.system(limpar)
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____      \ 
        ''')

def erro6():
    os.system(limpar)
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____    / \ Você Perdeu! :(
        ''')

def vitoria():
    print('''
    ( ) 
   \ | /
     |
    / \ 
        Você venceu!!!
    ''')