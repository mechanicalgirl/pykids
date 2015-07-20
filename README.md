To run locally:
---------------

```cd ~/path/to/pythonyoungcoders/young-coders-env/
source bin/activate
cd ..
pip install -r requirements.txt
cd youngcoders
python manage.py migrate
python manage.py runserver```

To create a superuser (for admin access):
-----------------------------------------

```cd ~/path/to/pythonyoungcoders/youngcoders/
python manage.py createsuperuser```

To view the admin:
------------------

http://127.0.0.1:8000/admin/
