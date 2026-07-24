# Flask Visitor Counter & Guestbook ☁️

A full-stack Python web application built and deployed 
on AWS EC2 as part of my cloud engineering journey.

## 🌍 Live Demo
http://13.62.104.80:5000

## 🔧 Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite
- **Server:** AWS EC2 (Ubuntu 22.04, t2.micro)
- **Version Control:** Git & GitHub

## 📋 Features
- Tracks and displays total visitor count
- Guestbook where visitors can leave messages
- Messages stored persistently in SQLite database
- Clean modern dark-themed UI
- Runs as a systemd service (auto-restarts on reboot)

## 🏗️ Architecture
Browser → AWS EC2 (Ubuntu 22.04) → Flask App → SQLite Database

## ☁️ What I learned
- Provisioning and configuring AWS EC2 instances
- Setting up Security Groups (ports 22, 80, 5000)
- Connecting to remote servers via SSH
- Deploying Python applications on Linux servers
- Managing virtual environments on a remote server
- Running apps as systemd services for auto-restart
- Hardening server security (Fail2ban, disabled root login)
- Understanding public vs private IP addresses in AWS

## 🚀 Run Locally
```bash
git clone https://github.com/sironmudalige/flask-visitor-counter.git
cd flask-visitor-counter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Visit: http://localhost:5000

## 👨💻 Author
**Siron Mudalige**
Computer Systems & Network Engineering Undergraduate
Building toward a career in Cloud Engineering

[GitHub](https://github.com/sironmudalige) | 
[LinkedIn](https://linkedin.com/in/YOUR-LINKEDIN-HERE)
