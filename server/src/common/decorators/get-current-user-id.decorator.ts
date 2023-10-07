// import { createParamDecorator, ExecutionContext } from '@nestjs/common';
// import { JwtPayload } from 'src/lib/auth/jwt-payload.interface';

// export const GetCurrentUserId = createParamDecorator(
//   (_: undefined, context: ExecutionContext): string => {
//     const request = context.switchToHttp().getRequest();
//     const user = request.user as JwtPayload;
//     return user.id;
//   },
// );
