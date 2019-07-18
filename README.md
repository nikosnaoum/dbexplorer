# DB Explorer 
# Implemetation with Django Haystack + Elasticsearch

Data set is from https://www.kaggle.com/orgesleka/used-cars-database 
370.000 cars - auto.csv is cleaned( from the rubish data, dublicates) and adobpted for the importing to the sqlite database


Installation

1.Download and Unzip the files

2.Install Elasticsearch and start the serve

3.create a virtualenv

4.virtualenv venv

5.Install dependencies

pip install -r requirements.txt

6.Run following Django commands:

python manage.py makemigrations 

python manage.py migrate 

python manage.py rebuild_index 

python manage.py runserver

7.Import data_set into database

7.Visit home page 127.0.0.1:8000 and try out some searches.
