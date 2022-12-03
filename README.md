# Куда пойти — Москва глазами Артёма

В проекте реализована интерактивная карта Москвы по замыслу Артема, на карте отображаются все известные ему виды активного отдыха с подробными описаниями и комментариями. 
Яндекс.Афиша занимается чем-то похожим, но это бездушный робот, собирающий всё подряд. 
Она никогда не обратит внимание на красивый канализационный люк или отвратительную вывеску.

### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости:

```sh
pip install -r requirements.txt
```

Запустите разработческий сервер:

```sh
python3 manage.py runserver
```

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
