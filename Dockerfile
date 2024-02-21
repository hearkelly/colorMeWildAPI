FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]

# RUN: docker run -dp 5000:5000 image-name
# local with reloading:
# docker run -dp 5000:5000 -w /app (director) -v "$(pwd):/app"
# creates volume from current directory and copies to container
