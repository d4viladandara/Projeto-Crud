from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/categoria")
def base():
    return render_template("base.html")

@app.route("/categoria/enviar", methods=["POST"])
def receber_categoria():
    comida = request.form.get("food")
    return f"<h1>Você escolheu: {comida.capitalize()}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
