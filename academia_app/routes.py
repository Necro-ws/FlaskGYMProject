from academia_app import db
from flask import render_template, request, redirect, url_for, abort
from .models import Dados_alunos, Ficha_A, Serie_Reps_A, Ficha_B, Serie_Reps_B, Ficha_C, Serie_Reps_C
from flask import current_app as app

from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def home():
    return render_template("index.htm")

@app.route("/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('alunos'))

    email = request.form.get("email")
    password = request.form.get("password")
    
    user = Dados_alunos.query.filter_by(email=email).first()

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('alunos'))
    else:
        status = {"type": "erro", "message": "Email ou senha inválidos."}
        return render_template('index.htm', status=status)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('index.htm')

@app.route("/alunos", methods=['GET', 'POST'])
@login_required
def alunos():
    if current_user.role == 'admin':
        if request.method == "POST":
            termo = request.form["pesquisa"]
            resultado = Dados_alunos.query.filter(Dados_alunos.nome.ilike(f'%{termo}%')).all()
            return render_template("alunos.htm", lista_alunos=resultado)
        else:
            lista_alunos = Dados_alunos.query.all()
            return render_template("alunos.htm", lista_alunos=lista_alunos)
    else:
        return redirect(url_for('fichas_alunos', id=current_user.id))
    
@app.route("/ficha/<int:id>")
@login_required
def fichas_alunos(id):
    if current_user.role != 'admin' and current_user.id != id:
        abort(403)

    aluno = Dados_alunos.query.get_or_404(id)

    ficha_aluno_a = Ficha_A.query.filter_by(user_id=id).first()
    serie_rep_a = Serie_Reps_A.query.filter_by(user_id=id).first()
    ficha_aluno_b = Ficha_B.query.filter_by(user_id=id).first()
    serie_rep_b = Serie_Reps_B.query.filter_by(user_id=id).first()
    ficha_aluno_c = Ficha_C.query.filter_by(user_id=id).first()
    serie_rep_c = Serie_Reps_C.query.filter_by(user_id=id).first()

    return render_template("ficha.htm", 
                           aluno=aluno,
                           ficha_aluno_a=ficha_aluno_a, serie_rep_a=serie_rep_a,
                           ficha_aluno_b=ficha_aluno_b, serie_rep_b=serie_rep_b,
                           ficha_aluno_c=ficha_aluno_c, serie_rep_c=serie_rep_c)
    
@app.route("/cadastro", methods=['GET', 'POST'])
@login_required
def cadastrar_aluno():
    if current_user.role != 'admin':
        abort(403)

    if request.method == 'POST':
        dados = request.form
        status = {"type": "sucesso", "message": "O Aluno foi cadastrado com sucesso!"}
        try:
            aluno = Dados_alunos(nome=dados['nome'], email=dados['email'], idade=dados['idade'],
                                 peso=dados['peso'], altura=dados['altura'], objetivo=dados['objetivo'],
                                 role='aluno')
            
            aluno.set_password(dados['senha'])
            db.session.add(aluno)
            db.session.commit()

            ficha_a = Ficha_A(user_id=aluno.id, ex_1=dados.get("ex_1_a"), ex_2=dados.get("ex_2_a"), ex_3=dados.get("ex_3_a"), ex_4=dados.get("ex_4_a"), ex_5=dados.get("ex_5_a"), ex_6=dados.get("ex_6_a"), ex_7=dados.get("ex_7_a"), ex_8=dados.get("ex_8_a"))
            serie_rep_a = Serie_Reps_A(user_id=aluno.id, serie_A=dados.get("series_a"), repeticoes_A=dados.get("repeticoes_a"))

            ficha_b = Ficha_B(user_id=aluno.id, ex_1=dados.get("ex_1_b"), ex_2=dados.get("ex_2_b"), ex_3=dados.get("ex_3_b"), ex_4=dados.get("ex_4_b"), ex_5=dados.get("ex_5_b"), ex_6=dados.get("ex_6_b"), ex_7=dados.get("ex_7_b"), ex_8=dados.get("ex_8_b"))
            serie_rep_b = Serie_Reps_B(user_id=aluno.id, serie_B=dados.get("series_b"), repeticoes_B=dados.get("repeticoes_b"))
            
            ficha_c = Ficha_C(user_id=aluno.id, ex_1=dados.get("ex_1_c"), ex_2=dados.get("ex_2_c"), ex_3=dados.get("ex_3_c"), ex_4=dados.get("ex_4_c"), ex_5=dados.get("ex_5_c"), ex_6=dados.get("ex_6_c"), ex_7=dados.get("ex_7_c"), ex_8=dados.get("ex_8_c"))
            serie_rep_c = Serie_Reps_C(user_id=aluno.id, serie_C=dados.get("series_c"), repeticoes_C=dados.get("repeticoes_c"))

            db.session.add(ficha_a)
            db.session.add(serie_rep_a)
            db.session.add(ficha_b)
            db.session.add(serie_rep_b)
            db.session.add(ficha_c)
            db.session.add(serie_rep_c)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            status = {"type": "erro", "message": f"Falha ao tentar cadastrar os dados do aluno: {e}"}
        
        return render_template("cadastro.htm", status=status)
    else:
        return render_template("cadastro.htm")
    
@app.route("/editar_dados/<int:id>", methods=["GET", "POST"])
@login_required
def editar_dados(id):
    if current_user.role != 'admin' and current_user.id != id:
        abort(403)

    aluno = Dados_alunos.query.get_or_404(id)

    if request.method == 'POST':
        dados_editados = request.form
    
        nova_senha = dados_editados.get('nova_senha')
        confirmar_senha = dados_editados.get('confirmar_senha')

        if nova_senha:
            if nova_senha != confirmar_senha:
                status = {"type": "erro", "message": "As novas senhas não coincidem. Nenhuma alteração foi salva."}
    
                ficha_aluno_a = Ficha_A.query.filter_by(user_id=id).first()
                serie_rep_a = Serie_Reps_A.query.filter_by(user_id=id).first()
                ficha_aluno_b = Ficha_B.query.filter_by(user_id=id).first()
                serie_rep_b = Serie_Reps_B.query.filter_by(user_id=id).first()
                ficha_aluno_c = Ficha_C.query.filter_by(user_id=id).first()
                serie_rep_c = Serie_Reps_C.query.filter_by(user_id=id).first()

                return render_template("editar_dados.htm", status=status,
                                       dados_aluno=aluno, ficha_aluno_a=ficha_aluno_a, serie_rep_a=serie_rep_a,
                                       ficha_aluno_b=ficha_aluno_b, serie_rep_b=serie_rep_b,
                                       ficha_aluno_c=ficha_aluno_c, serie_rep_c=serie_rep_c)
            else:
                aluno.set_password(nova_senha)

        aluno.nome = dados_editados["nome"]
        aluno.idade = dados_editados["idade"]
        aluno.peso = dados_editados["peso"]
        aluno.altura = dados_editados["altura"]
        aluno.objetivo = dados_editados["objetivo"]

        ficha_a = Ficha_A.query.filter_by(user_id=id).first()
        if not ficha_a:
            ficha_a = Ficha_A(user_id=id)
            db.session.add(ficha_a)
        ficha_a.ex_1 = dados_editados["ex_1_a"]
        ficha_a.ex_2 = dados_editados["ex_2_a"]
        ficha_a.ex_3 = dados_editados["ex_3_a"]
        ficha_a.ex_4 = dados_editados["ex_4_a"]
        ficha_a.ex_5 = dados_editados["ex_5_a"]
        ficha_a.ex_6 = dados_editados["ex_6_a"]
        ficha_a.ex_7 = dados_editados["ex_7_a"]
        ficha_a.ex_8 = dados_editados["ex_8_a"]

        serie_rep_a = Serie_Reps_A.query.filter_by(user_id=id).first()
        if not serie_rep_a:
            serie_rep_a = Serie_Reps_A(user_id=id)
            db.session.add(serie_rep_a)
        serie_rep_a.serie_A = dados_editados["series_a"]
        serie_rep_a.repeticoes_A = dados_editados["repeticoes_a"]
        
        ficha_b = Ficha_B.query.filter_by(user_id=id).first()
        if not ficha_b:
            ficha_b = Ficha_B(user_id=id)
            db.session.add(ficha_b)
        ficha_b.ex_1 = dados_editados["ex_1_b"]
        ficha_b.ex_2 = dados_editados["ex_2_b"]
        ficha_b.ex_3 = dados_editados["ex_3_b"]
        ficha_b.ex_4 = dados_editados["ex_4_b"]
        ficha_b.ex_5 = dados_editados["ex_5_b"]
        ficha_b.ex_6 = dados_editados["ex_6_b"]
        ficha_b.ex_7 = dados_editados["ex_7_b"]
        ficha_b.ex_8 = dados_editados["ex_8_b"]

        serie_rep_b = Serie_Reps_B.query.filter_by(user_id=id).first()
        if not serie_rep_b:
            serie_rep_b = Serie_Reps_B(user_id=id)
            db.session.add(serie_rep_b)
        serie_rep_b.serie_B = dados_editados["series_b"]
        serie_rep_b.repeticoes_B = dados_editados["repeticoes_b"]

        ficha_c = Ficha_C.query.filter_by(user_id=id).first()
        if not ficha_c:
            ficha_c = Ficha_C(user_id=id)
            db.session.add(ficha_c)
        ficha_c.ex_1 = dados_editados["ex_1_c"]
        ficha_c.ex_2 = dados_editados["ex_2_c"]
        ficha_c.ex_3 = dados_editados["ex_3_c"]
        ficha_c.ex_4 = dados_editados["ex_4_c"]
        ficha_c.ex_5 = dados_editados["ex_5_c"]
        ficha_c.ex_6 = dados_editados["ex_6_c"]
        ficha_c.ex_7 = dados_editados["ex_7_c"]
        ficha_c.ex_8 = dados_editados["ex_8_c"]

        serie_rep_c = Serie_Reps_C.query.filter_by(user_id=id).first()
        if not serie_rep_c:
            serie_rep_c = Serie_Reps_C(user_id=id)
            db.session.add(serie_rep_c)
        serie_rep_c.serie_C = dados_editados["series_c"]
        serie_rep_c.repeticoes_C = dados_editados["repeticoes_c"]
        
        db.session.commit()

        if current_user.role == 'admin':
            return redirect(url_for('alunos'))
        else:
            return redirect(url_for('fichas_alunos', id=id))

    else:
        ficha_aluno_a = Ficha_A.query.filter_by(user_id=id).first()
        serie_rep_a = Serie_Reps_A.query.filter_by(user_id=id).first()
        ficha_aluno_b = Ficha_B.query.filter_by(user_id=id).first()
        serie_rep_b = Serie_Reps_B.query.filter_by(user_id=id).first()
        ficha_aluno_c = Ficha_C.query.filter_by(user_id=id).first()
        serie_rep_c = Serie_Reps_C.query.filter_by(user_id=id).first()
        
        return render_template("editar_dados.htm", 
                               dados_aluno=aluno, ficha_aluno_a=ficha_aluno_a, serie_rep_a=serie_rep_a,
                               ficha_aluno_b=ficha_aluno_b, serie_rep_b=serie_rep_b,
                               ficha_aluno_c=ficha_aluno_c, serie_rep_c=serie_rep_c)
    
@app.route("/deletar_dados/<int:id>")
@login_required
def deletar_dados(id):
    if current_user.role != 'admin':
        abort(403)
    
    if current_user.id == id:
        return redirect(url_for('alunos'))

    Ficha_A.query.filter_by(user_id=id).delete()
    Serie_Reps_A.query.filter_by(user_id=id).delete()
    Ficha_B.query.filter_by(user_id=id).delete()
    Serie_Reps_B.query.filter_by(user_id=id).delete()
    Ficha_C.query.filter_by(user_id=id).delete()
    Serie_Reps_C.query.filter_by(user_id=id).delete()

    dados_aluno = Dados_alunos.query.get(id)
    if dados_aluno:
        db.session.delete(dados_aluno)
    
    db.session.commit()
    
    return redirect(url_for('alunos'))
