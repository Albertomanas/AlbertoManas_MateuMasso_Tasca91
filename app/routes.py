from app import app
from flask import render_template
from flask_bootstrap import Bootstrap
from Backend.parser import items_dict

bootstrap = Bootstrap(app)


@app.route('/index/<numero_de_dias>')
def index(numero_de_dias=0):
    dias = numero_de_dias
    items = "patatas lororlooo"
    return render_template('index.html', items=items, dias=dias)
# Aquí meteremos lo que queremos que le salga al usuario en cada ruta
# especifica

@app.route('/index', methods=['GET', 'POST'])
def lionel():
    return render_template('index.html', items=items_dict)