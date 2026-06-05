# 🚀 PohanTech Blog

A modern and professional blog platform built with **Django**. PohanTech allows users to create accounts, publish articles, organize content using categories and tags, and engage with readers through comments.

---

## ✨ Features

### 👤 User Authentication

* Sign Up
* Login
* Logout
* Secure User Authentication

### 📝 Blog Management

* Create Posts
* Update Posts
* Delete Posts
* View Detailed Articles
* Professional Blog Layout

### 🏷️ Content Organization

* Categories
* Tags
* Structured Content Management

### 💬 Community Engagement

* Post Comments
* Reader Discussions
* Interactive Blog Experience

### 🎨 Modern Design

* Responsive Layout
* Mobile-Friendly Interface
* Clean and Professional UI

---

## 🛠️ Technologies Used

* 🐍 Python
* 🌐 Django
* 🎨 HTML5
* 🎭 CSS3
* ⚡ JavaScript
* 🗄️ SQLite

---

## 📂 Project Structure

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

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Fazalrahman1000/PohanTech.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd PohanTech
```

### 3️⃣ Create a Virtual Environment

Linux/macOS

```bash
python3 -m venv blog_venv
```

Windows

```bash
python -m venv blog_venv
```

### 4️⃣ Activate the Virtual Environment

Linux/macOS

```bash
source blog_venv/bin/activate
```

Windows

```bash
blog_venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Create an Admin User

```bash
python manage.py createsuperuser
```

### 8️⃣ Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📖 Usage

### ✍️ Create an Account

Register and log in to access blog features.

### 📰 Publish Content

Create posts and organize them using categories and tags.

### 💬 Interact

Comment on articles and participate in discussions.

### 🔐 Admin Panel

```text
http://127.0.0.1:8000/admin/
```

Manage:

* 👥 Users
* 📝 Posts
* 🏷️ Categories
* 🔖 Tags
* 💬 Comments

---

## 🔮 Future Improvements

* 👤 User Profiles
* 🔍 Search Functionality
* ❤️ Like System
* 🔖 Bookmarks
* 📧 Email Verification
* 🔐 Password Reset
* 🌍 REST API

---

## 👨‍💻 Author

**Fazalrahman Waqar**

🐙 GitHub: https://github.com/Fazalrahman1000

---

## 📜 License

This project is available for educational and personal use.
