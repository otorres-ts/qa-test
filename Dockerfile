# getting base image ubuntu

# Indicates that the ubuntu image will be used as the base image.
FROM ubuntu

# Metadata indicating an image maintainer.
MAINTAINER Tester <otorres@testingsoft.com>

RUN apt-get update

# Sets a command or process that will run each time a container is run from the new image.
CMD ["echo", "Hello World...! from my first docjer image"  ]

