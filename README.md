# 🏋️‍♀️ FitFusion – Fitness & Gym Management Web Application

FitFusion is a Django-based web platform designed to support both **gym members** and **gym owners**. It combines fitness tracking, personalized diet plans,chatbot-based 
workout guidance, and member management into one seamless solution.

---

## 🚀 Key Features

### 🧍 For Users:
- 🍽️ Personalized diet plans (vegetarian & non-vegetarian)
- 🤖 Smart chatbot for workout suggestions and fitness tips
- 📊 BMI calculator with progress tracking and graphical representation
- 🎥 Video tutorials and fitness guidance
- 💬 Feedback system for users
- 💳 QR code-based subscription payment system

### 👨‍💼 For Gym Owners (Admin):
- 🔐 Separate admin login
- 👥 Dashboard to manage gym members
- 📅 Track membership status and joining dates
- 📈 View user progress (BMI graphs)
- 💰 Track and automate subscription payments
- 📝 View and manage user feedback

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Others:** QR Code Integration for payments

---

## 🧪 How to Run Locally

1. Create and activate a virtual environment

python -m venv .venv

.venv\Scripts\activate   # On Windows

2. Install dependencies
pip install -r requirements.txt

3. Set up the database

python manage.py makemigrations
python manage.py migrate

4. Run the server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📁 Project Structure
fitfusion/
├── fitfusion/                 # Django project settings
├── main_page/                # Landing page app
├── login_page/               # Login and signup system
├── bmigraph/                 # BMI tracking and graph app
├── gymdashboard/             # Gym owner's dashboard
├── chatbot/                  # FitnessBot chatbot app
├── diet/                     # Personalized diet plans
├── templates/                # Shared HTML templates
├── static/                   # CSS, JS, and media files
├── manage.py
├── requirements.txt
└── README.md

📄 Project Synopsis
A detailed synopsis of the project is included in the file:
📘 FitFusion_Project_Synopsis.docx
