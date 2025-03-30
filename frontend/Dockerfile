# Use Node.js for building the frontend
FROM node:20-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the app source code
COPY . .

# Build the frontend
RUN npm run build

# Use NGINX to serve the static files
FROM nginx:1.23-alpine
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

