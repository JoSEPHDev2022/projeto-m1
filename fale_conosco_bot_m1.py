# FALE CONOSCO - José Luiz

def saida():
    print('Foi um prazer ajudar!')
    exit()

def retorno_inicio(escolha, escolha2):
    print('Ok, vamos começar novamente!')
    escolha2 = False
    escolha = False
    return escolha2, escolha

bot = True

while bot == True:
    titulo_ini1 = 'Olá! Sou o assistente virtual da M&M. Conte comigo apra conhecer os recursos do portal'
    titulo_ini2 = 'Para começar, selecione um dos itens abaixo para que eu possa te ajudar!:'
    print(titulo_ini1.center(150, '='))
    print(titulo_ini2.center(150, '=') + '\n')

    escolha = int(input(' 1. Empréstimo\n 2. Financiamento\n 3. Benefícios\n 4. Fale Conosco\n 5. Sair\n Escolha: '))

    if escolha == 5:
        saida()

    if escolha == 4:
        escolha == True     
        escolha2 = int(input('\nComo posso ajudar nesse caso?\n 1. Contato\n 2. App M&M\n 3. Encontre Agências\n 4. Retorne ao início\n Escolha: '))
        
        if escolha2 == 4:
            retorno_inicio(escolha, escolha2)
        elif escolha2 == 1:
            print('\nVocê pode nos contatar por essas vias:\n  Central de atendimento: 0800 123 321 (segunda a sexta das 08:00 às 18:00\n  e-mail: suporte@mmfinanceira.com.br\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha:'))
            if opcoes_saida == 1:
                saida()
            elif opcoes_saida == 2:
                retorno_inicio(escolha, escolha2)

        elif escolha2 == 2:
            print('\nBaixe o nosso app e tenha o seu serviço disponível na palma da sua mão!\n  Disponível para Androis, IOS e Windows: www.mmfinanceira.com/App\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                saida()
            elif opcoes_saida == 2:
                retorno_inicio(escolha, escolha2)

        elif escolha2 == 3:
            print('\nEncontre um de nossos respresentantes mais perto de você pelo "M&M perto de você!"\n  Acesse em: www.mmfinanceira.com/Pertodevoce\n')
            opcoes_saida = int(input(' 1. Sair\n 2. Retornar ao início\n Escolha: '))
            if opcoes_saida == 1:
                saida()
            elif opcoes_saida == 2:
                retorno_inicio(escolha, escolha2)