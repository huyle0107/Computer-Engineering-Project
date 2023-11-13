"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __rest = (this && this.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.extractAsin = exports.jsonStringifyNoTrailingComma = exports.isJSON = exports.addDays = exports.createSlug = exports.createOTP = exports.cleanProductVariant = exports.cleanOneOrder = exports.cleanOneProduct = exports.removeAttributes = exports.bToa = exports.errorResponse = exports.successResponse = exports.diffDays = void 0;
var dayjs = require("dayjs");
var common_1 = require("@nestjs/common");
var _ = require("lodash");
var diffDays = function (date, otherDate) {
    return Math.ceil(Math.abs(date.valueOf() - otherDate.valueOf()) / (1000 * 60 * 60 * 24));
};
exports.diffDays = diffDays;
var successResponse = function (_a) {
    var data = _a.data, _b = _a.result, result = _b === void 0 ? true : _b, _c = _a.message, message = _c === void 0 ? 'Success' : _c, _d = _a.error, error = _d === void 0 ? '' : _d, _e = _a.meta, meta = _e === void 0 ? {} : _e;
    return {
        result: result,
        data: data,
        message: message,
        error: error,
        meta: meta,
    };
};
exports.successResponse = successResponse;
var errorResponse = function (error) {
    var _a, _b, _c, _d, _e;
    var status = (_a = error === null || error === void 0 ? void 0 : error.response) === null || _a === void 0 ? void 0 : _a.status;
    var errorMessage = (_d = (_c = (_b = error === null || error === void 0 ? void 0 : error.response) === null || _b === void 0 ? void 0 : _b.data) === null || _c === void 0 ? void 0 : _c.error) === null || _d === void 0 ? void 0 : _d.message;
    throw new common_1.HttpException(errorMessage || ((_e = error === null || error === void 0 ? void 0 : error.response) === null || _e === void 0 ? void 0 : _e.data), status);
};
exports.errorResponse = errorResponse;
var bToa = function (str) { return Buffer.from(str).toString('base64'); };
exports.bToa = bToa;
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
var removeAttributes = function (obj) {
    var attributes = obj.attributes, rest = __rest(obj, ["attributes"]);
    return __assign(__assign({}, rest), attributes);
};
exports.removeAttributes = removeAttributes;
var cleanOneProduct = function (product) {
    var _a, _b, _c, _d;
    var id = product.id, productAttributes = product.attributes;
    var store = (_b = (_a = productAttributes === null || productAttributes === void 0 ? void 0 : productAttributes.store) === null || _a === void 0 ? void 0 : _a.data) !== null && _b !== void 0 ? _b : {};
    var productVariants = (_d = (_c = productAttributes === null || productAttributes === void 0 ? void 0 : productAttributes.productVariants) === null || _c === void 0 ? void 0 : _c.data) !== null && _d !== void 0 ? _d : [];
    productVariants = productVariants.map(function (productVariant) {
        var id = productVariant.id, productVariantAttributes = productVariant.attributes;
        var currency = productVariantAttributes.currency, price = productVariantAttributes.price;
        if (currency === '￥') {
            var newPrice = (price + parseFloat(process.env.PRICE_BUFFER)) *
                parseFloat(process.env.JPY_TO_USD);
            productVariantAttributes.price = Math.round(newPrice * 100) / 100;
            productVariantAttributes.currency = 'USD';
        }
        return __assign({ id: id }, productVariantAttributes);
    });
    return __assign(__assign({ id: id }, productAttributes), { productVariants: productVariants.map(exports.removeAttributes), store: (0, exports.removeAttributes)(store) });
};
exports.cleanOneProduct = cleanOneProduct;
var cleanOneOrder = function (order) {
    var _a, _b, _c, _d, _e, _f, _g, _h, _j;
    var id = order.id, orderAttributes = order.attributes;
    var user = (_b = (_a = orderAttributes === null || orderAttributes === void 0 ? void 0 : orderAttributes.user) === null || _a === void 0 ? void 0 : _a.data) !== null && _b !== void 0 ? _b : {};
    var shipping = (_d = (_c = orderAttributes === null || orderAttributes === void 0 ? void 0 : orderAttributes.shipping) === null || _c === void 0 ? void 0 : _c.data) !== null && _d !== void 0 ? _d : {};
    var worker = (_f = (_e = orderAttributes === null || orderAttributes === void 0 ? void 0 : orderAttributes.worker) === null || _e === void 0 ? void 0 : _e.data) !== null && _f !== void 0 ? _f : {};
    var userAttributes = (_g = user === null || user === void 0 ? void 0 : user.attributes) !== null && _g !== void 0 ? _g : {};
    var shippingAttributes = (_h = shipping === null || shipping === void 0 ? void 0 : shipping.attributes) !== null && _h !== void 0 ? _h : {};
    var workerAttributes = (_j = worker === null || worker === void 0 ? void 0 : worker.attributes) !== null && _j !== void 0 ? _j : {};
    return __assign(__assign({ id: id }, orderAttributes), { user: __assign({ id: user.id }, userAttributes), shipping: __assign({ id: shipping.id }, shippingAttributes), worker: __assign({ id: worker.id }, workerAttributes) });
};
exports.cleanOneOrder = cleanOneOrder;
var cleanProductVariant = function (productVariant) {
    var _a;
    var id = productVariant.id, productVariantAttributes = productVariant.attributes;
    var product = (_a = productVariantAttributes.product.data) !== null && _a !== void 0 ? _a : {};
    console.log(id);
    var cleanedProduct = __assign({ id: product.id }, product.attributes);
    var res = __assign(__assign({ id: id }, productVariantAttributes), { product: cleanedProduct });
    return res;
};
exports.cleanProductVariant = cleanProductVariant;
var createOTP = function (length) {
    if (length === void 0) { length = 6; }
    var otp = '';
    for (var i = 0; i < length; i++) {
        otp += Math.floor(Math.random() * 10);
    }
    return otp;
};
exports.createOTP = createOTP;
var createSlug = function (str) {
    return str
        .toLowerCase() // Convert the string to lowercase
        .trim() // Remove leading and trailing whitespace
        .replace(/[^a-z0-9\s]+/g, '') // Remove any non-alphanumeric character and non-space
        .replace(/\s+/g, '-');
}; // Replace one or more spaces with a single hyphen
exports.createSlug = createSlug;
var addDays = function (date, days) {
    return dayjs(date).add(days, 'day').format('YYYY-MM-DD');
};
exports.addDays = addDays;
function isJSON(str) {
    if (_.isEmpty(str))
        return false;
    try {
        JSON.parse(str);
        return true;
    }
    catch (error) {
        return false;
    }
}
exports.isJSON = isJSON;
function jsonStringifyNoTrailingComma(str) {
    var obj;
    try {
        obj = eval('(' + str + ')');
    }
    catch (e) {
        console.error('Invalid string provided. Unable to parse into an object.');
        return;
    }
    return JSON.stringify(obj, null, 2); // Second parameter for replacer function is null and third for space is 2 for pretty-printing
}
exports.jsonStringifyNoTrailingComma = jsonStringifyNoTrailingComma;
function extractAsin(link) {
    // Regular expression pattern to match ASIN in Amazon URLs
    var asinPattern = /\/dp\/([A-Z0-9]{10})/;
    // Search for the ASIN pattern in the input link
    var match = link.match(asinPattern);
    if (match) {
        // If a match is found, return the matched ASIN
        return match[1]; // Capture group 1 contains the ASIN
    }
    // If no ASIN is found, return null
    return null;
}
exports.extractAsin = extractAsin;
