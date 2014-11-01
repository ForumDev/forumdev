# forumdev


#### Requirements


* Python = 2.7.0 (? >=)
* Django = 1.6.8 
* Pillow >= 2.4.0

> The app was tested with the versions above, but older versions might also work.

#### install


1) install python, pip, virtualenv
 
2) `cd /some/dev/dir`

> in case python2.7 is not your default use:
> export VIRTUALENV_PYTHON=/usr/bin/python2.7

3) `virtualenv fdenv`
 
4) `source fdenv/bin/activate`

> you can use `deactivate` to leave the virtual env.

5.a) get the requirements.txt from the repo

5.b) `pip install -r requirements.txt`

> this setup uses postgres database, make sure the following packages are installed: libpq-dev postgresql-client-9.3 python-dev

6) copy contents of repo into directory

6.1) check out the follwoing ... somewhere https://github.com/ForumDev/djangocms-publications.git somewhere
```
https://github.com/ForumDev/djangocms-publications.git
https://github.com/ForumDev/aldryn-blog.git
```
6.2) create a symlink from `djangocms-publications/publications` and `aldryn-blog/aldryn-blog` to forumdev/. 
> (examples in repo)

7) edit `forumdev/settings.py` and setup  DATABASES (at the end of the file)

8) comment out the following lines in settings.py

```
INSTALLED_APPS += (
    'myauth',
)

AUTH_USER_MODEL = 'myauth.User'
```

9) `python manage.py syncdb`

10) `python manage.py migrate`

11) uncomment the lines in 8)

12) run syncdb and migrate again
>might ask you here to delete initial user if you created before [yes delete it]

13) `python manage.py createsuperuser`


### you are all setup 

run server:
python manage.py runserver

access on localhost:8000

append `?edit` to url to login

setup froumdev the way you like with the custom usermodel


#### comments
>it's a little messy at the moment, didn't get to that yet :-)
>thanks for all these great resources out there I tried
>be sure to notice that this is a work in progress (I'll start working on a new branch starting tomorrow since I'll be on vacation and don't know what the internet situation will be)

