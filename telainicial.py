

def beneficios():
    print('1 - Vantagens em eventos')
    print('2 - Promoções e descontos')
    print('3 - Cashback com pontos')
    print('4 - Voltar ao menu anterior')
    escolha=int(input('escolha a opção desejada'))
    if escolha == 1:
        print('Os clientes da M$M possuem entradas para eventos exclusivos e descontos e prioridade. Consulte as condicoções em :www.mmfinanceira.com/BeneficiosEventos')
        sair()
    if escolha == 2:
        print('Tenha escontos exclusivos em shows, viagens, hospedagens e restaurantes. Participe também de promoções e sorteios mensais.')
        sair()
    if escolha == 3:
        print('Para os amantes de cashback, nós temos sim! Cadastre seu cpf e utilize nas compras das empresas parceiras e aproveite!')
        sair()
    if escolha == 4: 
        inicio()


def fale_conosco():
    escolha2 = int(input('\nComo posso ajudar nesse caso?\n 1. Contato\n 2. App M&M\n 3. Encontre Agências\n 4. Retorne ao início\n Escolha: '))
    if escolha2 == 4:
        inicio()
    elif escolha2 == 1:
        print('\nVocê pode nos contatar por essas vias:\n  Central de atendimento: 0800 123 321 (segunda a sexta das 08:00 às 18:00\n  e-mail: suporte@mmfinanceira.com.br\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha:'))
        if opcoes_saida == 1:
            exit()
        elif opcoes_saida == 2:
            inicio()
    elif escolha2 == 2:
        print('\nBaixe o nosso app e tenha o seu serviço disponível na palma da sua mão!\n  Disponível para Androis, IOS e Windows: www.mmfinanceira.com/App\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
        if opcoes_saida == 1:
            exit()
        elif opcoes_saida == 2:
            inicio()
    elif escolha2 == 3:
        print('\nEncontre um de nossos respresentantes mais perto de você pelo "M&M perto de você!"\n  Acesse em: www.mmfinanceira.com/Pertodevoce\n')
        opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
        if opcoes_saida == 1:
            exit()
        elif opcoes_saida == 2:
            inicio()

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

def sair():
    opcao1 = str(input('Se quiser voltar ao menu digite: "voltar"\nSe quiser Sair do programa digite: "sair"\n'))
    if opcao1 == 'voltar':
        emprestimo()
    if opcao1== 'sair':
        exit()
    else:
        print('Digite uma opção válida.')
        sair()

def emprestimo():
    print(' Seja bem vindo ao menu de Emprestimos, no que podemos ajudar hoje? ')
    print('1) Empréstimo Consignado ')
    print('2) Empréstimo Estudantil ')
    print('3) Condições de Emprestimo ')
    print('4) Voltar ao menu anterior ' )
    opcao=int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('Ao solicitar o empréstimo consignado você recebe o valor solicitado\n e terá as parcelas cobradas direto na folha de pagamento,\n o desconto é feito diretamente no salário ou na aposentadoria.')
        sair()
    if opcao == 2:
        print('Ao solicitar o empréstimo estudantil\n você terá o valor total para pagar os estudos e a cobrança é feita de forma\n parcelada de acordo com as cláusulas do contrato.')   
        sair()    
    if opcao == 3:
        print('Para fazer um empréstimo você, \nprecisa ser maior de 18 anos, ter documentos pessoais válidos, \ncomo RG e CPF e apresentar comprovante de renda  e de residência.' )
        sair()  
    if opcao == 4:
        inicio()
    else:
        print('Digite uma opção válida.')
        emprestimo()        

def inicio():
    print(' Sou o Assistente Virtual da M&M.\n Conte comigo para conhecer os recursos do Portal.\n Para começar, selecione um dos itens abaixo para que eu possa te ajudar!')
    print('1) Empréstimo')
    print('2) Financiamento')
    print('3) Benefícios')
    print('4) Fale Conosco')
    print('5) Sair do programa')
    txt = int(input('Digite a opção desejada:'))
    if txt == 1:
        emprestimo()
    if txt == 2:
        financiamentos()
    if txt == 3:
        beneficios()
    if txt == 4:
        fale_conosco()
    if txt == 5:
        exit()
    else:
        print('digite uma opção valida ')
        inicio()

inicio()