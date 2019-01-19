A playground project to test flask, react, docker, ...

pip install -r requirements.txt

docker build -t testwebapp:latest .
docker run --name testwebapp -d -p 8000:5000 --rm testwebapp:latest

http://localhost:8000

docker ps
docker stop <ID>


Jinhja templating
* base.html - a generic reusable template for the whole site.
* index.html - extends base.html defining the actual content to show