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
    return render_template('/categorias.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create_task():
    description = request.form['description']
    new_task = Tasks(description=description)
    
    existe_task = Tasks.query.filter_by(description=description).first()
    if existe_task:
        return 'Erro: Produto já cadastrado'
    
    db.session.add(new_task)
    db.session.commit()
    return redirect('/categorias')

# Para exluir da lista
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/categorias')

    
# Para editar a lista (update)
@app.route('/update/<int:task_id>', methods=["POST"])
def update_task(task_id):
    task = Tasks.query.get(task_id)
    
    if task: 
        task.description = request.form['description']
        db.session.commit()
    return redirect('/categorias')

if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    #Crud categorias