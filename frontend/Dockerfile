# Use a Node.js image as the base
FROM node:16-slim

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json, and install dependencies
COPY package.json package-lock.json /app/
RUN npm install

# Copy the React app files into the container
COPY . /app

# Build the React app
RUN npm run build

# Expose the port React will run on
EXPOSE 3000

# Serve the React app using a simple HTTP server
CMD ["npx", "serve", "build"]
