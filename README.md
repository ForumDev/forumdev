# forumdev


#### Requirements


* Python = 2.7.0 (? >=)
* Django = 1.6.8 
* Pillow >= 2.4.0

> The app was tested with the versions above, but older versions might also work.

#### install


1) install python, pip, virtualenv
 
> in case python2.7 is not your default use:
> export VIRTUALENV_PYTHON=/usr/bin/python2.7

3.1) check out the follwoing ... somewhere
```
https://github.com/ForumDev/forumdev.git
https://github.com/ForumDev/djangocms-publications.git
https://github.com/ForumDev/aldryn-blog.git
```
3.2) create a symlink from `djangocms-publications/publications` and `aldryn-blog/aldryn-blog` to forumdev/. 
> (examples in repo)

3) `virtualenv fdenv`
 
4) `source fdenv/bin/activate`

> you can use `deactivate` to leave the virtual env.

5.a) get the requirements.txt from the repo

> this setup uses postgres database, make sure the following packages are installed: 

> `libpq-dev python-dev` and `postgresql postgresql-contrib` for the postgres server

5.b) `pip install -r requirements.txt`

7) edit `forumdev/settings.py` and setup  DATABASES (at the end of the file)

8) comment out the following lines in settings.py

```
INSTALLED_APPS += (
    'myauth',
)

AUTH_USER_MODEL = 'myauth.User'
```

9) `python manage.py syncdb`

> create user [yes]

10) `python manage.py migrate`

11) uncomment the lines in 8)

12.1) `python manage.py syncdb`
> don't delete auth | user tables when asked [no] (might need fixing somewhere)

12.2) `python manage.py migrate myauth`

13) `python manage.py createsuperuser`


### you are all setup 

run server:
python manage.py runserver

access on localhost:8000

append `?edit` to url to login

setup froumdev the way you like with the custom usermodel

#### example page setup

> since no page fixtures exist yet...

create page "Home"

go to structure mode

top right 'sponsors' placeholder, add sponsors plugin

'content' placeholder, add sliders plugin

'content' placeholder, add multi-column: 2 / 50%
first column add categories plugin, select collab
second column add categories plugin, select workshops

Add page "Publications" -> save and continue editing -> advanced settings -> app hook-> publications

publish publications page

restart server


#### comments
>it's a little messy at the moment, didn't get to that yet :-)

>thanks for all these great resources out there I tried

>be sure to notice that this is a work in progress (I'll start working on a new branch starting tomorrow (2.11.2014) since I'll be on vacation until 11.10.2014 and don't know what the internet situation will be)

