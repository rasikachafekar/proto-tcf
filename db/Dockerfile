FROM postgres:17

COPY ./pg-init/init.sql /docker-entrypoint-initdb.d/

CMD ["postgres"]