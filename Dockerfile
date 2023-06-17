FROM jupyter/scipy-notebook

LABEL authors="V7SYA"

# Копирование исходного кода приложения в образ
WORKDIR /app
COPY . /app

USER root

# Установка дополнительных зависимостей
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Установка Python-зависимостей
RUN pip install --no-cache-dir opencv-python-headless && \
    pip install --no-cache-dir matplotlib && \
    pip install --no-cache-dir -r requirements_docker.txt

ENV DISPLAY=host.docker.internal:0

WORKDIR src
CMD ["python", "processing.py"]
