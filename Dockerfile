FROM python:3.10-slim

WORKDIR /.

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CASHE_DIR=OFF \
    PYTHON_PATH=/.

RUN groupadd --system service && useradd --system -g service api

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY todolist/ ./

USER api

CMD python manage.py runserver 0.0.0.0:8000
