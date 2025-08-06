# Event Management System 🎉

A Django-based web application to manage and organize various types of events like Weddings, Birthdays, and Corporate events.

---

## 📌 Features

- User-friendly interface to submit inquiries for events
- Admin panel to manage bookings and messages
- Categorized pages for:
  - Wedding
  - Birthday
  - Corporate Events
- Careers form for job applications
- Contact form with message saving

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Backend**: Python, Django
- **Database**: SQLite (default)

---

## 🗂️ Project Structure


event_management/

│├── event/ # Project configuration

│ ├── settings.py

│ └── urls.py
│

├── webapp/ # Main application

│ ├── models.py

│ ├── views.py

│ ├── urls.py

│ ├── templates/

│ └── static/
│

├── db.sqlite3 # Default database

├── manage.py # Django command-line tool

└── README.md




## 🚀 Getting Started

### 1. Clone the Repository


git clone https://github.com/snehamavinakai/Event_Management.git

cd Event_Management/event

### 2. Create Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate  # Windows

### 3. Install Dependencies

pip install -r requirements.txt
Or install manually:


pip install django

### 4. Run Migrations

python manage.py makemigrations

python manage.py migrate

### 5. Start Development Server

python manage.py runserver
Now open your browser and visit: http://127.0.0.1:8000

---

🧑‍💻 Admin Access
To access the Django admin panel:

python manage.py createsuperuser

Login at: http://127.0.0.1:8000/admin

---

## 📬 Contact

Developer: Sneha Mavinakai

📧 Email: snehamavinakai@gmail.com

🔗 GitHub: github.com/snehamavinakai

---

📄 License
This project is open-source and free to use for learning and development purposes.

