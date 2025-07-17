from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datasave.db"
db = SQLAlchemy()
db.init_app(app)

# ^^^^^^^^^^^^^^^^^^^^ IMPORTS ^^^^^^^^^^^^^^^^^^^^
# -------------------------------------------------
# vvvvvvvvvvvvvvvvvvvv CLASSES vvvvvvvvvvvvvvvvvvvv

class Dados_alunos(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    objetivo = db.Column(db.String(200), nullable=False)

    def __init__(self, nome: str, idade: int, peso: int, altura: int, objetivo: str) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

class Ficha_A(db.Model):
    __tablename__ = 'ficha_A'
    id = db.Column(db.Integer, primary_key=True)
    ex_1 = db.Column(db.String(100))
    ex_2 = db.Column(db.String(100))
    ex_3 = db.Column(db.String(100))
    ex_4 = db.Column(db.String(100))
    ex_5 = db.Column(db.String(100))
    ex_6 = db.Column(db.String(100))
    ex_7 = db.Column(db.String(100))
    ex_8 = db.Column(db.String(100))

    def __init__(self, ex_1: str, ex_2: str, ex_3: str, ex_4: str, ex_5: str, ex_6: str, ex_7: str, ex_8: str) -> None:
        self.ex_1 = ex_1
        self.ex_2 = ex_2
        self.ex_3 = ex_3
        self.ex_4 = ex_4
        self.ex_5 = ex_5
        self.ex_6 = ex_6
        self.ex_7 = ex_7
        self.ex_8 = ex_8

class Serie_Reps_A(db.Model):
    __tablename__ = 'serie_rep_A'
    id= db.Column(db.Integer, primary_key=True)
    serie_A = db.Column(db.Integer, nullable=False)
    repeticoes_A = db.Column(db.Integer, nullable=False)

    def __init__(self, serie_A: int, repeticoes_A: int) -> None:
        self.serie_A = serie_A
        self.repeticoes_A = repeticoes_A

class Ficha_B(db.Model):
    __tablename__ = 'ficha_B'
    id = db.Column(db.Integer, primary_key=True)
    ex_1 = db.Column(db.String(100))
    ex_2 = db.Column(db.String(100))
    ex_3 = db.Column(db.String(100))
    ex_4 = db.Column(db.String(100))
    ex_5 = db.Column(db.String(100))
    ex_6 = db.Column(db.String(100))
    ex_7 = db.Column(db.String(100))
    ex_8 = db.Column(db.String(100))

    def __init__(self, ex_1: str, ex_2: str, ex_3: str, ex_4: str, ex_5: str, ex_6: str, ex_7: str, ex_8: str) -> None:
        self.ex_1 = ex_1
        self.ex_2 = ex_2
        self.ex_3 = ex_3
        self.ex_4 = ex_4
        self.ex_5 = ex_5
        self.ex_6 = ex_6
        self.ex_7 = ex_7
        self.ex_8 = ex_8

class Serie_Reps_B(db.Model):
    __tablename__ = 'serie_rep_B'
    id= db.Column(db.Integer, primary_key=True)
    serie_B = db.Column(db.Integer, nullable=False)
    repeticoes_B = db.Column(db.Integer, nullable=False)

    def __init__(self, serie_B: int, repeticoes_B: int) -> None:
        self.serie_B = serie_B
        self.repeticoes_B = repeticoes_B

class Ficha_C(db.Model):
    __tablename__ = 'ficha_C'
    id = db.Column(db.Integer, primary_key=True)
    ex_1 = db.Column(db.String(100))
    ex_2 = db.Column(db.String(100))
    ex_3 = db.Column(db.String(100))
    ex_4 = db.Column(db.String(100))
    ex_5 = db.Column(db.String(100))
    ex_6 = db.Column(db.String(100))
    ex_7 = db.Column(db.String(100))
    ex_8 = db.Column(db.String(100))

    def __init__(self, ex_1: str, ex_2: str, ex_3: str, ex_4: str, ex_5: str, ex_6: str, ex_7: str, ex_8: str) -> None:
        self.ex_1 = ex_1
        self.ex_2 = ex_2
        self.ex_3 = ex_3
        self.ex_4 = ex_4
        self.ex_5 = ex_5
        self.ex_6 = ex_6
        self.ex_7 = ex_7
        self.ex_8 = ex_8

class Serie_Reps_C(db.Model):
    __tablename__ = 'serie_rep_C'
    id= db.Column(db.Integer, primary_key=True)
    serie_C = db.Column(db.Integer, nullable=False)
    repeticoes_C = db.Column(db.Integer, nullable=False)

    def __init__(self, serie_C: int, repeticoes_C: int) -> None:
        self.serie_C = serie_C
        self.repeticoes_C = repeticoes_C

# ^^^^^^^^^^^^^^^^^^^^ CLASSES ^^^^^^^^^^^^^^^^^^^^
# -------------------------------------------------
# vvvvvvvvvvvvvvvvvvvvv ROTAS vvvvvvvvvvvvvvvvvvvvv

@app.route("/")
def home():
    return render_template("index.htm")

@app.route("/alunos", methods=['GET', 'POST'])
def alunos():
    if request.method == "POST":
        termo = request.form["pesquisa"]
        resultado = db.session.execute(db.select(Dados_alunos).filter(Dados_alunos.nome.like(f"%{termo}%"))).scalars()
        return render_template("alunos.htm", lista_alunos=resultado)
    else:
        lista_alunos = db.session.execute(db.select(Dados_alunos)).scalars()
        return render_template("alunos.htm", lista_alunos=lista_alunos)
    
@app.route("/ficha/<int:id>", methods=["GET", "POST"])
def fichas_alunos(id):
    if request.method == "POST":
        pass
    else:
        ficha_aluno_a = db.session.execute(db.select(Ficha_A).filter(Ficha_A.id == id)).scalar()
        serie_rep_a = db.session.execute(db.select(Serie_Reps_A).filter(Serie_Reps_A.id == id)).scalar()
        ficha_aluno_b = db.session.execute(db.select(Ficha_B).filter(Ficha_B.id == id)).scalar()
        serie_rep_b = db.session.execute(db.select(Serie_Reps_B).filter(Serie_Reps_B.id == id)).scalar()
        ficha_aluno_c = db.session.execute(db.select(Ficha_C).filter(Ficha_C.id == id)).scalar()
        serie_rep_c = db.session.execute(db.select(Serie_Reps_C).filter(Serie_Reps_C.id == id)).scalar()

        return render_template("ficha.htm", ficha_aluno_a=ficha_aluno_a, serie_rep_a=serie_rep_a,
                                            ficha_aluno_b=ficha_aluno_b, serie_rep_b=serie_rep_b,
                                            ficha_aluno_c=ficha_aluno_c, serie_rep_c=serie_rep_c)
    
@app.route("/cadastro", methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == "POST":
        dados = request.form
        status = {"type": "sucesso", "message": f"O Aluno foi cadastrado com sucesso!"}
        try:
            aluno = Dados_alunos(dados["nome"], dados["idade"], dados["peso"], dados["altura"], dados["objetivo"])
            ficha_a = Ficha_A(dados["ex_1_a"], dados["ex_2_a"], dados["ex_3_a"], dados["ex_4_a"], dados["ex_5_a"], dados["ex_6_a"], dados["ex_7_a"], dados["ex_8_a"])
            serie_rep_a = Serie_Reps_A(dados["series_a"], dados["repeticoes_a"])
            ficha_b = Ficha_B(dados["ex_1_b"], dados["ex_2_b"], dados["ex_3_b"], dados["ex_4_b"], dados["ex_5_b"], dados["ex_6_b"], dados["ex_7_b"], dados["ex_8_b"])
            serie_rep_b = Serie_Reps_B(dados["series_b"], dados["repeticoes_b"])
            ficha_c = Ficha_C(dados["ex_1_c"], dados["ex_2_c"], dados["ex_3_c"], dados["ex_4_c"], dados["ex_5_c"], dados["ex_6_c"], dados["ex_7_c"], dados["ex_8_c"])
            serie_rep_c = Serie_Reps_C(dados["series_c"], dados["repeticoes_c"])
            db.session.add(aluno)
            db.session.add(ficha_a)
            db.session.add(serie_rep_a)
            db.session.add(ficha_b)
            db.session.add(serie_rep_b)
            db.session.add(ficha_c)
            db.session.add(serie_rep_c)
            db.session.commit()
        except:
            status = {"type": "erro", "message": f"Falha ao tentatar cadastrar os dados do aluno."}
        return render_template("cadastro.htm", status=status)
    else:
        return render_template("cadastro.htm")
    
@app.route("/editar_dados/<int:id>", methods=["GET", "POST"])
def editar_dados(id):
    if request.method == "POST":
        dados_editados = request.form
        aluno = db.session.execute(db.select(Dados_alunos).filter(Dados_alunos.id == id)).scalar()
        ficha_a = db.session.execute(db.select(Ficha_A).filter(Ficha_A.id == id)).scalar()
        serie_rep_a = db.session.execute(db.select(Serie_Reps_A).filter(Serie_Reps_A.id == id)).scalar()
        ficha_b = db.session.execute(db.select(Ficha_B).filter(Ficha_B.id == id)).scalar()
        serie_rep_b = db.session.execute(db.select(Serie_Reps_B).filter(Serie_Reps_B.id == id)).scalar()
        ficha_c = db.session.execute(db.select(Ficha_C).filter(Ficha_C.id == id)).scalar()
        serie_rep_c = db.session.execute(db.select(Serie_Reps_C).filter(Serie_Reps_C.id == id)).scalar()

        aluno.nome = dados_editados["nome"]
        aluno.idade = dados_editados["idade"]
        aluno.peso = dados_editados["peso"]
        aluno.altura = dados_editados["altura"]
        aluno.objetivo = dados_editados["objetivo"]

        ficha_a.ex_1 = dados_editados["ex_1_a"]
        ficha_a.ex_2 = dados_editados["ex_2_a"]
        ficha_a.ex_3 = dados_editados["ex_3_a"]
        ficha_a.ex_4 = dados_editados["ex_4_a"]
        ficha_a.ex_5 = dados_editados["ex_5_a"]
        ficha_a.ex_6 = dados_editados["ex_6_a"]
        ficha_a.ex_7 = dados_editados["ex_7_a"]
        ficha_a.ex_8 = dados_editados["ex_8_a"]

        serie_rep_a.serie_A = dados_editados["series_a"]
        serie_rep_a.repeticoes_A = dados_editados["repeticoes_a"]

        ficha_b.ex_1 = dados_editados["ex_1_b"]
        ficha_b.ex_2 = dados_editados["ex_2_b"]
        ficha_b.ex_3 = dados_editados["ex_3_b"]
        ficha_b.ex_4 = dados_editados["ex_4_b"]
        ficha_b.ex_5 = dados_editados["ex_5_b"]
        ficha_b.ex_6 = dados_editados["ex_6_b"]
        ficha_b.ex_7 = dados_editados["ex_7_b"]
        ficha_b.ex_8 = dados_editados["ex_8_b"]

        serie_rep_b.serie_B = dados_editados["series_b"]
        serie_rep_b.repeticoes_B = dados_editados["repeticoes_b"]

        ficha_c.ex_1 = dados_editados["ex_1_c"]
        ficha_c.ex_2 = dados_editados["ex_2_c"]
        ficha_c.ex_3 = dados_editados["ex_3_c"]
        ficha_c.ex_4 = dados_editados["ex_4_c"]
        ficha_c.ex_5 = dados_editados["ex_5_c"]
        ficha_c.ex_6 = dados_editados["ex_6_c"]
        ficha_c.ex_7 = dados_editados["ex_7_c"]
        ficha_c.ex_8 = dados_editados["ex_8_c"]

        serie_rep_c.serie_C = dados_editados["series_c"]
        serie_rep_c.repeticoes_C = dados_editados["repeticoes_c"]

        db.session.commit()
        return redirect("/alunos")

    else:
        dados_aluno = db.session.execute(db.select(Dados_alunos).filter(Dados_alunos.id == id)).scalar()
        ficha_aluno_a = db.session.execute(db.select(Ficha_A).filter(Ficha_A.id == id)).scalar()
        serie_rep_a = db.session.execute(db.select(Serie_Reps_A).filter(Serie_Reps_A.id == id)).scalar()
        ficha_aluno_b = db.session.execute(db.select(Ficha_B).filter(Ficha_B.id == id)).scalar()
        serie_rep_b = db.session.execute(db.select(Serie_Reps_B).filter(Serie_Reps_B.id == id)).scalar()
        ficha_aluno_c = db.session.execute(db.select(Ficha_C).filter(Ficha_C.id == id)).scalar()
        serie_rep_c = db.session.execute(db.select(Serie_Reps_C).filter(Serie_Reps_C.id == id)).scalar()
        
        return render_template("editar_dados.htm", dados_aluno=dados_aluno, ficha_aluno_a=ficha_aluno_a, serie_rep_a=serie_rep_a,
                                                                            ficha_aluno_b=ficha_aluno_b, serie_rep_b=serie_rep_b,
                                                                            ficha_aluno_c=ficha_aluno_c, serie_rep_c=serie_rep_c)
    
@app.route("/deletar_dados/<int:id>")
def deletar_dados(id):
    dados_aluno = db.session.execute(db.select(Dados_alunos).filter(Dados_alunos.id == id)).scalar()
    ficha_aluno_a = db.session.execute(db.select(Ficha_A).filter(Ficha_A.id == id)).scalar()
    serie_rep_a = db.session.execute(db.select(Serie_Reps_A).filter(Serie_Reps_A.id == id)).scalar()
    ficha_aluno_b = db.session.execute(db.select(Ficha_B).filter(Ficha_B.id == id)).scalar()
    serie_rep_b = db.session.execute(db.select(Serie_Reps_B).filter(Serie_Reps_B.id == id)).scalar()
    ficha_aluno_c = db.session.execute(db.select(Ficha_C).filter(Ficha_C.id == id)).scalar()
    serie_rep_c = db.session.execute(db.select(Serie_Reps_C).filter(Serie_Reps_C.id == id)).scalar()
    
    db.session.delete(dados_aluno)
    db.session.delete(ficha_aluno_a)
    db.session.delete(serie_rep_a)
    db.session.delete(ficha_aluno_b)
    db.session.delete(serie_rep_b)
    db.session.delete(ficha_aluno_c)
    db.session.delete(serie_rep_c)
    db.session.commit()
    return redirect("/alunos")

# ^^^^^^^^^^^^^^^^^^^^^ ROTAS ^^^^^^^^^^^^^^^^^^^^^
# -------------------------------------------------
# vvvvvvvvvvvvvvvvvvvvvv RUN vvvvvvvvvvvvvvvvvvvvvv

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        