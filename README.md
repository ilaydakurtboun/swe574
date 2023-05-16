# SWE573 Fall 2022 - Project
This repository is a project for the class named SWE573 - Software Development Practices in Boğaziçi University Software Engineering Deparment.

# The URLs:
Project URL: http://44.201.174.233:8000/<br/>
Swagger Documentation: http://44.201.174.233:8000/swagger/<br/>
Admin Panel: http://44.201.174.233:8000/admin/

## To run with docker at local machine:

After you started the docker and be sure about docker is running then you can simply
run these commands :

docker-compose build<br/>
then<br/>
docker-compose up<br/>
in the first time you start the project.

"docker-compose up" will create postgresql database and migrate all migrations file in the first time.
After that only docker-compose up will be sufficient unless any database or
library change occurs. If this will be the case you should also run "docker-compose build"
before "docker-compose up". Sometimes build does not install libraries that you need
if this is the case, you need to run docker-compose down first then build then up.

In this case the backend will be served in http://0.0.0.0:8000/


## To reach api documentation, visit "localhost:8000/swagger"
## To reach django admin panel interface, visit "localhost:8000/admin":
You should createsuperuser to use django admin panel, with the command "python manage.py createsuperuser"