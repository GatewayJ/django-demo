yum update & \
 yum -y install net-tools & \
 yum -y install python3 & \
 yum -y install vim & \
 yum -y install python3-devel & \
 yum -y install mysql-devel & \
 yum -y install python3-pip & \
 yum -y install nginx
mkdir /etc/supervisor/
pip3 install supervisor
echo_supervisord_conf > /etc/supervisor/supervisord.conf
