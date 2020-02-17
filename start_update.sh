git pull origin master

docker stop blog_admin
docker rm blog_admin
docker build -t blog/centos:latest .
docker run --name  blog_admin -d   -p 80:80    blog/centos:latest
