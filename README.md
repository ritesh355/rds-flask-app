# Flask App with AWS RDS (MySQL)

A simple Flask web application connected to an AWS RDS MySQL database, demonstrating real-world DevOps and Cloud integration.

---

## 🧠 Project Overview

This project shows how to:
- Host a web application on AWS EC2.
- Connect it securely to a managed MySQL database on AWS RDS.
- Display data from the database using a Flask REST API.

---

## ⚙️ Tech Stack
- **AWS EC2** – Web server
- **AWS RDS (MySQL)** – Managed database
- **Flask** – Web framework
- **Python** – Application language

---

## 🪜 Setup Instructions

### 1️⃣ Create RDS MySQL Database
- Engine: MySQL
- Instance type: `db.t3.micro` (Free Tier)
- Public access: Enabled
- Note down the endpoint, username, and password.

### 2️⃣ Launch EC2 Instance
- AMI: Ubuntu 22.04
- Security Group:
  - Allow **SSH (22)** from your IP
  - Allow **HTTP (80)** from anywhere
  - Allow **MySQL (3306)** from EC2 security group

### 3️⃣ Connect to EC2
```bash
ssh -i mykey.pem ubuntu@<EC2_PUBLIC_IP>
