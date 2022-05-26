virtualenv --python 3.9 .venv
source .venv/bin/activate

pip install django
pip install djangorestframework

django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart