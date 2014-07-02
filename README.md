pinax-project-zero
==================

This project lays the foundation for all other Pinax starter projects. It
provides the project directory layout and bootstrap-based theme.


Usage:

    django-admin.py startproject --template=https://github.com/pinax/pinax-project-zero/zipball/master <project_name>


Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.5
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-zero/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver
