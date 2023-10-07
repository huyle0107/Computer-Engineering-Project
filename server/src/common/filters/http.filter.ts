import {
  ArgumentsHost,
  Catch,
  ExceptionFilter,
  HttpException,
} from '@nestjs/common';
@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    console.log('HttpExceptionFilter', JSON.stringify(exception));
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const statusCode = exception.getStatus();
    const message = (exception.getResponse() as any) ?? {};
    return response.status(statusCode).json({
      result: false,
      data: null,
      error: statusCode,
      createdBy: 'HttpExceptionFilter',
      message,
      meta: {},
    });
  }
}
