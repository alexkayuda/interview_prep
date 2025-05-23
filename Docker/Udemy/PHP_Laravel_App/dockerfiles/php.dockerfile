FROM php:8.1-fpm-alpine

WORKDIR /var/www/html

COPY src .

RUN docker-php-ext-install pdo pdo_mysql

# To solve Permission Denied 
# Give permission to www-data to access /var/www/html
RUN chown -R www-data:www-data /var/www/html