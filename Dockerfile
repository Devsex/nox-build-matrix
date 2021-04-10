FROM python:3.9-alpine

COPY entrypoint.py /entrypoint.py
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ENTRYPOINT [ "python", "/entrypoint.py" ]
