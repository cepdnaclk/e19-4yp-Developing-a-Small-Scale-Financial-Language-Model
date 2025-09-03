# Node image
FROM node:20

# Set workdir
WORKDIR /app

# Copy package files and install deps
COPY ../frontend/package.json ../frontend/package-lock.json ./
RUN npm install

# Copy frontend code
COPY ../frontend /app

# Expose Vite dev server port
EXPOSE 5173

# Default command
CMD ["npm", "run", "dev", "--", "--host"]
