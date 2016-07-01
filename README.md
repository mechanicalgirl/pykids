To run locally:
---------------

```python
cd ~/path/to/pythonyoungcoders/young-coders-env
source bin/activate
cd ..
pip install -r requirements.txt
cd letslearnpython
python manage.py migrate
python manage.py runserver
```

To create a superuser (for admin access):
-----------------------------------------

```python
cd ~/path/to/pythonyoungcoders/letslearnpython/
python manage.py createsuperuser
```

To view the admin:
------------------

http://127.0.0.1:8000/admin/


To manage content changes:
--------------------------

To dump data out of the database and into fixtures (run these from within an active virtualenv any time you make changes to content through the admin, then be sure and commit the fixtures files):

    cd /path/to/pythonyoungcoders/letslearnpython
    python manage.py dumpdata --format=json lessons > lessons/fixtures/initial_data.json
    python manage.py dumpdata --format=json flatpages > letslearnpython/fixtures/initial_data.json
    python manage.py dumpdata --format=json teaching > teaching/fixtures/initial_data.json

To load data back into the db from fixtures (run these from within an active virtualenv after every pull to ensure you have current content):

    cd /path/to/pythonyoungcoders/letslearnpython
    python manage.py loaddata lessons/fixtures/initial_data.json
    python manage.py loaddata letslearnpython/fixtures/initial_data.json
    python manage.py loaddata teaching/fixtures/initial_data.json

You don't need to clear out or reset the database at any time - loaddata replaces the data for the apps you run it against - so, lessons/teaching and flatpages (the 'About' and 'Contribute' page content - the fixtures for this live under the letslearnpython app).

This should not blow away any auth data you've created.


To try out the contact page:
----------------------------

If you want to test out the contact form, you'll need to have Postfix running locally:

    sudo postfix start

That's for OS X - if you're on, say, Windows, then I don't know. :)


To run with Python3:
--------------------

    cd /path/to/pythonyoungcoders/
    virtualenv -p python3 young-coders-env

Stdout should be something like this:

    Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
    Using base prefix '/Library/Frameworks/Python.framework/Versions/3.5'
    New python executable in young-coders-env/bin/python3
    Also creating executable in young-coders-env/bin/python
    Installing setuptools, pip, wheel...done.

Then you need to reinstall requirements so that Django is on the path:

    source young-coders-env/bin/activate
    pip install -r requirements.txt

Now call runserver with 'python3' instead of 'python':

    cd /path/to/pythonyoungcoders/letslearnpython
    python3 manage.py migrate
    python3 manage.py runserver
