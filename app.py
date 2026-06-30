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
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

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
    if usuario.lower() not in USUARIOS:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        usuario=usuario.capitalize()
    )


@app.route("/viagens/<usuario>")
def viagens(usuario):
    if usuario.lower() not in USUARIOS:
        return redirect("/login")

    return render_template(
        "viagens.html",
        usuario=usuario.capitalize()
    )


@app.route("/nova-viagem/<usuario>")
def nova_viagem(usuario):
    if usuario.lower() not in USUARIOS:
        return redirect("/login")

    return render_template(
        "nova_viagem.html",
        usuario=usuario.capitalize()
    )


@app.route("/editar-viagem/<id>/<usuario>")
def editar_viagem(id, usuario):
    if usuario.lower() not in USUARIOS:
        return redirect("/login")

    viagem = {
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

    return render_template(
        "editar_viagem.html",
        usuario=usuario.capitalize(),
        viagem=viagem
    )


if __name__ == "__main__":
    app.run(debug=True)