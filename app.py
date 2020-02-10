from flask import Flask, render_template
app = Flask(__name__)


posts = [{
    'title': 'flask',
    'content': 'my first flask app',
    'author': 'sachin'
}, {

    'title': 'django',
    'content': 'hello world',
    'author': 'sanju'
}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
