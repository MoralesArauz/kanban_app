# 🗂️ Kanban Board App

A visually engaging, user-friendly Kanban board built with Flask, Bootstrap, and SQLite. Organize tasks into customizable lists, add cards with descriptions, and track progress in real time.

## 🚀 Features

- User authentication (login/register/logout)
- Create, rename, and color-code task lists
- Add cards with titles and descriptions
- Responsive layout with Bootstrap
- Flash messages for feedback
- Dynamic styling based on list names
- Seeded demo data for quick testing

## 🖼️ Screenshots

Coming soon — feel free to add screenshots of your board in action!

## 🛠️ Tech Stack

- **Backend:** Flask, SQLAlchemy, Flask-Login
- **Frontend:** HTML, CSS, Bootstrap 5, Jinja2
- **Database:** SQLite
- **Forms:** Flask-WTF

## 📦 Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed demo data (optional):

   ```bash
   python seed.py
   ```

6. Run the app:

   ```bash
   flask run
   ```

## 👤 User Demo

- Email: `test@example.com`
- Password: `password123`

## 📁 Project Structure

```
kanban_app/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── register.html
├── models.py
├── forms.py
├── routes.py
├── seed.py
├── requirements.txt
└── README.md
```

## 🧠 Future Enhancements

- Drag-and-drop with SortableJS
- AJAX-based card creation
- User-specific color customization
- Card editing and deletion
- Profile page and settings

## 📄 License

MIT License — feel free to use, modify, and share!
