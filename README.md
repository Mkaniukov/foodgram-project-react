![workflow](https://github.com/Mkaniukov/foodgram-project-react/actions/workflows/foodgram-project.yml
/badge.svg)



### Описание
Проект Foodgram - сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. А перед походом в магазин, сервис «Список покупок» позволяет пользователям скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Запуск проекта
* Склонируйте репозиторий с github на локальную машину:
> git clone <https://git@github.com:Mkaniukov/foodgram-project-react.git>

* На локальной машине отредактируйте файл nginx.conf, в строке server_name впишите IP своего удаленного сервера 

* Скопируйте файлы docker-compose.yml и nginx.conf из директории infra на сервер:
>scp docker-compose.yml username@host:/home/username/docker-compose.yml  
scp nginx.conf username@host:/home/username/nginx.conf

* Подключитесь к своему удаленному серверу:
> ssh username@host

* Установите Docker на сервер:
> sudo apt install docker.io 

* Cоздайте .env файл и впишите:
>SECRET_KEY=cекретный ключ проекта  
ALLOWED_HOSTS=['*']  
DB_ENGINE=django.db.backends.postgresql  
DB_NAME=<имя базы данных>  
POSTGRES_USER=<пользователь бд>  
POSTGRES_PASSWORD=<пароль бд>   
DB_HOST=db  
DB_PORT=5432   
 
* Соберите docker-compose:
> sudo docker-compose up -d --build

* После успешной сборки на сервере сделайте миграции:
>sudo docker-compose exec backend python manage.py makemigrations --noinput  
> sudo docker-compose exec backend python manage.py migrate --noinput
* Соберите статические файлы:
> sudo docker-compose exec backend python manage.py collectstatic --noinput
* Загрузите ингридиенты в базу данных:
> sudo docker-compose exec backend python manage.py load_data
* Создайте суперпользователя Django:
>sudo docker-compose exec backend python manage.py createsuperuser
* Проект будет доступен по IP вашего сервера

### Проект доступен по адресу:
http://158.160.6.41

lodin: admin@admin.com
pasword: admin
