Sistema de Gestão de Academia
Descrição Breve
Este é um aplicativo web desenvolvido com Flask para a gestão completa de alunos e fichas de treino em uma academia. O sistema conta com um robusto sistema de autenticação que diferencia usuários em dois níveis: Administradores e Alunos, garantindo que cada um tenha acesso apenas às funcionalidades permitidas.

Recursos Principais
Sistema de Autenticação e Segurança
Login Seguro: Autenticação de usuários baseada em email e senha.

Hashing de Senhas: As senhas são armazenadas de forma segura no banco de dados usando hashes, nunca em texto plano.

Sessões de Usuário: Gerenciamento de sessões para manter o usuário logado de forma segura.

Interface Dinâmica: A barra de navegação e as opções disponíveis se adaptam de acordo com o tipo de usuário logado (visitante, aluno ou admin).

Permissões de Administrador (Admin)
Visão Geral: Acesso completo a todos os dados do sistema.

Gerenciamento de Alunos: Pode cadastrar, visualizar, editar e excluir qualquer aluno.

Gerenciamento de Fichas: Cria e edita as fichas de treino (A, B, C) para todos os alunos.

Gerenciamento de Senha: Permissão para editar seus próprios dados e alterar a própria senha.

Pesquisa: Ferramenta de busca para encontrar alunos rapidamente.

Permissões de Aluno
Acesso Restrito: Um aluno só pode visualizar e interagir com seus próprios dados.

Visualização de Ficha: Acesso direto à sua ficha de treino detalhada após o login.

Edição de Dados: Permissão para editar suas próprias informações pessoais, treinos e alterar sua senha.

Como Instalar e Executar
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

1. Clone o Repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

(Lembre-se de substituir SEU_USUARIO e SEU_REPOSITORIO)

2. Crie e Ative um Ambiente Virtual
No Windows:

python -m venv venv
.\venv\Scripts\activate

No macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Instale as Dependências
pip install -r requirements.txt

4. Crie o Primeiro Usuário Administrador (Passo Obrigatório)
Execute o script fornecido para criar o primeiro usuário com permissões de administrador.

python create_admin.py

O script pedirá que você digite um email e uma senha. Siga as instruções.

5. Execute a Aplicação
python run.py

Acesse http://127.0.0.1:5000/ em seu navegador e faça login com as credenciais do admin que você acabou de criar.

Tecnologias Usadas
Backend:

Flask

Flask-SQLAlchemy

Flask-Login

Werkzeug

SQLite

Frontend:

HTML5 com Jinja2

Bootstrap 5