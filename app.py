from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USUARIOS = {
    "gabriel": "1234",
    "livia": "1234"
}

VIAGENS = []


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

    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        return redirect(f"/dashboard/{usuario}")

    return render_template("login.html", erro="Senha incorreta")


@app.route("/dashboard/<usuario>")
def dashboard(usuario):

    return render_template(
        "dashboard.html",
        usuario=usuario.capitalize()
    )


@app.route("/viagens/<usuario>")
def viagens(usuario):

    return render_template(
        "viagens.html",
        usuario=usuario.capitalize(),
        viagens=VIAGENS
    )


@app.route("/nova-viagem/<usuario>")
def nova_viagem(usuario):

    return render_template(
        "nova_viagem.html",
        usuario=usuario.capitalize()
    )


@app.route("/salvar-viagem/<usuario>", methods=["POST"])
def salvar_viagem(usuario):

    VIAGENS.append({

        "destino": request.form["destino"],
        "cidade": request.form["cidade"],
        "pais": request.form["pais"],
        "inicio": request.form["inicio"],
        "fim": request.form["fim"],
        "valor": request.form["valor"]

    })

    return redirect(f"/viagens/{usuario}")


if __name__ == "__main__":
    app.run(debug=True)