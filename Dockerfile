FROM python:3.9-alpine
WORKDIR /usr/src/E_gatepass1
COPY . /usr/src/E_gatepass1/
WORKDIR /usr/src/E_gatepass1/
RUN pip install -r requirements.txt
RUN ls
EXPOSE 8000/tcp
# RUN chown -R 777 /usr/src/E_gatepass1
# RUN python manage.py runserver
