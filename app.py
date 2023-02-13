from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/rendafixa')
def renda_fixa():
    return render_template('lista.html', titulo='Renda Fixa')
