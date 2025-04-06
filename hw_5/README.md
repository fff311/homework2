### Домашнее задание "Написание простых автотестов и основы Selenium"

#### Задача:

- Part 1
  - Написать фикстуру для запуска разных браузеров (firefox, chrome, edge, yandex(по желанию)).
    - Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest.
    - По завершению работы тестов должно осуществляться закрытие браузера.
    - Добавить опцию командной строки, которая указывает базовый URL opencart.
- Part 2
  - Написать тесты проверяющие элементарное наличие элементов на разных страницах приложения opencart
  - Реализовать минимум пять тестов (одни модуль с тестами = одна страница приложения)
  - Использовать методы явного ожидания элементов
  - Покрыть необходимо:
    - Главную
    - Каталог
    - Карточку товара
    - Страницу логина в админку /administration
    - Страницу регистрации пользователя (/index.php?route=account/register)
    - Какие именно элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы


Примеры с урока находятся в пакете hw_5, при сдаче домашней работы их не должно быть в пакете hw_5

#### Критерии оценки:

- Задание оформить отдельным merge-request'ом
- В репозитории отсутствуют лишние файлы
- Соблюдается минимальный кодстайл
- Под тесты каждой страницы создан отдельный модуль 

Иструкция по установке приложения на локальную машину под операционной систомой mac в видео модуля Основы Web-разработки
 
Иструкция по установке приложения на локальную машину под операционной систомой win
- Устанавливаем Докер https://docs.docker.com/
- Запускаем Докер
- В пайчарме создаём папку в проекте
- Создаём файл docker-compose.yml
- Капипастим 
```
version: '2'
services:
  mariadb:
    image: docker.io/bitnami/mariadb:11.3
    environment:
      # ALLOW_EMPTY_PASSWORD is recommended only for development.
      - ALLOW_EMPTY_PASSWORD=yes
      - MARIADB_USER=bn_opencart
      - MARIADB_DATABASE=bitnami_opencart
    volumes:
      - 'mariadb_data:/bitnami/mariadb'
  opencart:
    image: docker.io/bitnami/opencart:4
    ports:
      - '80:8080'
      - '443:8443'
    environment:
      - OPENCART_HOST=localhost
      - OPENCART_DATABASE_HOST=mariadb
      - OPENCART_DATABASE_PORT_NUMBER=3306
      - OPENCART_DATABASE_USER=bn_opencart
      - OPENCART_DATABASE_NAME=bitnami_opencart
      # ALLOW_EMPTY_PASSWORD is recommended only for development.
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - 'opencart_data:/bitnami/opencart'
      - 'opencart_storage_data:/bitnami/opencart_storage/'
    depends_on:
      - mariadb
volumes:
  mariadb_data:
    driver: local
  opencart_data:
    driver: local
  opencart_storage_data:
    driver: local
  ```

в свой созданный файл  docker-compose.yml
- В командной строке запускаем команду docker-compose up -d
- Проверяем запуск контейнеров в докере командой docker ps 
- Переходим в http://localhost:80 все иконки в приложении долны быть отображены правильно, не должно быть квадратов

Основные команды docker необходимы для работы с приложением opencart:
- docker-compose up -d - поднять образы из docker-compose.yml
- docker ps - посмотреть запущенные контейнеры
- docker ps -a - посмотреть все контейнеры (включая потушенные)
- docker-compose down - потушить все контейнеры из docker-compose файла
- docker images - показать все сборки
- docker system prune -a - удалить все образы
- docker volume prune - очистить кеш

