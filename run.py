from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proj1')
def proj1():
    return render_template('proj1.html')

@app.route('/proj1.1')
def proj1_1():
    return render_template('proj1-1.html')

@app.route('/proj2')
def proj2():
    return render_template('proj2.html')

@app.route('/proj3')
def proj3():
    return render_template('proj3.html')

@app.route('/proj4')
def proj4():
    return render_template('proj4.html')

@app.route('/proj5')
def proj5():
    return render_template('proj5.html')

@app.route('/proj6')
def proj6():
    return render_template('proj6.html')

@app.route('/projEnd')
def projEnd():
    return render_template('projEnd.html')


if __name__ == '__main__':
    app.run(debug = True)