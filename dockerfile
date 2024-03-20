# Use the official Nginx image
FROM nginx:latest

# copy Nginxcfg file
COPY nginx.cfg /etc/nginx/nginx.cfg

# Expose port 80 (HTTP)
EXPOSE 80