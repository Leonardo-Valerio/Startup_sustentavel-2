import os
import openai
import dotenv
import time
import tiktoken
from funcoes_de_cadastro import *
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
            tentaivas+=1
            response = openai.ChatCompletion.create(
                model= modelo,
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

def criar_arquivo_guia_descarte(nome,conteudo):
    i = 1
    arq = f'./arquivos_guia_descarte/guia_de_descarte_{nome}'
    nome_arquivo = arq + '.txt'
    while os.path.exists(nome_arquivo):

        nome_arquivo = f'{arq}_{i}.txt'
        i+=1
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f'Houve um erro: {e}')

materiais = {
    'plásticos descartáveis' : ['sacolas de plástico','garrafas de plástico','canudos de plástico', 'talheres de plástico','copos descartáveis'],
    'resíduos tóxicos' : ['pontas de cigarro','pilhas e baterias','pesticidas e herbicidas','tintas e solventes','medicamentos vencidos'],
    'resíduos eletrônicos': ['eletrônicos descartados','lâmpadas fluorescentes','cartuchos de tinta','cabos e fios','telefones celulares velhos'],
    'produtos de higiene e saúde': ['fraldas descartáveis', 'produtos de higiene pessoal', 'absorventes descartáveis', 'cotonetes de plástico', 'desodorantes em spray'],
    'materiais e embalagens': ['isopor','embalagens de alimentos','filtros de café','tampas de plástico','caixas de pizza sujas']
}

def validar_material_para_descarte(mat):
    lista_de_material = []
    material_valido = False

    while True:
        material_valido = False
        for key,value in materiais.items():
            cabecalho(key)
            for j in value:
                print(j)
        linha()
        material = input(mat)
        for key,value in materiais.items():
            for j in value:
                if material == j:
                    if material not in lista_de_material:
                        lista_de_material.append(material)
                    else:
                        cabecalho('material já adicionado')
                        break
                    material_valido = True
                    continuar = validar_continuar('deseja adicionar mais um material? (s/n) ')
                    if continuar == 'n':
                        return lista_de_material
        if not material_valido:
            cabecalho('Digite um material válido dentro dos tópicos')
            time.sleep(5)







def validar_continuar(msg):
    while True:
        continuar = input(msg)
        if continuar in ['s','n']:
            return continuar
        print('responda entre (s ou n)!')

