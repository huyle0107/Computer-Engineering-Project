# Use Node.js LTS version as base image
FROM node:18-alpine

# Install Yarn
RUN apk add --no-cache yarn

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and yarn.lock to work directory
COPY package*.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy all application files to work directory
COPY . .

# Build application
RUN NODE_OPTIONS="--max-old-space-size=4096" yarn build

# Expose the port on which the application is running
EXPOSE 4000

# Start the application
CMD [ "yarn", "start:prod" ]
