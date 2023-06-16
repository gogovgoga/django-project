# Практическая работа 12. Локализация и интернационализация

# Практика 

## Видео 1. Стандартные средства интернационализации в Django

- [Internationalization and localization](https://docs.djangoproject.com/en/4.1/topics/i18n/#definitions)
    

- [Internationalization: in Python code](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#internationalization-in-python-code)
    
- [Lazy translation](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#internationalization-in-python-code)
    
- [Pluralization](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#pluralization)
    

## Видео 2. Интернационализация в шаблонах

- [Internationalization: in template code](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#internationalization-in-template-code)
    
- [blocktranslate template tag](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#blocktranslate-template-tag)
    

# Цель практической работы

Научиться применять интернационализацию и локализацию для моделей и шаблонов.

# Что нужно сделать

Воспользуйтесь кодовой базой из пройденных модулей или файлами из репозитория с практической работой.

1. Подготовьте приложения к интернационализации и локализации в настройках проекта:
    

- путь к папке с переводами,
    
- доступные языки,
    
- middleware.
    

3. Подключите пути к админке через помощник i18n_patterns.
    
4. Добавьте перевод для имени моделей Product и Order в приложении ShopApp:
    

- поле verbose_name;
    
- поле verbose_name_plural.
    

6. Обновите шаблон для страницы с деталями по товару mysite/shopapp/templates/shopapp/products-details.html, добавьте перевод для всех строк:
    

- воспользуйтесь тегом translate для перевода однострочных надписей;
    
- воспользуйтесь тегом blocktranslate для перевода нескольких строк одновременно;
    
- воспользуйтесь тегом blocktranslate вместе с тегом plural для плюрализации надписи. Например, добавьте информацию о том, сколько картинок доступно в товаре.
    

# Что оценивается

- В настройках проекта settings.py: 
    

- указаны настройки:
    

- USE_L10N; 
    
- LOCALE_PATHS; 
    
- LANGUAGES;
    

- в список MIDDLEWARE добавлено LocaleMiddleware.
    

- Адреса admin и shopapp подключены через помощник i18n_patterns в корневом файле urls.py.
    
- Добавлен перевод имени модели для Product и Order (поля verbose_name и verbose_name_plural).
    
- Добавлен перевод для всех надписей на странице деталей товара:
    

- использован тег translate для перевода однострочных надписей;
    
- использован тег blocktranslate для перевода нескольких строк одновременно;
    
- использован тег blocktranslate вместе с тегом plural для плюрализации надписи (к примеру, добавлена информация о том, сколько картинок доступно в товаре).
    

# Как отправить работу на проверку

Сдайте практическую работу через Skillbox GitLab. В поле для сдачи практической работы напишите «Сделано» и прикрепите ссылку на репозиторий.
