from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(debug=('DEBUG' in os.environ), host='0.0.0.0', port=7000)
