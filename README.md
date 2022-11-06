# Учебный проект автотестов
Объект тестирования: http://demowebshop.tricentis.com/books

### Используемый стек:

Python, Selenium, Pytest



### Подготовка проекта:
- склонировать проект на локальную машину
`git clone https://github.com/remak/autotests_demowebshop.git`

- создать виртуальное окружение в директории с тестами любым способом (venv для примера):
`python -m venv venv`

- активировать виртуальное окружение
`source /venv/bin/activate` в linux
`venv\Scripts\activate.bat` в windows

- установить необходимые пакеты
`pip install -r /path/to/requirements.txt`

### Запуск тестов:
`pytest [params] [args]`

например,

`pytest --browser=firefox --headless=True -v -s`

**Параметры запуска:**
- `--browser` - выбор браузера для прогона тестов

   *chrome* (по умолчанию), *firefox*

- `--headless` - включение режима *headless*

   *False* (по умолчанию), *True*

- `--selenoid` - включение прогона на *Selenoid* (требует установки и настройки самого Selenoid) 
  
   *False* (по умолчанию), *True*
