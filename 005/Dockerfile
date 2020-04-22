FROM python:2.7-slim

RUN pip install --trusted-host pypi.python.org Flask

ADD app.py /app.py

CMD ["python", "/app.py"]

EXPOSE 8181
