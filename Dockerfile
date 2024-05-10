# Dockerfile
FROM python:3.11
COPY requirements.txt /productapp/requirements.txt
WORKDIR /productapp
RUN pip install -r requirements.txt
COPY . /productapp
ENTRYPOINT ["python"]
CMD ["run.py"]