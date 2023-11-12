export enum COLOR {
  GREEN = 1,
  YELLOW = 2,
}

export enum PRODUCT_STATUS {
  IN_STOCK = 'IN_STOCK',
  OUT_OF_STOCK = 'OUT_OF_STOCK',
}

export enum CURRENCY {
  USD = 'USD',
  VND = 'VND',
  JPY = 'JPY',
}

export enum ORDER_STATUS {
  PENDING = 'PENDING',
  PROCESSING = 'PROCESSING',
  COMPLETED = 'COMPLETED',
  CANCELLED = 'CANCELLED',
}

export enum SHIPPING_STATUS {
  PENDING = 'Pending',
  SHIPPED = 'Shipped',
  ON_THE_WAY = 'On the way',
  DELIVERED = 'Delivered',
  RETURNED = 'Returned',
  CANCELLED = 'Cancelled',
}

export enum CHAT_BOTS {
  SAGE = 'capybara',
  GPT4 = 'beaver',
  CLAUDE = 'a2',
  CLAUDEPLUS = 'a2_2',
  CHATGPT = 'chinchilla',
  DRAGONFLY = 'nutria',
}

export enum IMAGE_SOURCE {
  MIDJOURNEY = 'midjourney',
  DALLE = 'dalle',
}

export enum TaskStatus {
  PENDING = 'PENDING',
  REJECTED = 'REJECTED',
  FULFILLED = 'FULFILLED',
  NOTIFIED = 'NOTIFIED',
  UNNOTIFIED = 'UNNOTIFIED',
}

export enum WaterSensorType {}
