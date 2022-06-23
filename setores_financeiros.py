# BENEFÍCIOS - JANAYNA
def saida_ben():
    o1 = str(input('Para voltar ao menu anterior digite: "voltar"\nPara sair do sistema digite: "sair"\n'))
    if o1 == 'voltar':
        beneficios()
    if o1== 'sair':
        print("Foi um prazer ajudar!")
        exit()
    
def beneficios():
    while True:
        print('Bem vindo ao menu de Benefícios! No que posso ajudar?'.center(130, '-'))
        print('\n1) Vantagens em eventos')
        print('2) Promoções e descontos')
        print('3) Cashback com pontos')
        print('4) Voltar ao menu anterior')
        escolha=int(input('\nDigite a opção desejada: '))
        if escolha == 1:
            print('\n Os clientes da M$M possuem entradas para eventos exclusivos, descontos e prioridade nas compras.\n Consulte as condicoções em : www.mmfinanceira.com/BeneficiosEventos\n')
            saida_ben()
        if escolha == 2:
            print('\n Tenha escontos exclusivos em shows, viagens, hospedagens e restaurantes. Participe também de promoções e sorteios mensais.\n')
            saida_ben()
        if escolha == 3:
            print('\n Para os amantes de cashback, nós temos sim! Cadastre seu cpf e utilize nas compras das empresas parceiras e aproveite!\n')
            saida_ben()  
        else:            
            break
        break
#==================================================================================================================================================================================================#
# FALE CONOSCO - JOSÉ LUIZ
def fale_conosco():
    while True:
        print('Sessão Fale Conosco. No que posso ajudar?'.center(130, '-'))
        escolha2 = int(input('\n1) Contato\n2) App M&M\n3) Encontre Agências\n4) Retorne ao início \n\nDigite a opção desejada: '))
        if escolha2 == 4:
            break
        elif escolha2 == 1:
            print('\n Você pode nos contatar por essas vias:\n\n  Central de atendimento: 0800 123 321 (segunda a sexta das 08:00 às 18:00)\n  e-mail: suporte@mmfinanceira.com.br\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha:'))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break
        elif escolha2 == 2:
            print('\n Baixe o nosso app e tenha o seu serviço disponível na palma da sua mão!\n  Disponível para Androis, IOS e Windows: www.mmfinanceira.com/App\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break
        elif escolha2 == 3:
            print('\n Encontre um de nossos respresentantes mais perto de você pelo "M&M perto de você!"\n Acesse em: www.mmfinanceira.com/Pertodevoce\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break
#======================================================================================================================================================================================================#
# FINANCIAMENTOS - DAVID
def financiamentos():
    while True:
        print('Você escolheu a opção de Financiamento. O que deseja?'.center(130, '-'))
        opção = input(
        '\n1) Financiamento Estudantil.\n'
        '2) Financiamento Imobiliário\n'
        '3) Condições de Financiamento\n'
        '4) Retornar ao início\n'
        '\nDigite a opção desejada: ')
        if opção == '1':
            f_estudantil()
        elif opção == '2':
            f_imob()
        elif opção == '3':
            f_condições()
        elif opção == '4':
            break

def f_estudantil():
    while True:
        print('\n Ao solicitar o financiamento estudantil você receberá o crédito no valor das parcelas do curso, que será repassado diretamente para\n'
        ' a instituição de ensino\n')
        opção = input(
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        '\nDigite sua opção aqui: ')
        if opção == '1':
            print("Foi um prazer ajudar!")
            exit()
        else:
            break

def f_imob():
    while True:
        print('\n Ao solicitar o financiamento imobiliário você terá o valor disponível para comprar um imóvel, especificamente, seja para fins comerciais\n'
        ' ou resindeciais\n')
        opção = input(
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        '\nDigite sua opção aqui: ')
        if opção == '1':
            print("Foi um prazer ajudar!")
            exit()
        else:
            break

def  f_condições():
    while True:
        print('\n Para fazer um financiamento você precisa ser maior de 18 anos, ter documentos pessoais válidos (como RG e CPF)\n'
        ' e apresentar comprovante de renda e de residência\n')
        opção = input(
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        '\nDigite sua opção aqui: ')
        if opção == '1':
            return saida_fin()
        else:
            break

def saida_fin():
    opcao1 = str(input('Se quiser voltar ao menu digite: "voltar"\nSe quiser Sair do programa digite: "sair"\n'))
    if opcao1 == 'voltar':
        financiamentos()
    if opcao1== 'sair':
        print("Foi um prazer ajudar!")
        exit()
#================================================================================================================================================================================================#
# EMPRÉSTIMOS - ISA
def emprestimo():
    while True:
        print('Seja bem vindo ao menu de Empréstimos, no que podemos ajudar hoje?'.center(130, '-'))
        print('\n1) Empréstimo Consignado ')
        print('2) Empréstimo Estudantil ')
        print('3) Condições de Emprestimo ')
        print('4) Voltar ao menu anterior ' )
        opcao=int(input('\nDigite a opção desejada: '))
        if opcao == 1:
            print('\n Ao solicitar o empréstimo consignado você recebe o valor solicitado e terá as parcelas cobradas direto na folha de pagamento.\n O desconto é feito diretamente no salário ou na aposentadoria.\n')
            saida_emp()
        if opcao == 2:
            print('\n Ao solicitar o empréstimo estudantil, você terá o valor total para pagar os estudos e a cobrança é feita de forma parcelada,\n de acordo com as cláusulas do contrato.\n')   
            saida_emp()    
        if opcao == 3:
            print('\n Para fazer um empréstimo você precisa ser maior de 18 anos, ter documentos pessoais válidos \n (como RG e CPF) e apresentar comprovante de renda e de residência.\n')
            saida_emp()  
        else:
            break
        break
          

def saida_emp():
    opcao1 = str(input('Deseja voltar ao menu principal? digite "retornar"\nCaso queira finalizar o programa, digite "sair": '))
    if opcao1 == 'retornar':
        emprestimo()
    elif opcao1 == 'sair':
        print('Foi um prazer ajudar!')
        exit()