import { COLOR } from '../enum';
import * as dayjs from 'dayjs';
import { HttpException } from '@nestjs/common';
import * as _ from 'lodash';

export const diffDays = (date: Date, otherDate: Date): number =>
  Math.ceil(
    Math.abs(date.valueOf() - otherDate.valueOf()) / (1000 * 60 * 60 * 24),
  );

export const successResponse = ({
  data,
  result = true,
  message = 'Success',
  error = '',
  meta = {},
}) => {
  return {
    result,
    data,
    message,
    error,
    meta,
  };
};

export const errorResponse = (error) => {
  const status = error?.response?.status;
  const errorMessage = error?.response?.data?.error?.message;
  throw new HttpException(errorMessage || error?.response?.data, status);
};

export const bToa = (str) => Buffer.from(str).toString('base64');

// export const removeAttributes = (obj) => {
//   const { attributes, ...others } = obj;
//   if (!attributes) return others;
//   Object.keys(attributes).map((key) => {
//     if (typeof attributes[key] === 'object') {
//       attributes[key] = removeAttributes(attributes[key]);
//     }
//   });

//   return removeAttributes({ ...others, ...attributes });
// };

// export const cleanRes = (res) => {
//   const result = res.map((item) => {
//     return removeAttributes(item);
//   });
//   return result;
// };

export const removeAttributes = (obj) => {
  const { attributes, ...rest } = obj;
  return { ...rest, ...attributes };
};
export const cleanOneProduct = (product) => {
  const { id, attributes: productAttributes } = product;
  const store = productAttributes?.store?.data ?? {};
  let productVariants = productAttributes?.productVariants?.data ?? [];
  productVariants = productVariants.map((productVariant) => {
    const { id, attributes: productVariantAttributes } = productVariant;
    const { currency, price } = productVariantAttributes;
    if (currency === '￥') {
      const newPrice =
        (price + parseFloat(process.env.PRICE_BUFFER)) *
        parseFloat(process.env.JPY_TO_USD);
      productVariantAttributes.price = Math.round(newPrice * 100) / 100;
      productVariantAttributes.currency = 'USD';
    }
    return { id, ...productVariantAttributes };
  });

  return {
    id,
    ...productAttributes,
    productVariants: productVariants.map(removeAttributes),
    store: removeAttributes(store),
  };
};

export const cleanOneOrder = (order) => {
  const { id, attributes: orderAttributes } = order;
  const user = orderAttributes?.user?.data ?? {};
  const shipping = orderAttributes?.shipping?.data ?? {};
  const worker = orderAttributes?.worker?.data ?? {};
  const userAttributes = user?.attributes ?? {};
  const shippingAttributes = shipping?.attributes ?? {};
  const workerAttributes = worker?.attributes ?? {};
  return {
    id,
    ...orderAttributes,
    user: { id: user.id, ...userAttributes },
    shipping: { id: shipping.id, ...shippingAttributes },
    worker: { id: worker.id, ...workerAttributes },
  };
};

export const cleanProductVariant = (productVariant) => {
  const { id, attributes: productVariantAttributes } = productVariant;
  const product = productVariantAttributes.product.data ?? {};
  console.log(id);
  const cleanedProduct = {
    id: product.id,
    ...product.attributes,
  };
  const res = {
    id,
    ...productVariantAttributes,
    product: cleanedProduct,
  };
  return res;
};

export const createOTP = (length = 6) => {
  let otp = '';
  for (let i = 0; i < length; i++) {
    otp += Math.floor(Math.random() * 10);
  }
  return otp;
};

export const createSlug = (str) =>
  str
    .toLowerCase() // Convert the string to lowercase
    .trim() // Remove leading and trailing whitespace
    .replace(/[^a-z0-9\s]+/g, '') // Remove any non-alphanumeric character and non-space
    .replace(/\s+/g, '-'); // Replace one or more spaces with a single hyphen

export const addDays = (date, days) => {
  return dayjs(date).add(days, 'day').format('YYYY-MM-DD');
};

export function isJSON(str: string): boolean {
  if (_.isEmpty(str)) return false;
  try {
    JSON.parse(str);
    return true;
  } catch (error) {
    return false;
  }
}

export function jsonStringifyNoTrailingComma(str: string): string {
  let obj;
  try {
    obj = eval('(' + str + ')');
  } catch (e) {
    console.error('Invalid string provided. Unable to parse into an object.');
    return;
  }
  return JSON.stringify(obj, null, 2); // Second parameter for replacer function is null and third for space is 2 for pretty-printing
}

export function extractAsin(link: string) {
  // Regular expression pattern to match ASIN in Amazon URLs
  const asinPattern = /\/dp\/([A-Z0-9]{10})/;

  // Search for the ASIN pattern in the input link
  const match = link.match(asinPattern);

  if (match) {
    // If a match is found, return the matched ASIN
    return match[1]; // Capture group 1 contains the ASIN
  }

  // If no ASIN is found, return null
  return null;
}
