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

8) python manage.py syncdb

9) python manage.py migrate

publications
------
check out https://github.com/ForumDev/djangocms-publications.git somewhere and create a symlink to forumdev from djangocms-publications/publications to forumdev/.
example in repo (don't actually know if the symlink worked though)
