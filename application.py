from flask import Flask, render_template
import numpy as np
import sys

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def lang_simp():
    formula_str = 'np.exp(-t) * np.cos(2*np.pi*t)'
    t = np.arange(0.0, 5.0, 0.01)
    f1 = list(eval(formula_str))
    datos1 = {'y': f1}

    return render_template('index.html', datos=datos1)

