🐦 QuickTweet — A Simple Twitter-Like Django App

QuickTweet is a lightweight social posting application built using Django, allowing users to create, edit, and delete tweets with optional photo uploads and visibility settings (Public/Private).

🚀 Features
✔ Tweet Features

Create Tweets with text

Upload optional photos

Edit tweets (with option to update/remove photo)

Delete tweets

Public/Private visibility settings

Clean, modern UI with Bootstrap

✔ User Experience

Fully responsive

Dark theme interface

Easy navigation

Secure file upload handling

✔ Backend

Django 4+

SQLite database

Media storage for uploaded photos

Django forms for safe validation

QuickTweet/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── .gitignore
│── media/               # Uploaded photos
│── static/              # CSS, JS, etc.
│── templates/           # HTML files
│── tweet/               # Main app
│── QuickTweet/          # Django project config
└── venv/                # Virtual environment (ignored)

git clone https://github.com/Ritik-19-12/QuickTweet.git
cd QuickTweet
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

