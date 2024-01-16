FROM python:3.11
WORKDIR /code
# копируем файл зависимостей requirements.txt из текущей директории (где находится Dockerfile) в рабочую директорию внутри контейнера
COPY ./requirements.txt /code/requirements.txt
# запускаем установку зависимостей из файла requirements.txt с помощью pip. --no-cache-dir запрещает использование кэша для ускорения установки, но экономит место в образе
RUN pip install --no-cache-dir -r /code/requirements.txt
# копируем все файлы и директории из текущего каталога в рабочую директорию внутри контейнера
COPY ./ /code/
# uvicorn: Запускает приложение FastAPI.
# main:app: Указывает модуль и объект приложения FastAPI.
# `--port", "80": Устанавливает порт 80 для прослушивания запросов.
# `--host", "0.0.0.0": Делает приложение доступным извне контейнера.
# --env-file", ".env": Загружает переменные окружения из файла.env`.
ENTRYPOINT ["uvicorn", "main:app","--port", "80", "--host", "0.0.0.0", "--env-file", ".env"]
