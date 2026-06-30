from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USUARIOS = {
    "gabriel": "2906",
    "livia": "2906"
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/entrar", methods=["POST"])
def entrar():

    usuario = request.form.get("usuario", "").lower()
    senha = request.form.get("senha", "")

    if usuario in USUARIOS and senha == USUARIOS[usuario]:
        return redirect(f"/dashboard/{usuario}")

    return render_template(
        "login.html",
        erro="Senha incorreta"
    )


@app.route("/dashboard")
def dashboard_sem_usuario():
    return redirect("/login")


@app.route("/dashboard/<usuario>")
def dashboard(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        usuario=usuario.capitalize()
    )


# =========================
# VIAGENS
# =========================

@app.route("/viagens/<usuario>")
def viagens(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "viagens.html",
        usuario=usuario.capitalize()
    )


@app.route("/nova-viagem/<usuario>")
def nova_viagem(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "nova_viagem.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-viagem/<int:id>/<usuario>")
def editar_viagem(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_viagem.html",
        usuario=usuario.capitalize(),
        viagem={
            "id": id,
            "destino": "",
            "cidade": "",
            "pais": "",
            "inicio": "",
            "fim": "",
            "valor": "",
            "status": "Planejada",
            "observacoes": ""
        }
    )


# =========================
# RESTAURANTES
# =========================

@app.route("/restaurantes/<usuario>")
def restaurantes(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "restaurantes.html",
        usuario=usuario.capitalize()
    )


@app.route("/novo-restaurante/<usuario>")
def novo_restaurante(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "novo_restaurante.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-restaurante/<int:id>/<usuario>")
def editar_restaurante(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_restaurante.html",
        usuario=usuario.capitalize(),
        restaurante={
            "id": id,
            "nome": "",
            "cidade": "",
            "tipo": "",
            "data": "",
            "nota": "",
            "valor": "",
            "observacoes": ""
        }
    )


# =========================
# FILMES
# =========================

@app.route("/filmes/<usuario>")
def filmes(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "filmes.html",
        usuario=usuario.capitalize()
    )


@app.route("/novo-filme/<usuario>")
def novo_filme(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "novo_filme.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-filme/<int:id>/<usuario>")
def editar_filme(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_filme.html",
        usuario=usuario.capitalize(),
        filme={
            "id": id,
            "titulo": "",
            "genero": "",
            "data": "",
            "nota": "",
            "duracao": "",
            "observacoes": ""
        }
    )


# =========================
# MÚSICAS
# =========================

@app.route("/musicas/<usuario>")
def musicas(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "musicas.html",
        usuario=usuario.capitalize()
    )


@app.route("/nova-musica/<usuario>")
def nova_musica(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "nova_musica.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-musica/<int:id>/<usuario>")
def editar_musica(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_musica.html",
        usuario=usuario.capitalize(),
        musica={
            "id": id,
            "titulo": "",
            "artista": "",
            "album": "",
            "genero": "",
            "data": "",
            "nota": "",
            "observacoes": ""
        }
    )


# =========================
# EVENTOS
# =========================

@app.route("/eventos/<usuario>")
def eventos(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "eventos.html",
        usuario=usuario.capitalize()
    )


@app.route("/novo-evento/<usuario>")
def novo_evento(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "novo_evento.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-evento/<int:id>/<usuario>")
def editar_evento(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_evento.html",
        usuario=usuario.capitalize(),
        evento={
            "id": id,
            "titulo": "",
            "local": "",
            "categoria": "",
            "data": "",
            "hora": "",
            "valor": "",
            "observacoes": ""
        }
    )


# =========================
# DECLARAÇÕES
# =========================

@app.route("/declaracoes/<usuario>")
def declaracoes(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "declaracoes.html",
        usuario=usuario.capitalize()
    )


@app.route("/nova-declaracao/<usuario>")
def nova_declaracao(usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "nova_declaracao.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-declaracao/<int:id>/<usuario>")
def editar_declaracao(id, usuario):

    usuario = usuario.lower()

    if usuario not in USUARIOS:
        return redirect("/login")

    return render_template(
        "editar_declaracao.html",
        usuario=usuario.capitalize(),
        declaracao={
            "id": id,
            "titulo": "",
            "categoria": "",
            "data": "",
            "texto": ""
        }
    )


if __name__ == "__main__":
    app.run(debug=True)