from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ian')
def ian():
	return render_template('ian.html')

@app.route('/1203071595')
def prize():
	return "CONGRATZ!!! You did it!!!! Meet us in front of Sterling!"

if __name__ == '__main__':
    app.run(debug = True)