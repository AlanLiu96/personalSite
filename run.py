from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/graph.json')
def graph():
    return render_template('graph.json')


if __name__ == '__main__':
    app.run(debug = True)