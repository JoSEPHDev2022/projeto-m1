# FINANCIAMENTO - David Lima
from telainicial import inicio

def financiamentos():

    while True:
        opção = input('Você escolheu a opção FINANCIAMENTO. O que deseja?\n'
        '1 - FINANCIAMENTO ESTUDANTIL\n'
        '2 - FINANCIAMENTO IMOBILIÁRIO\n'
        '3 - CONDIÇÕES DE FINANCIAMENTO\n'
        '4 - RETORNAR AO INÍCIO\n'
        'Digite sua opção aqui: ')
        if opção == '1':
            f_estudantil()
        elif opção == '2':
            f_imob()
        elif opção == '3':
            f_condições()
        elif opção == '4':
            return inicio()
def sair():
    print('Você saiu do sistema')
    exit()

def f_estudantil():
    while True:
        print('Você escolheu a opção FINANCIAMENTO ESTUDANTIL. Ao solicitar o financiamento estudantil\n'
        'você receberá o crédito no valor das parcelas do curso que será repassado diretamente para\n'
        'a instituição d ensino\n')
        opção = input('Digite 1 para sair ou 2 para retornar ao início.\n'
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        'Digite sua opção aqui: ')
        if opção == '1':
            return sair()
        elif opção == '2':
            return inicio()

def f_imob():
    while True:
        print('Você escolheu a opção FINANCIAMENTO IMOBILIÁRIO. Ao solicitar o financiamento imobiliário\n'
        'você terá o valor disponível para comprar um imóvel, especificamente, seja para fim comercial\n'
        'ou resindecial\n')
        opção = input('Digite 1 para sair ou 2 para retornar ao início.\n'
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        'Digite sua opção aqui: ')
        if opção == '1':
            return sair()
        elif opção == '2':
            return inicio()

def  f_condições():
    while True:
        print('CONDIÇÕES DE EMPRÉSTIMO: Para fazer um empréstimo você precisa ser maior de 18 anos, ter documentos pessoais válidos,\n'
        'como RG e CPF, e apresentar comprovante de renda e de residência\n')
        opção = input('Digite 1 para sair ou 2 para retornar ao início.\n'
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        'Digite sua opção aqui: ')
        if opção == '1':
            return sair()
        elif opção == '2':
            return inicio()
            

