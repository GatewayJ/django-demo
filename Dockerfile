FROM centos

#维护人的信息
MAINTAINER The CentOS Project <835269233@qq.com>

#安装httpd软件包
RUN yum update & \
 yum -y install mysql-server & \
 yum  -y install net-tools & \
 yum  -y install python3 & \
 yum -y install vim & \
 yum -y install python3-devel & \
 yum  -y install mysql-devel & \
#  yum -y install pip3
#  pip3 install -r requirements.txt -i https://pypi.douban.com/simple/


#开启80端口
EXPOSE 80

#复制网站首页文件至镜像中web站点下
WORKDIR /home/wwww/blog/
ADD ./  .
