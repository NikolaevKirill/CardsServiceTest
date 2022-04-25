from flask import Blueprint, render_template, request, redirect
from .models import db, Card

main = Blueprint('main', __name__)


@main.route('/')
def hello():
    return render_template("index.html")


@main.route('/card')
def card():
    return render_template("card.html")


@main.route('/create', methods=['POST', 'GET'])
def create_card():
    if request.method == 'POST':

        title = request.form['title']
        text = request.form['text']
        references = request.form['references']
        card = Card(title=title,text=text,references=references)

        #try:
        db.session.add(card)
        db.session.commit()
        return redirect('/print')
        #except:

       #     return 'При добавлении произошла ошибка'
    else:
        return render_template("create.html")

@main.route('/print')
def print():
    cards = Card.query.order_by(Card.id.desc()).all()
    return render_template('print.html', cards = cards)

@main.route('/print/<int:id>')
def print_card(id):
    card = Card.query.get(id)
    return render_template('print_card.html', card=card)

@main.route('/change')
def change_card():
    return render_template("change.html")
