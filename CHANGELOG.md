Changelog
Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em Keep a Changelog.

[1.2.0] - 2025-07-21
Adicionado
Funcionalidade de Troca de Senha: Usuários (tanto Alunos quanto Administradores) agora podem alterar suas próprias senhas na página de edição de dados.

Redirecionamento Inteligente: Após editar o perfil, os administradores são redirecionados para a lista de alunos, enquanto os alunos são redirecionados de volta para sua própria ficha de treino.

Corrigido (Fixed)
Bug na Edição de Perfil sem Ficha: Corrigido um erro (AttributeError) que ocorria quando um usuário (como um admin recém-criado) tentava editar seu perfil sem ter fichas de treino (A, B, C) associadas. O sistema agora cria as fichas automaticamente se elas não existirem.

[1.1.0] - 2025-07-18
Adicionado
Sistema de Autenticação: Implementado sistema de login seguro com Flask-Login.

Níveis de Permissão: Criada a diferenciação entre usuários Administradores e Alunos, com acesso a funcionalidades distintas.

Segurança de Senhas: Adicionado hashing de senhas com Werkzeug para armazenamento seguro.

Interface Dinâmica: A barra de navegação e as opções visíveis agora mudam de acordo com o status e o tipo de usuário logado.

[1.0.0] - 2025-07-16
Adicionado
Versão Inicial do Projeto: Estrutura base da aplicação com Flask.

CRUD de Alunos e Fichas: Implementadas as funcionalidades básicas para Criar, Ler, Atualizar e Deletar alunos e suas fichas de treino (A, B e C).

Banco de Dados: Configuração inicial com Flask-SQLAlchemy e SQLite.

Templates Básicos: Criação das páginas HTML iniciais para visualização e manipulação dos dados.