Sistema de Gestão de Alunos e Fichas de Treino


Descrição Breve
Este é um aplicativo web desenvolvido com Flask e Flask-SQLAlchemy para gerenciar dados de alunos e suas respectivas fichas de treino (A, B e C). Ele permite cadastrar novos alunos com suas informações pessoais e objetivos, atribuir exercícios e séries/repetições para cada ficha, e visualizar, editar ou remover esses dados.

Recursos
Cadastro de Alunos: Adicione novos alunos com nome, idade, peso, altura e objetivo.

Gestão de Fichas de Treino: Crie e associe fichas de treino A, B e C para cada aluno, incluindo até 8 exercícios por ficha e suas respectivas séries e repetições.

Visualização de Alunos: Liste todos os alunos cadastrados e pesquise por nome.

Visualização de Fichas: Acesse as fichas de treino detalhadas de cada aluno.

Edição de Dados: Atualize informações de alunos e suas fichas de treino.

Exclusão de Dados: Remova registros de alunos e suas fichas associadas.

Persistência de Dados: Utiliza SQLite como banco de dados para armazenar todas as informações.

Como Instalar
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos
Python 3.x (recomenda-se Python 3.8 ou superior)

pip (gerenciador de pacotes do Python)

Passos de Instalação
Clone o repositório:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

(Lembre-se de substituir SEU_USUARIO e SEU_REPOSITORIO pelos seus dados reais no GitHub).

Crie e ative um ambiente virtual:
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

No Windows:

python -m venv venv
.\venv\Scripts\activate

Se você encontrar um erro ao ativar o ambiente virtual no PowerShell (.ps1), pode ser necessário ajustar a Política de Execução. Abra o PowerShell como Administrador e execute Set-ExecutionPolicy RemoteSigned. Confirme com S ou Y.

No macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Instale as dependências:
Com o ambiente virtual ativado, instale todas as bibliotecas necessárias usando o requirements.txt:

pip install -r requirements.txt

Como Executar
Após a instalação, você pode iniciar o aplicativo Flask:

Certifique-se de que seu ambiente virtual está ativado.

No diretório raiz do projeto, execute:

python app.py

O servidor Flask será iniciado e você poderá acessá-lo em seu navegador, geralmente em http://127.0.0.1:5000/.

Tecnologias Usadas
Backend:

Flask: Micro-framework web para Python.

Flask-SQLAlchemy: Extensão Flask para SQLAlchemy, um ORM (Object Relational Mapper).

SQLite: Banco de dados leve e baseado em arquivo.

Frontend (HTML/CSS/JS):

HTML: Para a estrutura das páginas.

CSS: Para estilização (assumindo que você usa CSS para os templates).

JavaScript: Para interatividade (se aplicável nos seus templates).