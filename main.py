from sistema import Cliente,Conta,Movimentacao
from peewee import *
import os
from datetime import date

with SqliteDatabase('banco.db') as db:
    
    while True:
        print(' Bem Vindo ao Banco DIO '.center(40,'#'))
        print(' Escolha uma das opição abaixo '.center(40,'#'))
        print('1 - Cadastrar conta')
        print('2 - Entrar Conta')
        print('s - Sair')
        menu = input()

        if menu == 's':
            break
        elif menu == '1':
            os.system('cls')
            print(' Cadastro de Conta '.center(40,'#'))
            cpf = input('Informe seu cpf: ')
            cliente = Cliente.select().where(Cliente.cpf==cpf)
            if cliente:
                senha = input('Informe sua senha: ')
                cliente = Cliente.create(nome=nome,cpf=cpf)
                conta = Conta.create(senha=hash(senha),saldo=0.0,cliente=cliente)
                conta.numero = conta.id
                conta.save()
                print(f' Conta cadastrada numero = {conta.id} '.center(40,'#'))
                os.system('pause') 
                os.system('cls') 
               

            else:
                print(' Cliente não encontrado '.center(40,'#'))     
                print(' Cadastre-se... '.center(40,'#'))
                nome = input('Informe seu nome: ')
                senha = input('Informe sua senha: ')
                cliente = Cliente.create(nome=nome,cpf=cpf)
                conta = Conta.create(senha=senha,saldo=0.0,cliente=cliente)
                conta.numero = conta.id
                conta.save()
                print(f' Conta cadastrada numero = {conta.id} '.center(40,'#'))
                os.system('pause') 
                os.system('cls') 
            
        elif menu == '2':
            numero = input('Informe o numero da conta: ')
            query = Conta.select().join(Cliente).where(Conta.numero==numero)
            if query:
                os.system('cls') 
                conta = query[0]
                senha = input('Informe a senha: ')
                if conta.senha == senha:
                    os.system('cls') 
                    print(f' Olá {conta.cliente.nome} '.center(40,'#'))   
                    print(f' Seu saldo é  R$ {conta.saldo:.2f} '.center(40,'#'))
                    while True: 
                        print(' Escolha uma das opição abaixo '.center(40,'#'))
                        print('1 - Depositar')
                        print('2 - Extrato')  
                        print('3 - Sacar')
                        print('4 - Saldo')
                        print('v - voltar') 
                        menu2 = input()
                        if menu2=='v':
                            break
                        if menu2 =='1':
                            valor = float(input('Qual valor deseja depositar: '))
                            conta.depositar(valor)
                            conta.save()
                            transacao = Movimentacao.create(conta=conta,valor=valor,tipo='D',data = date.today())
                            print(f' Seu saldo é  R$ {conta.saldo:.2f} '.center(40,'#'))
                            os.system('pause') 
                            os.system('cls') 
                        if menu2=='2':
                            os.system('cls') 
                            print(' Extrato '.center(40,'#'))   
                            transacao = Movimentacao.select().where(Movimentacao.conta==conta)
                            
                            for mov in transacao:
                                print(f'{mov.data} - {mov.tipo} - R$ {mov.valor:.2f}')
                            
                            print('')
                            os.system('pause') 
                            os.system('cls')     
                        if menu2=='3':
                            valor = float(input('Qual valor deseja sacar: (limite de R$ 500 por saque) '))
                            valido,mensagem = conta.sacar(valor)
                            if valido:
                                transacao = Movimentacao.create(conta=conta,valor=valor,tipo='S',data = date.today())
                                print(f' Seu saldo é  R$ {conta.saldo:.2f} '.center(40,'#'))
                                conta.save()
                                os.system('pause') 
                                os.system('cls') 
                            else:
                                print(f' {mensagem} '.center(40,'#'))
                                os.system('pause') 
                                os.system('cls') 
                        if menu2=='4':
                            print(f' Seu saldo é  R$ {conta.saldo:.2f} '.center(40,'#'))
                            os.system('pause') 
                            os.system('cls') 

                else:
                    print(' Senha Inválida '.center(40,'#'))   
                    os.system('pause') 
                    os.system('cls')   

            else:
                print(' Conta não Encontrada '.center(40,'#'))   
                os.system('pause') 
                os.system('cls') 



            




        


