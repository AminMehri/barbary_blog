FROM python:3.8
LABEL MAINTAINER="Mahdi Haddadzadeh | https://mahdi-hdz.ir"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /barbary
WORKDIR /barbary
COPY . /barbary

# Installing requirements
ADD requirements/requirements.txt /barbary
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "barbary", "--bind", ":8000", "barbary.wsgi:application"]