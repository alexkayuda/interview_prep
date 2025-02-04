FROM composer

WORKDIR /var/www/html

RUN "export COMPOSER_PROCESS_TIMEOUT=600"

ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]