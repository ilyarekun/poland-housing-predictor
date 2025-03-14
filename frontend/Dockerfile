FROM node:18-alpine

WORKDIR /app
COPY . .
RUN npm install -g serve@14.2.4

CMD ["sh", "-c", "sed -i \"s|__URL_S__|${URL_S}|g\" /app/index.html && serve -s . -l 3000"]
