FROM blog/centos:v2

#维护人的信息
MAINTAINER The CentOS Project <835269233@qq.com>

#开启80端口
EXPOSE 80
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple/

WORKDIR /home/wwww/blog/
ADD ./  .
COPY supervisord.conf /etc/supervisor/
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["supervisord", "-n"]