FROM python:3.4.5-alpine
WORKDIR /
COPY server.py server.py
COPY requirements.txt requirements.txt 
RUN  pip install -r requirements.txt

CMD ["python", "server.py"]


