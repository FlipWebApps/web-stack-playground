A playground project to test flask, react, docker, ...

pip install -r requirements.txt

docker build -t testwebapp:latest .
docker run --name testwebapp -d -p 8000:5000 --rm testwebapp:latest

http://localhost:8000

docker ps
docker stop <ID>