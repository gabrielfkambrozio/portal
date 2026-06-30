from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USUARIOS = {
    "gabriel": "1234",
    "livia": "1234"
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

    if usuario in USUARIOS and USUARIOS[usuario] == senha:
        return redirect(f"/dashboard/{usuario}")

    return render_template("login.html", erro="Senha incorreta")


@app.route("/dashboard/<usuario>")
def dashboard(usuario):

    return render_template(
        "dashboard.html",
        usuario=usuario.capitalize()
    )


if __name__ == "__main__":
    app.run(debug=True)