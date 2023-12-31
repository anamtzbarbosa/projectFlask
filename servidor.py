from flask import Flask, render_template, jsonify, request 
import numpy as np
from joblib import load
import os
# cargar modeo
dt = load('dt1.joblib')
servidorWeb = Flask(__name__)
@servidorWeb.route("/holamundo",methods = ['GET'])
def formulario():
    return render_template('pagina1.html')

@servidorWeb.route("/holamundo",methods = ['POST'])
def modeloPrediccion():
    contenido = request.json
    print(contenido)
    return jsonify({'resultado':'hola'})

if __name__ == '__main__':
    servidorWeb.run(debug=False, host = '0.0.0.0', port ='8080')