# Django email sender
An automated django contact me form
## Features
- Send emails with your personal email
- Django settings with environmental variables
- Contact form with these fields:
  - `name`
  - `email`
  - `subject`
  - `message`
## Requirements
- [Python3](https://www.python.org/downloads/)
- [django](https://www.djangoproject.com/download/)
- [django-crsipy-forms](https://pypi.org/project/django-crispy-forms/)
- [django-environ](https://pypi.org/project/django-environ/)
## Setup
Clone the repo and change to the project directory
```bash
git clone https://github.com/markbrlaise/email_sender_app.git
cd email_sender_app/email_project/
```
Create a virtual environment and activate it with venv or pipenv
- With venv
```bash
python3 -m venv .venv && .venv/bin/activate
```
- or with pipenv
```bash
pipenv shell
```
This will do everything for you
# Installing our dependencies
Do this with the following command
```bash
pip install -r requirements.txt
```
Enter to the project settings folder (`EmailProject/EmailProject`), and create an `.env` file with the following information:
```python
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=YourEmail@address
EMAIL_HOST_PASSWORD=YourAppPassword
RECIPIENT_ADDRESS=TheRecieverOfTheMails
```
Where the `EMAIL_HOST` depends on your personal email provider SMTP server.
```bash
ls
manage.py # Make sure you're inside the directory where manage.py is located
python manage.py runserver
```
Finally, run the server and visit your [localhost](http://localhost:8000).
