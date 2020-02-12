from flask import (
    Flask, render_template, flash, redirect, url_for, request, session, logging)
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'redsfsfsfsfis'


# mysql __init_
mysql = MySQL(app)

posts = [
    {
        'author': 'sachin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 20, 2020'
    },
    {
        'author': 'lokesh',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 21, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


class RegistrationForm(Form):
    name = StringField('Name', validators=[
                       validators.input_required(), validators.Length(min=2, max=50)])
    username = StringField('username', [
        validators.input_required(), validators.Length(min=2, max=50)])
    email = StringField('email', [
        validators.input_required(), validators.Length(min=2, max=50)])
    password = PasswordField('password', [validators.DataRequired(
    ), validators.EqualTo('confirmpassword', message='password do not match ')])
    confirmpassword = PasswordField('confirm password')


class LoginForm(Form):
    email = StringField('email', [
        validators.input_required(), validators.Length(min=2, max=50)])
    password = PasswordField('password', [validators.DataRequired()])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()
        new_value = cur.execute(
            "SELECT * FROM users where email LIKE %s or username LIKE %s ", [email, username])
        mysql.connection.commit()
        if new_value > 0:
            flash(
                'email or username address already exists.', 'warning')
            return redirect(url_for('register'))
        else:
            cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s, %s, %s, %s)",
                        (name, email, username, password))

        # commit to DB
            mysql.connection.commit()

        # close connection
            cur.close()

            flash(
                'Your account has been activated successfully. You can now login.', 'success')
            return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'rslh0758a9ztg!c(u9xo=p$snvrf=3wllxx01qev9%s^rra5dl'
    app.run(debug=True)
