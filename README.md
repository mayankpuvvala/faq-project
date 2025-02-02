# FAQ Management System (Backend) - Django

This is a backend system for managing FAQs using **Django** with support for **multilingual content** and a **WYSIWYG editor**. The system implements an **API** to manage FAQs, supporting translations in multiple languages, caching with **Redis**, and an intuitive admin panel.

## Objective
The objective of this project is to:
- Design and implement Django models with WYSIWYG editor support.
- Manage FAQs with multi-language translations (e.g., English, Hindi, Bengali).
- Build an efficient API for CRUD operations on FAQs.
- Optimize performance using Redis caching.
- Ensure the code follows **PEP8** conventions and **best practices**.

## Features
- **Django Models**: Store FAQs with multilingual translations (question and answer).
- **WYSIWYG Editor**: Use `django-ckeditor` to allow rich text formatting for answers.
- **API**: A REST API for managing FAQs, with support for fetching in different languages.
- **Caching**: Use **Redis** to cache translated FAQs for better performance.
- **Google Translate API**: Automatically translates FAQs into different languages during object creation.
- **Admin Panel**: A user-friendly admin panel for managing FAQs.
- **Unit Testing**: Unit tests using **pytest** to ensure correctness.

## Table of Contents
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Caching Mechanism](#caching-mechanism)
4. [Admin Panel](#admin-panel)
5. [Unit Tests](#unit-tests)
6. [Git & Version Control](#git--version-control)
7. [Contribution Guidelines](#contribution-guidelines)
8. [Deployment](#deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mayankpuvvala/faq-project.git
   cd faq-project
2. Create and activate a virtual environment:
   
   ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Mac/Linux
    source venv/bin/activate
  
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
4. Set up the database:
   ```bash
    python manage.py migrate
5. Run the development server:
   ```bash
    python manage.py runserver
6. You can access the API and admin panel at [http://127.0.0.1:8000/](https://cryptic-wave-27155-40db0e445078.herokuapp.com/admin).

## API Usage
- Fetch FAQs in English (default):
    curl [http://localhost:8000/api/faqs/](https://cryptic-wave-27155-40db0e445078.herokuapp.com/api/faqs/)
- Fetch FAQs in Hindi:

    curl [http://localhost:8000/api/faqs/?lang=hi](https://cryptic-wave-27155-40db0e445078.herokuapp.com/api/faqs/?lang=hi)
- Fetch FAQs in Bengali:

    curl http://localhost:8000/api/faqs/?lang=bn
- Create a New FAQ
  To create a new FAQ, send a POST request with the following JSON payload:
  
   ```bash
  {
      "question": "What is Django?",
      "answer": "A Python web framework.",
      "question_hi": "डjango क्या है?",
      "answer_hi": "एक पायथन वेब फ्रेमवर्क।",
      "question_bn": "ডjango কি?",
      "answer_bn": "একটি পাইথন ওয়েব ফ্রেমওয়ার্ক।"
  }
## caching-mechanism
The project implements Redis as a caching mechanism to store translated FAQs. The cache improves response time by storing frequently accessed FAQ translations. Cache invalidation occurs automatically when an FAQ is updated or created.

- Steps for Redis Setup
   - Install Redis
    - Start Redis server:
    - redis-server
    - Ensure that Redis is correctly configured in the Django settings
 
      
## admin-panel
The FAQ model is registered in the Django Admin, allowing easy management of FAQ entries.

- To access the admin panel:
    - Create a superuser:
    - python manage.py createsuperuser
    - Login to the admin panel at 
   ```bash
   http://127.0.0.1:8000/admin/
## Unit Tests
 - Unit tests are written using pytest and are included to ensure that all FAQ-related functionality works as expected.

- Run tests:
   ```bash
     pytest
## git--version-control:
This project follows conventional commits. Example commit messages:

   ```bash
feat: Add multilingual FAQ model
fix: Improve translation caching
docs: Update README with API examples
Contribution Guidelines
Fork the repository.
Create a feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m "feat: Add new feature").
Push to your branch (git push origin feature-branch).
-  Open a pull request.
-Deployment
  To deploy the application to Heroku, follow these steps:

-  Create a Procfile:
web: gunicorn faq_project.wsgi --log-file -
Create a requirements.txt (if not created already):
pip freeze > requirements.txt
-  Deploy to Heroku:
-  Create a new Heroku app:
  heroku create
- Push the code to Heroku:
  git push heroku main
-  Open your deployed application using:
    heroku open
-  For Docker support, you can create a Dockerfile and docker-compose.yml.
```
-  License
  This project is licensed under the MIT License - see the LICENSE file for details.