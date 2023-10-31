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
            cabecalho('GERANDO RELATÓRIO ...')
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
        cabecalho(f'{nome_arquivo} já encontrado')
        nome_arquivo = f'{arq}_{i}.txt'
        i+=1
    try:
        cabecalho(f'Criando arquivo {nome_arquivo}')
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
                    continuar = validar_continuar('deseja adicionar mais um material? (s/n) ').lower()
                    if continuar == 'n':
                        return lista_de_material
        if not material_valido:
            cabecalho('Digite um material válido dentro dos tópicos')
            time.sleep(2)

def validar_continuar(msg):
    while True:
        continuar = input(msg)
        if continuar in ['s','n']:
            return continuar
        print('responda entre (s ou n)!')


opcoes_sustentaveis =  {
    'plásticos descartáveis' : {
    'sacolas de plástico': ['sacolas reutilizáveis de pano','sacolas de juta','sacolas reutilizáveis de material reciclado'],
    'garrafas de plástico': ['garrafas de água reutilizáveis','garrafas de vidro', 'garrafas de metal'],
    'canudos de plástico': ['canudos de metal', 'canudos de papel','canudos de bambu'],
    'talheres de plástico': ['talheres de bambu', 'talheres de metal','talheres compostáveis'],
    'copos descartáveis': ['copos reutilizáveis', 'copos de papel', 'copos de vidro']
    },
    'resíduos tóxicos' : {
        'pontas de cigarro': ['cigarros com filtros biodegradáveis', 'vaporizadores', 'uso de cinzeiros portáteis'],
        'pilhas e baterias' : ['baterias recarregáveis',' baterias solares', 'pilhas de sal'],
        'pesticidas e herbicidas' : ['opções orgânicas', 'opções caseiras', 'métodos mecânicos'],
        'tintas e solventes' : ['tintas à base de água','tintas de cal','tintas orgânicas'],
        'medicamentos vencidos': ['programas de recolhimento de medicamentos', 'devolução em farmácias', 'descarte controlado']
    },

    'resíduos eletrônicos': {
        'eletrônicos descartados': ['dispositivos recondicionados', 'doações', ' trocas'],
        'lâmpadas fluorescentes': ['lâmpadas led', 'lâmpadas solares', 'lâmpadas de halogéneo com eficiência energética'],
        'cartuchos de tinta': ['cartuchos recarregáveis','programas de devolução', 'cartuchos de tinta eco-friendly'],
        'cabos e fios': ['cabos feitos de materiais reciclados', ' cabos reutilizáveis', 'organizadores de cabo reutilizáveis'],
        'telefones celulares velhos': ['programas de reciclagem de celular', 'trocas', 'doações']
    },
    'produtos de higiene e saúde': {
        'fraldas descartáveis' : ['fraldas de pano reutilizáveis', 'fraldas biodegradáveis', 'fraldas de bambu'],
        'produtos de higiene pessoal': ['produtos sólidos (ex: xampu em barra)', 'produtos naturais', 'produtos em embalagens recicláveis'],
        'absorventes descartáveis': ['copo menstrual', 'absorventes reutilizáveis', 'calcinhas absorventes'],
        'cotonetes de plástico': ['cotonetes de bambu', 'cotonetes de papel', 'hastes flexíveis reutilizáveis'],
        'desodorantes em spray': ['desodorantes roll-on', 'desodorantes naturais', 'desodorantes em barra']
    },
    'materiais e embalagens': {
        'isopor': ['alternativas à base de amido', 'embalagens de fibra natural', 'embalagens compostáveis'],
        'embalagens de alimentos': ['embalagens de vidro', 'embalagens de papel', 'embalagens reutilizáveis'],
        'filtros de café': ['filtros de pano', 'prensa francesa', 'filtros de metal'],
        'tampas de plástico': ['tampas de metal reutilizáveis', 'tampas de silicone', 'tampas de cortiça'],
        'caixas de pizza sujas': ['caixas compostáveis', 'caixas de papelão reciclável', 'embalagens reutilizáveis']
    }
}

def validar_opcoes_sustentaveis(mat):
    while True:
        material_valido = False
        for key,values in opcoes_sustentaveis.items():
            cabecalho(key)
            for k,v in values.items():
                print(k)
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
                    continuar = validar_continuar('deseja ver mais opções sobre um material? (s/n) ').lower()
                    if continuar == 'n':
                        return linha()
        if not material_valido:
            cabecalho('Digite um material válido dentro dos tópicos')
            time.sleep(1)

def atividades():
    try:
        with open('./lista_de_atividades/atividades.txt', 'r', encoding='utf-8') as arquivo:
            dados = arquivo.read()
            dados = dados.strip().split('\n')
    except IOError as e:
        print(f'ERRO: {e}')
    else:
        return dados
def validar_atividade(atividade,lista_de_ativivades):
    linha()
    for i in lista_de_ativivades:
        print(i)
    linha()
    lista_de_atividades_com_limite = []
    atividade_escolhida = input(atividade).lower()
    while atividade_escolhida not in lista_de_ativivades:
        cabecalho('A ATIVIDADE DEVE ESTAR DENTRE AS OPÇÕES!')
        time.sleep(1)
        linha()
        for i in lista_de_ativivades:
            print(i)
        linha()
        atividade_escolhida = input(atividade).lower()
        linha()
    return atividade_escolhida
#mudar o def validar_atividades para permitir o usuatio adicionar mais de uma atividade
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
