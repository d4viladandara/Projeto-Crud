from flask import Flask

app = Flask(__name__)

from app import views  # importa as rotas no final, depois do app estar criado
