# Project for NGO Semear

This project aims to create an online structure for the NGO Semear in Marília-SP, which requires an organized and efficient way to manage its students and mentors. For this purpose, the project will be developed using Django for the web and API components, and Flutter for the mobile application. MySQL will be used as the database.

## Dependencies

To run the project, you need to have at least Python 3.6 and MySQL 5.7 installed. For the mobile application, Flutter 2.0.3 is required.

## Installation

> MySQL:

```sql
CREATE DATABASE semear;
```

> Environment

Linux (Debian-based):
```bash
apt install python3-pip
```

Windows and macOS already come with pip installed.

```bash
pip install virtualenv

git clone ...

cd .../site

virtualenv -p python3 env

. ./env/bin/activate

pip install -r requirements.txt
```

Create a `.env` file based on `.env.example`, update the key information, and run:

```bash
python manage.py migrate

python manage.py runserver
```

The website will start on port 8000 of the localhost.

> Mobile

```bash
cd .../app/semear

flutter pub get

flutter run
```

