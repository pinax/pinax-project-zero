# pinax-project-zero

[![Join the chat at https://gitter.im/pinax/pinax-project-zero](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pinax/pinax-project-zero?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This project lays the foundation for all other Pinax starter projects. It
provides the project directory layout and bootstrap-based theme.


Usage:

```
django-admin.py startproject --template=https://github.com/pinax/pinax-project-zero/zipball/master <project_name>
```

Getting Started:

```
pip install virtualenv
virtualenv mysiteenv
source mysiteenv/bin/activate
pip install Django==1.7.4
django-admin.py startproject --template=https://github.com/pinax/pinax-project-zero/zipball/master mysite
cd mysite
chmod +x manage.py
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
./manage.py runserver
```
