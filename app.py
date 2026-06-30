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


if __name__ == "__main__":
    app.run(debug=True)