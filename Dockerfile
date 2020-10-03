FROM python:3

WORKDIR /usr/src/app

# Need psql client to do inserts to db
# Not for the time being. Using quick installation with package psycopg2-binary
# RUN apt-get update -y; \
#     apt-get install -y libpq-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash"]
