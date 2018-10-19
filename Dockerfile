# specify the node base image with your desired version node:<version>
# FROM node:6
# replace this with your application's default port
# EXPOSE 80

FROM nginx

COPY wrapper.sh /

COPY html /usr/share/nginx/html

RUN chmod +x wrapper.sh

CMD ["./wrapper.sh"]