from app import app, db
from models import User, List, Card
from werkzeug.security import generate_password_hash

with app.app_context():
    # Clear existing data (optional)
    db.drop_all()
    db.create_all()

    # Create test user
    user = User(email='test@example.com', password=generate_password_hash('password123'))
    db.session.add(user)
    db.session.commit()

    # Create visible lists
    todo = List(name='To Do', user_id=user.id)
    doing = List(name='Doing', user_id=user.id)
    done = List(name='Done', user_id=user.id)

    # Create hidden deleted list
    deleted = List(name='deleted_task', user_id=user.id)

    db.session.add_all([todo, doing, done, deleted])
    db.session.commit()

    # Create cards
    card1 = Card(title='Write seed script', description='Create user, lists, and cards', list_id=todo.id, user_id=user.id)
    card2 = Card(title='Test drag-and-drop', description='Move cards between lists', list_id=doing.id, user_id=user.id)
    card3 = Card(title='Celebrate', description='Seed data works!', list_id=done.id, user_id=user.id)
    db.session.add_all([card1, card2, card3])
    db.session.commit()

    print("✅ Seed complete: test user, lists, and cards added.")
