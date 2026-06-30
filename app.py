from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

USUARIOS = {
    "gabriel": "1234",
    "livia": "1234"
}


def conectar():
    conn = sqlite3.connect("portal.db")
    conn.row_factory = sqlite3.Row
    return conn


def criar_banco():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS viagens(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            destino TEXT,
            cidade TEXT,
            pais TEXT,

            inicio TEXT,
            fim TEXT,

            valor REAL,

            status TEXT,

            observacoes TEXT

        )
    """)

    conn.commit()
    conn.close()


criar_banco()


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


@app.route("/dashboard/<usuario>")
def dashboard(usuario):

    return render_template(
        "dashboard.html",
        usuario=usuario.capitalize()
    )


@app.route("/viagens/<usuario>")
def viagens(usuario):

    conn = conectar()

    viagens = conn.execute("""

        SELECT *

        FROM viagens

        ORDER BY inicio DESC

    """).fetchall()

    conn.close()

    return render_template(

        "viagens.html",

        usuario=usuario.capitalize(),

        viagens=viagens

    )


@app.route("/nova-viagem/<usuario>")
def nova_viagem(usuario):

    return render_template(

        "nova_viagem.html",

        usuario=usuario.capitalize()

    )


@app.route("/salvar-viagem/<usuario>", methods=["POST"])
def salvar_viagem(usuario):

    conn = conectar()

    conn.execute("""

        INSERT INTO viagens(

            destino,
            cidade,
            pais,
            inicio,
            fim,
            valor,
            status,
            observacoes

        )

        VALUES(

            ?,?,?,?,?,?,?,?

        )

    """,(

        request.form["destino"],
        request.form["cidade"],
        request.form["pais"],
        request.form["inicio"],
        request.form["fim"],
        request.form["valor"],
        request.form["status"],
        request.form["observacoes"]

    ))

    conn.commit()
    conn.close()

    return redirect(f"/viagens/{usuario}")


@app.route("/excluir-viagem/<int:id>/<usuario>")
def excluir_viagem(id, usuario):

    conn = conectar()

    conn.execute("""

        DELETE

        FROM viagens

        WHERE id = ?

    """,(id,))

    conn.commit()
    conn.close()

    return redirect(f"/viagens/{usuario}")


@app.route("/editar-viagem/<int:id>/<usuario>")
def editar_viagem(id, usuario):

    conn = conectar()

    viagem = conn.execute("""

        SELECT *

        FROM viagens

        WHERE id = ?

    """,(id,)).fetchone()

    conn.close()

    return render_template(

        "editar_viagem.html",

        usuario=usuario.capitalize(),

        viagem=viagem

    )


@app.route("/atualizar-viagem/<int:id>/<usuario>", methods=["POST"])
def atualizar_viagem(id, usuario):

    conn = conectar()

    conn.execute("""

        UPDATE viagens

        SET

            destino=?,
            cidade=?,
            pais=?,
            inicio=?,
            fim=?,
            valor=?,
            status=?,
            observacoes=?

        WHERE id=?

    """,(

        request.form["destino"],
        request.form["cidade"],
        request.form["pais"],
        request.form["inicio"],
        request.form["fim"],
        request.form["valor"],
        request.form["status"],
        request.form["observacoes"],
        id

    ))

    conn.commit()
    conn.close()

    return redirect(f"/viagens/{usuario}")


if __name__ == "__main__":
    app.run(debug=True)