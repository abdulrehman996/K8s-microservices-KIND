FROM python:3.9

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY wait-for-it.sh /wait-for-it.sh
EXPOSE 8000
CMD ["/wait-for-it.sh", "mysql:3306", "--", "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]