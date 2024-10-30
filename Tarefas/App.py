from flask import Flask, render_template, request, redirect, url_for

# Inicializar o Flask
app = Flask(__name__)

# Lista para armazenar as tarefas
tarefas = []

@app.route('/')
def index():
    return render_template('Index.html', tarefas=tarefas)

@app.route("/add", methods=['POST'])
def add():
    tarefa = request.form['tarefa']
    tarefas.append(tarefa)
    return redirect(url_for('index'))

@app.route("/delete/<int:index>", methods=['GET'])
def delete(index):
   if 0 <= index < len(tarefas):# Verifica se o índice está dentro do intervalo
        tarefas.pop(index) # Remove a tarefa do índice especificado
   return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)
