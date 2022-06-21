def beneficios():
    print('1 - Vantagens em eventos')
    print('2 - Promoções e descontos')
    print('3 - Cashback com pontos')
    print('4 - Voltar ao menu anterior')

    escolha=int(input('escolha a opção desejada'))
    
    if escolha == 1:
        print('Os clientes da M$M possuem entradas para eventos exclusivos e descontos e prioridade. Consulte as condicoções em :www.mmfinanceira.com/BeneficiosEventos')
    if escolha == 2:
        print('Tenha escontos exclusivos em shows, viagens, hospedagens e restaurantes. Participe também de promoções e sorteios mensais.')
    if escolha == 3:
        print('Para os amantes de cashback, nós temos sim! Cadastre seu cpf e utilize nas compras das empresas parceiras e aproveite!')
    if escolha == 4: 
        print('Voltar ao menu anterior')