# Page Object Project

Автоматизированные тесты для сайта http://selenium1py.pythonanywhere.com с использованием Selenium WebDriver и pytest.

## Структура проекта

- `pages/` — классы страниц (Page Object Model)
- `conftest.py` — фикстуры и параметры pytest
- `requirements.txt` — зависимости Python
- `pytest.ini` — конфигурация pytest

## Установка и запуск

Технологии и инструменты
Python 3.12

Selenium WebDriver

Pytest

Pytest markers для группировки тестов

Page Object Model для организации кода

## Структура проекта

page_object_project/
├── pages/               # Файлы с классами страниц (Page Objects)
│   ├── base_page.py
│   ├── basket_page.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── product_page.py
│   └── locators.py
├── tests/               # Тесты (test_main_page.py, test_product_page.py и др.)
├── conftest.py          # Фикстуры pytest
├── requirements.txt     # Зависимости проекта
├── __init__.py          # Для поддержки относительных импортов
└── pytest.ini           # Конфигурация pytest





Git и GitHub для контроля версий
1. Клонируйте репозиторий:

```bash
git clone https://github.com/worsezero/page_object_project.git
cd page_object_project

