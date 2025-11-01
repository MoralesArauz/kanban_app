from flask import Flask, render_template, redirect, url_for, request,flash
from flask_sqlalchemy import SQLAlchemy
from forms import CardForm, ListForm, LoginForm, RegisterForm
from models import User, db, List, Card
from flask_migrate import Migrate
from flask_login import LoginManager,login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def get_color_from_name(name):
    colors = ['#e6f0ff', '#fff4e6', '#e6ffe6', '#f0f0f0', '#fce4ec', '#e8f5e9', '#ede7f6']
    index = int(hashlib.md5(name.encode()).hexdigest(), 16) % len(colors)
    return colors[index]


@app.route('/')
@login_required
def index():
    lists = List.query.filter_by(user_id=current_user.id).all()
    for l in lists:
        l.color = get_color_from_name(l.name)
    list_form = ListForm()
    card_form = CardForm()
    return render_template('index.html', lists=lists, list_form=list_form, form=card_form)


@app.route('/move_card/<int:card_id>', methods=['POST'])
def move_card(card_id):
    data = request.get_json()
    new_list_id = data.get('list_id')
    card = Card.query.get(card_id)
    if card and new_list_id:
        card.list_id = int(new_list_id)
        db.session.commit()
    return '', 204

@app.route('/create_list', methods=['POST'])
@login_required
def create_list():
    form = ListForm()
    if form.validate_on_submit():
        new_list = List(name=form.name.data, user_id=current_user.id)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_card/<list_id>', methods=['POST'])
def add_card(list_id):
    form = CardForm()
    if form.validate_on_submit():
        new_card = Card(title=form.title.data, description=form.description.data, list_id=list_id,user_id=current_user.id)
        db.session.add(new_card)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/add_list', methods=['POST'])
@login_required
def add_list():
    form = ListForm()
    if form.validate_on_submit():
        new_list = List(name=form.name.data, user_id=current_user.id)
        db.session.add(new_list)
        db.session.commit()
        flash('List added successfully!', 'success')
    else:
        flash('Failed to add list.', 'danger')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)