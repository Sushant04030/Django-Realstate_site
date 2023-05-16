change value of ALLOWED_HOSTS with hosting url, 

Create Mysql user and database then change values of
DB_NAME with database name,
DB_HOST with hosting url, 
DB_USER with database user admin, 
DB_PASSWORD with database user password
as it is without using quotation( '' or "" ) 

----go step by step in terminal----

pip install virtualenv
pip install Pillow
pip install django
pip install django-admin-interface
pip install django-colorfield
pip install mysqlclient
pip install python-decouple
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

requirement.txt file includes all the necessary library.