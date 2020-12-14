FROM python:3.6

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y netcat-traditional && update-alternatives --config nc

COPY ./src /usr/src/app/triumph
WORKDIR /usr/src/app

RUN mkdir -p ./requirements ./conf ./var

COPY ./requirements/ ./requirements
RUN pip install --no-cache-dir -r ./requirements/production.txt

COPY ./conf/env ./conf/nginx.conf ./conf/
COPY ./var ./var

# copy entrypoint.sh
COPY ./bin ./bin


EXPOSE 8000

# run entrypoints
RUN ["chmod", "+x", "/usr/src/app/bin/triumphapp-entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/bin/triumphapp-entrypoint.sh"]

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "triumph", "--bind", ":8000", "triumph.wsgi:application"]