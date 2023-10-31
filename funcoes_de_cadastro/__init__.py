import requests

def linha():
    print('-' * 100)

def cabecalho(msg):
    linha()
    print(msg.center(100))
    linha()

def exibir_menu(lista):
    for i in range(len(lista)):
        print(f'{i+1} - {lista[i]}')

def validar_int(n):
    while True:
        try:
            num = int(input(n))
        except:
            print('Digite um número válido!!!')
        else:
            return num
def cadastrar(nome, senha, cep):
    try:
        with open('./arquivo_cadastros/cadastros.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{senha};{cep["cep"]};{cep["logradouro"]};{cep["numero"]}\n')
        cabecalho("Cadastro realizado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao realizar o cadastro: {e}")
def validar_nome(nome):
    try:
        with open('./arquivo_cadastros/cadastros.txt', 'r') as arquivo:
            dados = arquivo.readlines()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    else:
        while True:
            liberar_usuario = True
            name = input(nome)
            if name.isalpha() and len(name) >= 3:
                for i in dados:
                    nome_existente = i.strip().split(';')[0]
                    if name == nome_existente:
                        print('ERRO, usuário já existente, digite outro')
                        liberar_usuario = False
                        break
                if liberar_usuario:
                    return name
            else:
                print('digite um nome válido, com pelo menos 5 dígitos, utilize apenas letras no nome! ')

def validar_senha(password):
    while True:
        try:
            senha = input(password)
            if senha.isalnum() and len(senha) >5:
                return senha
            else:
                print('digite uma senha válida, com mais de 5 dígitos!')
        except IOError as e:
            print(f'ERRO: {e}')

def encontrar_cep(num_cep, num_casa):
    while True:
        cep = validar_int(num_cep)
        try:
            respose = requests.get(f"https://viacep.com.br/ws/{str(cep)}/json/")
            if respose.status_code == 200:
                endereco = respose.json()
                endereco['numero'] = num_casa
                return endereco
            else:
                print('CEP inválido')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


def login(name,password):
    try:
        with open('./arquivo_cadastros/cadastros.txt', 'r') as arquivo:
            dados = arquivo.readlines()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    else:
        nome = input(name).lower()
        senha = input(password).lower()
        for i in dados:
            linha = i.strip().split(';')
            if linha[0] == nome and linha[1] == senha:
                return [nome,senha]
        print('Nome ou senha incorretos!')
        return []
