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
        exit()
    else:
        print('Digite uma opção válida.')
        emprestimo()        


emprestimo()

