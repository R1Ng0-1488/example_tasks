# example_tasks


### Запустить код
##### docker-compose up --build

### Выполнить миграции
##### docker-compose exec web python manage.py migrate

### Доступ к каждому ендпоинту есть только у авторизированных пользователей
получает по HTTP имя CSV-файла  в хранилище и суммирует каждый 10й столбец
api/create-task/ POST
показывает количество задач на вычисление, которые на текущий момент в работе
api/tasks/ GET
принимает ID задачи и отображает результат в JSON-формате
api/tasks/{id}/ GET

### Создать пользователя
##### docker-compose exec web python manage.py createsuperuser
##### api-auth/register/ POST

### Авторизация пользователя
##### api-auth/login/ POST
##### api-token-auth/ POST

###  Добавление csv файлов
##### admin/main/csvfile/ GET
