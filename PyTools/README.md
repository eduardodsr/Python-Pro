# Python Pro

[![](https://img.shields.io/badge/made_by-eduardodsr-green)](https://github.com/eduardodsr/)
![Visitor](https://visitor-badge.glitch.me/badge?page_id=eduardodsr.Python)

## PyTools

### Objetivo
Apresentar um conjunto de ferramentas básico, mas poderoso, que Pythonistas experientes usam no dia-a-dia.

### Público
Alunos iniciantes de Python que desejam conhecer as ferramentas de seu ecossistema.

### Descrição
Nesse módulo será abordada a leitura e escrita de arquivos, com definição de unicode e encode. 
Instalação e criação de bibliotecas utilizando pip, virtualenv e pypi. Criação de testes automáticos com o framework pytest.


### Conteúdo:

### 1. Criação de Projetos
Nessa seção você vai conferir várias boas práticas para criação de um projeto de código aberto em Python. Primeiros passos, versionamento, criação de virtualenvs, instação de libs de terceiros e publicação no PyPi. Assim você vai ter conhecimento sobre todo o ferramental que os projetos existentes utilizam e também vai aprender como reutilizar e compartilhar código criando sua própria biblioteca

### 1.1. Afiando o Machado - Git
"Para cortar lenha na metade do tempo, gaste o dobro de tempo afiando seu machado". Esse ditado ensina que é preciso ter suas ferramentas sempre prontas e no ponto ideal de facilitar o seu trabalho. Portanto nesse capítulo você vai aprender como criar o seu projeto e fazer o setup de seu ambiente para fazer com que ele o auxilie em suas tarefas. Esse é o mote principal de todo esse módulo e começaremos investigando o git e como contribuir com open source

1.1.1. Motivação

1.1.2. Criação de Repositório

1.1.3. Chaves SSH

1.1.4. Fork

1.1.5. Pull Request

1.1.6. Pull Request Não Aceito

1.1.7. Feature Branch

1.1.8. Resolução de Conflito no Git

1.1.9. Arquivo Gitignore

### 1.2. Isolando o Ambiente
Nesse capítulo você vai aprender a isolar seu ambiente para poder conviver com diversas versões de Python e diversas versões de bibliotecas. Você também vai automatizar ainda mais seu ambiente para aumentar a qualidade de seu código.

1.2.1. Pyenv no Ubuntu

1.2.2. Pyenv no Mac

1.2.3. Python 2 e 3 no Windows

1.2.4. Virtualenv

1.2.5. Virtualenv no Windows

1.2.6. Virtualenv no Linux e OSX

1.2.7. Virtualenv no Pycharm

### 1.3. Gestão de Dependências
Nesse capítulo você vai aprender o que são Dependências. Confira como instalar bibliotecas de terceiros para reutilizar código, como instalar e gerir dependências para outros projetos e como publicar se código no PyPi

1.3.1. Instalação de Libs com PIP

1.3.2. Requirements

1.3.3. Flake8

1.3.4. Integração Contínua com Travis CI

1.3.5. Upgrade de Dependências

### 1.4. Publicação de Pacote
Nesse capítulo você vai aprender como criar a infra estrutura necessária para disponibilizar um projeto seu como um pacote instalável no PyPi

1.4.1. Arquivo Setup.py

1.4.2. Instalação Local de Pacote

1.4.3. Criação de Release

1.4.4. Publicação no PyPi

1.4.5. Upgrade de Lib no PyPi

1.4.6. Conclusão - Construção de Projetos

### 2. Testes Automáticos
Nessa seção você vai aprofundar nos conceitos e ferramentas para automatização de testes. Essa tarefa é muito importante para aumentar a qualidade de seu projeto, dando confiança na hora de adicionar novas funcionalidades e prevenindo que muitos bugs sequer cheguem em seu ambiente de produção.

Você vai conferir o framework pytest, mock, cobertura de testes e muito mais. Divirta-se!

### 2.1. Framework Pytest

Nesse capítulo você vai aprender como escrever testes automatizados utilizando o framework Pytest. Apesar de já terem sido apresentados os framewords doctest e unitest no módulo Python Birds, aprender o Pytest é fundamental porque ele vem sendo utilizados por diversas empresas e projetos por proporcionar a escrita de testes mais simples.

2.2.1. Pytest: Instalação

2.2.2. Criação e Execução de Testes

2.2.3.  Cobertura de Testes

2.2.4. TDD e Baby Steps

2.2.5. Parametrização de Testes

2.2.6. Teste de Exceções

### 2.2. Pytest Fixtures

Nessa capítulo você vai conhecer umas das funcionalidades mais interessantes do framework Pytest: as fixtures. Com elas você vai conseguir escrever código mais legível e controlar de forma granular o ciclo de vida de objetos para manter a sua suite de testes legível e performática.

2.2.1. Emulando Teste com Banco de Dados

2.2.2. Implementação de Conexão, Sessão e Usuário

2.2.3. Isolamento de Testes

2.2.4. Setup e Tear Down com Fixture

2.2.5. Escopos de Fixture

2.2.6. Arquivo Conftest

### 2.3. Injeção de Dependências

Nesse capitulo você vai aprender como utilizar o conceito de injeção de dependências para conseguir tornar o seu código testável, conhecendo biblitecas que vão facilitar a escrita e isolamento de testes, como a lib mock.

2.3.1. Produção de Código Testável

2.3.2. Injeção de Dependências

2.3.3. Mock

2.3.4. Módulo como Objeto

2.3.5. Isolamento de Imports

2.3.6. Biblioteca Pytest-Mock

2.3.7. Conclusão Testes Automáticos

### 3. Pipenv
Nessa sessão você vai conhecer a evolução na gestão de dependências em Python, a biblioteca Pipenv. Ela foi criada pelo autor da biblioteca requests, Kenneth Reitz.

Seu objetivo é facilitar a vida dos desenvolvedores e aumentar a segurança durante a instalação de pacotes.

### 3.1. Instalação e Princípios Básicos

Nesse capítulo você vai instalar biblioteca pipenv e aprender como gerenciar seus projetos com ela.

3.1.1. Pipenv - Motivação

3.1.2. Instalação e Configuração do Pipenv

3.1.3. Instalação e Remoção de Dependências

3.1.4. Execução de Comandos no Virtualenv

### 3.2. Atualizando Projeto Legado

Nesse capítulo você vai atualizar o projeto legado utilizando pip + virtualenv para passar a utilizar o pipenv.

3.2.1. Criando Arquivos do Pipenv

3.2.2. Pipenv e Travis

3.2.3. Pipenv e Pyup

3.2.4. Atualizando Dependências com Pipenv
