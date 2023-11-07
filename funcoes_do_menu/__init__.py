

import openai
import dotenv
import time
import tiktoken
from funcoes_de_cadastro import *

def validar_continuar(msg):
    while True:
        continuar = input(msg)
        if continuar in ['s','n']:
            return continuar
        print('responda entre (s ou n)!')

#opção1
def validar_material_para_descarte(mat):
    try:
        with open('./arquivos_json/materiais_descarte.json', 'r', encoding='utf-8') as arquivo:
            materiais = json.load(arquivo)
    except IOError as e:
        print(f'Houve um erro: {e}')
    else:

        lista_de_material = []
        while True:
            material_valido = False
            for key, value in materiais.items():
                cabecalho(key)
                time.sleep(0.8)
                for j in value:
                    print(j)
                    time.sleep(0.3)
            linha()
            material = input(mat)
            for key, value in materiais.items():
                for j in value:
                    if material == j:
                        if material not in lista_de_material:
                            lista_de_material.append(material)
                        else:
                            cabecalho('material já adicionado')
                            break
                        material_valido = True
                        continuar = validar_continuar('deseja adicionar mais um material? (s/n) ').lower()
                        if continuar == 'n':
                            return lista_de_material
            if not material_valido:
                cabecalho('Digite um material válido dentro dos tópicos')
                time.sleep(2)


def guia_descarte(prompt_user):
    dotenv.load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_sistema = """
        você é um assistente de sustentabilidade
        eu irei te passar alguns materiais que vão para o lixo, e você me fará um tutorial
        de como eu posso descartar corretamente esses materiais para evitar problemas para a natureza
        ###
        formato de saída:
        para cada material, uma descrição breve  sobre como descartar cada um desses materiais de maneira correta
    """
    tentativas = 0
    tempo_exponencial = 5
    modelo = "gpt-3.5-turbo"
    codificador = tiktoken.encoding_for_model(modelo)
    lista_de_tokens = codificador.encode(prompt_sistema + prompt_user)
    tokens = len(lista_de_tokens)
    tamanho_esperado_saida = 2048
    if tokens > (4096 - tamanho_esperado_saida):
        modelo = "gpt-3.5-turbo-16k"
    while tentativas < 5:
        try:
            cabecalho('GERANDO RELATÓRIO ...')
            tentativas+=1
            response = openai.ChatCompletion.create(
                model=modelo,
                messages=[
                    {
                        "role": "system",
                        "content": prompt_sistema
                    },
                    {
                        "role": "user",
                        "content": prompt_user
                    }
                ],
                temperature=1,
                max_tokens=tamanho_esperado_saida,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            resposta = response.choices[0].message.content
            return resposta
        except openai.error.AuthenticationError as e:
            print(f'ERRO DE AUTENTICAÇÃO: {e}')
        except openai.error.APIError as e:
            print(f'ERRO DE API: {e}')
            time.sleep(5)
        except openai.error.RateLimitError as e:
            print(f'ERRO LIMITE DE TAXA: {e}')
            time.sleep(tempo_exponencial)
            tempo_exponencial *= 2

def criar_arquivo(nome,conteudo,caminho):
    i = 1
    arq = caminho + nome
    nome_arquivo = arq + '.txt'
    while os.path.exists(nome_arquivo):
        cabecalho(f'{nome_arquivo} já encontrado')
        nome_arquivo = f'{arq}_{i}.txt'
        i+=1
    try:
        cabecalho(f'Criando arquivo {nome_arquivo}')
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f'Houve um erro: {e}')

#opção2
def validar_opcoes_sustentaveis(mat):
    try:
        with open('./arquivos_json/opcoes_sustentaveis.json', 'r', encoding='utf-8') as arquivo:
            opcoes_sustentaveis = json.load(arquivo)
    except IOError as e:
        print(f'Houve um erro: {e}')
    else:
        while True:
            material_valido = False
            for key,values in opcoes_sustentaveis.items():
                cabecalho(key)
                time.sleep(0.8)
                for k in values.keys():
                    print(k)
                    time.sleep(0.3)
            linha()
            material = input(mat).lower()
            for key,values in opcoes_sustentaveis.items():
                for k,v in values.items():
                    if material == k:
                        material_valido = True
                        cabecalho(f'OPÇÕES SUSTENTÁVEIS PARA SUBSTITUIR {material.upper()}')
                        for i in range(len(v)):
                            print(f'Opção {i+1} : {v[i]}')
                        linha()
                        continuar = validar_continuar('deseja ver mais opções sobre alguma opção? (s/n) ').lower()
                        if continuar == 'n':
                            return linha()
            if not material_valido:
                cabecalho('Digite um material válido dentro dos tópicos')
                time.sleep(1)

#opção3
def validar_atividade(atividade):
    try:
        with open('./lista_de_atividades/atividades.txt', 'r', encoding='utf-8') as arquivo:
            lista_de_ativivades = arquivo.read()
            lista_de_ativivades = lista_de_ativivades.strip().split('\n')
    except IOError as e:
        print(f'ERRO: {e}')
    else:
        lista_de_atividades_com_limite = []
        while True:
            atividade_encontrada = False
            linha()
            for i in lista_de_ativivades:
                time.sleep(0.2)
                print(i)
            linha()
            atividade_escolhida = input(atividade).lower()
            for i in lista_de_ativivades:
                if i == atividade_escolhida:
                    atividade_encontrada = True
                    if len(lista_de_atividades_com_limite) <3:
                        if i not in lista_de_atividades_com_limite:
                            lista_de_atividades_com_limite.append(atividade_escolhida)
                            continuar = validar_continuar('deseja ver mais opções sobre um material? (s/n) ').lower()
                            if continuar == 'n':
                                return lista_de_atividades_com_limite
                        else:
                            cabecalho('Atividade já adicionada!')
                            time.sleep(1)
                    else:
                        cabecalho('Limite de atividades para um arquivo atingido')
                        return lista_de_atividades_com_limite
            if not atividade_encontrada:
                cabecalho('A ATIVIDADE DEVE ESTAR DENTRE AS OPÇÕES LISTADAS!')
                time.sleep(1)

def guia_de_atividades(prompt_user):
    dotenv.load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_sistema = """
            você é um assistente de sustentabilidade
            eu irei te passar algumas atividades e você me dará dicas de como tornar
            essas atividades mais sustentáveis e ecologicas, me passando boas práticas
            para evitar que essa atividade de alguma forma possa prejudicar a natureza
            ###
            formato de saída:
            para cada atividade, uma breve descrição sobre como tornar essa atividade mais sustentável 
        """
    tentaivas = 0
    tempo_exponencial = 5
    modelo = "gpt-3.5-turbo"
    codificador = tiktoken.encoding_for_model(modelo)
    lista_de_tokens = codificador.encode(prompt_sistema + prompt_user)
    tokens = len(lista_de_tokens)
    tamanho_esperado_saida = 2048
    if tokens > (4096 - tamanho_esperado_saida):
        modelo = "gpt-3.5-turbo-16k"
    while tentaivas < 3:
        try:
            cabecalho('GERANDO RELATÓRIO ...')
            tentaivas += 1
            response = openai.ChatCompletion.create(
                model=modelo,
                messages=[
                    {
                        "role": "system",
                        "content": prompt_sistema
                    },
                    {
                        "role": "user",
                        "content": prompt_user
                    }
                ],
                temperature=1,
                max_tokens=tamanho_esperado_saida,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            resposta = response.choices[0].message.content
            return resposta
        except openai.error.AuthenticationError as e:
            print(f'ERRO DE AUTENTICAÇÃO: {e}')
        except openai.error.APIError as e:
            print(f'ERRO DE API: {e}')
            time.sleep(5)
        except openai.error.RateLimitError as e:
            print(f'ERRO LIMITE DE TAXA: {e}')
            time.sleep(tempo_exponencial)
            tempo_exponencial *= 2


#opção4

def validar_alternativa(letra):
    while True:
        resposta = input(letra).lower()
        if resposta in ['a','b','c','d']:
            return resposta
        cabecalho('Digite uma alternativa válida!')

def quiz():
    try:
        with open('./arquivos_json/quiz.json', 'r', encoding='utf-8') as arquivo:
            quiz_json = json.load(arquivo)
    except IOError as e:
        print(f'Houve um erro: {e}')
    else:
        acertos = 0
        for key,values in quiz_json.items():
            cabecalho(key)
            print(values["pergunta"])
            linha()
            for opcoes in values['opções']:
                print(opcoes)
            linha()
            resposta_usuario = validar_alternativa('digite a alternativa correta: ')
            if resposta_usuario == values['resposta_correta']:
                cabecalho('CERTA RESPOSTA')
                acertos+=1
            else:
                cabecalho('ERRADA RESPOSTA')

        cabecalho(f'SUA NOTA FOI: {acertos}')
        return acertos



def validar_tentativas(nome):
    liberar_usuario = False
    try:
        with open('./arquivo_cadastros/cadastros.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except IOError as e:
        print(f'ERRO: {e}')
    else:
        for usuario in dados:
            if usuario["nome"] == nome:
                if usuario["tentativas"] > 0:
                    usuario["tentativas"] -= 1
                    liberar_usuario = True
                    with open('./arquivo_cadastros/cadastros.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(dados, arquivo, indent=4)
                    return liberar_usuario
        if not liberar_usuario:
            cabecalho(f"POXA, SUAS TENTATIVAS ESTÃO ESGOTADAS :-(")
            return liberar_usuario


def realizar_recompensa(nome):
    try:
        with open('./arquivo_cadastros/cadastros.json', 'r',encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except IOError as e:
        print(f'ERRO: {e}')
    else:
        for usuario in dados:
            if usuario["nome"] == nome:
                if usuario["recompensa"] < 1:
                    usuario["recompensa"]+=1
                print('confirme o seu endereço abaixo para te enviarmos ;-)')
                linha()
                print(f'CEP: {usuario["cep"]}')
                linha()
                print(f'Rua: {usuario["rua"]}')
                linha()
                print(f'Número da residência: {usuario["numero"]}')
                linha()
                continuar = validar_continuar('o endereço está correto? (s/n) ').lower()
                if continuar == 'n':
                    numero_casa = validar_int('Digite o número da sua casa: ')
                    linha()
                    novo_cep = encontrar_cep('digite o seu CEP (apenas números nesse campo): ', numero_casa)
                    usuario["cep"] = novo_cep["cep"]
                    usuario["rua"] = novo_cep["logradouro"]
                    usuario["numero"] = novo_cep["numero"]
                    try:
                        with open('./arquivo_cadastros/cadastros.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(dados, arquivo, indent=4)
                    except IOError as e:
                        print(f'ERRO: {e}')
                    else:
                        cabecalho("ENDEREÇO ALTERADO COM SUCESSO")
                        realizar_recompensa(nome)
                else:
                    time.sleep(1)
                    cabecalho('SEU LIVRO SERÁ ENVIADO GRATUITAMENTE NOS PRÓXIMOS DIAS')
                    return

def validar_se_ja_ganhou(nome):
    try:
        with open('./arquivo_cadastros/cadastros.json', 'r',encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except IOError as e:
        print(f'ERRO: {e}')
    else:
        for usuario in dados:
            if usuario["nome"] == nome:
                if usuario["recompensa"] > 0:
                    return False
        return True



