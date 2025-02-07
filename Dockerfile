FROM python:3.9
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000
