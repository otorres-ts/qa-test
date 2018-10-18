# Sample Dockerfile by Oskr

# Indicates that the ubuntu image will be used as the base image.
FROM ubuntu

# Metadata indicating an image maintainer.
LABEL maintainer="otorres@testingsoft.com"

# Uses dism.exe to install the IIS role.
RUN dism.exe /online /enable-feature /all /featurename:iis-webserver /NoRestart

# Creates an HTML file and adds content to this file.
RUN ["C:\\Users\\Tester\\Desktop\\Trabajo\\Docker\\qa-test\\Test_formWidgetCSS_production.html"]

# Sets a command or process that will run each time a container is run from the new image.
CMD [ "cmd" ]

