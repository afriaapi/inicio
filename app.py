from iqoptionapi.stable_api import IQ_Option
import time


email = "josemussa00@gmail.com"
senha ='Cadeira33'
api = IQ_Option(email, senha)

verificar,razao = api.connect()

if verificar:
    print("Conectado com sucesso")

else:
    if razao =='{"code":"invalid_credentials","message":"You entered the wrong credentials. Please ensure that your login/password is correct."}':
        print('Erro de conexão')

    else:
        print('erro desconhecido')

while True:
    escolha = input("Selecione a escolha que vice que conectar: demo ou relar ")

    if escolha =="demo":
        conta = 'PRACTICE'
        print("treinamento escolhido ")
        break

    if escolha==  "real":
        conta =  'REAL'
        print("Conta Real Escolhida!")
        break
    else:
        print('escolha invalida ')

api.change_balance(conta)


def compra (activo, valor, direccao, exp, tipo):
    if tipo=='digital':
        verificar, id = api.buy_digital_spot(activo, valor, direccao, exp)

    else:
        verificar, id = api.buy(activo,valor,exp)

    if verificar:
        print ('Compra realizada com sucesso', id)
        
        while True:
            time.sleep(1)
            status, resultado = api.check_win_digital_v2(id) if tipo =="digital " else api.check_win_v3(id)

            if status:
                if resultado > 0:
                    print("win", round(resultado,2))

                elif resultado == 0:
                    print("empate", round(resultado))

                else:
                    print("LOSS") 
                break

    else:
        print ("Erro na compra")

activo ="EURUSD"
valor= 10
direccao="call"
exp= 1
tipo="digital"


compra(activo, valor,direccao,exp, tipo)