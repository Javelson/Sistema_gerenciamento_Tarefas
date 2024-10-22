from flask import Flask, render_template, request, redirect, url_for

#Inicializar o Flask
app = Flask(__name__)

#Criar rota

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

app.run(debug=True)