FROM node:22-alpine

WORKDIR /app

COPY package*.json prisma.config.ts ./
COPY prisma ./prisma
RUN npm ci

COPY . .

# On start: regenerate the Prisma client, apply migrations, run NestJS in watch mode.
CMD ["sh", "-c", "npx prisma generate && npx prisma migrate deploy && npm run start:dev"]
