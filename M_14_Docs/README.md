# Практическая работа 14. Документирование

# Практика 

## Видео 1. Зачем нужно документирование

- [Документирование кодовой базы. Зачем и как?](https://habr.com/ru/post/565342/) 
    

## Видео 2. Знакомство с docstring и Django admindocs

- [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/) 
    

## Видео 3. Best practices документирования проекта

- [Документация в порядке / Хабр](https://habr.com/ru/post/549588/) 
    

## Видео 4. Документация в Django REST framework

- [Documenting your API — Django REST framework](https://www.django-rest-framework.org/topics/documenting-your-api/)
    
- [Flake8](https://flake8.pycqa.org/en/latest/)
    
- [GitHub — PyCQA/flake8-docstrings: Integration of pydocstyle and flake8 for combined linting and reporting](https://github.com/pycqa/flake8-docstrings) 
    

## Видео 5. Знакомство со сторонними инструментами для генерации спецификаций

- [OpenAPI Initiative](https://www.openapis.org/)
    
- [OpenAPI Specification v3.1.0 | Introduction, Definitions, & More](https://spec.openapis.org/oas/latest.html)
    
- [What Is the Difference Between Swagger and OpenAPI?](https://swagger.io/blog/api-strategy/difference-between-swagger-and-openapi/)
    
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
    
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
    
- [GitHub — Redocly/redoc: 📘 OpenAPI/Swagger-generated API Reference Documentation](https://github.com/Redocly/redoc)
    

# Цель практической работы

Научиться создавать интерактивную Swagger-документацию для своего проекта на Django REST framework.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория практической работы.

1. Установите библиотеку drf-spectacular, заморозьте зависимости.
    
2. Обновите настройки в mysite/settings.py:
    

- Установите drf_spectacular в INSTALLED_APPS;
    
- REST_FRAMEWORK — добавьте DEFAULT_SCHEMA_CLASS, указывающий на AutoSchema из drf_spectacular;
    
- SPECTACULAR_SETTINGS — укажите TITLE, DESCRIPTION, VERSION, SERVE_INCLUDE_SCHEMA.
    

4. Обновите mysite/urls.py. Укажите SpectacularAPIView и SpectacularSwaggerView для интерактивной документации.
    

# Что оценивается

- Установлена библиотека drf_spectacular.
    
- В настройках проекта settings.py: 
    

- установлено приложение drf_spectacular:
    
- указаны дополнительные настройки:
    

- DEFAULT_SCHEMA_CLASS в REST_FRAMEWORK;
    
- параметры в SPECTACULAR_SETTINGS.
    

- Указаны адреса в urls для SpectacularAPIView и SpectacularSwaggerView.
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле для сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
