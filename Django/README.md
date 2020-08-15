# Python Pro

# Django

### Objetivo
•	Construção de web site

### Público
•	Alunos com conhecimento intermediário de Python interessados em aprender sobre desenvolvimento web.

### Descrição
•	Nesse módulo será construído uma aplicação web real utilizando o Web Django, o mais famoso framework web de Python. Ele serve como prática, onde todos os conceitos vistos nos demais módulos serão colocados à prova.
Além dos conceitos, será exemplificado um processo de entrega contínua com deploys regulares no Heroku.

1.	Twelve Factor App

- 1.1.	Entrega Contínua
- 1.1.1.	Motivação Django
- 1.1.2.	Pipenv
- 1.1.3.	Integrando Pipenv Travis e Pyup
- 1.1.4.	Setup de Projeto e Arquivo Manage
- 1.1.5.	Publicação no Heroku
- 1.1.6.	Deploy Automático
- 1.1.7.	Rodando Servidor no Pycharm
- 1.1.8.	Olá Django
- 1.1.9.	Pytest Django
- 1.1.10.	Cobertura de Testes

- 1.2.	Configurações de Projeto
- 1.2.1.	Lib Python Decouple
- 1.2.2.	Secret Key
- 1.2.3.	Domínio e ALLOWED_HOSTS
- 1.2.4.	Endereço de Banco de Dados
- 1.2.5.	Testando Postgresql no Travis
- 1.2.6.	Lingua e Fuso Horário

- 1.3.	Arquivos Estáticos e Upload de Arquivos
- 1.3.1.	Comando de Coleta de Arquivos Estáticos
- 1.3.2.	Criação de Usuário na Amazon
- 1.3.3.	Criação e Configuração do S3
- 1.3.4.	Configurando a Lib django_s3_folder_storage
- 1.3.5.	Otimizando Uploads com Collectfast

- 1.4.	Migrações e Customização de Usuário
- 1.4.1.	Sobrescrevendo a Classe User
- 1.4.2.	Customizando a Classe UserManager
- 1.4.3.	Comando Makemigrations e Alias mng
- 1.4.4.	Conexão com Banco e Migrações
- 1.4.5.	Admin do Usuário
- 1.4.6.	Aplicando Migrações no Heroku

- 1.5.	Backup, Debug, Sentry e Conclusão
- 1.5.1.	Backup do Postgresql
- 1.5.2.	Django Debug Toolbar
- 1.5.3.	Monitorando Erros com Sentry
- 1.5.4.	Conclusão The Twelve-Factor App

2.	Frontend e Emails

2.1.	Landing Page
- 2.1.1.	Projeto Fechado
- 2.1.2.	Twitter Bootstrap e Layoutit
- 2.1.3.	Instalando Arquivos Estáticos Localmente
- 2.1.4.	Template Tag Static
- 2.1.5.	Criação de Função para Testar Conteúdo
- 2.1.6.	Urls Nomeadas
- 2.1.7.	Encapsulando Urls em Apps
- 2.1..8.	Favicon, Imagens e HTML
- 2.1.9.	Rodapé
- 2.1.10.	Entrega da Landing Page

2.2. Integrações Simples
- 2.2.1.	Criação de Conta Mailchimp
- 2.2.2.	Criação de Lista de Espera
- 2.2.3.	Envio de Emails com Mailchimp
- 2.2.4.	Configurando Botão de Pagamento
- 2.2.5.	Serviço de Video Vimeo
- 2.2.6.	Criação de App Aperitivo
- 2.2.7.	Publicando o Video em Produção

2.3.	HTTP e Templates
- 2.1.	Fluxo HTTP no Django
- 2.2.	Herança de Templates
- 2.3.	Bloco de Template
- 2.4.	Contexto de Template
- 2.5.	Video de Acordo com Slug
- 2.6.	Filtros
- 2.7.	Lista de Elementos com For
- 2.8.	Acesso a Atributos no Template
- 2.9.	Acesso a Método no Template
- 2.10.	Composição de Templates

- 3.	Banco de Dados
- 3.1.	Instalação e Fundamentos
- 3.1.1.	Motivação - Banco de Dados
- 3.1.2.	Instalação de Postgres com Docker
- 3.1.3.	Acesso e Configuração Local do Postgres
- 3.1.4.	Modelos do Django
- 3.1.5.	Introdução a QuerySet e Migrações

- 3.2.	Testes com Banco de Dados
- 3.2.1.	Executar Testes Com e Sem Migrações
- 3.2.2.	Criação de Modelos nos Testes
- 3.2.3.	Criação Automágica de Propriedades de Modelo
- 3.2.4.	Final de Testes de Video e Criação de Migração
- 3.2.5.	Introdução ao Admin do Django

- 3.3.	Criação de App de Módulos de Aulas
- 3.3.1.	Requisitos da App Módulos de Aulas
- 3.3.2.	Teste de Títulos de Aba Módulos
- 3.3.3.	Fachada com Regras de Negócio
- 3.3.4.	Processador de Contexto
- 3.3.5.	Reaproveitando Apps de Terceiros
- 3.3.6.	Migração de Dados
- 3.3.7.	Consertando Links do Dropdown
- 3.3.8.	Construção da Página de Detalhes do Módulo

- 3.4.	Relacionamento Muitos para Um
- 3.4.1.	Como Criar Relacionamento entre Módulo e Aulas
- 3.4.2.	Acesso a Relação com Atributo _set
- 3.4.3.	Unindo Tabelas com SQL JOIN
- 3.4.4.	Criando Links para Aulas
- 3.4.5.	Página de Detalhe da Aula
- 3.4.6.	Adição de Coluna em Tabela

- 3.5.	Como Escapar das Armadilhas do ORM
- 3.5.1.	Tunando o Shell com IPython e Django Extensions
- 3.5.2.	Problema do N+1 Selects
- 3.5.3.	Implementando um Breadcrumb
- 3.5.4.	Corrigindo Ineficiência do Breacrumb
- 3.5.5.	Funcionalidade de Indice de Módulos
- 3.5.6.	Acesso ao lado N do relacionamento
- 3.5.7.	Método prefetch_related
- 3.5.8.	Objeto Prefetch

- 3.6.	Relacionamento de Muitos para Muitos
- 3.6.1.	Funcionalidade de Turmas
- 3.6.2.	Campo ManyToManyField
- 3.6.3.	Revertendo Migrações
- 3.6.4.	Criação de Tabela Intermediária
- 3.6.5.	Configuração de Modelo com Model Meta
- 3.6.6.	Admin com Modelos Relacionados

4.	Autenticação de Usuários
- 4.1.	Autenticação e Autorização
- 4.1.1.	Controle de Acesso nas Aulas
- 4.1.2.	Formulário de Login Simples
- 4.1.3.	Configuração de Redirect de Login
- 4.1.4.	Inserção de Botão de Login
- 4.1.5.	Teste com Usuário Logado
- 4.1.6.	Dados de Usuário no Cabeçalho
- 4.1.7.	Implementação de Logout
- 4.1.8.	Decorator Login Required

- 4.2.	Recuperação de Senha
- 4.2.1.	Formulário de Recuperação de Senhas
- 4.2.2.	Configurações de Envio de Email
