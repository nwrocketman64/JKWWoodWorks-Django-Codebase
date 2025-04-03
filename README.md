# Overview
This is the main codebase for the JKW Woodworks website. The code here is made open-source under Apache 2.0 license and you are free to look at the code to either add any suggestions to improve the code or to copy it and use it as the base template for your website. The purpose of this website is to sell woodworks created by the client for this website.  It is designed to run on Python 3.12 or later.


# Installing
To install the website for running on your computer, you can clone the codebase either by using the GitHub website or through git. Once it is on your computer, to get the website running you must create an `.env` file and place it in the second JKWWoodWorks folder where the settings.py file is located. 

## .env File Template
Your `.env` file should include the following settings:
```
DEBUG_SET=TRUE
SECRET_KEY=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=3306
TIMEZONE=
RECAP_PUBLIC_KEY=
RECAP_PRIVATE_KEY=
EMAIL_USER=
EMAIL_PASS=
HTTPS=
```
Set `HTTPS=TRUE` when deploying to production to enable secure cookie settings and HSTS.

Add all the database information, set the timezone, and set Debug to false. Run this code in the Python shell to generate a secret key.
```
from django.core.management.utils import get_random_secret_key  
print(get_random_secret_key())
```

## Installation Steps
Make sure that the latest version of Python is installed with an updated version of pip. Then, install the required packages:

```
pip3 install django pillow mysqlclient django-environ django-recaptcha django-money django-embed-video django-cleanup django-crispy-forms crispy-bootstrap5 django-extensions django-csp
```

Once the packages are installed, make sure that you have a database server installed on your computer such as MariaDB or another SQL database. After that, you'll need to migrate the database using these commands:

```
python manage.py makemigrations
```
```
python manage.py migrate --run-syncdb
```

Make sure that you include `--run-syncdb` otherwise the tables for the models won't be created. Then, create a user for the admin although this isn't required to start the website. Only if you want to use the admin section:

```
python manage.py createsuperuser
```

## Running the Website
For development with HTTP:
```
python manage.py runserver
```

For development with HTTPS (using django-extensions):
```
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```
This will generate a self-signed certificate for local HTTPS testing.


# Development Environment
* [VS code](https://code.visualstudio.com/) - The main IDE for creating the source code.
* [MariaDB](https://mariadb.org/) - The main database used for development and production.
* [Python 3.10.6](https://www.python.org/) - The runtime enviroment used for Python.
* [Bootstrap 5.2.1](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - The CSS Framework use for the frontend of each web page.


# Libraries Used
* [Django](https://www.djangoproject.com/) - The main web framework that powers the website.
* [Python Imaging Library or PIL](https://python-pillow.org/) - I used this to resize the images when they are uploaded.
* [django-environ](https://django-environ.readthedocs.io/en/latest/) - Used to load the enviroment variables.
* [django-recaptcha](https://github.com/torchbox/django-recaptcha) - Used to implement ReCaptcha for the contact form.
* [django-money](https://django-money.readthedocs.io/en/stable/) - Used to process money data values and how they are display on each web page.
* [django-embed-video](https://django-embed-video.readthedocs.io/en/latest/) - Used to embed videos from YouTube into the website.
* [Bootstrap](https://getbootstrap.com/) - The CSS Framework used for the frontend.
* [django-csp](https://github.com/mozilla/django-csp) - Used to implement Content Security Policy for improved security.
* [django-extensions](https://django-extensions.readthedocs.io/) - Provides additional management commands and development tools.
* [django-cleanup](https://github.com/un1t/django-cleanup) - Automatically deletes files when models are deleted.
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - Provides beautiful rendering of forms.


# Useful Websites
These were a few website that I found to be very helpful in building this website.

* [Python Django - The Practical Guide](https://www.udemy.com/share/104wQs3@RslbiNqsmO9a3w8M7W1O6VrwpLagNEYjMZD12G0NKmY3VKk0391vZ1EhRKe6fyIiUw==/)
* [Sending email | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/email/)
* [Setup Sending Email in Django Project](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/)
* [Integrating Youtube Videos Into a Django Application](https://www.section.io/engineering-education/integrating-youtube-videos-into-a-django-application/)
* [Pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/)

# Change Log
* 2.5.0 - Enhanced security with Content Security Policy (CSP) and HTTP Strict Transport Security (HSTS). Removed inline styles and moved them to CSS files. Fixed resizing of textboxes in contact form. Updated Django to version 5.2. - 5/29/2024
* 2.4.1 - Updated Django and fixed issues with models. - 3/7/2025
* 2.4.0 - Updated Django and other packages, Added Django Cleanup and Crispy Forms, clean code in model and templates. - 1/14/2025
* 2.3.9 - Updated Django and a few other packages. - 8/6/2024
* 2.3.8 - Updated Django and a few other packages. - 7/9/2024
* 2.3.7 - Redo VENV, Updated Django. - 5/27/2024
* 2.3.6 - Updated Django. - 4/5/2024
* 2.3.5 - Updated Django, mysqlclient, and Bootstrap. - 3/7/2024
* 2.3.4 - Updated Django to 5.0.2. - 2/7/2024
* 2.3.3 - Updated Bootstrap, Updated Django and Python packages. - 2/4/2024
* 2.3.2 - Updated Etsy link, Update Django, and Updated Bootstrap. - 9/9/2023
* 2.3.1 - Added venv so website could run on the current version of Ubuntu Server. - 7/27/2023
* 2.3.0 - Added the Plan section to the website. - 4/28/2023
* 2.2.5 - Updated Bootstrap to 5.3-alpha3. Updated Python Django to 4.2, adjust the main section max-width. - 4/3/2023
* 2.2.4 - Updated Bootstrap to 5.3. Fixed a resize issues in contact. - 2/16/2023
* 2.2.3 - Updated the paging navigation on the Videos and Products pages. - 12/22/2022
* 2.2.2 - Fixed issues with the Video and Product page. Added paging to the Product page. - 12/21/2022
* 2.2.1 - Fixed issues with 404 and 500 pages, Add SEO to the Video page and Product page. - 12/20/2022
* 2.2.0 - Fixed issues in the products page, Updated Bootstrap to version 5.2.3, Website now sends out emails when requests are made, Now able to control the order the images appear in the slides, Added the video section to the website, Added two new icons to the footer. - 12/20/2022
* 2.1.2 - Updated packages for Django 4.1.3, Updated Bootstrap to version 5.2.2, Adjusted the background according to the request of the client. - 11/4/2022
* 2.1.1 - Updated packages for Django 4.1.2. - 10/22/2022
* 2.1.0 - Added Background, centered text on home page, adjusted SEO, updated the about page. - 9/30/2022
* 2.0.0 - Changed the backend to Python Django. Rebuilt the frontent using Bootstrap. Changed the database from MongoDB to MariaDB. - 9/9/2022

# Website Link
This is the link to active website deployed.

[JKW Wood Works](https://www.jkwwoodworks.com/)
