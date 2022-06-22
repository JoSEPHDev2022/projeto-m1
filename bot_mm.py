import setores_financeiros as set_if

def inicio():
    print('Sou o Assistente Virtual da M&M, conte comigo para conhecer os recursos do Portal.'.center(130, '='))
    print('Para começar, selecione um dos itens abaixo para que eu possa te ajudar!'.center(130, '='))
    print('\n1) Empréstimo')
    print('2) Financiamento')
    print('3) Benefícios')
    print('4) Fale Conosco')
    print('5) Sair do programa')
    txt = int(input('\nDigite a opção desejada: '))
    if txt == 1:
        set_if.emprestimo()
    if txt == 2:
        set_if.financiamentos()
    if txt == 3:
        set_if.beneficios()
    if txt == 4:
        set_if.fale_conosco()
    if txt == 5:
        print('Foi um prazer ajudar!')
        exit()
    else:
        inicio()

inicio()