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
