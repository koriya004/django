# django
Example for insert, update, delete and select data in database

do following changes in settings.py

add application "books" in installed app
1.Setting up database
		DATABASES = {
		'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}

	2. Writing a database in models.py
				from django.db import models
				# Create your models here.
				class book(models.Model): # model - class - table
				name = models.CharField(max_length=255) # field - instance - row
				
	3.Creating and alter database structure for a model
				run command for migration
				python manage.py makemigrations <appname>
if cannot create database and table then reopen cmd and run migrate command so create automatic database and table in your Sqlite
	python manage.py migrate
	
	The model using interactive python shell which allows us to access python module in our App: run below command to start shell
python manage.py shell
do insert update, delete and select opereation in python shell

		
