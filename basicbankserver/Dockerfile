FROM python3
WORKDIR /app
RUN pip install requirements.txt
COPY . /app
CMD [python3, manage.py, runserver]
