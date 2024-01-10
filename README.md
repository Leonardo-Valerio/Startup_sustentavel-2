# Assistente de Vida Sustentável

## Visão Geral

O Assistente de Vida Sustentável é um programa baseado em Python projetado para auxiliar os usuários na adoção de práticas sustentáveis em suas vidas diárias. Ele engloba diversas funcionalidades, como orientação para descarte de resíduos, recomendações de produtos sustentáveis, dicas para atividades ecologicamente corretas e um quiz de sustentabilidade com possíveis recompensas.

## Funcionalidades

### Guia de Descarte de Resíduos

- Os usuários podem selecionar materiais para obter orientações sobre o descarte adequado.
- O programa gera um relatório personalizado usando o modelo GPT-3.5 da OpenAI, explicando como descartar corretamente os materiais escolhidos.

### Recomendador de Produtos Sustentáveis

- Os usuários escolhem um material, e o sistema sugere alternativas sustentáveis para incentivar escolhas eco-amigáveis.

### Guia de Atividades Sustentáveis

- Os usuários selecionam até três atividades de interesse.
- O sistema gera um relatório sobre como tornar essas atividades mais sustentáveis e ecologicamente corretas, utilizando conteúdo gerado por IA.

### Eco Quiz

- Um quiz sobre sustentabilidade com a chance de ganhar uma recompensa.
- Os usuários têm um máximo de três tentativas para atingir uma pontuação de 7 ou mais e ganhar uma recompensa.

## Como Executar

### Requisitos

- Python 3.x
- Pacotes Python necessários: json, requests, os, time, tiktoken, openai (instale com `pip install -r requirements.txt`)

### Executando o Programa

- Execute `main.py` no seu ambiente Python.

## Instruções para o Usuário

1. **Login/Cadastro**
   - Os usuários podem se cadastrar ou fazer login para acessar as funcionalidades.
   - O sistema mantém as informações do usuário em um arquivo JSON (`cadastros.json`).

2. **Navegue pelo Menu**
   - Escolha opções no menu principal (Guia de Descarte de Resíduos, Recomendador de Produtos Sustentáveis, Guia de Atividades Sustentáveis, Eco Quiz, Sair).

3. **Siga as Instruções**
   - O sistema fornece instruções claras para cada funcionalidade.
   - Os usuários são orientados na seleção de materiais, escolha de atividades e participação no quiz.

## Observações

- O programa incorpora o modelo GPT-3.5 da OpenAI para gerar conteúdo impulsionado por IA.
- Os dados do usuário, incluindo recompensas e quizzes concluídos, são armazenados no arquivo `cadastros.json`.


