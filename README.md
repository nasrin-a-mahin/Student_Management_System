# 🎓 Student Management System (Django)

A role-based Student Management System built using Django.
This system allows Admins to manage students and courses, Teachers to handle academic operations, and Students to view their academic information.

🚀 Features
🔐 Authentication & Roles

Custom User Profile

Role-based access:

- Admin

- Teacher

- Student

👤 Admin Panel

- Create & manage students

- Create & manage courses

- Assign students to courses

- Assign teachers to courses

Full system control

👨‍🏫 Teacher Dashboard

- View assigned courses

- View enrolled students

- (Planned) Mark attendance

- (Planned) Add student marks

🎓 Student Dashboard

- View profile

- View enrolled courses

- (Planned) View attendance

- (Planned) View grades

🏗 Project Structure
Student_Management_System/
│
├── accounts/        # User profile & role management
├── students/        # Student model & management
├── courses/         # Course management
├── templates/       # HTML templates
├── manage.py
🛠 Tech Stack

Python 3.x

Django

SQLite (default)

Bootstrap (for UI)

## ⚙️ Installation

1️⃣ Clone Repository

git clone https://github.com/your-username/Student-Management-System-Django.git

cd Student-Management-System-Django

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependencies
pip install django

5️⃣ Apply Migrations
python manage.py makemigrations

python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/
🧠 System Design

Many-to-Many relationship between Courses and Students

Role-based access control using decorators

Modular app structure for scalability

📌 Future Improvements

Attendance tracking (course-wise)

Marks/Grades module

Dashboard analytics

REST API integration

Deployment on AWS / Heroku

📄 License

This project is built for educational purposes.