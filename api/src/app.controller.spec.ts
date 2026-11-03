import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    // Fake AppService so the test does not need a database or the Python service.
    const fakeAppService = {
      getHello: () =>
        Promise.resolve({
          message: 'Hello from the API',
          database: 'connected (0 subjects)',
          search: 'Hello from the search service',
        }),
    };

    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [{ provide: AppService, useValue: fakeAppService }],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  it('should say hello', async () => {
    const result = await appController.getHello();
    expect(result.message).toBe('Hello from the API');
  });
});
