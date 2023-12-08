from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:YOUR_PASSWORD@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

# Home route test
@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask!'


# Querry Strings
@app.route('/new')
def query_strings(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return f'<h1> The greeting is: {query_val}</h1>'

# Remove query strings
@app.route('/user')
@app.route('/user/<name>')
def no_query_stirngs(name='mina'):
    return f'<h1>Hello there! {name}</h1>'

# Strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return f'<h1>Here is a string: {name}</h1>'


# Numbers as Integer
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return f'<h1>The number you picked is: {num}</h1>'

# Add Number as Integer
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1,num2):
    return f'<h1>The sum is: {num1 + num2}</h1>'

# Product number as float
@app.route('/product/<float:num1>/<float:num2>')
def product_two_number(num1,num2):
    return f'<h1>The product is: {num1 * num2}</h1>'

# Render html template
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

# Jinja templates
@app.route('/watch')
def top_movies():
    movie_list = [
        'autospy of jane doe',
        'neon daemon',
        'ghost in a shell',
        'kong: skull island',
        'john wick 2',
        'spiderman - homecoming'
    ]
    return render_template('movies.html',movies=movie_list,name='Harry')


@app.route('/tables')
def movies_plus():
    movie_dict = {
        'autospy of jane doe': 02.14,
        'neon daemon': 3.20,
        'ghost in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2':02.50,
        'spiderman - homecoming': 1.48
    }
    return render_template('table_data.html',movies=movie_dict,name='Tam Tran')


@app.route('/filters')
def filter_data():
    movie_dict = {
        'autospy of jane doe': 02.14,
        'neon daemon': 3.20,
        'ghost in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2':02.50,
        'spiderman - homecoming': 1.48
    }
    return render_template('filter_data.html',movies=movie_dict,name='None',film='a chrismas carol')

# JINJA2 - MACROS
@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html', movies=movies_dict)

# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'The id is {}, Name is is {}'.format(self.id, self.name)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)