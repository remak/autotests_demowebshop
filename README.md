# Учебный проект автотестов
Объект тестирования: http://demowebshop.tricentis.com/books

### Используемый стек:

Python, Selenium, Pytest



### Подготовка проекта:
- установить необходимые пакеты
`pip install -r /path/to/requirements.txt`

### Запуск тестов:
`pytest [params] [args]`

например,

`pytest --browser=firefox --headless=True -v -s`

**Параметры запуска:**
- `--browser` - выбор браузера для прогона тестов

   *chrome* (по умолчанию), *firefox*, *opera*

- `--headless` - включение режима *headless*

   *False* (по умолчанию), *True*

- `--selenoid` - включение прогодна на *Selenoid*
  
   *False* (по умолчанию), *True*
