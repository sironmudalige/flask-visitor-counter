# Flask Visitor Counter & Guestbook 🐳☁️

A full-stack Python web application containerized
with Docker and deployed on AWS EC2.

## 🌍 Live Demo
http://16.192.130.167:5000

## 🔧 Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **Database:** SQLite
- **Container:** Docker, Docker Compose
- **Server:** AWS EC2 (Ubuntu 22.04, t2.micro)
- **Registry:** Docker Hub
- **Version Control:** Git & GitHub

## 📋 Features
- Tracks and displays total visitor count
- Guestbook where visitors can leave messages
- Data persists using Docker volumes
- Production-ready with Gunicorn WSGI server
- Auto-restarts on container or server failure
- 🐳 Running in Docker badge on UI

## 🏗️ Architecture
Browser → AWS EC2 (Ubuntu 22.04) → Docker Container → Flask/Gunicorn → SQLite

## 🐳 Run with Docker (one command)
docker pull sironmudalige/flask-visitor-counter:v2
docker run -p 5000:5000 sironmudalige/flask-visitor-counter:v2

Visit: http://localhost:5000

## 🚀 Run Locally Without Docker
git clone https://github.com/sironmudalige/flask-visitor-counter.git
cd flask-visitor-counter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run

Visit: http://localhost:5000

## ☁️ What I learned
- Writing production Dockerfiles
- Docker layer caching for faster builds
- Docker Compose for container management
- Docker volumes for data persistence
- Pushing images to Docker Hub
- Deploying Docker containers on AWS EC2
- Running Flask with Gunicorn in production
- Container auto-restart policies
- Difference between GitHub and Docker Hub

## 👨‍💻 Author
**Siron Mudalige**
Computer Systems & Network Engineering Undergraduate
Building toward a career in Cloud Engineering

[GitHub](https://github.com/sironmudalige) |
[LinkedIn](https://linkedin.com/in/YOUR-LINKEDIN-HERE)
