from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)

# definindo o modelo de dados
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)


#cRud base (fazer depoissss)
@app.route('/')
def index():
    return render_template('base.html')


#cRud categorias 
@app.route('/categorias')
def categorias():
    tasks = Tasks.query.all()
    return render_template('categorias.html', tasks=tasks)

if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    #Crud categorias