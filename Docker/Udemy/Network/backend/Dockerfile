ARG DEFAULT_PORT=80

FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ENV PORT=$DEFAULT_PORT
ENV MONGODB_USERNAME=root
ENV MONGODB_PASSWORD=root

EXPOSE ${PORT}

CMD [ "node", "app.js" ]