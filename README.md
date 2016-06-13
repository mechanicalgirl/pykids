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

If you make changes to any content in the admin, dump the data back out into fixtures, then commit the new fixtures files:

```cd /path/to/pythonyoungcoders/letslearnpython
python manage.py dumpdata --format=json lessons > ~/path/to/pythonyoungcoders/letslearnpython/lessons/fixtures/initial_data.json
python manage.py dumpdata --format=json flatpages > ~/path/to/pythonyoungcoders/letslearnpython/letslearnpython/fixtures/initial_data.json
python manage.py dumpdata --format=json teaching > ~/path/to/pythonyoungcoders/letslearnpython/teaching/fixtures/initial_data.json
```


To load data back into the db from fixtures:

```cd /path/to/pythonyoungcoders/letslearnpython
python manage.py loaddata lessons/fixtures/initial_data.json
python manage.py loaddata letslearnpython/fixtures/initial_data.json
python manage.py loaddata teaching/fixtures/initial_data.json
```

You don't need to clear out or reset the database at any time - loaddata 

This should not blow away any auth data you've created, it just replaces the data for the apps you run loaddata against - so, lessons/teaching and flatpages (the 'About' and 'Contribute' page content - the fixtures for this live under the letslearnpython app).

