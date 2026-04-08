# Stage 1: Use Nginx to serve the static content
FROM nginx:alpine

# Remove the default Nginx welcome page
RUN rm -rf /usr/share/nginx/html/*

# Copy your local frontend files into the Nginx container
# This includes index.html, script.js, and style.css
COPY . /usr/share/nginx/html/

# Expose port 80 (standard for HTTP)
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
