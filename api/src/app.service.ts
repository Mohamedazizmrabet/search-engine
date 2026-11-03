import { Injectable } from '@nestjs/common';
import { PrismaService } from './prisma/prisma.service';

export interface HelloResponse {
  message: string;
  database: string;
  search: string;
}

@Injectable()
export class AppService {
  constructor(private readonly prisma: PrismaService) {}

  /** Says hello and shows whether the database and the Python service can be reached. */
  async getHello(): Promise<HelloResponse> {
    return {
      message: 'Hello from the API',
      database: await this.checkDatabase(),
      search: await this.checkSearchService(),
    };
  }

  private async checkDatabase(): Promise<string> {
    try {
      const subjects = await this.prisma.subject.count();
      return `connected (${subjects} subjects)`;
    } catch {
      return 'not reachable';
    }
  }

  private async checkSearchService(): Promise<string> {
    try {
      const response = await fetch(`${process.env.SEARCH_URL}/`);
      const body = (await response.json()) as { message: string };
      return body.message;
    } catch {
      return 'not reachable';
    }
  }
}
