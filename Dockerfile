FROM python:3
MAINTAINER Vadym Korshunov "korshunov@ucu.edu.ua"
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["load_service.py"]
