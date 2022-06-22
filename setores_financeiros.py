
def saida_ben():
    o1 = str(input('Para voltar ao menu anterior digite: "voltar"\nPara sair do sistema digite: "sair"\n'))
    if o1 == 'voltar':
        beneficios()
    if o1== 'sair':
        print("Foi um prazer ajudar!")
        exit()
    
def beneficios():
    while True:
        print('1 - Vantagens em eventos')
        print('2 - Promoções e descontos')
        print('3 - Cashback com pontos')
        print('4 - Voltar ao menu anterior')
        escolha=int(input('escolha a opção desejada: '))
        if escolha == 1:
            print('Os clientes da M$M possuem entradas para eventos exclusivos, descontos e prioridade nas compras. Consulte as condicoções em :www.mmfinanceira.com/BeneficiosEventos')
            saida_ben()
        if escolha == 2:
            print('Tenha escontos exclusivos em shows, viagens, hospedagens e restaurantes. Participe também de promoções e sorteios mensais.')
            saida_ben()
        if escolha == 3:
            print('Para os amantes de cashback, nós temos sim! Cadastre seu cpf e utilize nas compras das empresas parceiras e aproveite!')
            saida_ben()
        else: 
            break

def fale_conosco():
    while True:
        escolha2 = int(input('\nComo posso ajudar nesse caso?\n 1. Contato\n 2. App M&M\n 3. Encontre Agências\n 4. Retorne ao início\n Escolha: '))
        if escolha2 == 4:
            break
        elif escolha2 == 1:
            print('\nVocê pode nos contatar por essas vias:\n  Central de atendimento: 0800 123 321 (segunda a sexta das 08:00 às 18:00\n  e-mail: suporte@mmfinanceira.com.br\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha:'))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break
        elif escolha2 == 2:
            print('\nBaixe o nosso app e tenha o seu serviço disponível na palma da sua mão!\n  Disponível para Androis, IOS e Windows: www.mmfinanceira.com/App\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break
        elif escolha2 == 3:
            print('\nEncontre um de nossos respresentantes mais perto de você pelo "M&M perto de você!"\n  Acesse em: www.mmfinanceira.com/Pertodevoce\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                print("Foi um prazer ajudar!")
                exit()
            elif opcoes_saida == 2:
                break

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
            break

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
            print("Foi um prazer ajudar!")
            exit()
        else:
            break

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
            print("Foi um prazer ajudar!")
            exit()
        else:
            break

def  f_condições():
    while True:
        print('CONDIÇÕES DE EMPRÉSTIMO: Para fazer um empréstimo você precisa ser maior de 18 anos, ter documentos pessoais válidos,\n'
        'como RG e CPF, e apresentar comprovante de renda e de residência\n')
        opção = input('Digite 1 para sair ou 2 para retornar ao início.\n'
        '1 - Sair\n'
        '2 - Retornar ao início\n'
        'Digite sua opção aqui: ')
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
    

def emprestimo():
    while True:
        print(' Seja bem vindo ao menu de Emprestimos, no que podemos ajudar hoje? ')
        print('1) Empréstimo Consignado ')
        print('2) Empréstimo Estudantil ')
        print('3) Condições de Emprestimo ')
        print('4) Voltar ao menu anterior ' )
        opcao=int(input('Digite a opção desejada: '))
        if opcao == 1:
            print('Ao solicitar o empréstimo consignado você recebe o valor solicitado\n e terá as parcelas cobradas direto na folha de pagamento,\n o desconto é feito diretamente no salário ou na aposentadoria.')
            saida_emp()
        if opcao == 2:
            print('Ao solicitar o empréstimo estudantil\n você terá o valor total para pagar os estudos e a cobrança é feita de forma\n parcelada de acordo com as cláusulas do contrato.')   
            saida_emp()    
        if opcao == 3:
            print('Para fazer um empréstimo você, \nprecisa ser maior de 18 anos, ter documentos pessoais válidos, \ncomo RG e CPF e apresentar comprovante de renda  e de residência.' )
            saida_emp()  
        else:
            break
          

def saida_emp():
    opcao1 = str(input('Deseja voltar ao menu principal? digite "retornar"\nCaso queira finalizar o programa, digite "sair": '))
    if opcao1 == 'retornar':
        emprestimo()
    elif opcao1 == 'sair':
        print('Foi um prazer ajudar!')
        exit()
          
