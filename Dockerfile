FROM python:3.7-slim

WORKDIR /jayhunGulshan

COPY requirements.txt /jayhunGulshan/
RUN pip install -r /jayhunGulshan/requirements.txt
COPY . /jayhunGulshan/

CMD python3 /jayhunGulshan/app.py