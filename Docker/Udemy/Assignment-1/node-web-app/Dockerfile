FROM node:latest

WORKDIR /node-app

COPY package.json .

RUN npm install

COPY server.js .

EXPOSE 3000

CMD [ "node", "server.js" ]