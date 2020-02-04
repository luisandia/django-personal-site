FROM python:3.7
LABEL Luis Andia

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN python manage.py collectstatic --no-input --clear
CMD ['gunicorn', 'personalSite.wsgi:application', '--workers=2', '--bind' ,'0.0.0.0:8000']
