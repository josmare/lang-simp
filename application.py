import numpy as np
from scipy import signal
from flask import Flask, render_template, request

application = Flask(__name__)


def lang(input, tolerance, look_ahead):
    output = [input[0]]
    key_index = 0
    while True:
        segment = np.array(input[key_index: key_index + look_ahead + 1])
        tolerance_segment = points_within_toler(segment, tolerance)
        new_key = tolerance_segment[-1].tolist()
        output.append(new_key)
        key_index = input.index(new_key)
        if key_index == len(input) - 1:
            break
    return list(output)


def points_within_toler(points, tolerance):
    points = points.copy()
    start_point = points[0]
    end_point = points[-1]
    intermediate_points = points[1:-1]

    if intermediate_points.shape[0] < 1:
        return points

    points_within_reg = np.abs(np.cross(end_point - start_point, start_point - intermediate_points) /
                               np.linalg.norm(end_point - start_point))

    if np.any(points_within_reg > tolerance):
        points = points[:-1]
        return points_within_toler(points, tolerance)

    return points


@application.route('/', methods=['GET', 'POST'])
def lang_simp():
    if request.method == 'POST':
        formula_str = request.form['formula']
        tolerance = int(request.form['tolerance'])
        look_ahead = int(request.form['look_ahead'])
    else:
        formula_str = 'np.exp(-t) * np.cos(2*np.pi*t)'
        tolerance = 2
        look_ahead = 40

    t = np.arange(0.0, 5.0, 0.01)
    f1 = list(eval(formula_str))

    fx = [list(ele) for ele in zip(t, f1)]

    f2 = lang(fx, tolerance, look_ahead)
    f2 = [i[1] for i in f2]
    datos1 = {'y': f1}
    datos2 = {'y': f2}

    return render_template('index.html', datos=datos1,
                           formula_str=formula_str, datos2=datos2,
                           tolerance=tolerance, look_ahead=look_ahead)

