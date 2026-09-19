from flask import Flask, render_template, request
import sqlite3
import re

app = Flask(__name__)

def criar_banco():
    conexao = sqlite3.connect("conectanegocios.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS negocios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            descricao TEXT NOT NULL,
            cidade TEXT NOT NULL,
            bairro TEXT NOT NULL,
            whatsapp TEXT,
            instagram TEXT,
            produtos TEXT
        )
    """)

    conexao.commit()
    conexao.close()


criar_banco()



@app.route("/")
def home():
    conexao = sqlite3.connect("conectanegocios.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    negocios = cursor.execute(
        "SELECT * FROM negocios ORDER BY id DESC"
    ).fetchall()

    conexao.close()

    return render_template("index.html", negocios=negocios)



@app.route("/beleza-funcional")
def beleza_funcional():
    return render_template("beleza_funcional.html")



@app.route("/missara")
def missara():
    return render_template("missara.html")



@app.route('/momentomeu')
def momentomeu():
    return render_template('momentomeu.html')



@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    sucesso = False

    if request.method == "POST":

        nome = request.form.get("nome-negocio")
        categoria = request.form.get("categoria")
        descricao = request.form.get("descricao")
        cidade = request.form.get("cidade")
        bairro = request.form.get("bairro")
        whatsapp = request.form.get("whatsapp")
        instagram = request.form.get("instagram")
        produtos = request.form.get("produtos")

        conexao = sqlite3.connect("conectanegocios.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO negocios
            (nome, categoria, descricao, cidade, bairro, whatsapp, instagram, produtos)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            nome,
            categoria,
            descricao,
            cidade,
            bairro,
            whatsapp,
            instagram,
            produtos
        ))

        conexao.commit()
        conexao.close()

        print("----- NOVO CADASTRO -----")
        print("Nome:", nome)
        print("Categoria:", categoria)
        print("Descrição:", descricao)
        print("Cidade:", cidade)
        print("Bairro:", bairro)
        print("WhatsApp:", whatsapp)
        print("Instagram:", instagram)
        print("Produtos/Serviços:", produtos)
        print("-------------------------")

        sucesso = True

    return render_template("cadastro.html", sucesso=sucesso)

@app.route("/negocio/<int:id>")
def ver_negocio(id):
    conexao = sqlite3.connect("conectanegocios.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    negocio = cursor.execute(
        "SELECT * FROM negocios WHERE id = ?",
        (id,)
    ).fetchone()

    conexao.close()

    whatsapp_link = ""

    if negocio and negocio["whatsapp"]:
        numero = re.sub(r"\D", "", negocio["whatsapp"])

        if not numero.startswith("55"):
            numero = "55" + numero

        whatsapp_link = "https://wa.me/" + numero

    return render_template(
        "negocio.html",
        negocio=negocio,
        whatsapp_link=whatsapp_link
    )

if __name__ == "__main__":
    criar_banco()
    app.run(host="0.0.0.0", port=5000, debug=True)