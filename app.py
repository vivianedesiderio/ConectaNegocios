from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



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

if __name__ == "__main__":
    app.run(debug=True)