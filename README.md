# pz2-cicd
Учебный проект: библиотека арифметических функций с автоматическим тестированием (CI) и генерацией документации (CD) на GitHub Actions.
## Установка
python -m pip install -r requirements.txt
## Использование

    python -m calculator add 2 3
    python -m calculator div 10 4
Операции: `add`, `sub`, `mul`, `div`.
## Тесты

    python -m pytest -v
## Документация

Автоматически генерируется из описаний функций (docstring) и публикуется на GitHub Pages:
https://slavik-04.github.io/pz2-cicd/
