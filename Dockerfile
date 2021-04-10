FROM python:3.9-alpine

COPY entrypoint.py /entrypoint.py
RUN pip install nox
ENTRYPOINT [ "python", "/entrypoint.py" ]
