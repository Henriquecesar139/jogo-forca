#Funções

import os

#Devido a mudança de comando no cmd do windows e no terminal do linux
#Adaptei o comando para o cmd e terminal
if os.name == 'nt':
	limpar = 'cls'
else:
	limpar = 'clear'

ciano = '\033[1;36m'
reset = '\033[0;00m'

#Funções que desenha o titulo e as forcas

def titulo():
    print(ciano + '''
 _ ____ ____ ____    ___  ____    ____ ____ ____ ____ ____ 
 | |  | | __ |  |    |  \ |__|    |___ |  | |__/ |    |__| 
_| |__| |__] |__|    |__/ |  |    |    |__| |  \ |___ |  | 
                                                          
    
    ''' + reset)

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
    titulo()
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
    titulo()
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
    titulo()
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
    titulo()
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
    titulo()
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
    titulo()
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____    / \ Você Perdeu! :(
        ''')

def vitoria():
    os.system(limpar)
    titulo()
    print('''
    ( ) 
   \ | /
     |
    / \ 
        Você venceu!!!
    ''')
