'''
Framework Flask
- Instalar o Flask - pip install Flask (no terminal)
- Criar uma pasta (diretório raiz) para o arquivo python
  - Criar uma pasta templates para o arquivo html
'''

from flask import Flask, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/hello')
def hello_word():
    return '<h1>Olá, 1TDSA! Bem-vindos ao Flask!</h1>'

@app.route('/python')
def hello_python():
    return '<h1>Hello, Python!</h1>'

@app.route('/hello/<nome>') #param String
def hello_name(nome):
    #Lógica da função...
    return f'Olá, {nome}!'

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return f'A soma de {n1} com {n2} é {n1+n2}'

@app.route('/review/<float:rev>')
def set_review(rev):
    #lógica...
    return f'review: {rev}'

@app.route('/status')
def status():
    #return {"status" : "OK"} # retorno de dicionário
    return jsonify({"status" : "OK"})

@app.route('/todo')
def todo_list():
    lista_tarefas = {"Tarefa ": "Estudar Python",
                     "Tarefa 2" : "Estudar Java",
                     "Tarefa 3" : "Fazer o CP de Python",
                     "Tarefa 4" : "Participar do NEXT",
                     "Tarefa 5" : "Ir para a FIAP"}
    return jsonify(lista_tarefas)

@app.route('/pagina1.html')
def pagina1():
    #...
    return render_template("pagina1.html")

@app.route('/home')
def pagina_inicial():
    return 'Bem-vindo à página inicial!'

@app.route('/')
def home():
    #return render_template('home.html', titulo= "Página Inicial")
    return redirect(url_for('pagina_inicial'))

#Programa Principal
if __name__ == '__main__':
    app.run()