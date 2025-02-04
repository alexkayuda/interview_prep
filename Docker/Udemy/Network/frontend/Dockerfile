ARG DEFAULT_PORT=3000

FROM node:latest

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ENV PORT=$DEFAULT_PORT

EXPOSE ${PORT}

CMD [ "npm", "start" ]