from flask import Flask, render_template, request
import numpy as np
import sys

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def lang_simp():
    if request.method == 'POST':
        formula_str = request.form['formula']
    else:
        formula_str = 'np.exp(-t) * np.cos(2*np.pi*t)'
    print(formula_str, file=sys.stderr)
    t = np.arange(0.0, 5.0, 0.01)
    f1 = list(eval(formula_str))
    datos1 = {'y': f1}

    return render_template('index.html', datos=datos1, formula_str=formula_str)

