from funcoes_do_menu import *



menu_cadastro = ['CADASTRAR','LOGIN','ENTRAR SEM LOGIN']

cabecalho('BEM VINDO!')


while True:
    linha()
    exibir_menu(menu_cadastro)
    linha()
    opcao = validar_int('Digite a opção que deseja: ')
    if opcao == 1:
        cabecalho(menu_cadastro[0])
        novo_nome = validar_nome('digite seu nome: ').lower()
        nova_senha = validar_senha('crie sua senha: ').lower()
        numero_casa = validar_int('digite o número da sua residência: ')
        cep = encontrar_cep('digite o seu CEP (apenas números nesse campo): ', numero_casa)
        cadastrar(novo_nome,nova_senha,cep)
    elif opcao == 2:
        cabecalho(menu_cadastro[1])
        acesso = login('digite seu nome: ','digite sua senha: ')
        if acesso != []:
            cabecalho('Login realizado com sucesso!')
            break
    elif opcao == 3:
        cabecalho(menu_cadastro[2])
        acesso = []
        break
    else:
        print('Digite um número dentre as opções acima!')

menu = ['GUIA DE DESCARTE DE LIXO','RECOMENDADOR DE PRODUTOS','GUIA DE ATIVIDADES SUSTENTÁVEIS', 'ECO QUIZ', 'SAIR']

if acesso != []:
    cabecalho(f'SEJA BEM VINDO {acesso[0].upper()}!')
else:
    cabecalho('SEJA BEM VINDO')
while True:
    exibir_menu(menu)
    linha()
    opcao = validar_int('Digite a opção que deseja: ')
    if opcao == 1:
        if acesso != []:
            cabecalho(menu[0])
            materiais = validar_material_para_descarte('digite o material que deseja receber um tutorial do nosso guia: ')
            print(materiais)
            items_str = ', '.join(materiais)
            conteudo = guia_descarte(items_str)
            criar_arquivo_guia_descarte(acesso[0], conteudo)

        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNÇIONALIDADE')

    elif opcao == 2:
        cabecalho(menu[1])
        materiais = validar_opcoes_sustentaveis('digite o material que deseja saber seus possiveis substitutos sustentáveis: ')
    elif opcao == 3:
        cabecalho(menu[2])
        tipos_de_atividades = validar_atividade('Digite a atividade que deseja saber mais: ',atividades())
    elif opcao == 4:
        cabecalho(menu[3])
    elif opcao == 5:
        cabecalho('SAIR')
        break
