forumdev
========



install
------
1) install python, pip, virtualenv
 
2) cd /some/dev/dir

in case python2.7 is not your default use:
export VIRTUALENV_PYTHON=/usr/bin/python2.7

3) virtualenv fdenv
 
4) source fdenv/bin/activate

you can use 'deactivate' to leave the virtual env.


5.a) get the requirements.txt from the repo

5.b) pip install -r requirements.txt

this setup uses postgres database, make sure the following packages are installed: libpq-dev postgresql-client-9.3 python-dev

6) copy contents of repo into directory

7) edit forumdev/settings.py and setup  DATABASES (at the end of the file)

(the no-initial-data is because I didn't get the fixtures to work yet :-( )
 
8) python manage.py syncdb --no-initial-data

9) python manage.py migrate --no-initial-data