import { Global, Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

/** Global module: PrismaService can be injected everywhere without importing this module again. */
@Global()
@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
