from flask import render_template, request, redirect
from . import db
from .models import Dados_alunos, Ficha_A, Serie_Reps_A, Ficha_B, Serie_Reps_B, Ficha_C, Serie_Reps_C
from flask import current_app as app

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
