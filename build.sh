#!/bin/bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
gunicorn handtracking_project.wsgi:application
