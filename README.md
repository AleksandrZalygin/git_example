# Проект "ООО Ромашка"

## Описание
Этот проект представляет собой систему программного обеспечения для осуществления набора автоматизаций в сети ресторанов `Ромашка`.

## Класс `settings`
Класс `settings` содержит следующие атрибуты:

- `inn`: ИНН (Идентификационный номер налогоплательщика)
- `account`: Номер счета
- `correspondent_account`: Номер корреспондентского счета
- `bic`: БИК (Банковский идентификационный код)
- `name`: Наименование
- `type_of_property`: Тип собственности

Каждый атрибут имеет соответствующий геттер и сеттер для получения и установки его значения.

## Методы класса `settings`
- `inn.setter`: Устанавливает значение атрибута `inn` с проверкой входных данных.
- `account.setter`: Устанавливает значение атрибута `account` с проверкой входных данных.
- `correspondent_account.setter`: Устанавливает значение атрибута `correspondent_account` с проверкой входных данных.
- `bic.setter`: Устанавливает значение атрибута `bic` с проверкой входных данных.
- `name.setter`: Устанавливает значение атрибута `name` с проверкой входных данных.
- `type_of_property.setter`: Устанавливает значение атрибута `type_of_property` с проверкой входных данных.

## Тесты
В файле `test_settings.py` представлены тесты, проверяющие функциональность классов `settings` и `settings_manager`.
