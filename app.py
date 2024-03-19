from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.sqlite3'
app.config['SECRET_KEY'] = "random strings"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column('rating_id', db.Integer, primary_key=True)
    school = db.Column(db.String(200), unique=True)
    category = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, school, category, rating, comments):
        self.school = school
        self.category = category
        self.rating = rating
        self.comments = comments
    def __repr__(self):
        return f'<{self.id}: {self.school} - {self.category} - {self.rating} - {self.comments}>'


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # print(Feedback.query.all())
    feedbacks = Feedback.query.all()
    return render_template('index.html', feedbacks=feedbacks)

@app.post('/submit')
def submit():
    feedbacks = Feedback.query.all()
    if request.method == 'POST':
        school = request.form['schools']
        category = request.form['categories']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if school == '' or category == '':
            return render_template('index.html', message='Please enter School or Category', feedbacks=feedbacks)
        if Feedback.query.filter(Feedback.school == school).count() == 0:
            data = Feedback(school, category, rating, comments)
            db.session.add(data)
            db.session.commit()
            # send_mail(school, category, rating, comments)
            # print(Feedback.query.all())
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback', feedbacks=feedbacks)
        


if __name__ == '__main__':
    app.run(debug=True)