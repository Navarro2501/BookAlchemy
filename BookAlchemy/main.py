from flask import Flask, render_template, request as fkreq, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from form import BookForm, EditForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
db.create_all()

def get_books():
    return db.session.query(Book).all()


@app.route('/')
def home():
    return render_template('index.html', book_list=get_books())


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if fkreq.method == "POST":        
        new_book = Book(
            title=form.name.data, 
            author=form.author.data, 
            rating=float(form.rating.data)
            )
        db.session.add(new_book)
        db.session.commit()

        return render_template('index.html', book_list=get_books())
    return render_template('add.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    form = EditForm()
    if fkreq.method == 'GET':
        book_data = Book.query.get(id)
        return render_template('edit.html', book=book_data, form=form)
    elif fkreq.method == 'POST':
        book_to_update = Book.query.get(id)
        book_to_update.rating = float(form.rating.data)
        db.session.commit()  
    return render_template('index.html', book_list=get_books())


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    book_data = Book.query.get(id)
    db.session.delete(book_data)
    db.session.commit()
    return render_template('index.html', book_list=get_books())


if __name__ == "__main__":
    app.run(debug=True)

