#!/bin/bash
pip install -r /usr/local/requirements/requirements.txt
python /usr/local/{{cookiecutter.project_name}}/manage.py migrate
python /usr/local/{{cookiecutter.project_name}}/manage.py runserver 0:8000
