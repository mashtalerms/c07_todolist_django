FROM python:3.10-slim

WORKDIR /.

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
COPY entrypoint.sh .

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD python manage.py runserver 0.0.0.0:8000
