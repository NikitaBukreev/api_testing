# api_testing
api tests for best api app
## Настройка и запуск проекта
### Создать и активировать окружение 
```shell
python -m venv venv 
source venv/bin/activate
```
### Установить зависимости
```shell
pip3 install -r requirements.txt
```
### Для запуска тестов использовать команду 
```shell
pytest -v
```
### Для запуска smoke тестов использовать команду 
```shell
pytest -m smoke
```
### Для запуска regress тестов использовать команду 
```shell
pytest -m regress
```
### Для запуска тестов с генерацией отчета 
```shell
pytest --alluredir=allure-results
```
### Для просмотра отчета 
```shell
allure serve allure-results
```
### В корне проекта создайте пустой файл (необязательно, в коде предусмотрено автосоздание файла)
```
token.txt
```
