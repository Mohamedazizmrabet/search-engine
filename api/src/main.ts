import 'dotenv/config';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // Allow the React front-end to call this API from the browser.
  app.enableCors({ origin: process.env.WEB_URL ?? 'http://localhost:5173' });
  await app.listen(process.env.PORT ?? 3000);
}
void bootstrap();
