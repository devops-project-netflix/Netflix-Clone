from python:3.6.5-alpine

workdir /app

COPY ./source /app
COPY ./requirements/requirements.txt /app

RUN ls -l && pwd
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["sh"]
CMD ["local.sh"]
