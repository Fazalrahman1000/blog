# PohanTech Blog

A modern and professional blog platform built with Django. PohanTech allows users to create accounts, publish blog posts, organize content using categories and tags, and engage with articles through comments.

## Features

### User Authentication

* User Registration (Sign Up)
* User Login
* User Logout
* Secure Authentication System

### Blog Management

* Create Blog Posts
* Update Existing Posts
* Delete Posts
* View Detailed Post Pages
* Professional Blog Layout

### Content Organization

* Categories for Better Content Management
* Tags for Easy Content Discovery
* Organized and Search-Friendly Structure

### Community Interaction

* Comment on Blog Posts
* User Engagement and Discussions

### Responsive Design

* Modern User Interface
* Clean and Professional Design
* Mobile-Friendly Layout

---

## Technologies Used

* Python
* Django
* HTML5
* CSS3
* JavaScript
* SQLite

---

## Project Structure

```text
PohanTech/
│
├── blog/
├── users/
├── static/
├── templates/
├── manage.py
└── requirements.txt
```

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Fazalrahman1000/PohanTech.git
```

### 2. Navigate to the Project Directory

```bash
cd PohanTech
```

### 3. Create a Virtual Environment

Linux / macOS

```bash
python3 -m venv blog_venv
```

Windows

```bash
python -m venv blog_venv
```

### 4. Activate the Virtual Environment

Linux / macOS

```bash
source blog_venv/bin/activate
```

Windows

```bash
blog_venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Usage

### Create an Account

* Register a new account using the Sign Up page.
* Log in with your credentials.

### Publish a Blog Post

* Create and manage blog posts.
* Assign categories and tags to organize content.

### Interact with Posts

* Read articles.
* Leave comments and participate in discussions.

### Admin Panel

Access the Django administration panel:

```text
http://127.0.0.1:8000/admin/
```

Login with your superuser account to manage:

* Users
* Posts
* Categories
* Tags
* Comments

---

## Future Improvements

* User Profiles
* Post Search Functionality
* Rich Text Editor
* Like and Bookmark System
* Email Verification
* Password Reset via Email
* REST API Integration

---

## Author

**Fazalrahman Waqar**

GitHub: https://github.com/Fazalrahman1000

---

## License

This project is available for educational and personal use.
