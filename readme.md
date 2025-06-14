# About This Repository

I will create a Django-base web application following the Python Crash Course.  
And also I will use Git to manage my code.

## Documentation

### manage.py

manage.py is a short program that takes in commands and feeds them to the relevant part of Django to run them.
We'll use these commands to manage tasks like working with databases and running servers.

### learning_log/settings.py

The settings.py file controls how Django interacts with your system and manage your porject.
We'll modify a few of these settings and add some settings of our own as project evolves.

### learning_log/urls.py

The urls.py file tells Django which pages to build in response to browser requests.

### learning_log/wsgi.py

wsgi.py file helps Django serve the files it creates. The filename is an acronym for web server gateway interface

### learning_logs_app/models.py

We'll use models.py to define the data we want to manage in our app.

### learning_logs_app/admin.py

We'll use admin.py to register the models that we have defined. Such as Topic and Entry.

### learning_logs_app/views.py

A view in Django is a Python function or class that takes a web request and returns a web response. The response can be an HTML page, a redirect, an error message, or any other HTTP response.

### learning_logs_app/templates

learning_log/urls.py -> learning_logs_app/views.py -> learning_logs_app/templates
