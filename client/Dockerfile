FROM node:16-alpine

ENV CI=true

WORKDIR /usr/src/app

COPY package.json ./

COPY package-lock.json ./

RUN npm install --silent

# RUN npm install react-scripts@3.4.0 -g --silent

COPY . ./

