FROM python:3.10-alpine

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt 
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "vprokoshev_dev.wsgi", "--workers=4"]
