from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 
import os 
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/ErnestGeo24/dati/main/AVASILOAE%20ERNEST%20-%20ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021.csv', sep = ';')

@app.route('/')
def home():
   
    return render_template("home.html")

@app.route('/esercizio1', methods = ["GET"])
def esercizio():
    
    text = request.form['text']
    processed_text = text.upper()
    df[df['DenominazioneScuola'] == processed_text]
    return render_template("esercizio1.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)