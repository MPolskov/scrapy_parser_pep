# Проект парсинга pep на фреймворке Scrapy

## Описание:

Парсер документов PEP на базе фреймворка Scrapy.

Результатом работы парсера является создание 2 файлов:
* pep_ДатаВремя.csv - перечень всех Pep.
* status_summary_ДатаВремя.csv - сводка по статусам Pep.

Файлы сохраняются в папке /results.

## Технологии:
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
## Пример результата:
* pep_ДатаВремя.csv:
```
number,name,status
1,PEP Purpose and Guidelines,Active
13,Python Language Governance,Active
2,Procedure for Adding New Modules,Active
3,Guidelines for Handling Bug Reports,Withdrawn
5,Guidelines for Language Evolution,Superseded
4,Deprecation of Standard Modules,Active
6,Bug Fix Releases,Superseded
...
```
* status_summary_ДатаВремя.csv:
```
Статус,Количество
Active,33
Withdrawn,57
Superseded,23
Final,285
Rejected,124
Accepted,44
Draft,31
Deferred,36
Provisional,1
April Fool!,1
Total,635
```

## Автор:
Полшков Михаил
