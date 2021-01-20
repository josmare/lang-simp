from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def lang_simp():
    datos = {'date': [1, 2, 3, 4, 5],
             'original': [13, 20, 200, 100, 5, 100],
             'simpli': [1, 20, 30, 43, 51]}

    return render_template('index.html', datos=datos)
