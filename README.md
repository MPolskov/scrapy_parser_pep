# Проект парсинга pep на фреймворке Scrapy

## Описание

Парсер документов PEP на базе фреймворка Scrapy.

По завершению работы парсер создает 2 файла:
* pep_ДатаВремя.csv - перечень всех Pep.
* status_summary_ДатаВремя.csv - сводка по статусам Pep.

Файлы сохраняется в папке /results.

## Технологии
* Python 3.9
* Scrapy 2.5

## Установка и запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:MPolskov/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```
# для Windows:
py -3.9 -m venv venv
# для Linux:
python3.9 -m venv venv
```
```
# для Windows:
source venv/Scripts/activate
# для Linux:
sourse venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install -r requirements.txt
```
Запуск парсера:
```
scrapy crawl pep
```

## Автор:
Полшков Михаил