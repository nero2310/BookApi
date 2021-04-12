FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /main_app
COPY requirements.txt /main_app/requirements.txt

RUN pip install -r requirements.txt
COPY . /main_app

CMD python main_app/manage.py runserver 0.0.0.0:8000
