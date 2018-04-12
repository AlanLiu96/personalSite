from flask import Flask, render_template, render_template_string, redirect, session, request, flash
from sqlalchemy import create_engine, MetaData
from flask.ext.login import UserMixin, LoginManager, \
    login_user, logout_user
from flask.ext.blogging import SQLAStorage, BloggingEngine
from flask.ext.heroku import Heroku
import os

app = Flask(__name__)
heroku = Heroku(app)

app.config["SECRET_KEY"] = "secretLoginKey"  # for WTF-forms and login
app.config["BLOGGING_URL_PREFIX"] = "/blog"
app.config["BLOGGING_DISQUS_SITENAME"] = "Alan's Blog"
app.config["BLOGGING_SITEURL"] = "http://localhost:3000"
app.config['BLOG_PASS']= 'iLikeToBlog'
dbUrl = os.environ['BLOG_DATABASE_URL']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('project.html')

# BLOG BELOW

# extensions
engine = create_engine(dbUrl)
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
login_manager = LoginManager(app)
meta.create_all(bind=engine)

# user class for providing authentication
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return "Alan Liu"  # typically the user's name

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)


from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    passcode = StringField('passcode', validators=[DataRequired()])

admin = 'alan'
@app.route("/blog/login/", methods=['GET', 'POST'])
def blog_login():
    if session.get('user') and session.get('user') == admin:
        return redirect("/blog")
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.passcode.data == app.config['BLOG_PASS']:
            session['user'] = admin
            flash('Logged in successfully.')
            user = User(admin)
            login_user(user)
            return redirect("/blog")
        else:
            flash('Incorrect passcode')
    return render_template('blog_login.html', form=form)

@app.route("/blogLoginAlan/")
def login():
    user = User("alan")
    login_user(user)
    return redirect("/blog")

@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug = True, port = 3000)