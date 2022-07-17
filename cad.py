#Pedro Henrique de Almeida e Padua   537674
import datetime
from time import sleep
from datetime import date
clientes = {}
dados = []
#Funções Criadas
def CadastrarCliente():
    global clientes
    global dados
    arquivo = open("cad.txt","r")
    check = False
    clientes['Login:'] = str(input('\033[92mDigite um login: \033[0m'))
    for linhas in arquivo.readlines():
        if clientes['Login:'] in linhas:
            print('\033[91mO login inserido já existe! Tente novamente:\033[m')
            check = True

    if not check:
        clientes['Nome:'] = str(input('\033[92mDigite seu Nome Completo: \033[0m'))
        clientes['Senha:'] = str(input('\033[92mDigite uma senha: \033[0m'))
        clientes['Email:'] = str(input('\033[92mDigite seu Email: \033[0m'))
        while not '@' in clientes['Email:']:
            clientes['Email:'] = str(input('\033[1;31mDigite um Email valido:\033[m'))
            if '@' in clientes['Email:']:
                break
    if not check:
        clientes['Data:'] = str(input('\033[92mDigite sua Data de Nascimento(xx/xx/xxxx): \033[0m'))
        clientes['Numero:'] = str(input('\033[92mDigite seu Numero de Telefone: \033[0m'))
        clientes['Endereço:'] = str(input('\033[92mDigite seu Endereço: \033[0m'))
        print(f'\033[94mCadastro Realizado Com Sucesso!')
        sleep(1)
        dados = [clientes]

    if not check:
        arq = open('cad.txt', 'a')
        arq.write(f"{clientes['Login:']} - {clientes['Nome:']} - {clientes['Senha:']} - {clientes['Email:']} - {clientes['Data:']} - {clientes['Numero:']} - {clientes['Endereço:']}\n")
def Mostrardadosdocliente():
    global clientes
    global dados
    c= 40* '-'
    infos= open('cad.txt', 'r')
    texto= infos.readlines()
    sep=[]
    logcliente= input(f'\033[94mDigite o login do cliente que deseja ver: \033[0m' )
    verificacao= False
    for peoples in texto:
        sep= peoples.split('-')
        if logcliente + ' ' in sep:
            verificacao= True
    if verificacao == True:
        print(f"\033[93m************ Dados do cliente {logcliente}  ************\033[0m\n\033[92mNome:\033[0m {c} \033[94m{sep[1]}\033[0m\n\033[92mSenha:\033[0m {c} \033[94m{sep[2]}\033[0m\n\033[92mEmail:\033[0m {c} \033[94m{sep[3]}\033[0m\n\033[92mData:\033[0m {c}  \033[94m{sep[4]}\033[0m\n\033[92mCelular:\033[0m {c}  \033[94m{sep[5]}\033[0m\n\033[92mEndereço:\033[0m {c} \033[94m{sep[6]}\033[0m")
    else:
        print(f"\n\033[91mO login digitado não existe, tente novamente:\033[0m\n\n\n")
    infos.close()
    sleep(4)
def MostrarClientes():
    arq= open('cad.txt', 'r')
    arq1= arq.readlines()
    sep= []
    num=0
    for linha2 in arq1:
        num+= 1
        sep= linha2.split('-')
        print(f'\033[92m{num}-NOME:\033[0m{sep[1]}\n\033[92mLOGIN:\033[0m{sep[0]}\n\033[92mEMAIL:\033[0m{sep[3]}\n\033[92mDATA DE NASCIMENTO:\033[0m{sep[4]}\n\033[92mTELEFONE:\033[0m{sep[5]}\n\033[92mENDEREÇO:\033[0m{sep[6]}\n')
    arq.close()
def gerarrelaorio():
    global dados
    arq= open('relatorio.txt', 'w')
    arq1 = open('cad.txt', 'r')
    arq2 = arq1.readlines()
    sep = []
    num=0
    num2=0
    data = date.today()
    dia= data.day
    ano=data.year
    mes=data.month
    mes2= ''

    if mes == 1:
        mes2= 'Janeiro'
    elif mes == 2:
        mes2= 'Fevereiro'
    elif mes == 3:
        mes2= 'marco'
    elif mes == 4:
        mes2= 'Abril'
    elif mes == 5:
        mes2= 'Maio'
    elif mes == 6:
        mes2= 'Junho'
    elif mes == 7:
        mes2= 'Julho'
    elif mes == 8:
        mes2= 'Agosto'
    elif mes == 9:
        mes2 = 'Setembro'
    elif mes == 10:
        mes2 = 'Outubro'
    elif mes == 11:
        mes2 = 'Novembro'
    elif mes == 12:
        mes2 = 'Dezembro'

    for linha in arq2:
        num+=1
    arq.write(f'''Relatorio de Clientes\n\nA loja Almeida&Almeida possui {num} clientes que estao listados abaixo:''')
    for linha2 in arq2:
        num2+=1
        sep = linha2.split('-')
        arq.write(f'\n{num2}-{sep[1]}\n\n')
    arq.write(f'Russas, Dia {dia} de {mes2} de {ano} ')
    print(f"\033[94mRelatório Gerado Com Sucesso! \033[0m")




#Corpo Principal
while True:
    a='*'
    b= ' '
    print(f"\033[93m{a * 20} Almeida&Almeida {a * 20}\033[0m")
    print("\033[92m<1> Cadastrar Cliente\033[0m")
    print("\033[92m<2> Mostar dados do cliente\033[0m")                            #Printa o menu
    print("\033[92m<3> Mostrar clientes cadastrados\033[0m")
    print("\033[92m<4> Gerar relatório de clientes\033[0m")
    print("\033[92m<0> Sair\033[0m")
    print(f"\033[93m{a * 20} Almeida&Almeida {a * 20}\033[0m")
    menu= int(input("\033[92mEscolha uma das opções a cima\033[0m\033[91m(Somente numeros)\033[0m: "))

    if menu==1:
        CadastrarCliente()
    if menu==2:
        Mostrardadosdocliente()
    if menu==3:
        MostrarClientes()
    if menu==4:
        gerarrelaorio()
    if menu==0:
        break
    if 0<=menu>=5:
        print(f'\n\n\n\n\n\033[91m*****Opção {menu} não é valida. Tente Novamente*****\n\n\n\n\n\033[0m')
        continue
