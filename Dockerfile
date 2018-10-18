# specify the node base image with your desired version node:<version>
# FROM node:6
# replace this with your application's default port
# EXPOSE 80

FROM nginx

COPY wrapper.sh $HOME

COPY html /usr/share/nginx/html

CMD ["./wrapper.sh"]