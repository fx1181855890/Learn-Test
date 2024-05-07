FROM php:7.4-apache

COPY dzq-full-install-pack/ /var/www/html/
RUN chown -R www-data:www-data /var/www/html
RUN a2enmod rewrite

# 启用 mysqli 模块
RUN docker-php-ext-install mysqli
# 安装 exif 模块
RUN docker-php-ext-install exif
# 安装 gd 模块
RUN apt-get update -y && apt-get install -y libwebp-dev libjpeg62-turbo-dev libpng-dev libxpm-dev libfreetype6-dev
RUN docker-php-ext-install gd
# 安装 pdo_mysql 模块
RUN docker-php-ext-install pdo_mysql

# 修改默认根目录
RUN sed -i 's/\/var\/www\/html/\/var\/www\/html\/public/g' /etc/apache2/sites-available/000-default.conf

WORKDIR /var/www/html
VOLUME /var/www/html
EXPOSE 80

CMD ["apache2-foreground"]
