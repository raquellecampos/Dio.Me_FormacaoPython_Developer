menu = f'''
====== Caixa eletrônico da DIO ======

 [D] Depositar
 [S] Sacar
 [E] Extrato
 [Q] Sair

===================================== 
--> Qual sua opção? 
'''

Saldo_Inicial = 100
limite_Diario = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

deposito = 0
deposito_qtde = 0
saque_valor = 0
while True:
    opcao = input(menu).upper()
    
    if opcao in ('D'):
        deposito = float(input('Digite o valor do Deposito: '))
        while True:
            if deposito <= 0:
                resposta = str(input('Ops! Valor inválido, tente novamente! Deseja inserir novamente o valor? [S/N]: ')).upper()
                if resposta in ('S','SIM'):
                  deposito = float(input('Digite o valor do Deposito novamente: '))
                elif resposta in ('N','NAO'):
                    break
            elif deposito > 0: 
              deposito_qtde += 1
              Saldo_Inicial += deposito
              extrato = (f'{deposito_qtde}° depósito no valor de R${deposito:.2f}\n')
              print(f'Depósito de R${deposito:.2f} realizado com sucesso')
              break
       
    elif opcao == 'S':
        while numero_saques <= LIMITE_SAQUES:
            saque_valor = float(input('Digite o valor a ser sacado: '))
            if saque_valor > Saldo_Inicial:
                print(f'Saldo insuficiente para efetuar o saque! Seu saldo atual é de R${Saldo_Inicial:.2f}')
            elif saque_valor <= Saldo_Inicial:
                Saldo_Inicial = Saldo_Inicial - saque_valor
                numero_saques += 1
                extrato += (f'{numero_saques}° saque no valor de R${saque_valor:.2f}\n') 
                print(f'Saque no valor de R${saque_valor} efetuado com sucesso.')
                print(extrato)
                break

    elif opcao == 'E':
        print('=-=-=-=-=-=-=-=- Extrato da sua conta =-=-=-=-=-=-=-=-')
        print(extrato)
        print('=-=-=-=-=-=-= Obrigada por usar o banco =-=-=-=-=-=-=-')

    elif opcao == 'Q':
        break

    else:
        print('Opção inválida! Verifique.')