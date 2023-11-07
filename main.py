

from funcoes_do_menu import *

menu_cadastro = ['CADASTRAR','LOGIN','ENTRAR SEM LOGIN']

cabecalho('BEM VINDO!')

acesso = cadastro(menu_cadastro)

menu = ['GUIA DE DESCARTE DE LIXO','RECOMENDADOR DE PRODUTOS','GUIA DE ATIVIDADES SUSTENTÁVEIS', 'ECO QUIZ', 'SAIR']

if acesso != []:
    cabecalho(f'SEJA BEM VINDO {acesso["nome"].upper()}!')
else:
    cabecalho('SEJA BEM VINDO')
while True:
    exibir_menu(menu)
    linha()
    opcao = validar_int('Digite a opção que deseja: ')
    if opcao == 1:
        if acesso != []:
            cabecalho(menu[0])
            print('Nessa função será exibida uma lista de materiais que você vai poder escolher alguns deles para\n'
            'gerarmos para você um relatório exclusivo feito por IA explicando como descartar esse material\n'
            'de maneira correta')
            linha()
            time.sleep(3)
            materiais = validar_material_para_descarte('digite o material que deseja receber um tutorial do nosso guia: ')
            print(materiais)
            items_str = ', '.join(materiais)
            conteudo = guia_descarte(items_str)
            criar_arquivo(acesso["nome"], conteudo,f'./arquivos_guia_descarte/guia_de_descarte_')

        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNÇIONALIDADE')
            acesso = cadastro(menu_cadastro)

    elif opcao == 2:
        cabecalho(menu[1])
        print("Nessa função será exibida uma lista de materiais, que você poderá escolher um deles, que te\n"
        "passaremos uma lista de opções sustentáveis que podem substituir esse material escolhido")
        linha()
        time.sleep(3)
        materiais = validar_opcoes_sustentaveis('digite o material que deseja saber seus possiveis substitutos sustentáveis: ')
    elif opcao == 3:
        if acesso != []:
            cabecalho(menu[2])
            print('Nessa função será exibida uma lista de atividades que você poderá escolher até 3 delas\n'
            'do seu interesse para te gerarmos um relatório exclusivo para você feito por IA, de como tornar\n'
            'essas atividades mais sustentáveis e ecológicas')
            linha()
            tipos_de_atividades = validar_atividade('Digite a atividade que deseja saber mais: ')
            print(tipos_de_atividades)
            atividades_str = ', '.join(tipos_de_atividades)
            conteudo = guia_de_atividades(atividades_str)
            criar_arquivo(acesso["nome"],conteudo,f'./arquivos_guia_atividades/guia_de_atividades_')
        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNÇIONALIDADE')
            acesso = cadastro(menu_cadastro)

    elif opcao == 4:
        if acesso != []:
            cabecalho(menu[3])
            print("Nessa função será exibido um quiz de sustentabilidade, onde você tem até 3 chances no máximo para\n"
            "ganhar uma recompensa, o quiz são de 10 perguntas e você precisará tirar uma nota MAIOR do que 7 para\n"
            "conseguir o prêmio.")
            time.sleep(3)
            linha()
            permissao = validar_tentativas(acesso["nome"])
            if permissao:
                nota = quiz()
                ganhou = validar_se_ja_ganhou(acesso["nome"])
                if ganhou:
                    if nota >= 7:
                        cabecalho('PARABÉNS VOCÊ GANHOU O NOSSO LIVRO "Sementes do Amanhã: Educando para Reciclar e Conservar"')
                        time.sleep(1)
                        recompensa = realizar_recompensa(acesso["nome"])
                    else:
                        cabecalho('SUA NOTA FOI MENOR DO QUE 7, TENTE FAZER O QUIZ NOVAMENTE PARA CONSEGUIR SUA RECOMPENSA')
                else:
                    cabecalho('VOCÊ JÁ GANHOU SUA RECOMPENSA, ELA JÁ ESTÁ A CAMINHO ;-)')
        else:
            cabecalho('FAÇA SEU LOGIN PARA ACESSAR ESSA FUNCIONALIDADE')
            acesso = cadastro(menu_cadastro)
    elif opcao == 5:
        cabecalho('SAIR')
        break

