from . import db

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
        