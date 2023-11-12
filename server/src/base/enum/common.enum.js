"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WaterSensorType = exports.TaskStatus = exports.IMAGE_SOURCE = exports.CHAT_BOTS = exports.SHIPPING_STATUS = exports.ORDER_STATUS = exports.CURRENCY = exports.PRODUCT_STATUS = exports.COLOR = void 0;
var COLOR;
(function (COLOR) {
    COLOR[COLOR["GREEN"] = 1] = "GREEN";
    COLOR[COLOR["YELLOW"] = 2] = "YELLOW";
})(COLOR || (exports.COLOR = COLOR = {}));
var PRODUCT_STATUS;
(function (PRODUCT_STATUS) {
    PRODUCT_STATUS["IN_STOCK"] = "IN_STOCK";
    PRODUCT_STATUS["OUT_OF_STOCK"] = "OUT_OF_STOCK";
})(PRODUCT_STATUS || (exports.PRODUCT_STATUS = PRODUCT_STATUS = {}));
var CURRENCY;
(function (CURRENCY) {
    CURRENCY["USD"] = "USD";
    CURRENCY["VND"] = "VND";
    CURRENCY["JPY"] = "JPY";
})(CURRENCY || (exports.CURRENCY = CURRENCY = {}));
var ORDER_STATUS;
(function (ORDER_STATUS) {
    ORDER_STATUS["PENDING"] = "PENDING";
    ORDER_STATUS["PROCESSING"] = "PROCESSING";
    ORDER_STATUS["COMPLETED"] = "COMPLETED";
    ORDER_STATUS["CANCELLED"] = "CANCELLED";
})(ORDER_STATUS || (exports.ORDER_STATUS = ORDER_STATUS = {}));
var SHIPPING_STATUS;
(function (SHIPPING_STATUS) {
    SHIPPING_STATUS["PENDING"] = "Pending";
    SHIPPING_STATUS["SHIPPED"] = "Shipped";
    SHIPPING_STATUS["ON_THE_WAY"] = "On the way";
    SHIPPING_STATUS["DELIVERED"] = "Delivered";
    SHIPPING_STATUS["RETURNED"] = "Returned";
    SHIPPING_STATUS["CANCELLED"] = "Cancelled";
})(SHIPPING_STATUS || (exports.SHIPPING_STATUS = SHIPPING_STATUS = {}));
var CHAT_BOTS;
(function (CHAT_BOTS) {
    CHAT_BOTS["SAGE"] = "capybara";
    CHAT_BOTS["GPT4"] = "beaver";
    CHAT_BOTS["CLAUDE"] = "a2";
    CHAT_BOTS["CLAUDEPLUS"] = "a2_2";
    CHAT_BOTS["CHATGPT"] = "chinchilla";
    CHAT_BOTS["DRAGONFLY"] = "nutria";
})(CHAT_BOTS || (exports.CHAT_BOTS = CHAT_BOTS = {}));
var IMAGE_SOURCE;
(function (IMAGE_SOURCE) {
    IMAGE_SOURCE["MIDJOURNEY"] = "midjourney";
    IMAGE_SOURCE["DALLE"] = "dalle";
})(IMAGE_SOURCE || (exports.IMAGE_SOURCE = IMAGE_SOURCE = {}));
var TaskStatus;
(function (TaskStatus) {
    TaskStatus["PENDING"] = "PENDING";
    TaskStatus["REJECTED"] = "REJECTED";
    TaskStatus["FULFILLED"] = "FULFILLED";
    TaskStatus["NOTIFIED"] = "NOTIFIED";
    TaskStatus["UNNOTIFIED"] = "UNNOTIFIED";
})(TaskStatus || (exports.TaskStatus = TaskStatus = {}));
var WaterSensorType;
(function (WaterSensorType) {
})(WaterSensorType || (exports.WaterSensorType = WaterSensorType = {}));
