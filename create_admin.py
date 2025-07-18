from academia_app import create_app, db
from academia_app.models import Dados_alunos
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

def criar_primeiro_admin():
    print("--- Criador de Usuário Administrador ---")
    if Dados_alunos.query.filter_by(role='admin').first():
        print("Um usuário admin já existe. Nenhuma ação necessária.")
        return
    try:
        email = input("Digite o email do novo admin: ")
        password = input("Digite a senha para o novo admin: ")

        admin = Dados_alunos(
            nome='Admin',
            email=email,
            idade=99,
            peso=99,
            altura=199,
            objetivo='Administrar o sistema',
            role='admin'
        )
        admin.set_password(password)

        db.session.add(admin)
        db.session.commit()

        print(f"\nUsuário admin '{email}' criado com sucesso!")
        print("O arquivo 'datasave.db' foi criado ou atualizado na pasta 'instance'.")

    except Exception as e:
        db.session.rollback()
        print(f"\nOcorreu um erro ao criar o admin: {e}")

if __name__ == '__main__':
    criar_primeiro_admin()