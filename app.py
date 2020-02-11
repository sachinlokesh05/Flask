from flask import (
    Flask, render_template, flash, redirect, url_for, request, session, logging)
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
app = Flask(__name__)

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
    ), validators.EqualTo('confirm', message='password do not match ')])
    confirmpassword = PasswordField('confirm password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
