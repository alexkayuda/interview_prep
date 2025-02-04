FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# The scope of ARG is ONLY inside of the Dockerfile (unlike ENV which is global env variable inside of a container)
# Can not be embedded in a CMD command because ARG is a build time and not a runtime command
ARG DEFAULT_PORT=80

# Environment variable PORT with a default value 80
# Set as an environment variable inside of a container as well
# Can be overwritten by --evn PORT=8000 command
ENV PORT $DEFAULT_PORT

EXPOSE $PORT

# Anonumous Volumes are managed by Docker
# Anonomous Volumes are not persistent (if conter is deleted - volume is also deleted)
# Can be defined inside of a Dockerfile like shown below) or by using the following flag: -v /app/feedback
# VOLUME [ "/feedback" ]

CMD [ "node", "server.js" ]