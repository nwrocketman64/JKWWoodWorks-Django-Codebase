# Overview
This is the main codebase for the JKW Woodworks website. The code here is made open-source under Apache 2.0 license and you are free to look at the code to either add any suggestments to improve the code or to copy it and use it as the base template for your website. The purpose of this website is to sell woodworks created by the client for this website. This website is designed to run on Python 3.8 or later.


# Installing
To install the website for running on your computer, you can clone the codebase either by using the GitHub website or through git. Once it is on your computer, to get the website running you must create an .env and place it in the second sewing_site folder where the settings.py file is located. You must have values set in the .env file for DEBUG_SET, SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, TIMEZONE, RECAP_PUBLIC_KEY, RECAP_PRIVATE_KEY, EMAIL_USER, and EMAIL_PASS. You must also make sure that the latest version of Python is installed with an updated version of pip. Then, make sure that these packages are installed.
```
pip3 install django pillow mysqlclient django-environ django-recaptcha django-money django-embed-video
```
Once it is done installing, make sure that you have a database server install on you computer such MariaDB or another SQL database. After that, you'll need to migrate the database using these commands.
```
python manage.py makemigrations
```
```
python manage.py migrate --run-syncdb
```
Make sure that you include --run-syncdb otherwise the tables for the models won't be created. Then, make sure that you create a user for the admin although this isn't required to start the website. Only if you want to use the admin section.
```
python manage.py createsuperuser
```
After that, the website should be able to run and you can run it using this command.
```
python manage.py runserver
```


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


# Useful Websites
These were a few website that I found to be very helpful in building this website.

* [Python Django - The Practical Guide](https://www.udemy.com/share/104wQs3@RslbiNqsmO9a3w8M7W1O6VrwpLagNEYjMZD12G0NKmY3VKk0391vZ1EhRKe6fyIiUw==/)
* [Sending email | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/email/)
* [Setup Sending Email in Django Project](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/)
* [Integrating Youtube Videos Into a Django Application](https://www.section.io/engineering-education/integrating-youtube-videos-into-a-django-application/)
* [Pagination](https://docs.djangoproject.com/en/4.1/topics/pagination/)

# Change Log
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