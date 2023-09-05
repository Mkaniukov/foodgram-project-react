![workflow](https://github.com/Mkaniukov/foodgram-project-react/actions/workflows/foodgram-project.yml/badge.svg)



### Description
The Foodgram project is a site where users can publish recipes, add other people's recipes to their favorites and subscribe to other authors' publications. And before going to the store, the "Shopping List" service allows users to download a consolidated list of products needed to prepare one or more selected dishes.

### Project Launch
* Clone the repository from github to your local machine:
> git clone <https://git@github.com:Mkaniukov/foodgram-project-react.git>

* On the local machine, edit the nginx.conf file, and in the server_name line write the IP of your remote server.

* Copy the docker-compose.yml and nginx.conf files from the infra directory to the server:
>scp docker-compose.yml username@host:/home/username/docker-compose.yml  
scp nginx.conf username@host:/home/username/nginx.conf

* Connect to your remote server:
> ssh username@host

* Install Docker on the server:
> sudo apt install docker.io 

* Create an .env file and type in:
>SECRET_KEY=cекретный ключ проекта  
ALLOWED_HOSTS=['*']  
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=<имя базы данных>  
POSTGRES_USER=<пользователь бд>  
POSTGRES_PASSWORD=<пароль бд>   
DB_HOST=db  
DB_PORT=5432   
 
* Build docker-compose:
> sudo docker-compose up -d --build

* After successful build on the server, do the migrations:
>sudo docker-compose exec backend python manage.py makemigrations --noinput  
> sudo docker-compose exec backend python manage.py migrate --noinput
* Compile the static files:
> sudo docker-compose exec backend python manage.py collectstatic --noinput
* Load the ingredients into the database:
> sudo docker-compose exec backend python manage.py load_data
* Create a Django superuser:
>sudo docker-compose exec backend python manage.py createsuperuser
* The project will be accessible by your server IP
