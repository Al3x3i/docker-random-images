FROM python:3.6

COPY . /app
RUN app/install-dependencies.sh

EXPOSE 3333

CMD ["python", "./app/app.py"]
