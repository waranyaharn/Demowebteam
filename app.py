from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'

db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)

@app.route('/')
def index():
    foods = Food.query.all()
    return render_template('index.html', foods=foods)

@app.route('/add', methods=['POST'])
def add():
    food = Food(
        name=request.form['name'],
        category=request.form['category'],
        price=request.form['price'],
        stock=request.form['stock']
    )
    db.session.add(food)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)