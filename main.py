from funcoes_do_menu import *

menu_cadastro = ['CADASTRAR','LOGIN','ENTRAR SEM LOGIN']

cabecalho('BEM VINDO!')

acesso = cadastro(menu_cadastro)

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
            criar_arquivo(acesso[0], conteudo,f'./arquivos_guia_descarte/guia_de_descarte_')

        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNÇIONALIDADE')
            acesso = cadastro(menu_cadastro)

    elif opcao == 2:
        cabecalho(menu[1])
        materiais = validar_opcoes_sustentaveis('digite o material que deseja saber seus possiveis substitutos sustentáveis: ')
    elif opcao == 3:
        if acesso != []:
            cabecalho(menu[2])
            tipos_de_atividades = validar_atividade('Digite a atividade que deseja saber mais: ')
            print(tipos_de_atividades)
            atividades_str = ', '.join(tipos_de_atividades)
            conteudo = guia_de_atividades(atividades_str)
            criar_arquivo(acesso[0],conteudo,f'./arquivos_guia_atividades/guia_de_atividades_')
        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNÇIONALIDADE')
            acesso = cadastro(menu_cadastro)

    elif opcao == 4:
        cabecalho(menu[3])
        quiz()
    elif opcao == 5:
        cabecalho('SAIR')
        break

