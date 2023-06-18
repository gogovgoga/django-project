# Практическая работа 13. Введение в Django REST framework

# Практика 

## Видео 1. REST как основа дизайна API-приложений

- [What is a REST API?](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
    
- [What is RESTful API? — RESTful API Explained — AWS](https://aws.amazon.com/what-is/restful-api/)
    

## Видео 2. Знакомство с Django REST framework

- [Django REST framework | Installation](https://www.django-rest-framework.org/#installation)
    
- [Views — Django REST framework | Function Based Views](https://www.django-rest-framework.org/api-guide/views/#function-based-views)
    
- [The Browsable API — Django REST framework](https://www.django-rest-framework.org/topics/browsable-api/)
    
- [Настройка аутентификации JWT в новом проекте Django](https://habr.com/ru/post/538040/)
    

## Видео 3. Class Based Views в Django REST framework

- [Views — Django REST framework | Class-based Views](https://www.django-rest-framework.org/api-guide/views/#class-based-views)
    

## Видео 4. Django REST framework Serializer

- [Serializers — Django REST framework](https://www.django-rest-framework.org/api-guide/serializers/#serializers)
    
- [Serializers — Django REST framework | ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
    

## Видео 5. Django REST framework Mixins

- [Generic views — Django REST framework](https://www.django-rest-framework.org/api-guide/generic-views/#mixins)
    

## Видео 6. ViewSet в Django REST framework

- [Viewsets — Django REST framework](https://www.django-rest-framework.org/api-guide/viewsets/#viewset)
    

## Видео 7. Фильтрация и сортировка

- [Filtering — Django REST framework](https://www.django-rest-framework.org/api-guide/filtering/)
    
- [Filtering — Django REST framework | API Guide](https://www.django-rest-framework.org/api-guide/filtering/#api-guide)
    
- [Filtering — Django REST framework | SearchFilter](https://www.django-rest-framework.org/api-guide/filtering/#searchfilter)
    
- [Filtering — Django REST framework | OrderingFilter](https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter)
    

# Цель практической работы

Научиться применять Django REST framework для получения (в том числе фильтрации и поиска), создания, обновления, удаления сущностей в Django-приложении.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория практической работы.

1. Установите Django REST framework.
    
2. Подключите Django REST framework в настройках проекта:
    

- добавьте rest_framework в INSTALLED_APPS;
    
- укажите словарь REST_FRAMEWORK, добавьте туда стандартные настройки для пагинации (DEFAULT_PAGINATION_CLASS, PAGE_SIZE).
    

4. Создайте сериализатор для модели (на основе ModelSerializer):
    

- Product,
    
- Order.
    

6. Создайте ViewSet для моделей (на основе ModelViewSet):
    

- Product,
    
- Order.
    

8. Через DefaultRouter подключите созданные ViewSet к urls в приложении ShopApp:
    

- подключите ViewSet для Product к routers,
    
- подключите ViewSet для Order к routers,
    
- подключите ссылки из routers к urlpatterns.
    

10. Установите django-filters.
    
11. Обновите настройки проекта:
    

- установите приложение django_filters (добавив в список INSTALLED_APPS);
    
- укажите стандартный бэкенд для фильтрации DEFAULT_FILTER_BACKENDS.
    

13. Добавьте правила фильтрации на ViewSet для Product:
    

- правила поиска через SearchFilter (фильтр и поля, по которым можно фильтровать);
    
- правила сортировки через OrderingFilter (фильтр и поля, по которым можно сортировать).
    

15. Добавьте правила фильтрации на ViewSet для Order:
    

- правила фильтрации через DjangoFilterBackend (фильтр и поля, по которым можно фильтровать);
    
- правила сортировки через OrderingFilter (фильтр и поля, по которым можно сортировать).
    

# Что оценивается

- В настройках проекта settings.py: 
    

- указаны настройки в REST_FRAMEWORK:
    

- DEFAULT_PAGINATION_CLASS;
    
- PAGE_SIZE;
    
- DEFAULT_FILTER_BACKENDS.
    

- установлены приложения:
    

- rest_framework;
    
- django_filters.
    

- Созданы сериализаторы на основе ModelSerializer для моделей:
    

- Product,
    
- Order.
    

- Созданы ViewSet на основе ModelViewSet для моделей:
    

- Product,
    
- Order.
    

- На ViewSet добавлены правила фильтрации:
    

- для Product:
    

- правила поиска через SearchFilter;
    
- правила сортировки через OrderingFilter;
    

- для Order:
    

- правила фильтрации через DjangoFilterBackend;
    
- правила сортировки через OrderingFilter.
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле для сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
